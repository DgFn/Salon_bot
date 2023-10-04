from statistics import mode
from django.db import models as m

# Create your m here.

class Message_element(m.Model):
    name = m.CharField('имя элемента', max_length=255, default=None, null=True, blank=True, )
    handler = m.CharField('обработчик', max_length=255, default=None, null=True, blank=True, )
    adminhandler = m.CharField('админобработчик', max_length=255, default=None, null=True, blank=True, )
    dophandler =  m.BooleanField(default = False,)
    deletewait =  m.BooleanField(default = False,)
    dopaction =  m.TextField('Доп.команды', max_length=255, default=None, null=True, blank=True, )
    pass    

class User(m.Model):
    usernick = m.CharField(max_length=100, default=None, null=True, blank=True,)
    role = m.CharField(max_length=100, default=None, null=True, blank=True,)
    user_id = m.BigIntegerField(default=None, null=True, blank=True)
    frame = m.CharField(max_length=100, default=None, null=True, blank=True,)
    FIO = m.CharField(max_length=100,  default=None, null=True, blank=True,)
    jopa_size = m.BigIntegerField(default= 0, null=True, blank=True)
    waitmessage = m.BooleanField(default = False)
    message_element = m.ForeignKey(Message_element, on_delete=m.SET_DEFAULT, default=None, null=True, blank=True)





class Text_element(m.Model):
    text = m.TextField('текст', default=None, null=True, blank=True)
    message_element = m.ForeignKey(Message_element, on_delete=m.SET_DEFAULT, default=None, null=True, blank=True)
    pass


class Button_element(m.Model):
    text = m.TextField('текст', default=None, null=True, blank=True)
    callback_data = m.TextField('параметр в кнопке', default=None, null=True, blank=True)
    message_element = m.ForeignKey(Message_element, on_delete=m.SET_DEFAULT, default=None, null=True, blank=True)
    pass


class Command(m.Model):
    action = m.CharField(max_length=100,default="", null=True, blank=True)
    command = m.CharField(max_length=100, default="", null=True, blank=True)
    masframe = m.CharField(max_length=100, default="", null=True, blank=True)
    message_element = m.ForeignKey(Message_element, on_delete=m.SET_DEFAULT, default=None, null=True, blank=True)

class AdminRole(m.Model):
    action = m.CharField(max_length=100,default="", null=True, blank=True)
    message_element = m.ForeignKey(Message_element, on_delete=m.SET_DEFAULT, default=None, null=True, blank=True)
    button_element = m.ForeignKey(Button_element, on_delete=m.SET_DEFAULT, default=None, null=True, blank=True)