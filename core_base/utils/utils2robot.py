import collections
import copy
import random
import string
import types
from random import randint
from random import randrange
from re import sub
# from urlparse import urlparse

# import exrex
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


def __for_each_key(f_name, in_dict):
    logger.debug("{1} keys: In dict: {0}".format(in_dict, f_name))
    result_dict = {}
    for k in in_dict.keys():
        logger.debug("handling '{0}'".format(k))
        result_dict[getattr(k, f_name)()] = copy.deepcopy(in_dict[k])
    logger.debug("{1} keys:Out dict: {0}".format(result_dict, f_name))
    return result_dict


def make_dictionaries_keys_upper(in_dict):
    return __for_each_key("upper", in_dict)


def make_dictionaries_keys_lower(in_dict):
    return __for_each_key("lower", in_dict)


def transform_to_iterable(value):
    logger.debug("Transforming to iterable: {0}".format(value))
    if isinstance(value, types.StringTypes) or \
            not isinstance(value, collections.Iterable):
        logger.debug("Creating list with value: {0}".format(value))
        result = list()
        result.append(value)
        return result
    logger.debug("{0} is already iterable".format(value))
    return value


def exclude_from_dictionary_by_keys(in_dict, keys):
    """
    method deletes key:values from dictionary with passed keys
    :param in_dict: dictionary to be thin out
    :param keys: list of keys to be deleted
    :return:
    """
    result_dict = copy.deepcopy(in_dict)
    logger.debug(
        "Excluding from dictionary: {0} \n keys: {1}".format(result_dict,
                                                             keys))
    for key_to_exclude in keys:
        if key_to_exclude in result_dict.keys():
            del result_dict[key_to_exclude]
    logger.debug("Result after excluding: {0}".format(result_dict))
    return result_dict


def generate_random_ip():
    not_valid = [10, 127, 169, 172, 192]

    first = randrange(1, 256)
    while first in not_valid:
        first = randrange(1, 256)

    ip = ".".join([str(first), str(randrange(1, 256)),
                   str(randrange(1, 256)), str(randrange(1, 256))])
    return ip


def random_string(s_len, reg_exp=None):
    if reg_exp:
        rand_string = exrex.getone(reg_exp, limit=int(s_len))
        return rand_string[2:-1]
    return ''.join(
        random.choice(string.ascii_letters) for _ in range(int(s_len)))


def random_boolean():
    return random.choice((True, False))


def random_int(len):
    return randint(1, int(len))


def random_int_string(a, b):
    return str(randint(int(a), int(b)))


def random_ip(**kwargs):
    return '.'.join([str(kwargs.get('a') or random.randint(0, 255)),
                     str(kwargs.get('b') or random.randint(0, 255)),
                     str(kwargs.get('c') or random.randint(0, 255)),
                     str(kwargs.get('d') or random.randint(0, 255))])


def get_random_email(user_len):
    domains = ["hotmail.com", "gmail.com", "yahoo.com"]

    def get_one_random_domain():
        return random.choice(domains)

    return '@'.join([random_string(int(user_len)), get_one_random_domain()])


def select_random_item(u_list, random_amount=False):
    if not isinstance(u_list, list):
        raise AssertionError(
            "Incorrect param is passed to random method! "
            "Should be list type but was {}".format(type(u_list)))
    if not u_list:
        raise AssertionError("Passed list is empty!")
    if random_amount:
        # example:
        #    in  [1, 2, 3, 4]
        #    out [3, 1]
        result = []
        for i in xrange(random_int(len(u_list))):
            result.append(u_list.pop(random_int(len(u_list)) - 1))
        return result
    return random.choice(u_list)


def select_random(source):
    if type(source) is list or type(source) is tuple:
        return random.choice(source)
    elif type(source) is dict:
        return random.choice(source.keys())


def generate_screenshot_name(test_name):
    id = sub("[ _].*", "", test_name)
    return "{0}_{1}.png".format(id, random_string(10))


def generate_policy_name():
    return "auto_webui_{0}".format(random_string(7))


def random_length_string(len):
    return random_string(random_int(int(len)))


def get_clean_url(url):
    up = urlparse(url)
    return "{0}://{1}".format(up.scheme, up.netloc)


def get_test_case_id():
    test_name = BuiltIn().get_variable_value("${TEST_NAME}")[2:]
    test_id = sub('[ _].*', '', test_name)
    return test_id
