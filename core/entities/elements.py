from contextlib import suppress
from random import choice

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select as WebDriverSelect

from core.entities.mixins import Fillable, Clicking
from core.entities.htmlelement import HtmlElement
from core.utils.helpers import random_value_from_list_not_contains_value


class Button(Clicking, HtmlElement):
    pass

class CheckBox(Clicking, HtmlElement, Fillable):
    def click(self):
        self.js_click()

    def is_checked(self):
        """
        :return: ``True`` if checkbox is checked, ``False`` if not
        """
        return self._web_element.is_selected()

    def check(self):
        if not self.is_checked():
            self.click()

    def uncheck(self):
        if self.is_checked():
            self.click()

    def js_check(self):
        if not self.is_checked():
            self.js_click()

    def js_unckeck(self):
        if self.is_checked():
            self.js_click()

    def fill(self, choice):
        """
        Derived from Fillable abstract class.
        :param choice: ``bool`` value, set it to ``True`` to check checkbox, to ``False`` - to uncheck
        :return: ``None``
        """
        if choice is True:
            self.check()
        else:
            self.uncheck()


class Image(Clicking, HtmlElement):
    @property
    def width(self):
        return self._web_element.size['width']

    @property
    def height(self):
        return self._web_element.size['height']

    def has_size(self):
        return self.width > 0 and self.height > 0

    @property
    def alternate_text(self):
        """
        Returns value of ``alt`` attribute:
        """
        return self._web_element.get_attribute('alt')


class Link(Clicking, HtmlElement):
    def get_href(self):
        self._web_element.get_attribute('href')

    @property
    def text(self):
        return self._web_element.text


class Select(HtmlElement, Fillable):

    @property
    def first_selected_option(self):
        return WebDriverSelect(self._web_element).first_selected_option

    @property
    def current_option(self):
        with suppress(NoSuchElementException):
            return self.first_selected_option.text
        return None

    @property
    def current_option_value(self):
        with suppress(NoSuchElementException):
            return self.first_selected_option.get_attribute('value')
        return None

    def get_values(self):
        options = self._web_element.find_elements(By.CSS_SELECTOR, "option")
        if not options:
            return None
        return [option.get_attribute('value') for option in options]

    def get_options(self):
        """
        Returns a list of all options as web elements
        """
        return WebDriverSelect(self._web_element).options

    def get_options_str_list(self):
        """
        Returns list of strings from ``option`` tags
        """
        options = self._web_element.find_elements(By.CSS_SELECTOR, "option")
        if not options:
            return None
        return [option.text for option in options]

    def select_random(self):
        with suppress(NoSuchElementException):
            self.first_selected_option.get_attribute('value')
            values = self.get_values()
            WebDriverSelect(self._web_element).select_by_value(choice(values))
        return None

    def select_random_not_current(self):
        with suppress(NoSuchElementException):
            current_value = self.first_selected_option.get_attribute('value')
            values = self.get_values()
            WebDriverSelect(self._web_element).select_by_value(
                random_value_from_list_not_contains_value(values, current_value))

    def select_by_visible_text(self, text):
        if text is not None:
            WebDriverSelect(self._web_element).select_by_visible_text(text)

    def select_by_value(self, value):
        WebDriverSelect(self._web_element).select_by_value(value)

    def select_by_index(self, index):
        WebDriverSelect(self._web_element).select_by_index(index)

    def fill(self, text, by='value'):
        if by == 'value':
            self.select_by_value(text)
        elif by == 'index':
            self.select_by_index(text)
        elif by == 'visible':
            self.select_by_visible_text(text)
        else:
            raise ValueError(
                    'Expected "value", "index" or "visible" by, not "%s"' % by)
        return self


class TextInput(HtmlElement, Fillable):
    def send_keys(self, text):
        self._web_element.send_keys(text)
        return self

    def clear(self):
        self._web_element.clear()
        return self

    def type(self, text):
        if text is not None:
            self.clear().send_keys(text)
        return self

    @property
    def text(self):
        return self._web_element.get_attribute('value')

    def fill(self, text):
        self.type(text)
        return self


class Text(Clicking, HtmlElement):
    @property
    def text(self):
        return self._web_element.text
