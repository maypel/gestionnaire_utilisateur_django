from crm_docstring import User
import pytest
from tinydb import TinyDB
from tinydb.storages import MemoryStorage


@pytest.fixture()
def setup_db():
    User.DB = TinyDB(storage=MemoryStorage)


@pytest.fixture
def user(setup_db):
    u = User(first_name="Patrick",
             last_name="Martin",
             address="1 tue des templiers, 54850 Toulouse",
             phone_number="1234567890")
    u.save()
    return u


def test_full_name(user):
    assert user.full_name == "Patrick Martin"

def test_exists():gjoim
    assert False

def test_db_instance():
    assert False


def test__check_phone_number():
    assert False


def test__check_names():
    assert False





def test_delete():
    assert False


def test_save():
    assert False
