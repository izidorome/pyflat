import pytest

import pyflat


class SimpleUser(pyflat.Base):
    name = pyflat.Field(size=20)


class BasicInfoUser(pyflat.Base):
    name = pyflat.Field(size=20)
    age = pyflat.Field(size=4, sep="0", pad=pyflat.PAD_RIGHT)


class CompleteUser(pyflat.Base):
    name = pyflat.Field(size=20)
    age = pyflat.Field(size=4, sep="0", pad=pyflat.PAD_RIGHT)
    email = pyflat.Field(size=30)
    income = pyflat.Field(size=12, sep="0", pad=pyflat.PAD_RIGHT)


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

    return u


@pytest.fixture
def complete_user():
    u = CompleteUser()
    u.name = "John Doe"
    u.email = "johndoe@email.com"
    u.income = 2000.99
    u.age = 35

    return u


def test_field_size(simple_user):
    expected = "John Doe            "

    assert repr(simple_user) == expected


def test_separator_modifier(basic_info_user):
    expected = "John Doe            0035"

    assert repr(basic_info_user) == expected


def test_nofp(complete_user):
    expected = "John Doe            0035johndoe@email.com             000000200099"

    assert repr(complete_user) == expected
