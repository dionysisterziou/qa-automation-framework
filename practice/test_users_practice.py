import pytest
from practice.users_practice import validate_user


def test_user_ok():
    user = {"role": "admin", "active": True}
    validate_user(user)


def test_user_inactive_should_fail():
    user = {"role": "admin", "active": False}
    with pytest.raises(AssertionError):
        validate_user(user)