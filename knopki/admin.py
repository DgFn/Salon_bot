from django.contrib import admin
from .models import *

#admin.site.register(Command)
admin.site.register(User)
# Register your models here.

@admin.register(Command)
class Command_admin(admin.ModelAdmin):
    
    list_display = ('id', 'action', )


class Text_element_inline(admin.StackedInline):
    model = Text_element
    extra = 0
    fields = ('text', )

class Button_element_inline(admin.StackedInline):
    model = Button_element
    extra = 0
    fields = ('text', 'callback_data', )

class Command_inline(admin.StackedInline):
    model = Command
    extra = 0
    # fields = ('text', 'callback_data', )

class AdminRole_inline(admin.StackedInline):
    model = AdminRole
    extra = 0


@admin.register(Message_element)
class Message_element_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'handler', )
    inlines = [Command_inline, Text_element_inline, Button_element_inline, AdminRole_inline]
    save_as = True
    pass
