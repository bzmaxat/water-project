from django.contrib import admin
from .models import Catalog
from .models import Customer


admin.site.register(Catalog)
admin.site.register(Customer)
