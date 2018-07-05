from time import sleep
from entities.elements import Text, Image
from entities.locators import ID, XPath


class SeleniumDemoDragAndDrop(object):

    column_a = Text(ID("column-a"), timeout=30)
    column_b = Text(ID("column-b"), timeout=30)

    def do_drag_and_drop(self):
        self.column_a.actions.drag_and_drop(target=self.column_b).perform()
        sleep(2)
