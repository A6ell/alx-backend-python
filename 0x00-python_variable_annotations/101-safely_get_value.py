#!/usr/bin/env python3
'''
this module contains the sum_mixed_list function
'''
from typing import Mapping, Any, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    '''
    function
    '''
    if key in dct:
        return dct[key]
    else:
        return default
