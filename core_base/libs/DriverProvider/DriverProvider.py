from robot.libraries.BuiltIn import BuiltIn

from core_base import get_config
from core_base.entities.errors import ConfigurationError
from core_base.loggers import logger
from core_base.utils.helpers import is_truthy

_CHROME = "Chrome"
_FIREFOX = "Firefox"
_IE = "Ie"
_REMOTE = "Remote"


class DriverProvider(object):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    supported_browser_names = {
        'googlechrome': _CHROME,
        'gc': _CHROME,
        'chrome': _CHROME,
        'ff': _FIREFOX,
        'firefox': _FIREFOX,
        'ie': _IE,
        'internetexplorer': _IE
    }

    @staticmethod
    def get_se_lib():
        return BuiltIn().get_library_instance('SeleniumLibrary')

    def _get_driver_init_kwargs(self):
        config = get_config()
        browser_name = config.browser_name.lower().replace(" _", "")
        init_kwargs = {}
        if browser_name in self.supported_browser_names.keys():
            remote_url = config.browser.grid_url if config.browser.use_grid else None
            if is_truthy(remote_url):
                driver_name = _REMOTE
                init_kwargs['command_executor'] = remote_url
            else:
                driver_name = self.supported_browser_names[browser_name]
            init_kwargs['driver_name'] = driver_name
            if driver_name in (_CHROME, _REMOTE):
                init_kwargs['desired_capabilities'] = config.desired_capabilities
            else:
                init_kwargs['capabilities'] = config.desired_capabilities
            if driver_name == _FIREFOX:
                init_kwargs['firefox_profile'] = None
        else:
            raise ConfigurationError('Browser "%s" is not supported' % browser_name)
        return init_kwargs

    def inizialize_driver(self):
        init_kwargs = self._get_driver_init_kwargs()
        logger.debug("Initializing web driver with parameters:\n{}".format(init_kwargs))
        self.get_se_lib().create_webdriver(**init_kwargs)
        self.configure_driver()

    def configure_driver(self):
        self.driver.set_script_timeout(5)
        self.driver.implicitly_wait(0)

    @property
    def driver(self):
        return self.get_se_lib().driver

    @staticmethod
    def should(condition):
        condition.wait_until(DriverProvider.get_se_lib().driver)
