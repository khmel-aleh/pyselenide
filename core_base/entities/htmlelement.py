import core_base.entities.wait as wait
from core_base import get_driver, get_config
from core_base.entities.actions import Actions


wait_timeout = get_config().project.wait_timeout


class HtmlElement(object):

    def __init__(self, locator, waiter=wait.until_html_element_visible, timeout=wait_timeout):
        self._locator = locator
        self._waiter = waiter
        self._timeout = timeout
        self._parent = None
        self._web_element = None
        self._finder = None
        self._actions = None

    @property
    def locator(self):
        return self._locator.by, self._locator.value

    @property
    def actions(self):
        if self._actions is None:
            self._actions = Actions(self._web_element, get_driver())
        return self._actions

    def __get__(self, instance, owner):
        self._parent = instance
        self._web_element = self._find_element()
        return self

    def _find_element(self):
        finder = self.get_finder()
        self._waiter(finder=finder, locator=self._locator, timeout=self._timeout)
        return finder.find_element(self._locator.by, self._locator.value)

    def get_finder(self):
        if isinstance(self._parent, HtmlElement):
            return self._parent._web_element
        else:
            return get_driver()

    def execute_script(self, script):
        self._web_element.execute_script(script)

    def scroll_to_element(self):
        get_driver().execute_script('return arguments[0].scrollIntoView();', self._web_element)
        return self

    def submit(self):
        with wait.for_page_load(10):
            self._web_element.submit()
        return self

    def should(self, condition):
        condition.wait_until(self)
        return self
