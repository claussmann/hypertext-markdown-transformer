from html.parser import HTMLParser
from enum import Enum

class ImageHandling(Enum):
    REFERENCE = 0
    IGNORE = 1
    DESCRIBE = 2

class LinkHandling(Enum):
    REFERENCE = 0
    IGNORE = 1

class LogLevel(Enum):
    NO_LOGS = 0
    ERROR = 1
    WARN = 2
    INFO = 3
    DEBUG = 4

class HTMT_Parser(HTMLParser):
    def __init__(self,
                loglevel=LogLevel.WARN,
                imagehandling=ImageHandling.DESCRIBE,
                linkhandling=LinkHandling.REFERENCE):
        self.loglevel = loglevel
        self.imagehandling = imagehandling
        self.linkhandling = linkhandling
        # Not all of these are supported, but they are recognized as start-end-tags
        # in HTML (otherwise the parser searches for missing end tags).
        self.known_startend_tags = ["br", "hr", "img", "meta", "source", "link", "input"]
        # Everything within these tags is ignored.
        self.skipped_tags = ["head", "script", "header", "footer", "form"]
        super().__init__()

    def error(self, msg):
        if self.loglevel != LogLevel.NO_LOGS:
            print("[ERROR] In HTMT_Parser: %s" % msg)

    def warn(self, msg):
        if self.loglevel in [LogLevel.WARN, LogLevel.INFO, LogLevel.DEBUG]:
            print("[WARN] In HTMT_Parser: %s" % msg)

    def info(self, msg):
        if self.loglevel in [LogLevel.INFO, LogLevel.DEBUG]:
            print("[INFO] In HTMT_Parser: %s" % msg)

    def debug(self, msg):
        if self.loglevel == LogLevel.DEBUG:
            print("[DEBUG] In HTMT_Parser: %s" % msg)

    def markdownify(self, html: str) -> str:
        self.md = "\n"
        self.stack = ["BOTTOM"]
        self.attr_stack = ["BOTTOM"]
        self.table_stack = [-1]
        self.is_table = False
        try:
            self.feed(html)
            self.close()
            self.reset()
        except Exception as e:
            self.error(str(e))
        if self.stack.pop() != "BOTTOM":
            self.warn("There were unmatched tags.")
        return self.md

    def handle_starttag(self, tag, attrs):
        stack_top = self.stack[-1]

        if tag in self.skipped_tags:
            # We mark on the stack that the following must be ignored.
            # This helps us especially because we don't need to handle
            # special sequences within javascript etc.
            self.stack.append("skip[%s]" % tag)
            self.debug("Begin skipped: %s" % tag)
            return

        if stack_top.startswith("skip"):
            return

        if tag in self.known_startend_tags:
            # In malformatted HTML tags like <br/> are sometimes
            # written as <br> which causes them to land in this
            # function, but causes errors since they have no end tag.
            return self.handle_startendtag(tag, attrs)

        # This is the default case: Put the tag on the stack s.t. the
        # handle_data function knows what to do, and set start tag in
        # markdown if needed.
        match tag:
            case "h1":
                if not self.is_table:
                    self.md += "\n# "
            case "h2":
                if not self.is_table:
                    self.md += "\n## "
            case "h3" | "h4" | "h5":
                if not self.is_table:
                    self.md += "\n### "
            case "p":
                if not self.is_table:
                    self.md += "\n"
            case "i" | "em":
                if stack_top in ["b", "strong"] and self.md[-1] == "*":
                    self.md += "*"
                else: # to handle <b><i>...</i></b> tags.
                    self.md += " *"
            case "b" | "strong":
                if stack_top in ["i", "em"] and self.md[-1] == "*":
                    self.md += "**"
                else: # to handle <i><b>...</b></i> tags.
                    self.md += " **"
            case "ol" | "ul":
                self.md += "\n\n"
            case "li":
                self.md += "- "
            case "table":
                self.md += "\n"
                self.table_stack.append(0) # Record number of columns for underlining the header.
                self.is_table = True # Prevent newlines within a table cell.
            case "tr":
                self.md += "| "

        self.stack.append(tag)
        self.attr_stack.append(attrs)
        self.debug(self.stack)

    def handle_endtag(self, tag):
        stack_top = self.stack[-1]

        if tag in self.skipped_tags:
            # This is the end tag of a skipped sequence. Mark on the
            # stack that the skipping sequence ends.
            if stack_top == ("skip[%s]" % tag):
                self.stack.pop()
                self.debug("End skipped: %s" % tag)
            else:
                self.warn("Skip-tag unexpected: %s" % tag)
                return

        if stack_top.startswith("skip"):
            return

        if tag != stack_top:
            self.warn("There were unmatched tags: expected: %s got: %s" % (stack_top, tag))

        # The default case: We take the tag from the stack to mark
        # that the tag sequence ends here for handle_data function.
        # We also add delimiters in the markdown to if needed.
        match tag:
            case "p" | "h1" | "h2" | "h3" | "h4" | "h5" | "li":
                self.md = self.md.strip()
                if not self.is_table:
                    self.md += "\n"
            case "i" | "em":
                self.md += "*"
            case "b" | "strong":
                self.md += "**"
            case "table":
                self.md += "\n"
                self.table_stack.pop()
                self.is_table = False
            case "td" | "th":
                self.md += " |"
                self.table_stack[-1] += 1
            case "tr":
                self.md += "\n"
                # We add one underline after every row. This is not perfectly markdown conform,
                # however, most HTML tables have different number of columns in the rows. Thus,
                # it would be malformatted otherwise.
                self.md += ("| --- " * self.table_stack[-1]) + "|\n\n"
                self.table_stack[-1] = 0

        self.stack.pop()
        self.attr_stack.pop()
        self.debug(self.stack)

    def handle_startendtag(self, tag, attrs):
        match tag:
            case "br":
                if not self.is_table:
                    self.md += "\n\n"
            case "hr":
                if not self.is_table:
                    self.md += "\n***\n"
            case "img":
                match self.imagehandling:
                    case ImageHandling.REFERENCE:
                        for k,v in attrs:
                            if k == "src":
                                self.md += " [image](%s) " % v
                                return
                        self.md += " [image] "
                    case ImageHandling.IGNORE:
                        self.md += " [image] "
                    case ImageHandling.DESCRIBE:
                        for k,v in attrs:
                            if k == "src":
                                img_name = v.split("/")[-1]
                                self.md += " [image: %s) " % img_name
                                return
                        self.md += " [image: Unnamed] "

    def handle_data(self, data):
        tag = self.stack[-1]
        attrs = self.attr_stack[-1]

        # We put everything in one line and strip whitespaces (often due to format in HTML)
        data_lines = data.split("\n")
        data = ""
        for line in data_lines:
            line = line.strip()
            if line not in ["", "\n"]:
                data += line + " "
        data = data.strip() # remove trailing whitespace.

        # We now decide what to do with the tag.
        self.debug("For tag %s I got data: %s" % (tag, data))
        match tag:
            case "h1" | "h2" | "h3" | "h4" | "h5" | "b" | "strong" | "i" | "em" | "li" | "th" | "td":
                self.md += data
            case "p" | "span":
                if self.md[-1] not in [" ", "\n"] and len(data) > 0:
                    self.md += " %s" % data
                else:
                    self.md += data
            case "a":
                match self.linkhandling:
                    case LinkHandling.REFERENCE:
                        for k,v in attrs:
                            if k == "href":
                                if data == "":
                                    data = v
                                self.md += " [%s](%s) " % (data, v)
                                return
                        self.md += " %s " % data
                    case LinkHandling.IGNORE:
                        self.md += " %s " % data