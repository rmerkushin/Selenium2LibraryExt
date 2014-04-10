#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 Roman Merkushin
# rmerkushin@ya.ru


class Table(object):

    def get_table_header(self, xpath, row_slice=None):
        """
        <p>Returns text of table header identified by xpath as list of lists.<br>
        <i>"row_slice"</i> argument allows to set slice of table row from i to j.</p>
        <p><b>Table example:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>№</b></td>
                    <td><b>Name</b></td>
                    <td><b>Surname</b></td>
                    <td><b>Login</b></td>
                    <td><b>E-mail</b></td>
                    <td><b>Phone</b></td>
                </tr>
            </thead>
            <tfoot>
                <tr>
                    <td colspan="5"><b>Total:</b></td>
                    <td><b>1</b></td>
                </tr>
            </tfoot>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>John</td>
                    <td>Malkovich</td>
                    <td>malkovich</td>
                    <td>malkovich@mail.com</td>
                    <td>+7-945-781-76-82</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>William</td>
                    <td>Wallace</td>
                    <td>wallace</td>
                    <td>wallace@mail.com</td>
                    <td>+7-923-631-45-21</td>
                </tr>
            </tbody>
        </table>
        <br>
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
                    <td>@{header_rows}</td>
                    <td>Get Table Header</td>
                    <td>//table[@id='staff']</td>
                    <td>1:5</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : @{header_rows} = [["Name", "Surname", "Login", "E-mail"]]</p>
        """
        pass

    def get_table_rows(self, xpath, row_slice=None):
        """
        <p>Returns text of table rows identified by xpath as list of lists.<br>
        <i>"row_slice"</i> argument allows to set slice of table row from i to j.</p>
        <p><b>Table example:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>№</b></td>
                    <td><b>Name</b></td>
                    <td><b>Surname</b></td>
                    <td><b>Login</b></td>
                    <td><b>E-mail</b></td>
                    <td><b>Phone</b></td>
                </tr>
            </thead>
            <tfoot>
                <tr>
                    <td colspan="5"><b>Total:</b></td>
                    <td><b>1</b></td>
                </tr>
            </tfoot>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>John</td>
                    <td>Malkovich</td>
                    <td>malkovich</td>
                    <td>malkovich@mail.com</td>
                    <td>+7-945-781-76-82</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>William</td>
                    <td>Wallace</td>
                    <td>wallace</td>
                    <td>wallace@mail.com</td>
                    <td>+7-923-631-45-21</td>
                </tr>
            </tbody>
        </table>
        <br>
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
                    <td>@{table_rows}</td>
                    <td>Get Table Rows</td>
                    <td>//table[@id='staff']</td>
                    <td>1:5</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : @{table_rows} = [["John", "Malkovich", "malkovich", "malkovich@mail.com"], ["William", "Wallace", "wallace", "wallace@mail.com"]]</p>
        """
        pass

    def get_table_footer(self,  xpath, row_slice=None):
        """
        <p>Returns text of table footer identified by xpath as list of lists.<br>
        <i>"row_slice"</i> argument allows to set slice of table row from i to j.</p>
        <p><b>Table example:</b></p>
        <table>
            <thead>
                <tr>
                    <td><b>№</b></td>
                    <td><b>Name</b></td>
                    <td><b>Surname</b></td>
                    <td><b>Login</b></td>
                    <td><b>E-mail</b></td>
                    <td><b>Phone</b></td>
                </tr>
            </thead>
            <tfoot>
                <tr>
                    <td colspan="5"><b>Total:</b></td>
                    <td><b>1</b></td>
                </tr>
            </tfoot>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>John</td>
                    <td>Malkovich</td>
                    <td>malkovich</td>
                    <td>malkovich@mail.com</td>
                    <td>+7-945-781-76-82</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>William</td>
                    <td>Wallace</td>
                    <td>wallace</td>
                    <td>wallace@mail.com</td>
                    <td>+7-923-631-45-21</td>
                </tr>
            </tbody>
        </table>
        <br>
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
                    <td>@{footer_rows}</td>
                    <td>Get Table Footer</td>
                    <td>//table[@id='staff']</td>
                </tr>
            </tbody>
        </table>
        <p><b>Example result:</b><br>
        INFO : @{footer_rows} = [["Total", "1"]]</p>
        """
        pass