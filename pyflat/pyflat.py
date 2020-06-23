from inspect import getmembers, getsourcelines

LJUST = 0
RJUST = 1
EXCLUDE = 3
INCLUDE = 4

class Field:
    def __init__(self, size=0, sep=" ", justify=LJUST, decimal_point=EXCLUDE):
        self._size = size
        self._sep = sep
        self._value = None
        self._justify = justify
        self._decimal_point = decimal_point

    def __set__(self, instance, value):
        self._value = value


class Base:
    def __init__(self):
        allfields = list(type(self).__dict__)
        self._fields = {}

        for name, attribute in getmembers(self, lambda o: isinstance(o, Field)):
            sortkey = allfields.index(name)

            attribute._sortkey = sortkey
            attribute._fieldname = name
            self._fields[name] = attribute

    def __repr__(self):
        line = []

        for _, val in sorted(self._fields.items(), key=lambda o: o[1]._sortkey):
            value = val._value

            if val._decimal_point == EXCLUDE and type(value) == float:
                value = str(round(value, 2)).replace(".", "")

            if val._justify == RJUST:
                column = str(value).rjust(val._size, val._sep)
            else:
                column = str(value).ljust(val._size, val._sep)

            line.append(column[: val._size])

        return "".join(line)

