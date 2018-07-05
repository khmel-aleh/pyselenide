
import sys

from random import choice


def random_value_from_list_not_contains_value(l, v):
    """
    Returns random value from list ``l`` that not matches value ``v``.
    List must contain value ``v``.

    For example:
        l = [1, 2, 3]
        v = 2
    return value can be 1 or 3.

    :param l: list
    :param v: value in list ``l``
    :return: value in list that not equals to ``v``
    """
    ll = len(l)
    if v not in l:
        raise ValueError('Can\'t find value "{}" in list. Value must be present in list'.format(v))
    if ll == 0:
        raise ValueError("List can't be empty")
    elif ll == 1:
        return v
    nl = l[:]
    nl.remove(v)
    return choice(nl)

def is_truthy(item):
    if isinstance(item, str):
        return item.upper() not in ('FALSE', 'NO', '', 'NONE')
    return bool(item)

