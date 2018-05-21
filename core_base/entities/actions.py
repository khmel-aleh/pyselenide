from selenium.webdriver import ActionChains

from core_base import get_driver


class Actions(ActionChains):

    def __init__(self, web_element, driver):
        self._web_element = web_element
        super(Actions, self).__init__(driver)

    def move_to_element(self, to_element=None):
        _element = to_element or self._web_element
        return super(Actions, self).move_to_element(to_element=_element)

    hover = move_to_element

    def click(self, on_element=None):
        _element = on_element or self._web_element
        return super(Actions, self).click(on_element=_element)

    def context_click(self, on_element=None):
        _element = on_element or self._web_element
        return super(Actions, self).context_click(on_element=_element)

    def click_and_hold(self, on_element=None):
        _element = on_element or self._web_element
        return super(Actions, self).click_and_hold(on_element=_element)

    def double_click(self, on_element=None):
        _element = on_element or self._web_element
        return super(Actions, self).double_click(on_element=_element)

    def drag_and_drop(self, source=None, target=None):
        _source = source or self._web_element
        return super(Actions, self).drag_and_drop(source=_source, target=target._web_element)

    def drag_and_drop_by_offset(self, source=None, xoffset=0, yoffset=0):
        _source = source or self._web_element
        return super(Actions, self).drag_and_drop_by_offset(source=_source, xoffset=xoffset, yoffset=yoffset)

    def key_down(self, value, element=True):
        _element = self._web_element if element else None
        return super(Actions, self).key_down(value=value, element=_element)

    def key_up(self, value, element=True):
        _element = element or self._web_element
        return super(Actions, self).key_up(value=value, element=_element)

    def move_by_offset(self, xoffset, yoffset):
        return super(Actions, self).move_by_offset(xoffset=xoffset, yoffset=yoffset)

    def move_to_element_with_offset(self, to_element=None, xoffset=0, yoffset=0):
        to_element = to_element or self._web_element
        return super(Actions, self).move_to_element_with_offset(to_element=to_element,
                                                                xoffset=xoffset, yoffset=yoffset)

    def pause(self, seconds):
        return super(Actions, self).pause(seconds=seconds)

    def release(self, on_element=True):
        _on_element = on_element or self._web_element
        return super(Actions, self).release(on_element=_on_element)

    @staticmethod
    def send_keys(*keys_to_send):
        print(get_driver())
        return ActionChains(driver=get_driver()).send_keys(*keys_to_send)

    def send_keys_to_element(self, element=None, *keys_to_send):
        _element = element or self._web_element
        return super(Actions, self).send_keys_to_element(element=_element, *keys_to_send)
