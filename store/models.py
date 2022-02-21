from django.db import models
from django.forms import CharField, DateField, IntegerField, TextField
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    ADMIN = 1
    MODERATOR = 2
    SUPER_OWNER = 3
    OWNER = 4
    BASE_USER = 5

    PERMISSIONS = [
        (ADMIN, 'Admin'),
        (MODERATOR, 'Moderator'),
        (SUPER_OWNER, 'Super Owner'),
        (OWNER, 'Owner'),
        (BASE_USER, 'Base User')
    ]

    email = CharField(max_length=50)
    username = CharField(max_length=20)
    password = CharField(max_length=50)
    birth_date = DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    permission = IntegerField(choices=PERMISSIONS)

    def __str__(self):
        return self.username


class Figurine(models.Model):
    TINY = 'T'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    HUGE = 'H'
    GARGANTUAN = 'G'

    SIZES = [
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (HUGE, 'Huge'),
        (GARGANTUAN, 'Gargantuan')
    ]

    name = CharField(max_length=50)
    description = TextField(blank=True)
    size = CharField(max_length=1, choices=SIZES)
    set_number = CharField(max_length=10, null=True)
    image = 0
