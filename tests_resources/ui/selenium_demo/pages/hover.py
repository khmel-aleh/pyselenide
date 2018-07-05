from time import sleep

from entities.elements import Image
from entities.locators import XPath


class SDHover(object):

    prof1 = Image(XPath('//*[@id="content"]/div/div[1]/img'), timeout=30)
    prof2 = Image(XPath('//*[@id="content"]/div/div[2]/img'), timeout=30)
    prof3 = Image(XPath('//*[@id="content"]/div/div[3]/img'), timeout=30)

    def hover(self):
        self.prof1.actions.hover().perform()
        # sleep(1)
        self.prof2.actions.hover().perform()
        # sleep(1)
        self.prof3.actions.hover().perform()
        # sleep(1)
