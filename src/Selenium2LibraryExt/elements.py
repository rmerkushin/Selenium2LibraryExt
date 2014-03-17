#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Roman Merkushin
# rmerkushin@ya.ru

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Elements(object):

    @property
    def driver(self):
        selenium2lib = BuiltIn().get_library_instance("Selenium2Library")
        return selenium2lib._current_browser()

    def get_elements_text(self, xpath):
        """
        Returns a list of text values ​​of elements identified by xpath.\n
        *Example usage:*
        | *Variable* | *Keyword* | *Argument* |
        | @{row_values} | Get Elements Text | //table[@id='staff']/tbody/tr[1] |
        *Example result:*\n
        INFO : @{row_values} = ['1', 'Vasiliy', 'Zayczev', 'zayczev@mail.com']
        """
        elements_text = []
        try:
            elements = self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            raise AssertionError("Element locator '" + xpath + "' did not match any elements.")
        for element in elements:
            elements_text.append(element.text)
        return elements_text

    def get_elements_attribute(self, xpath, attribute):
        """
        Returns a list of elements attribute identified by xpath.\n
        *Example usage:*
        | *Variable* | *Keyword* | *Argument* |
        | @{attributes_values} | Get Elements Attribute | //table[@id='calendar']/tbody//td | class |
        *Example result:*\n
        INFO : @{attributes_values} = ['calendar-selected', 'calendar-today', 'calendar-day', ... 'calendar-disabled']
        """
        elements_attributes = []
        try:
            elements = self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            raise AssertionError("Element locator '" + xpath + "' did not match any elements.")
        for element in elements:
            elements_attributes.append(element.get_attribute(attribute))
        return elements_attributes

    def get_element_computed_style(self, xpath, property_name):
        """
        Returns a CSS style object that represents the computed style for the element identified by xpath.\n
        *Example usage:*
        | *Variable* | *Keyword* | *Argument* | *Argument* |
        | ${display} | Get Element Computed Style | //div[@id='delete_confirm'] | display |
        *Example result:*\n
        INFO : ${display} = block
        """
        try:
            element = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            raise AssertionError("Element locator '" + xpath + "' did not match any elements.")
        return element.value_of_css_property(property_name)

    def get_elements_computed_style(self, xpath, property_name):
        """
        Returns a list of CSS style objects that represents the computed style for the elements identified by xpath.\n
        *Example usage:*
        | *Variable* | *Keyword* | *Argument* | *Argument* |
        | @{display} | Get Elements Computed Style | //tr//a[@class='delete_user'] | display |
        *Example result:*\n
        INFO : @{display} = ['block', 'none', 'block', 'block']
        """
        elements_properties = []
        try:
            elements = self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            raise AssertionError("Element locator '" + xpath + "' did not match any elements.")
        for element in elements:
            elements_properties.append(element.value_of_css_property(property_name))
        return elements_properties

    def wait_until_element_is_not_visible(self, xpath, timeout=5):
        """
        Waits until element specified with locator is hidden.\n
        Fails if _"timeout"_ expires before the element is hidden. Timeout should be specified in seconds.\n
        *Example usage:*
        | *Keyword* | *Argument* | *Argument* |
        | Wait Until Element Is Not Visible | //div[@id='delete_confirm'] | 10 |
        """
        wait = WebDriverWait(self.driver, timeout=int(timeout))
        message = "Element '%s' was not hidden in %s second(s)." % (xpath, str(timeout))
        wait.until_not(lambda driver: driver.find_element_by_xpath(xpath).is_displayed(), message=message)

    def wait_until_page_not_contain_element(self, xpath, timeout=5):
        """
        Waits until element specified with locator disappears on current page.\n
        Fails if _"timeout"_ expires before the element disappears. Timeout should be specified in seconds.\n
        *Example usage:*
        | *Keyword* | *Argument* | *Argument* |
        | Wait Until Page Not Contain Element | //table[@id='staff']/tbody/tr[1] | 10 |
        """
        wait = WebDriverWait(self.driver, timeout=int(timeout))
        message = "Element '%s' was not deleted from page in %s second(s)." % (xpath, str(timeout))
        wait.until_not(lambda driver: driver.find_element_by_xpath(xpath), message=message)