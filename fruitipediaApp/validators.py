from django.core.exceptions import ValidationError


def is_alpha_validator(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")
