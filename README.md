# pyflat

The pyflat package aims to provide easy serialization of Python objects into positional fixed-width strings.
These kind of structures are useful when integrating with old system which depends on positional flat files.

## Quick Start

### Instalation
To install Pyflat, use pip or pipenv:

```bash
$ pip install pyflat
```

### Example Usage

```python
from pyflat import Base, Field, PAD_RIGHT

class User(Base):
    name = Field(size=20)
    income = Field(size=10, pos='0', pad=PAD_RIGHT)


user = User()
user.name = 'John Doe'
user.income = 4500.35


print(user) # => John Doe            0000450035
```
