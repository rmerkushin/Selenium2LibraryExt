#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Roman Merkushin
# rmerkushin@ya.ru


class Elements(object):

    def get_elements_text(self, xpath):
        """
        <p>Returns a list of text values ​​of elements identified by xpath.</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Variable</b></td>
                    <td><b>Keyword</b></td>
                    <td><b>Argument</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>@{row_values}</td>
                    <td>Get Elements Text</td>
                    <td>//table[@id='staff']/tbody/tr[1]</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : @{row_values} = ['1', 'Vasiliy', 'Zayczev', 'zayczev@mail.com']</p>
        """
        pass

    def get_elements_attribute(self, xpath, attribute):
        """
        <p>Returns a list of elements attribute identified by xpath.</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Variable</b></td>
                    <td><b>Keyword</b></td>
                    <td><b>Argument</b></td>
                    <td><b>Argument</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>@{attributes_values}</td>
                    <td>Get Elements Attribute</td>
                    <td>//table[@id='calendar']/tbody//td</td>
                    <td>class</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : @{attributes_values} = ['calendar-selected', 'calendar-today', 'calendar-day', ... 'calendar-disabled']</p>
        """
        pass

    def get_element_computed_style(self, xpath, property_name):
        """
        <p>Returns a CSS style object that represents the computed style for the element identified by xpath.</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Variable</b></td>
                    <td><b>Keyword</b></td>
                    <td><b>Argument</b></td>
                    <td><b>Argument</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>${display}</td>
                    <td>Get Element Computed Style</td>
                    <td>//div[@id='delete_confirm']</td>
                    <td>display</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : ${display} = block</p>
        """
        pass

    def get_elements_computed_style(self, xpath, property_name):
        """
        <p>Returns a list of CSS style objects that represents the computed style for the elements identified by xpath.</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Variable</b></td>
                    <td><b>Keyword</b></td>
                    <td><b>Argument</b></td>
                    <td><b>Argument</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>@{display}</td>
                    <td>Get Elements Computed Style</td>
                    <td>//tr//a[@class='delete_user']</td>
                    <td>display</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : @{display} = ['block', 'none', 'block', 'block']</p>
        """
        pass

    def wait_until_element_is_not_visible(self, xpath, timeout=5):
        """
        <p>Waits until element specified with locator is hiding.<br>
        Fails if <i>"timeout"</i> expires before the element is hidden. Timeout should be specified in seconds.</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Keyword</b></td>
                    <td><b>Argument</b></td>
                    <td><b>Argument</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Wait Until Element Is Not Visible</td>
                    <td>//div[@id='delete_confirm']</td>
                    <td>10</td>
                </tr>
            </tbody>
        </table>
        """
        pass

    def wait_until_page_not_contain_element(self, xpath, timeout=5):
        """
        <p>Waits until element specified with locator disappears on current page.<br>
        Fails if <i>"timeout"</i> expires before the element disappears. Timeout should be specified in seconds.</p>
        <p><b>Example usage:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>Keyword</b></td>
                    <td><b>Argument</b></td>
                    <td><b>Argument</b></td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Wait Until Page Not Contain Element</td>
                    <td>//table[@id='staff']/tbody/tr[1]</td>
                    <td>10</td>
                </tr>
            </tbody>
        </table>
        """
        pass