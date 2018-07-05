from entities.elements import TextInput
from entities.locators import ID
from entities.conditions import be, have
from rf_libs.DriverProvider import DriverProvider



class GooglePage(object):

    search_input = TextInput(ID("lst-ib"), timeout=30)

    def search(self, txt):
        self.search_input.should(be.displayed()).type(txt).submit()

    def check_query_text(self, text_to_check):
        self.search_input.should(have.value(text_to_check, timeout=1))

    def check_browser_title(self, text_to_check):
        DriverProvider.should(have.title(text_to_check, timeout=1))

    def check_browser_url(self, text_to_check):
        DriverProvider.should(have.url(text_to_check, timeout=1))