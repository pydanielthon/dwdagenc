from django.contrib import admin
from .models import Category, Product

#pnizsze linie kodu umozliwa kopiowanie obiektow
#bardzo pytdadne do testow
#przejdz do admina zaznacz obiekty o wibierz skopjuj
def duplicate(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate.short_description = "Copy select element"

class AdminProject(admin.ModelAdmin):
    actions = [duplicate]

admin.site.register(Category)
admin.site.register(Product, AdminProject)