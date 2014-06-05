#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Roman Merkushin
# rmerkushin@ya.ru

from selenium.common.exceptions import NoSuchElementException


class Additional(object):

    def upload_file(self, xpath, file_path):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            element.send_keys(file_path)
        except NoSuchElementException:
            raise AssertionError("Element locator '" + xpath + "' did not match any elements.")