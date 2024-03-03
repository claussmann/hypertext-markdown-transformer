html_general = """<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <title>The Title</title>
        <script>
            let x = 5;
        </script>
        <!-- This comment should be ignored -->
    </head>
    <body>
        <div>
            <h1>My Title</h1>
            <hr>
            <p>Foo<br/>Bar bla</p>
            <p>
                Please see <a href="https://bar/foo">My Link</a> for details.
                Note, there are also <a>defective links.</a>
                We can <span>also add <i>some</i> spans</span> to the text.
            </p>
        </div>
    </body>
</html>
"""
makrdown_general = """# My Title

***

Foo

Bar bla

Please see [My Link](https://bar/foo) for details. Note, there are also defective links. We can also add *some* spans to the text.
"""


html_bold_italic = """<html>
    <body>
        <h1>Italic and Bold Text</h1>
        <p>
            Here we see how italic and bold text works.
            <i>This is simply italic.</i>
            <b>This is simply bold.</b>
            <i>This is <b>bold and italic</b> at the same time</i>
            <b><i>This is also Bold and italic.</i></b>
            <i>Next, we have two times</i><i>italic in a row.</i>
            <strong>Finally, this is also bold, but with the strong tag.</strong>
            <em>We can do the same with em.</em>
        </p>
    </body>
</html>
"""
markdown_bold_italic = """# Italic and Bold Text

Here we see how italic and bold text works. *This is simply italic.* **This is simply bold.** *This is **bold and italic**at the same time* ***This is also Bold and italic.*** *Next, we have two times* *italic in a row.* **Finally, this is also bold, but with the strong tag.** *We can do the same with em.*
"""


html_headers = """<html>
    <body>
        <h1>Different Headers</h1>
        <p>This is a paragraph.</p>
        <h2>Second header</h2>
        <p>This is a paragraph.</p>
        <h3>Third header</h3>
        <h4>Forth header</h4>
        <p>This is a paragraph.</p>
        <h2>Again second header</h2>
    </body>
</html>
"""
markdown_headers = """# Different Headers

This is a paragraph.

## Second header

This is a paragraph.

### Third header

### Forth header

This is a paragraph.

## Again second header
"""



html_lists = """<html>
    <body>
        <ul>
            <li>This is a list</li>
            <li>With <b>some</b> items</li>
        </ul>
        <ol>
            <li>And another list.</li>
            <li>This is an <i>ordered list</i> this time.</li>
        </ol>
    </body>
</html>
"""
markdown_lists = """- This is a list
- With **some**items


- And another list.
- This is an *ordered list*this time.
"""


html_tables = """<html>
    <body>
        <table>
            <tr>
                <th>Header 1</th>
                <th>Header 2</th>
                <th>Header 3</th>
                <th>Header 4</th>
            </tr>
            <tr>
                <td>Foo1</td>
                <td>Foo2 <i>with italic</i> text</td>
                <td><p>Foo3 with paragraph</p></td>
                <td>Foo4</td>
            </tr>
        </table>
        <br>
        <table>
            <tr>
                <td>No header</td>
                <td>Table has no header</td>
                <td>There is no header.</td>
            </tr>
            <tr>
                <td>Foo1</td>
                <td>Foo2</td>
                <td>Foo3</td>
            </tr>
        </table>
    </body>
</html>
"""
markdown_tables = """| Header 1 |Header 2 |Header 3 |Header 4 |
| --- | --- | --- | --- |

| Foo1 |Foo2 *with italic*text | Foo3 with paragraph |Foo4 |
| --- | --- | --- | --- |





| No header |Table has no header |There is no header. |
| --- | --- | --- |

| Foo1 |Foo2 |Foo3 |
| --- | --- | --- |


"""



html_links = """<html>
    <body>
        <p>
            <a href="http://foo.bar">This is a link with text.</a>
            This is a link without text: <a href="http://foo.bar"></a><br>
            With in<a href="http://foo.bar">this link <b>we have bold</b> parts.</a> And...<br>
            Finally, this link <a>has no href</a>.
        </p>
    </body>
</html>
"""
markdown_links = """[This is a link with text.](http://foo.bar) This is a link without text:

With in [this link](http://foo.bar)  **we have bold** [parts.](http://foo.bar) And...

Finally, this link has no href .
"""


html_img = """<html>
    <body>
        <p>
            This is an image:
            <img src="foo.bar"/>
            With forgotten end tag:
            <img src="foo.bar">
            With missing source:
            <img/>
        </p>
    </body>
</html>
"""
markdown_img_ignore = """This is an image: [image] With forgotten end tag: [image] With missing source: [image]
"""
markdown_img_describe = """This is an image: [image: foo.bar) With forgotten end tag: [image: foo.bar) With missing source: [image: Unnamed]
"""
markdown_img_reference = """This is an image: [image](foo.bar) With forgotten end tag: [image](foo.bar) With missing source: [image]
"""


html_ignored_stuff = """<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <title>The Title</title>
        <script>
            let x = 5;
        </script>
        <!-- This comment should be ignored -->
    </head>
    <body>
        <p>
            This is some text.
            <!-- This comment should be ignored -->
        </p>
        <meta content="foo">
        <p>
            Here we have italic <i>Foo</i>
            <script>
                let x = 5;
            </script>
            <button>Some button.</button>
        </p>
        <form>
            <input type="text">
        </form>
    </body>
</html>
"""
markdown_ignored_stuff = """This is some text.

Here we have italic *Foo*
"""