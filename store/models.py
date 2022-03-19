from django.db import models
from django.db.models import CharField, DateField, IntegerField, TextField, ForeignKey, ImageField
from django.core.validators import RegexValidator, EmailValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(models.Model):
    ADMIN = 1
    MODERATOR = 2
    SUPER_OWNER = 3
    OWNER = 4
    BASE_USER = 5

    PERMISSIONS = [
        (ADMIN, _('Admin')),
        (MODERATOR, _('Moderator')),
        (SUPER_OWNER, _('Super Owner')),
        (OWNER, _('Owner')),
        (BASE_USER, _('Base User'))
    ]

    email_validator = EmailValidator()
    email = CharField(max_length=50, validators=[email_validator])
    username = CharField(max_length=20)
    password = CharField(max_length=50)
    birth_date = DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    permission = IntegerField(choices=PERMISSIONS)

    def __str__(self) -> str:
        return self.username


class Figurine(models.Model):
    TINY = 'T'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    HUGE = 'H'
    GARGANTUAN = 'G'

    SIZES = [
        (TINY, _('Tiny')),
        (SMALL, _('Small')),
        (MEDIUM, _('Medium')),
        (LARGE, _('Large')),
        (HUGE, _('Huge')),
        (GARGANTUAN, _('Gargantuan'))
    ]

    name = CharField(max_length=50)
    description = TextField(blank=True)
    size = CharField(max_length=1, choices=SIZES)
    set_number = CharField(max_length=10, null=True)

    def __str__(self) -> str:
        return f"{self.name=}, {self.size=}"


class FigurineImage(models.Model):
    figurine = ForeignKey(Figurine, on_delete=models.CASCADE)
    image_name = CharField(max_length=50)
    image = ImageField()

    def __str__(self) -> str:
        return f"{self.figurine_id=}, {self.image_name=}"


class OnwnedFigurine(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    figurine = ForeignKey(Figurine, on_delete=models.CASCADE)
    amount = IntegerField()

    def __str__(self) -> str:
        return f"{self.user_id=}, {self.figurine_id=}, {self.amount=}"


class RentedFigurine(models.Model):
    owned_figurine = ForeignKey(OnwnedFigurine, on_delete=models.CASCADE)
    owner = ForeignKey(User, on_delete=models.CASCADE, related_name="owner_id")
    renter = ForeignKey(User, on_delete=models.CASCADE, related_name="renter_id")
    rented_date = DateField()
    returned_date = DateField()

    def __str__(self) -> str:
        return f"{self.owned_figurine_id=}, {self.owner_id=}, {self.renter_id=}, {self.rented_date=}, {self.returned_date=}"