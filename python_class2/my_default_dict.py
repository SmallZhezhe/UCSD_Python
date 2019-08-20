"""Create your own defaultdict"""
from collections import UserDict


class MyDefaultDict(UserDict):

    def __init__(self, default_factory, *args, **kwargs):
        self.factory = default_factory
        super().__init__(*args, **kwargs)

    def __missing__(self, value):
        return self.factory()
