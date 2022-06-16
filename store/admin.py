# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Figurine Store
from store.models import Figurine, FigurineImage, Ownership, Rental, User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Figurine)
admin.site.register(FigurineImage)
admin.site.register(Ownership)
admin.site.register(Rental)
