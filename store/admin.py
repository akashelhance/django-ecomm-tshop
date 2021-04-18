from django.contrib import admin
from .models import Tshirt, Brand, Color,IdealFor, NeckType,Occasion, Sleeve, SizeVariant

class SizeVariantConfiguration(admin.TabularInline):
    model = SizeVariant



class TshirtConfiguration(admin.ModelAdmin):
    inlines = [ SizeVariantConfiguration ]

# Register your models here.
admin.site.register(Tshirt,TshirtConfiguration)
admin.site.register(Brand)

admin.site.register(Color)

admin.site.register(IdealFor)

admin.site.register(NeckType)

admin.site.register(Occasion)
admin.site.register(Sleeve)

