from re import compile, fullmatch
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class RangeValidator:
    def __init__(self, min: int, max: int, error_msg: str = "") -> None:
        self.min = min
        self.max = max
        self.error_msg = error_msg

    def __call__(self, value):
        if not (self.min <= value <= self.max):
            raise ValidationError(_(self.error_msg), code="invalid")

    def __eq__(self, other: "RangeValidator") -> bool:
        return self.__dict__ == other.__dict__


@deconstructible
class MyRegexValidator:

    def __init__(self, regex: str, error_msg: str) -> None:
        self.regex = compile(regex)
        self.error_msg = error_msg

    def __call__(self, value):
        if not self.regex.fullmatch(str(value)):
            raise ValidationError(_(self.error_msg), code="invalid")

    def __eq__(self, other: "MyRegexValidator") -> bool:
        return self.__dict__ == other.__dict__


def ratingValidator(value: str):
    value = float(value)
    if not (0 <= value <= 5) or len(str(value)) > 3:
        raise ValidationError(
            _("Rating should be decimal number in range [0, 5]!"), code="invalid")


def languageValidator(value: str):
    if not fullmatch(r"[a-zA-Z]{3,30}", value):
        raise ValidationError(
            _("Incorrect Language!"), code="invalid")


def beverageValidator(value: str):
    if not fullmatch(r"[a-zA-Z]{2,40}", value):
        raise ValidationError(
            _("Incorrect beverage name!"), code="invalid")


def deviceValidator(value: str):
    if not fullmatch(r"(?!.*_)\w+", value):
        raise ValidationError(
            _("Incorrect device name!"), code="invalid")


def emailValidator(value: str):
    if not fullmatch(r"[\w\-\.]+@[\w-]+\.[\w-]{2,4}", value):
        raise ValidationError(
            _("Incorrect email!"), code="invalid")
