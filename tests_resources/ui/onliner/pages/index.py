from time import sleep

from rf_libs import get_driver
from entities.elements import Image, TextInput, Link, Text
from entities.locators import XPath, Name, ClassName, ID
from entities.find import All
from entities.htmlelement import HtmlElement


from robot.api import logger


class SearchResults(HtmlElement):

    links = All(Link, ClassName('product__title-link'))


class Images(HtmlElement):

    items = All(Image, XPath( r'//*[@id="mCSB_1_container"]/div/div'))


class Onliner(object):

    query = TextInput(Name('query'), timeout=30)

    search_frame = HtmlElement(XPath(r'//*[@id="fast-search-modal"]/div/div/iframe'))
    results = SearchResults(ClassName('search__content-wrapper'), timeout=3)

    description = Text(ClassName('offers-description__specs'), timeout=3)
    images = Images(ID('mCSB_1'))


    def do_search(self):
        self.query.fill('termos')
        logger.warn('OK')
        get_driver().switch_to.frame(self.search_frame._web_element)
        links = self.results.links
        parsed_result = {}
        item = links[1]
        parsed_result['link'] = item.get_href()
        parsed_result['name'] = item.text
        item._web_element.click()
        parsed_result['description'] = self.description.text
        parsed_result['images'] = []
        for img in self.images.items:
            parsed_result['images'].append(img._web_element.get_attribute('data-original'))


        sleep(10)
