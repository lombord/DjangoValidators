from django.db import models

from .validators import (RangeValidator, MyRegexValidator,
                         beverageValidator,
                         deviceValidator, emailValidator,
                         languageValidator, ratingValidator)

# Create your models here.


class ClubUser(models.Model):
    name = models.CharField(max_length=200, validators=[
        MyRegexValidator(r'(?!.*_)(?!.*\d)\w+',
                         'Name can only contain letters'),])
    surname = models.CharField(max_length=200, validators=[
        MyRegexValidator(r'(?!.*_)(?!.*\d)\w+',
                         'Surname can only contain letters'),])
    email = models.CharField(max_length=255, validators=[emailValidator,])
    password = models.CharField(max_length=255, validators=[
                                MyRegexValidator(
                                    r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[a-zA-Z\d@$!%*#?&]{8,}",
                                    "Password should contain"
                                    " minimum eight characters, at least one "
                                    "letter, one number and one special character")])
    age = models.PositiveIntegerField(
        validators=[RangeValidator(12, 100)],
        error_messages={
            "invalid": "Age should be positive integer in range (12, 100)"}
    )
    language = models.CharField(
        max_length=255, validators=[languageValidator,])
    favorite_game = models.CharField(max_length=255, validators=[
        MyRegexValidator(r"[\w\s]+", "Incorrect game name!")
    ])
    favorite_genre = models.CharField(max_length=255, validators=[
        MyRegexValidator(r"[\w\s]+", "Incorrect genre!")
    ])
    favorite_beverage = models.CharField(
        max_length=255, validators=[beverageValidator,])
    device = models.CharField(max_length=255, validators=[deviceValidator,])
    club_rating = models.DecimalField(
        max_digits=2, decimal_places=1, validators=[ratingValidator,],
        error_messages={"invalid": "Rating should be decimal number in range [0, 5]"})

    def __str__(self) -> str:
        return f"{self.pk}.{self.name} {self.surname}"
