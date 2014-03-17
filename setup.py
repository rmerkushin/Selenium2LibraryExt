#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
version = open("VERSION.txt").read()

setup(name="robotframework-selenium2libraryext",
      version=version,
      description="Selenium2LibraryExt library for Robot Framework",
      author="Roman Merkushin",
      author_email="rmerkushin@ya.ru",
      url="https://github.com/rmerkushin/Selenium2LibraryExt",
      package_dir={ "" : "src" },
      packages=["Selenium2LibraryExt"]
)
