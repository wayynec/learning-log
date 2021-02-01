from django.contrib import admin

# Register your models here.
# can be managed through admin site

from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)