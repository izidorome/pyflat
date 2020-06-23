import pytest

import pyflat


class SimpleUser(pyflat.Base):
    name = pyflat.Field(size=20)


class BasicInfoUser(pyflat.Base):
    name = pyflat.Field(size=20)
    age = pyflat.Field(size=4, sep="0", justify=pyflat.RIGHT)
    rate = pyflat.Field(size=10,sep="0", justify=pyflat.RIGHT, decimal_point=pyflat.INCLUDE)


class CompleteUser(pyflat.Base):
    name = pyflat.Field(size=20)
    age = pyflat.Field(size=4, sep="0", justify=pyflat.RIGHT)
    email = pyflat.Field(size=30)
    income = pyflat.Field(size=12, sep="0", justify=pyflat.RIGHT)


@pytest.fixture
def simple_user():
    u = SimpleUser()
    u.name = "John Doe"

    return u


@pytest.fixture
def basic_info_user():
    u = BasicInfoUser()
    u.name = "John Doe"
    u.age = 35
    u.rate = 3.21

    return u


@pytest.fixture
def complete_user():
    c = CompleteUser()
    c.name = "John Doe"
    c.email = "johndoe@email.com"
    c.income = 2000.99
    c.age = 35

    return c


def test_field_size(simple_user):
    expected = "John Doe            "

    assert simple_user.dump() == expected


def test_separator_modifier(basic_info_user):
    expected = "John Doe            00350000003.21"

    assert basic_info_user.dump() == expected


def test_decimal_point(complete_user):
    expected = "John Doe            0035johndoe@email.com             000000200099"

    assert complete_user.dump() == expected
