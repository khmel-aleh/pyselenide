import json
import os

from robot.libraries.BuiltIn import BuiltIn

from utils.loggers import logger
from .sections import BrowsersSection, ProjectSection


class ConfigLoader(object):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    CONFIG_ROOT_DIR = "config"
    _PROJECT_SECTION_KEY = 'project'
    _BROWSERS_SECTION_KEY = 'browsers'

    project = ProjectSection(_PROJECT_SECTION_KEY)
    browsers = BrowsersSection(_BROWSERS_SECTION_KEY)

    @staticmethod
    def get_rf_var(name, default=None):
        value = BuiltIn().get_variable_value("${" + name + "}", default=default)
        logger.debug("Getting Robot Variable. '{0}' is set to '{1}'.".format(name, value))
        return value

    @staticmethod
    def set_rf_var(name, value):
        logger.debug("Setting {0}: {1}".format(name, value))
        BuiltIn().set_global_variable("${" + name + "}", value)

    @staticmethod
    def build_config_path(conf_file):
        return os.path.normpath(os.path.join(os.getcwd(), ConfigLoader.CONFIG_ROOT_DIR, conf_file))

    def __init__(self, conf_file=None):
        conf_file = conf_file or ConfigLoader.get_rf_var('CONFIG_FILE', 'default.json')
        conf_file_path = ConfigLoader.build_config_path(conf_file)
        try:
            logger.debug("Using config file: {}".format(conf_file))
            with open(conf_file_path, 'rt') as fd:
                self._config = json.load(fd)
        except:
            raise

    @property
    def browser_name(self):
        return self.project.browser_name

    @property
    def browser(self):
        return self.browsers.current

    @property
    def desired_capabilities(self):
        des_cap = {
            "browserName": self.browser.dc_name,
            "version": self.browser.version,
            "enableVNC": self.browser.vnc,
            "enableVideo": self.browser.video,
            "name": "myCoolTestName"
        }
        logger.info("desired_capabilities: {0}".format(des_cap))
        return des_cap

    def __str__(self):
        return "Project:\n\t{0}\nBrowser:\n\t{1}".format(self.project, self.browser)
