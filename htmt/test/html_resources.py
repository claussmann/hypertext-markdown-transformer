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
        <p>Second paragraph</p>
        </div>
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
Second paragraph
"""