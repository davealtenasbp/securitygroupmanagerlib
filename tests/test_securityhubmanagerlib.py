#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: test_securitygroupmanagerlib.py
#
# Copyright 2023 Dave Altena
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#

"""
test_securitygroupmanagerlib
----------------------------------
Tests for `securitygroupmanagerlib` module.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

from betamax.fixtures import unittest

__author__ = '''Dave Altena <daltena@schubergphilis.com>'''
__docformat__ = '''google'''
__date__ = '''01-06-2023'''
__copyright__ = '''Copyright 2023, Dave Altena'''
__credits__ = ["Dave Altena"]
__license__ = '''MIT'''
__maintainer__ = '''Dave Altena'''
__email__ = '''<daltena@schubergphilis.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".


class Testsecuritygroupmanagerlib(unittest.BetamaxTestCase):

    def setUp(self):
        """
        Test set up

        This is where you can setup things that you use throughout the tests. This method is called before every test.
        """
        pass

    def tearDown(self):
        """
        Test tear down

        This is where you should tear down what you've setup in setUp before. This method is called after every test.
        """
        pass
