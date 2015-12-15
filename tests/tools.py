#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-14 21:37:52
# @Author  : 马俊杰 (mjjsojava@163.com)
# @Link    :

from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None, headers=None, status="200"):

    assert status in resp.status, "Expected response %r not in %r"  % (status, resp.status)

    if status == "200":
        assert resp.data, "Response data is empty."

    if contains:
        assert contains in resp.data, "Response does not contains %r" % contains

    if matches:
        reg = re.compile(matches)
        assert reg.matches(resp.data), "Response does not match %r " % matches

    if headers:
        assert_equal(resp.headers, headers)

