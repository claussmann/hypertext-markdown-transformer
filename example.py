import htmt
import sys

with open(sys.argv[1], "r") as f:
    content = f.read()

parser = htmt.HTMT_Parser(loglevel=htmt.LogLevel.WARN)
result = parser.markdownify(content)

print(result)
