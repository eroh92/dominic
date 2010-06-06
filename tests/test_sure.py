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

import sure
from sure import that
from threading import local
from nose.tools import assert_equals

def test_setup_with_context():
    "sure.with_context() runs setup before the function itself"

    def setup(context):
        context.name = "John Resig"

    @sure.that_with_context(setup)
    def john_is_within_context(context):
        assert isinstance(context, local)
        assert hasattr(context, "name")

    john_is_within_context()
    assert_equals(
        john_is_within_context.__name__,
        'test_john_is_within_context'
    )

def test_teardown_with_context():
    "sure.with_context() runs teardown before the function itself"

    class something:
        pass

    def setup(context):
        something.modified = True

    def teardown(context):
        del something.modified

    @sure.that_with_context(setup, teardown)
    def something_was_modified(context):
        assert hasattr(something, "modified")
        assert something.modified

    something_was_modified()
    assert not hasattr(something, "modified")

def test_that_is_a():
    "sure.that() is_a(object)"

    something = "something"

    assert that(something).is_a(str)
    assert isinstance(something, str)

def test_that_equals():
    "sure.that() equals(object)"

    something = "something"

    assert that(something).equals(something)
    assert something == something

def test_that_differs():
    "sure.that() differs(object)"

    something = "something"

    assert that(something).differs("23123%FYTUGIHOfdf")
    assert something != "23123%FYTUGIHOfdf"

def test_that_has():
    "sure.that() has(object)"

    class Class:
        name = "some class"
    Object = Class()
    dictionary = {
        'name': 'John'
    }
    name = "john"

    assert hasattr(Class, 'name')
    assert that(Class).has("name")
    assert that(Class).like("name")
    assert "name" in sure.that(Class)

    assert hasattr(Object, 'name')
    assert that(Object).has("name")
    assert that(Object).like("name")
    assert "name" in sure.that(Object)

    assert dictionary.has_key('name')
    assert that(dictionary).has("name")
    assert that(dictionary).like("name")
    assert "name" in sure.that(dictionary)

    assert that(name).has("john")
    assert that(name).like("john")
    assert "john" in sure.that(name)
    assert that(name).has("hn")
    assert that(name).like("hn")
    assert "hn" in sure.that(name)
    assert that(name).has("jo")
    assert that(name).like("jo")
    assert "jo" in sure.that(name)
