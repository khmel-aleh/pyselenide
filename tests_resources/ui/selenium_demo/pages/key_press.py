from time import sleep

from entities.elements import Text
from entities.locators import ID
from entities.conditions import have
from entities.actions import Actions

from rf_libs import get_driver


class SDKeyPress(object):

    result = Text(ID('result'), timeout=30)

    def key_press(self, key):
        try:
            a = get_driver()
        except Exception as e:
            print('Got exception')
            print(e)
        print(a)

        Actions.send_keys(key).perform()
        # sleep(2)
        self.result.should(have.value('You entered: ' + key, timeout=3))
        # sleep(2)
