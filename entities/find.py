from selenium.webdriver.remote.webelement import WebElement

from rf_libs import get_driver
from entities.htmlelement import HtmlElement
from entities.wait import until_html_element_visible
from utils.loggers import logger


class All(object):
    def __init__(self, element_type=WebElement, locator=None,
                 waiter=until_html_element_visible):
        self.element_type = element_type
        self.locator = locator
        self.waiter = waiter

    def __get__(self, instance, owner):
        self.parent = instance
        logger.info("Getting elements {0} in {1}".format(self.element_type,
                                                         self.parent))
        return self._find_elements()

    def _find_elements(self):
        if isinstance(self.parent, HtmlElement):
            finder = self.parent._web_element
        else:
            finder = get_driver()
        self.waiter(finder=finder, locator=self.locator)
        web_elements = finder.find_elements(self.locator.by,
                                            self.locator.value)
        if issubclass(self.element_type, WebElement):
            return web_elements
        else:
            return [self.element_type(web_element=webelement)
                    for webelement in web_elements]
