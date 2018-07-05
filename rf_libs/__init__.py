from robot.libraries.BuiltIn import BuiltIn

builtin = BuiltIn()


def get_driver():
    return builtin.get_library_instance('DriverProvider').driver


def get_config():
    return builtin.get_library_instance('ConfigLoader')