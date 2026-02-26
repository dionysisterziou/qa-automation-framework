import pytest
from validations.payments import validate_payment
from validations.payments import validate_payment_currency


def test_payment_ok():
    payment = {"amount": 100, "status": "SUCCESS"}

    validate_payment(payment)


def test_payment_invalid_amount_should_fail():
    payment = {"amount": 0, "status": "SUCCESS"}

    with pytest.raises(AssertionError):
        validate_payment(payment)


def test_payment_currency():
    payment = {"amount": 10, "status": "SUCCESS", "currency": "EUR"}

    validate_payment(payment)
    validate_payment_currency(payment)