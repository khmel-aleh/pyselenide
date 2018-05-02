from selenium.webdriver.common.by import By


class Locator(object):
    def __init__(self, by=None, value=None):
        self.by = by
        self.value = value


class ID(Locator):
    def __init__(self, value=None):
        super(ID, self).__init__(By.ID, value)


class Css(Locator):
    def __init__(self, value=None):
        super(Css, self).__init__(By.CSS_SELECTOR, value)


class ClassName(Locator):
    def __init__(self, value=None):
        super(ClassName, self).__init__(By.CLASS_NAME, value)


class LinkText(Locator):
    def __init__(self, value=None):
        super(LinkText, self).__init__(By.LINK_TEXT, value)


class PartialLinkText(Locator):
    def __init__(self, value=None):
        super(PartialLinkText, self).__init__(By.PARTIAL_LINK_TEXT, value)


class TagName(Locator):
    def __init__(self, value=None):
        super(TagName, self).__init__(By.TAG_NAME, value)


class Name(Locator):
    def __init__(self, value=None):
        super(Name, self).__init__(By.NAME, value)


class XPath(Locator):
    def __init__(self, value=None):
        super(XPath, self).__init__(By.XPATH, value)
