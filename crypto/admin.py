from django.contrib import admin

from .models import MyModel, Producer, Default

admin.site.register(MyModel)
admin.site.register(Producer)
admin.site.register(Default)
