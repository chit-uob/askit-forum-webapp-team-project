from django.contrib import admin
from .models import Question, Module, Answer, Tag, UserProfile

# Register your models here.
admin.site.register(Question)
admin.site.register(Module)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(UserProfile)

