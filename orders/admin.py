from django.contrib import admin

# Register your models here.

from .models import SicilianPizza, RegularPizza, Subs, Pasta, Salads, Parm

# Register your models here.
admin.site.register(SicilianPizza)
admin.site.register(RegularPizza)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Parm)
