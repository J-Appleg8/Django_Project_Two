from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from second_app.models import Topic, Webpage, AccessRecord, User

# Password: testpassword123
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]
