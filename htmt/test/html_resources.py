html1 = """<html>
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
        <p>Foo<br/>Bar</p>
        <img src="/foo/bar"/>
        <p>
            Please see <a href="https://bar/foo">My Link</a> for details.
            Note, there are also <a>defective links.</a>
        </p>
        <h2>This is a secondary title</h2>
        <p>
            Second paragraph
            <i>some italic text</i>
            <b>some bold text</b>
            <i>some <b>bold and italic</b>text</i>
            <b><i>Bold and italic</i></b>
            <i>two times</i><i>italic.</i>

            <ul>
                <li>And we have a list</li>
                <li>With <b>some</b> items</li>
            </ul>
            <ol>
                <li>And another list.</li>
                <li>This is an <a href="foo.bar">ordered list</a> this time.</li>
            </ol>
        </p>
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
                <td>Foo4 and <a href="#">a link in it</a></td>
            </tr>
        </table>
        </div>
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

makrdown1 = """# My Title

***

Foo

Bar

(image available in original ressource)

Please see [My Link](https://bar/foo) for details. Note, there are also defective links.

## This is a secondary title

Second paragraph *some italic text* **some bold text** *some **bold and italic**text* ***Bold and italic*** *two times* *italic.*

- And we have a list
- With **some**items


- And another list.
- This is an [ordered list](foo.bar) this time.

| Header 1 |Header 2 |Header 3 |Header 4 |
| --- | --- | --- | --- |

| Foo1 |Foo2 *with italic*text |Foo3 with paragraph |Foo4 and [a link in it](#)  |
| --- | --- | --- | --- |



| No header |Table has no header |There is no header. |
| --- | --- | --- |

| Foo1 |Foo2 |Foo3 |
| --- | --- | --- |


"""