# Django
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import (
    CharField,
    DateField,
    ForeignKey,
    ImageField,
    IntegerField,
    TextField,
)
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    birth_date = DateField()
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message=_(
            "Phone number must be entered in the format: '+999999999'. Up to"
            " 15 digits allowed."
        ),
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, null=True
    )

    def __str__(self) -> str:
        return self.username


class Figurine(models.Model):
    TINY = "T"
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    HUGE = "H"
    GARGANTUAN = "G"

    SIZES = [
        (TINY, _("Tiny")),
        (SMALL, _("Small")),
        (MEDIUM, _("Medium")),
        (LARGE, _("Large")),
        (HUGE, _("Huge")),
        (GARGANTUAN, _("Gargantuan")),
    ]

    name = CharField(max_length=50)
    description = TextField(blank=True)
    size = CharField(max_length=1, choices=SIZES)
    bottom_text = CharField(max_length=10, null=True)

    def __str__(self) -> str:
        return f"{self.name=}, {self.size=}"


class FigurineImage(models.Model):
    figurine = ForeignKey(Figurine, on_delete=models.CASCADE)
    image_name = CharField(max_length=50)
    image = ImageField(upload_to="figurine_images")

    def __str__(self) -> str:
        return f"{self.figurine.id=}, {self.image_name=}"


class Ownership(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    figurine = ForeignKey(Figurine, on_delete=models.CASCADE)
    amount = IntegerField()

    def __str__(self) -> str:
        return f"{self.user.id=}, {self.figurine.id=}, {self.amount=}"


class Rental(models.Model):
    ownership = ForeignKey(Ownership, on_delete=models.CASCADE)
    renter = ForeignKey(User, on_delete=models.CASCADE, related_name="renter")
    rented_date = DateField()
    returned_date = DateField()

    def __str__(self) -> str:
        return (
            f"{self.ownership.figurine.id=}, {self.ownership.user.id=},"
            f" {self.renter.id=}, {self.rented_date=}, {self.returned_date=}"
        )
