from abc import abstractmethod
from collections.abc import Iterable
from functools import wraps


def _cached_property(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if getattr(self, '_cache', None) is None:
            self._cache = {}
        key = '_' + method.__name__
        if key not in self._cache:
            self._cache[key] = method(self, *args, **kwargs)
        return self._cache[key]

    return property(wrapper)


class IterableToString(Iterable):
    @abstractmethod
    def __iter__(self):
        return NotImplemented

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.lisp_case)

    @_cached_property
    def snake_case(self):
        return '_'.join((
            s.lower() for s in self
        ))

    @_cached_property
    def screaming_snake_case(self):
        return '_'.join((
            s.upper() for s in self
        ))

    @_cached_property
    def upper_camel_case(self):
        return ''.join((
            s.capitalize() for s in self
        ))

    @_cached_property
    def lower_camel_case(self):
        return self.upper_camel_case[0].lower() + self.upper_camel_case[1:]

    @_cached_property
    def lisp_case(self):
        return '-'.join((
            s.lower() for s in self
        ))

    @_cached_property
    def train_case(self):
        return '-'.join((
            s.capitalize() for s in self
        ))

    # Aliases:
    SCREAMING_SNAKE_CASE = screaming_snake_case

    camel_case = upper_camel_case
    CamelCase = upper_camel_case
    UpperCamelCase = upper_camel_case

    camelCase = lower_camel_case
    lowerCamelCase = lower_camel_case

    kebab_case = lisp_case
