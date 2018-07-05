import os
from collections import namedtuple

from rf_libs import get_config
from utils.loggers import logger
from entities.errors import ConfigurationError

_BROWSER_NAME_VAR = 'BROWSER'

Browser = namedtuple("Browser", "name,dc_name,version,use_grid,grid_url,driver_path,vnc,video", )


class IConfigSection(object):

    def __init__(self, section_name):
        self._config = None
        self._section_name = section_name
        self._config_loader = None

    def __get__(self, instance, owner):
        if self._config is None:
            try:
                self._config = instance._config[self._section_name]
                self._config_loader = instance
            except KeyError:
                raise ConfigurationError('Config section "%s" was not found' % self._section_name)
        return self


class BrowsersSection(IConfigSection):

    def __init__(self, *args, **kwargs):
        self._current = None
        super(BrowsersSection, self).__init__(*args, **kwargs)

    def _get_current_browser_value(self, value, default=None, use_defaults_conf=True):
        _value = self._current_browser_config.get(value, default)
        if _value is None and use_defaults_conf:
            _value = self._get_default_browser_value(value, default)
        return _value

    def _get_default_browser_value(self, value, default):
        return self._config.get('defaults', {}).get(value, default)

    @property
    def _current_browser_config(self):
        return self._config[self._config_loader.browser_name]

    @property
    def dc_name(self):
        return self._get_current_browser_value('dc_name', default=self._config_loader.browser_name)

    @property
    def version(self):
        return self._get_current_browser_value('version', default=None)

    @property
    def use_grid(self):
        return bool(self._get_current_browser_value('use_grid'))

    @property
    def grid_url(self):
        return self._get_current_browser_value('grid_url')

    @property
    def driver_path(self):
        return self._get_current_browser_value('driver_path')

    @property
    def vnc(self):
        return bool(self._get_current_browser_value('vnc'))

    @property
    def video(self):
        return bool(self._get_current_browser_value('video'))

    @property
    def current(self):
        if self._current is None:
            self._current = Browser(
                name=self._config_loader.browser_name,
                dc_name=self.dc_name,
                version=self.version,
                use_grid=self.use_grid,
                grid_url=self.grid_url,
                driver_path=self.driver_path,
                vnc=self.vnc,
                video=self.video
            )
            logger.debug("Browser configuration:\n{}".format(self._current))
            if not self._current.use_grid:
                logger.debug("Adding path to web drivers to PATH: {}".format(self._current.driver_path))
                os.environ["PATH"] += os.pathsep + self._current.driver_path
        return self._current


class ProjectSection(IConfigSection):

    def __init__(self, *args, **kwargs):
        self._browser_name = None
        super(ProjectSection, self).__init__(*args, **kwargs)

    @property
    def browser_name(self):
        if self._browser_name is None:
            self._browser_name = get_config().get_rf_var(_BROWSER_NAME_VAR,
                                                         default=self._config.get('browser', None))
            if self._browser_name is None:
                raise ConfigurationError("Browser is not specified")
        return self._browser_name

    @property
    def threads_count(self):
        return self._config.get('threads', None)

    @property
    def wait_timeout(self):
        return self._config.get('wait_timeout', 5)

    @property
    def condition_log_level(self):
        return self._config.get('condition_log_level', 'info').upper()

