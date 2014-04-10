#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Roman Merkushin
# rmerkushin@ya.ru

from robot.libraries.BuiltIn import BuiltIn


class Driver(object):

    @property
    def driver(self):
        selenium2lib = BuiltIn().get_library_instance("Selenium2Library")
        return selenium2lib._current_browser()