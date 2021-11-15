from django.contrib import admin
from second_app.models import Topic, Webpage, AccessRecord

# Password: testpassword123
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
