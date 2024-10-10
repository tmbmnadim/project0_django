from django.contrib import admin
from .models import Services, SiteDetails

class ServiceInline(admin.TabularInline):
    model = Services
    extra = 1
    fields = ["name", "details"]


class SiteDetailsAdmin(admin.ModelAdmin):
    list_display = ["name", "about", "phone", "email", "address", "partner"]
    inlines = [ServiceInline]


admin.site.register(SiteDetails, SiteDetailsAdmin)