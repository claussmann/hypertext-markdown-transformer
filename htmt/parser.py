from html.parser import HTMLParser


class HTMT_Parser(HTMLParser):
    def __init__(self, loglevel="INFO"):
        self.loglevel = loglevel
        self.supported_tags = ["p", "h1", "h2", "h3", "h4", "h5", "a"]
        self.supported_startend_tags = ["br", "hr", "img"]
        self.skipped_tags = ["head", "script"]
        super().__init__()

    def error(self, msg):
        print("[ERROR] In HTMT_Parser: %s" % msg)

    def warn(self, msg):
        if self.loglevel in ["DEBUG", "INFO", "WARN"]:
            print("[WARN] In HTMT_Parser: %s" % msg)

    def info(self, msg):
        if self.loglevel in ["DEBUG", "INFO"]:
            print("[INFO] In HTMT_Parser: %s" % msg)

    def debug(self, msg):
        if self.loglevel in ["DEBUG"]:
            print("[DEBUG] In HTMT_Parser: %s" % msg)

    def markdownify(self, html: str) -> str:
        self.md = ""
        self.stack = ["BOTTOM"]
        self.attr_stack = ["BOTTOM"]
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

        if tag in self.supported_startend_tags:
            # In malformatted HTML tags like <br/> are sometimes
            # written as <br> which causes them to land in this
            # function, but causes errors since they have no end tag.
            return self.handle_startendtag(tag, attrs)

        # This is the default case: Put the tag on the stack s.t. the
        # handle_data function knows what to do.
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
        # We also add a new line in some cases to mark the end of the
        # section also in the markdown.
        if tag in ["p", "div"]:
            self.md += "\n"
        self.stack.pop()
        self.attr_stack.pop()
        self.debug(self.stack)

    def handle_startendtag(self, tag, attrs):
        match tag:
            case "br":
                self.md += "\n\n"
            case "hr":
                self.md += "\n***\n"
            case "img":
                self.md += "\n(image available in original ressource)\n"

    def handle_data(self, data):
        tag = self.stack[-1]
        attr = self.attr_stack[-1]
        if tag not in self.supported_tags:
            return
        # We put everything in one line and strip whitespaces (often due to format in HTML)
        data_lines = data.split("\n")
        data = ""
        for line in data_lines:
            line = line.strip()
            if line not in ["", "\n"]:
                data += line + " "
        self.debug("For tag %s I got data: %s" % (tag, data))
        match tag:
            case "p":
                self.md += data
            case "h1":
                self.md += "\n# " + data
            case "h2":
                self.md += "\n## " + data
            case "h3" | "h4" | "h5":
                self.md += "\n### " + data
            case "a":
                for k,v in attr:
                    if k == "href":
                        self.md += "[%s](%s)" % (data, v)
                        return
                self.md += data