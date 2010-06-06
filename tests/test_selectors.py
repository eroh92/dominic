# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# <dominic - python-pure implementation of CSS Selectors>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
from os.path import join, dirname, abspath
from sure import that, that_with_context

from dominic import DOM, Element

def set_html(context):
    fobj = open(join(abspath(dirname(__file__)), "fixtures.html"))
    context.html = fobj.read()
    fobj.close()

@that_with_context(set_html)
def select_paragraphs(context):
    "dominic selecting paragraphs"
    dom = DOM(context.html)

    identifiers = ["firstp", "ap", "sndp", "en", "sap", "first"]
    paragraphs = dom.find("p")

    assert that(dom).is_a(DOM)
    for identifier, paragraph in zip(identifiers, paragraphs):
        assert that(paragraph.attribute['id']).equals(identifier)

@that_with_context(set_html)
def select_html(context):
    "dominic selecting html"
    dom = DOM(context.html)

    html = dom.get("html")
    assert that(html).is_a(Element)
    assert that(html.attribute['id']).equals("html")
