# dominic
> Version 0.1 (unreleased)

# What

python-pure implementation of CSS selectors, and DOM traversing

# Basic usage

## install:

    user@machine:~$ [sudo] pip install dominic

## documentation

    from dominic import DOM

    html = """<html>
      <head>
        <title>My Title</title>
      </head>
      <body>
        <p class="paragraph" id="main">Hello!</p>
        <input type="text" id="string" value="value" />
        <div class="one two three">
          <span id="the-span">text here!</span>
        </div>
      </body>
    </html>"""

    dom = DOM(html)

    body_elements = dom.find("body *")

    assert body_elements.length is 4

    p1 = for p in dom.find("p")[0]
    p2 = for p in dom.find("p").first()

    p3 = for p in dom.find("#main").first()
    p4 = for p in dom.find(".paragraph").first()

    assert p1.text() == p2.text()
    assert p2.text() == p3.text()
    assert p3.text() == p4.text()
    assert p4.text() == "Hello!"
    assert p4.html() == "<p class="paragraph" id="main">Hello!</p>"

    span = dom.find("div.one.two.three > span#the-span").first()

    assert span.text() == 'text here!'

    assert span.text('reflect changes')

    assert span.text() == 'reflect changes'
    assert span.html() == '<span id="the-span">reflect changes</span>'

    assert dom.html() == """<html>
      <head>
        <title>My Title</title>
      </head>
      <body>
        <p class="paragraph" id="main">Hello!</p>
        <input type="text" id="string" value="value" />
        <div class="one two three">
          <span id="the-span">reflect changes</span>
        </div>
      </body>
    </html>"""

# Why ?

As a webdeveloper I have to handle HTML nodes within python code all
the time.

Hence this I love [lxml](http://codespeak.net/lxml/) and have a
extensively use of it's
[CSSSelector](http://codespeak.net/lxml/cssselect.html), I mean,
totally.

Althrough, lxml is built with
[C-based](http://www.python.org/doc/ext/intro.html) python extensions,
and whenever I need to use it in a sandboxed environment,
[Google App Engine](http://code.google.com/p/googleappengine/issues/detail?id=18),
for example, I cannot use lxml.

So that, when I've met
[py-dom-xpath](http://code.google.com/p/py-dom-xpath/), I decided to
write my own python implementation of CSSSelector, which translates
into xpath paths.

# Inspiration and thanks

dominic's test suite is a python port of sizzle's test suite.

thanks to [@jeresig](http://github.com/jeresig) for its **TERRIFIC** work
on [sizzle](http://github.com/jeresig/sizzle), such a clean and
easy-to-understand test suite.

thanks to [py-dom-xpath](http://code.google.com/p/py-dom-xpath/) crew,
it rocks out loud!

# contribute!

**install dependencies**

    user@machine:~$ [sudo] pip install sure

**run tests**

    user@machine:~Projects/dominic$ make test

# license

dominic is under MIT license, so that it can be embedded into your
project, and ran within your sandbox. It can also be put together with
[py-dom-xpath](http://code.google.com/p/py-dom-xpath/)

    Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
