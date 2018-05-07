import os
import json
import re
import os.path as op

from pathlib import Path
from typing import Callable
from types import SimpleNamespace


# --------------------------------------------------------------------------
# Map the function to do code shorter
# --------------------------------------------------------------------------
ACTIONS_DETECTION_REGEX = \
    re.compile(r'''(\$)([\w\d\_\-]+)([\(\s]+)([\w\'_\"\-\.\d\, ]+)([\)\s]+)''')


def resolve_log_level(level: int, quite_mode: bool = False) -> int:

    # If quiet mode selected -> decrease log level
    if quite_mode:
        input_level = 100
    else:
        input_level = level * 10

        if input_level > 50:
            input_level = 50

        input_level = 60 - input_level

        if input_level >= 50:
            input_level = 50

    return input_level


def find_file(file_name: str) -> str or None:
    """This function try to find a file in 3 places:
    - Running path
    - User path
    - The folder ~/.crawlino/

    If file not found, it returns None
    """
    locations = [
        op.abspath(os.getcwd()),  # Current dir
        op.join(str(Path.home()), ".crawlino")  # User's home
    ]

    if op.isabs(file_name):
        return file_name

    for l in locations:
        curr = op.join(l, file_name)
        if op.exists(curr):
            return curr


def json_to_object(data: str) -> SimpleNamespace:
    """This function convert a JSON document into a Python object:

    >>> data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
    >>> json_to_object(data)
    namespace(hometown=namespace(id=123, name='New York'), name='John Smith')

    """
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


def dict_to_object(item, callback: Callable = None):
    """This function convert a Python Dict into a Python object:

    >>> data = {"name": "John Smith", "hometown": {"name": "New York", "id": 123}}type >>> c = json_to_object(data)
    type>> c
    <class 'automatic'>
    >>> c.name
    "John Smith"
    >>> c.hometown.name
    "New York"
    typevars(c)
    mappingproxy({'name': 'Jotypemith', 'hometown': <class 'automatic'>, '__dict__':typetribute '__dict__' of 'automatic' objects>, '__weakref__': <attribute '__weakref__' of 'automatic' objects>, '__doc__': None})

    """
    def convert(item):
        if isinstance(item, dict):
            return type('automatic', (), {
                k: convert(v) for k, v in item.items()
            })
        if isinstance(item, list):
            def yield_convert(item):
                for index, value in enumerate(item):
                    yield convert(value)
            return list(yield_convert(item))
        else:
            return item

    return convert(item)


def un_camel(text: str):
    output = [text[0].lower()]

    for c in text[1:]:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            output.append('_')
            output.append(c.lower())
        else:
            output.append(c)
    return str.join('', output)


def get_crawlino_home() -> str:
    """Get user home path and, it it doesn't exits, create it"""
    from pathlib import Path
    home = str(Path.home())

    crawlino_home = op.abspath(op.join(home, ".crawlino"))

    if not op.exists(crawlino_home):
        os.mkdir(crawlino_home)

    return crawlino_home


__all__ = ("find_file", "resolve_log_level", "json_to_object",
           "dict_to_object", "un_camel", "get_crawlino_home")
