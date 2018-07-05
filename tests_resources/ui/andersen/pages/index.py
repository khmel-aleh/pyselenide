from entities.elements import Image, TextInput, Link, Text
from entities.locators import XPath, Name, ClassName, ID, PartialLinkText
from entities.find import All
from entities.htmlelement import HtmlElement
from rf_libs.DriverProvider import DriverProvider
from entities.conditions import be, have


class AndersenSite(object):

    find_devs_link = Link(PartialLinkText('Find Developers'), timeout=3)

    def hover_find_develops(self):
        self.find_devs_link.actions.hover().perform()

    def click_find_develops(self):
        self.find_devs_link.click()
        develops_url = 'https://newdsgn.andersenlab.com/find-developers.php'
        # develops_url = 'https://newdsgn.andersenlab.com/run-project.php'
        DriverProvider.should(have.url(develops_url, timeout=1))

    # query = TextInput(Name('query'), timeout=30)
    # search_frame = HtmlElement(XPath(r'//*[@id="fast-search-modal"]/div/div/iframe'))
    # description = Text(ClassName('offers-description__specs'), timeout=3)
    #
    # def do_search(self):
    #     self.query.fill('termos')
    #     logger.warn('OK')
    #     get_driver().switch_to.frame(self.search_frame._web_element)
    #     links = self.results.links
    #     parsed_result = {}
    #     item = links[1]
    #     parsed_result['link'] = item.get_href()
    #     parsed_result['name'] = item.text
    #     item._web_element.click()
    #     parsed_result['description'] = self.description.text
    #     parsed_result['images'] = []
    #     for img in self.images.items:
    #         parsed_result['images'].append(img._web_element.get_attribute('data-original'))
    #
    #
        # sleep(10)

    def my_test(self, *args):
        pass
