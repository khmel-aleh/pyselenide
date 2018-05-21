from abc import ABCMeta
from inspect import isclass

import core_base.entities.wait as wait
from core_base.entities.htmlelement import HtmlElement
from core_base import get_driver, get_config

wait_timeout = get_config().project.wait_timeout


class Fillable(object):
    """
    Abstract class for elements that have common method ``fill`` used in 'fill-fields' loops
    """
    __metaclass__ = ABCMeta

    @property
    def class_dict(self):
        return self.__class__.__dict__

    def _get_element(self, element_name):
        return self.class_dict[element_name].__get__(self, self.__class__)

    def _get_names(self):
        names = [attr_name for attr_name, value in self.class_dict.items()
                 if isinstance(value, (HtmlElement, Fillable))]
        return names

    def fill(self, data):
        """
        :param data: dictionary with elements names as keys and fillable data as values
        """

        if isclass(self):
            raise RuntimeError(
                'Should instantiate from {} class'.format(self.__name__))

        names = self._get_names()

        for k, v in data.items():
            if k in names and v is not None:
                self._get_element(k).fill(v)

    def get_state(self):
        return {el_name: self._get_element(el_name).get_state() for el_name in self._get_names()}


class Clicking(object):
    """
    HtmlElement mixin
    """
    def click(self):
        with wait.for_page_load(10):
            self.scroll_to_element()._web_element.click()
        return self

    def js_click(self):
        with wait.for_page_load(10):
            self.scroll_to_element()
            get_driver().execute_script('return arguments[0].click();', self._web_element)
        return self
