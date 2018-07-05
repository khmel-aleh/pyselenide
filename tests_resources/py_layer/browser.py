from rf_libs.DriverProvider import DriverProvider
from entities.conditions import have


def check_browser_url(url, timeout=1):
    DriverProvider.should(have.url(url, timeout=timeout))
