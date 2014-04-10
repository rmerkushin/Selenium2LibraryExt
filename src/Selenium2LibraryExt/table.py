#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Roman Merkushin
# rmerkushin@ya.ru

from selenium.common.exceptions import NoSuchElementException


class Table(object):

    def get_table_header(self, xpath, row_slice=None):
        """
        Returns text of table header identified by xpath as list of lists.\n
        _"row_slice"_ argument allows to set slice of table row from i to j.\n
        *Table example:*
        | *№* | *Name* | *Surname* | *Login* | *E-mail* | *Phone* |
        | 1 | John | Malkovich | malkovich | malkovich@mail.com | +7-945-781-76-82 |
        | 2 | William | Wallace | wallace | wallace@mail.com | +7-923-631-45-21 |
        | | | | | *Total:* | *1* |
        *Example usage:*
        | *Variable* | *Keyword* | *Argument* | *Argument* |
        | @{header_rows} | Get Table Header | //table[@id='staff'] | 1:5 |
        *Example result:*\n
        INFO : @{header_rows} = [["Name", "Surname", "Login", "E-mail"]]
        """
        try:
            table = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            raise AssertionError("Element locator '" + xpath + "' did not match any elements.")
        rows = table.find_elements_by_xpath("./thead/tr")
        rows_arr = []
        for row in rows:
            cells_arr = []
            cells = row.find_elements_by_xpath("./td")
            if row_slice:
                _slice = row_slice.split(":")
                cells = cells[int(_slice[0]):int(_slice[1])]
            for cell in cells:
                cells_arr.append(cell.text)
            rows_arr.append(cells_arr)
        return rows_arr

    def get_table_rows(self, xpath, row_slice=None):
        """
        Returns text of table rows identified by xpath as list of lists.\n
        _"row_slice"_ argument allows to set slice of table row from i to j.\n
        *Table example:*
        | *№* | *Name* | *Surname* | *Login* | *E-mail* | *Phone* |
        | 1 | John | Malkovich | malkovich | malkovich@mail.com | +7-945-781-76-82 |
        | 2 | William | Wallace | wallace | wallace@mail.com | +7-923-631-45-21 |
        | | | | | *Total:* | *1* |
        *Example usage:*
        | *Variable* | *Keyword* | *Argument* | *Argument* |
        | @{table_rows} | Get Table Rows | //table[@id='staff'] | 1:5 |
        *Example result:*\n
        INFO : @{table_rows} = [["John", "Malkovich", "malkovich", "malkovich@mail.com"], ["William", "Wallace", "wallace", "wallace@mail.com"]]
        """
        try:
            table = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            raise AssertionError("Element locator '" + xpath + "' did not match any elements.")
        rows = table.find_elements_by_xpath("./tbody/tr")
        rows_arr = []
        for row in rows:
            cells_arr = []
            cells = row.find_elements_by_xpath("./td")
            if row_slice:
                _slice = row_slice.split(":")
                cells = cells[int(_slice[0]):int(_slice[1])]
            for cell in cells:
                cells_arr.append(cell.text)
            rows_arr.append(cells_arr)
        return rows_arr

    def get_table_footer(self,  xpath, row_slice=None):
        """
        Returns text of table footer identified by xpath as list of lists.\n
        _"row_slice"_ argument allows to set slice of table row from i to j.\n
        *Table example:*
        | *№* | *Name* | *Surname* | *Login* | *E-mail* | *Phone* |
        | 1 | John | Malkovich | malkovich | malkovich@mail.com | +7-945-781-76-82 |
        | 2 | William | Wallace | wallace | wallace@mail.com | +7-923-631-45-21 |
        | | | | | *Total:* | *1* |
        *Example usage:*
        | *Variable* | *Keyword* | *Argument* | *Argument* |
        | @{footer_rows} | Get Table Rows | //table[@id='staff'] | |
        *Example result:*\n
        INFO : @{footer_rows} = [["Total", "1"]]
        """
        try:
            table = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            raise AssertionError("Element locator '" + xpath + "' did not match any elements.")
        rows = table.find_elements_by_xpath("./tfoot/tr")
        rows_arr = []
        for row in rows:
            cells_arr = []
            cells = row.find_elements_by_xpath("./td")
            if row_slice:
                _slice = row_slice.split(":")
                cells = cells[int(_slice[0]):int(_slice[1])]
            for cell in cells:
                cells_arr.append(cell.text)
            rows_arr.append(cells_arr)
        return rows_arr