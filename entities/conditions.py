import time
from abc import ABCMeta

from selenium.webdriver.remote.webdriver import WebDriver

from entities.htmlelement import HtmlElement
from entities.errors import ParameterError
from rf_libs import get_config
from utils.loggers import logger, levels

_wait_timeout = get_config().project.wait_timeout
_log_level = get_config().project.condition_log_level


class ICondition(object):
    __meta__ = ABCMeta

    @property
    def description(self):
        return self.__class__.__name__

    def __init__(self, timeout=_wait_timeout, sleep_time=0.1, log_level=_log_level):
        self._timeout = timeout
        self._sleep_time = sleep_time
        log_level = log_level.upper()
        if log_level in levels:
            self._log_level = log_level
        else:
            self._log_level = 'DEBUG'

    def wait_until(self, element=None):
        start_time = time.time()
        while time.time() < start_time + self._timeout:
            if not self.check(element):
                time.sleep(self._sleep_time)
            else:
                logger.log('Condition "%s" met' % self.description, level=self._log_level)
                return True
        raise TimeoutError('Condition "%s" not met' % self.description)


class IHtmlElCondition(ICondition):
    __meta__ = ABCMeta

    def check(self, _object):
        if not isinstance(_object, HtmlElement):
            raise ParameterError('%s should be instance of %s' % (object, HtmlElement))


class IBrowserCondition(ICondition):
    __meta__ = ABCMeta

    def check(self, _object):
        if not isinstance(_object, WebDriver):
            raise ParameterError('%s should be instance of %s' % (_object, WebDriver))


class Have(object):

    @staticmethod
    def value(value, strict=False, *args, **kwargs):
        return ValueCondition(value, strict=strict, *args, **kwargs)

    @staticmethod
    def title(value, strict=False, *args, **kwargs):
        return TitleCondition(value, strict=strict, *args, **kwargs)

    @staticmethod
    def url(value, strict=False, *args, **kwargs):
        return UrlCondition(value, strict=strict, *args, **kwargs)


class Be(object):

    @staticmethod
    def visible(*args, **kwargs):
        return VisibleCondition(*args, **kwargs)

    displayed = visible



have = Have
be = Be


class ValueCondition(IHtmlElCondition):

    def __init__(self, text, strict, *args, **kwargs):
        self._text = text
        self._strict = strict
        super(ValueCondition, self).__init__(*args, **kwargs)

    def check(self, html_element):
        super(ValueCondition, self).check(html_element)
        if self._strict:
            return self._text == html_element.text
        else:
            return self._text in html_element.text

    @property
    def description(self):
        return 'Text "%s" in value' % self._text


class VisibleCondition(IHtmlElCondition):

    def check(self, html_element):
        super(VisibleCondition, self).check(html_element)
        return html_element._web_element.is_displayed()

    @property
    def description(self):
        return 'Element is visible'


class TitleCondition(IBrowserCondition):

    def __init__(self, exp_title, strict, *args, **kwargs):
        self._exp_title = exp_title
        self._strict = strict
        super(TitleCondition, self).__init__(*args, **kwargs)

    def check(self, browser):
        super(TitleCondition, self).check(browser)
        if self._strict:
            return self._exp_title == browser.title
        else:
            return self._exp_title in browser.title

    @property
    def description(self):
        return 'Browser has "%s" title' % self._exp_title


class UrlCondition(IBrowserCondition):

    def __init__(self, exp_url, strict, *args, **kwargs):
        self._exp_url = exp_url
        self._strict = strict
        super(UrlCondition, self).__init__(*args, **kwargs)

    def check(self, browser):
        super(UrlCondition, self).check(browser)
        if self._strict:
            return self._exp_url == browser.current_url
        else:
            return self._exp_url in browser.current_url

    @property
    def description(self):
        return 'Browser has "%s" url' % self._exp_url
