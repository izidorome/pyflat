from inspect import getmembers, getsourcelines

LEFT = 0
RIGHT = 1
EXCLUDE = 3
INCLUDE = 4

class Field:
    def __init__(self, size=0, sep=" ", justify=LEFT, decimal_point=EXCLUDE):
        self._size = size
        self._sep = sep
        self._justify = justify
        self._decimal_point = decimal_point

    def __set__(self, instance, value):
        instance._values[self._fieldname] = value



class Base:
    def __init__(self):
        allfields = list(type(self).__dict__)
        self._fields = {}
        self._values = {}

        for name, attribute in getmembers(self, lambda o: isinstance(o, Field)):
            sortkey = allfields.index(name)

            attribute._sortkey = sortkey
            attribute._fieldname = name
            self._fields[name] = attribute
            self._values[name] = None


    def dump(self):
        line = []

        for _, val in sorted(self._fields.items(), key=lambda o: o[1]._sortkey):
            value = self._values[val._fieldname]

            if value is None:
                value = ""

            if val._decimal_point == EXCLUDE and type(value) == float:
                value = str(round(value, 2)).replace(".", "")

            if val._justify == RIGHT:
                column = str(value).rjust(val._size, val._sep)
            else:
                column = str(value).ljust(val._size, val._sep)

            line.append(column[: val._size])

        return "".join(line)