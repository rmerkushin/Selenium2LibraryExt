#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Roman Merkushin
# rmerkushin@ya.ru

from driver import Driver
from elements import Elements
from table import Table

__version__ = "v0.1.1"


class Selenium2LibraryExt(Driver, Elements, Table):

    """
    The Robot Framework Selenium2LibraryExt is a library which extends Selenium2Library by some new keywords.
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"