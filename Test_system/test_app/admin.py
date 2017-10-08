from django.contrib import admin

from test_app.models import User,Test, Group, Message, Applications, Review

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, AuthorAdmin)
admin.site.register(Test, AuthorAdmin)
admin.site.register(Group, AuthorAdmin)
admin.site.register(Message, AuthorAdmin)
admin.site.register(Applications, AuthorAdmin)
admin.site.register(Review, AuthorAdmin)
# Register your models here.
