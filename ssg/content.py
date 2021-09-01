import re

from yaml import FullLoader, load
from collections.abc import Mapping


class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(_, fm, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data += {"content": content}

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if "type" in self.data.keys() else None

    @property.setter
    def type(self, type):
        self.data["type"] = type

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        return self.data # iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key != "content":
                value = data[key]

        return str(data)


#
# d = {"content": 'dsds'}
#
# if "content" in d.keys():
#     print("yes")
# else:
#     print("No")