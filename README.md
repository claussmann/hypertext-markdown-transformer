# Hypertext Markdown Transformer (HTMT)

Transforms HTML websites to a simple Markdown format.
Note that the format is somewhat restricted.
Parts of the HTML are completely ignored (e.g. header and footer tags).
HTMT currently supports the following:

- Paragraphs
- Headings
- Italic and boldface
- Lists
- Linebreaks and horizontal rules
- Spans

Further, the following is supported in reduced form:

- Tables (every row is a header row)
- Links (some problems if a link text contains further tags)
- Images (Only references to the actual image are possible)




## Usage

You can install HTMT locally (it is not yet available at pypi).
To do so, simply clone this repository to a path of your choice (say `/home/you/hypertext-markdown-transformer`).
Then run `pip install /home/you/hypertext-markdown-transformer/` (preferably in a virtual enviroment).
Then you can use HTMT as follows:

```
import htmt

with open("testfile.html", "r") as f:
    content = f.read()

parser = htmt.HTMT_Parser()
print(parser.markdownify(content))
```



## System Requirements

HTMT uses the feature of case matching introduced in Python 3.10.
Thus, it will not run with a Python version before 3.10.



## Contribute

Feel free to report bugs at [Github](https://github.com/claussmann/hypertext-markdown-transformer).
Pull requests are always welcome.