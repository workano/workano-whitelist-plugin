# validator.py
from wazo_confd.helpers.validator import Validator, ValidationGroup


class WhitelistValidator(Validator):
    def validate(self, model):
        return


def build_whitelist_validator():
    whitelist_validator = WhitelistValidator()
    return ValidationGroup(create=[whitelist_validator], edit=[whitelist_validator])
