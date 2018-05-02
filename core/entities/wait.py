import contextlib

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core import get_driver

wait_timeout = 120


def until_html_element_visible(finder, locator, timeout=wait_timeout):
    wait = WebDriverWait(finder, timeout)
    wait.until(EC.visibility_of_element_located((locator.by, locator.value)))


@contextlib.contextmanager
def for_page_load(timeout=30):
    driver = get_driver()
    old_page = driver.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until(EC.staleness_of(old_page))
