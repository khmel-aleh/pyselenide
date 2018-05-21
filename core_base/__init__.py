import os
import sys

from robot.libraries.BuiltIn import BuiltIn

builtin = BuiltIn()
sys.path.append(os.path.join(os.getcwd(), 'core'))


def get_driver():
    return builtin.get_library_instance('DriverProvider').driver


def get_config():
    return builtin.get_library_instance('ConfigLoader')
