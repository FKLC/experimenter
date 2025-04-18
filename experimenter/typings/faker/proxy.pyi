"""
This type stub file was generated by pyright.
"""

import random

_UNIQUE_ATTEMPTS = ...

class Faker:
    """Proxy class capable of supporting multiple locales"""

    cache_pattern = ...
    generator_attrs = ...
    def __init__(
        self,
        locale=...,
        providers=...,
        generator=...,
        includes=...,
        use_weighting=...,
        **config,
    ) -> None: ...
    def __dir__(self): ...
    def __getitem__(self, locale): ...
    def __getattribute__(self, attr):  # -> Any:
        """
        Handles the "attribute resolution" behavior for declared members of this proxy class

        The class method `seed` cannot be called from an instance.

        :param attr: attribute name
        :return: the appropriate attribute
        """
        ...
    def __getattr__(self, attr):  # -> Any:
        """
        Handles cache access and proxying behavior

        :param attr: attribute name
        :return: the appropriate attribute
        """
        ...
    def __deepcopy__(self, memodict=...): ...
    def __setstate__(self, state): ...
    @property
    def unique(self): ...
    @classmethod
    def seed(cls, seed=...):  # -> None:
        """
        Seeds the shared `random.Random` object across all factories

        :param seed: seed value
        """
        ...
    def seed_instance(self, seed=...):  # -> None:
        """
        Creates and seeds a new `random.Random` object for each factory

        :param seed: seed value
        """
        ...
    def seed_locale(self, locale, seed=...):  # -> None:
        """
        Creates and seeds a new `random.Random` object for the factory of the specified locale

        :param locale: locale string
        :param seed: seed value
        """
        ...
    @property
    def random(self):
        """
        Proxies `random` getter calls

        In single locale mode, this will be proxied to the `random` getter
        of the only internal `Generator` object. Subclasses will have to
        implement desired behavior in multiple locale mode.
        """
        ...
    @random.setter
    def random(self, value):  # -> None:
        """
        Proxies `random` setter calls

        In single locale mode, this will be proxied to the `random` setter
        of the only internal `Generator` object. Subclasses will have to
        implement desired behavior in multiple locale mode.
        """
        ...
    @property
    def locales(self): ...
    @property
    def weights(self): ...
    @property
    def factories(self): ...
    def items(self): ...

class UniqueProxy:
    def __init__(self, proxy) -> None: ...
    def clear(self): ...
    def __getattr__(self, name: str): ...
    def __getstate__(self): ...
    def __setstate__(self, state): ...
