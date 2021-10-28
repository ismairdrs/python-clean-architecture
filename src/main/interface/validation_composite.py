from typing import List
from .validation_interface import Validation


class ValidationComposite(Validation):
    def __init__(self, validators: List[Validation]):
        self.validators: List[Validation] = validators

    def add(self, validator):
        self.validators.append(validator)

    def remove(self, validator):
        self.validators.remove(validator)

    def validate(self):
        for validator in self.validators:
            validator.validate()
