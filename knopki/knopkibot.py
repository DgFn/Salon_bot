
import time
import telebot
from telebot import types
# from .models import Command,User
from . import models as m



class FMS():


    def frame_assembler(self, user, message_element):
        button_data = []#cписок для информации о кнопках,каждая кнопка в отдельности
        inline_buttons = []#cписок с кнопками
        texts = message_element.text_element_set.all()
        buttons = message_element.button_element_set.all()
        try:# создание списка с инфой о кнопке
            for element in buttons:
                buttons_element = {
                    'text' : element.text,
                    'callback_data' : element.callback_data,
                    }
                button_data.append(buttons_element)
        except:
            pass

        
        
        if len(buttons) !=0:
            print(len(buttons))
            for buttons_info in button_data:
                textovetbutton = texts[0]
                text = buttons_info['text']
                callback_data = buttons_info['callback_data']
                button = types.InlineKeyboardButton(text = text,callback_data = callback_data)
                inline_buttons.append(button)
            inline_keyboard = types.InlineKeyboardMarkup()
            inline_keyboard.add(*inline_buttons)
            bot.send_message(user.user_id, f'{textovetbutton.text}', reply_markup = inline_keyboard)
        elif len(texts) != 0:
            text = texts[0]
            bot.send_message(user.user_id, text = text.text)














    def base_logic(self, message = None, data = None, user = None, message_element = None):

        if message_element is not None:
            self.frame_assembler(user, message_element)

    def jopa(self, message = None, data = None, user = None, message_element = None):

        user.jopa_size += 1
        user.save()

        if message_element is not None:
            self.frame_assembler(user, message_element)

    def proverka(self, message = None, data = None, user = None, message_element = None):
        if message_element is not None:
            bot.send_message(user.user.id, text = user.FIO)


    # def base_logic_old(self, message, data = None, user = None):
    #     if message:
    #         commands = Command.objects.filter(command = message.text.lower())
    #         if commands.exists():
    #             x = commands[0].helptext
    #             bot.send_message(user.user_id, f'{x}')
    #         else:
    #             print('memes')
    #             noneaction = Command.objects.filter(action = "helpuserpls")
    #             noneaction = noneaction[0]
    #             bot.send_message(user.user_id,f'{noneaction.helptext}')
    #     elif data != None:
    #         selectdata = Command.objects.filter(masframe = data)
    #         messagetext = selectdata[0].helptext
    #         bot.send_message(user.user_id, f'{messagetext}')
    #     else:
    #             print('mem')
    #             noneaction = Command.objects.filter(action = "helpuserpls")
    #             noneaction = noneaction[0]
    #             bot.send_message(user.user_id,f'{noneaction.helptext}')


    #def start(self,message,data = None, user = None):
    #    startmessage = m.Command.objects.filter(action = message.text).first()


    #    if message.text == '/start':
    #        keyboard = types.InlineKeyboardMarkup(row_width=2)

    #        butmas = [
    #            types.InlineKeyboardButton(text="Тест на аку", callback_data ="testiq"),
    #            types.InlineKeyboardButton(text="Тест на pedika", callback_data =  "testpedik")
    #            ]

    #        keyboard.add(*butmas)
    #        #messageuser = startmessage.messagefromuser
    #        bot.send_message(user.user_id, f'Давай дальше', reply_markup = keyboard)
    #    else:
    #        messageus = m.Command.objects.filter(action = "helpuserpls").first()
    #        messagehepluser = messageus.helptext
    #        bot.send_message(user.user_id, f'{messagehepluser}')


    #def testiq(self,user):
    #    record, created = m.User.objects.get_or_create(usernick = user, frame = "testiq1")
    #    if created:
    #        record.frame = 'testiq1'
    #    record.save()

    #    bot.send_message(user, f'Проверка тема: {record.frame}')


    #def testiq1(self,user):
    #    bot.send_message(user, 'Э ты красавчик да!')


    def registeruser(self, message = None, data = None, user = None, message_element = None):
        print('ec1')
        if data != None:
            self.base_logic(message = message, data = data, user = user, message_element = message_element)
            user.waitmessage = True
            print('ec')
            user.frame = "registeruser"
            user.save()

        elif data == None:
            fio = message.text
            user.FIO = fio
            user.frame = None
            user.waitmessage = False
            user.save()
        
    def adminrole(self,message = None, data = None, user = None, message_element = None,):
        if user.role == 'admin':
            self.base_logic(message = message, data = data, user = user, message_element = message_element)

    def adminrecord(self,message = None, data = None, user = None, message_element = None,):
        if data != None:
            self.base_logic(message = message, data = data, user = user, message_element = message_element)
            user.waitmessage = True
            user.frame = "adminrecord"
            user.save()
        elif data == None:
            message_elements = m.Message_element.objects.filter(adminhandler = user.frame)
            for message_element in message_elements:
                new_button = m.Button_element.objects.create(
                    text = message.text,
                    callback_data = "/pop",
                    message_element = message_element,

                    )
                user.waitmessage = False
                user.frame = ""
                user.save()
            new_button.save()

    def admindelrecord(self,message = None, data = None, user = None, message_element = None,):
        source_message_element_id = 16  #Получение нужно мне message_element
        source_message_element = m.Message_element.objects.get(id=source_message_element_id)
        button_to_new = m.Button_element.objects.filter(message_element = message_element)
        
        if message_element.deletewait != True:
            for button_to_newdel in button_to_new:
                button_id = button_to_newdel.id
                button_to_delete = m.Button_element.objects.get(id=button_id)
                button_to_delete.delete()
            buttons_to_copy = m.Button_element.objects.filter(message_element=source_message_element)
            count = 0
            for button_to_copy in buttons_to_copy:
                count +=1
                new_button = m.Button_element.objects.create(
                        text=button_to_copy.text,  # Копировать текст
                    callback_data=f"/delrecord  {count} ",  # Копировать callback_data
                    message_element=message_element,
                        )

                new_button.save()
            message_element.deletewait = True
            message_element.save()
            self.base_logic(message = message, data = data, user = user, message_element = message_element)
        else:
            if data != '/deleteadmin':
                button_to_del = m.Button_element.objects.filter(callback_data = data)
                buttons_to_del_record = m.Button_element.objects.filter(message_element=source_message_element)
                for button_to_delete in button_to_del:
                    text_to_del = button_to_delete.text
                    for v in buttons_to_del_record:
                        v = m.Button_element.objects.filter(text =text_to_del ).first()
                        if v != None:
                            print(v)
                            v_id = v.id
                            v_delete = m.Button_element.objects.get(id = v_id)
                            v_delete.delete()
                            source_message_element.save()
                        
                message_element.deletewait = False
                message_element.save()
            else:
                print("Пусто")

            #self.base_logic(message = message, data = data, user = user, message_element = message_element)
                


    def copyrecordforuser(self,message = None, data = None, user = None, message_element = None,):

        source_message_element_id = 16  
        source_message_element = m.Message_element.objects.get(id=source_message_element_id)

        buttons_to_copy = m.Button_element.objects.filter(message_element=source_message_element)
        buttons_to_del = m.Button_element.objects.filter(message_element = message_element)
        for button_to_del in buttons_to_del:
            button_id = button_to_del.id
            button_to_delete = m.Button_element.objects.get(id=button_id)
            button_to_delete.delete()
        for button_to_copy in buttons_to_copy:
            new_button = m.Button_element.objects.create(
                    text=button_to_copy.text,  # Копировать текст
                callback_data=button_to_copy.callback_data,  # Копировать callback_data
                message_element=message_element,
                    )
            new_button.save()
        self.base_logic(message = message, data = data, user = user, message_element = message_element)
            

    #def recordel(self, user, message_element,):
    #    if user.frame != "recordel":
    #        user.frame = "recordel"
    #    elif user.frame == "recordel":

            


    def dophandler(self, message = None, data = None, user =None, message_element = None, call_id = None):
        time.sleep(2)
        self.executor( message = None, data = message_element.dopaction, user_id = user.user_id, call_id = call_id)
        







    def executor(self, message, data=None, user_id=None, call_id = None):
        user, flag = m.User.objects.get_or_create(user_id = user_id)
        if user.role == "admin":
            if data is not None:
                if data.split() !=None:
                    dats = data.split()
                    actionadmin = m.AdminRole.objects.filter(action = dats[0]).first()
                elif data.split() == None:
                    actionadmin = m.AdminRole.objects.filter(action = data).first()  
                if actionadmin != None:
                    bot.answer_callback_query(callback_query_id=call_id, text="")
                    message_element = actionadmin.message_element
                    if message_element.adminhandler is not None:
                        x = getattr(self, message_element.adminhandler)
                        x(message = message,data = data, user = user, message_element = message_element,)
                    else:
                        self.base_logic(message = message, data = data, user = user, message_element = message_element)#подумать, потомуша не нрав
            elif len(message.text) !=0:
                action = m.Command.objects.filter(action=message.text.lower()).first()
                waitmessage = m.User.objects.filter(waitmessage = True)
                if waitmessage:
                    frame_value = user.frame
                    x = getattr(self, frame_value)
                    x(message = message, data = None, user = user, message_element = None)
                if action is not None:
                    message_element = action.message_element
                    if message_element.handler == None:
                        self.base_logic(message = message, data = data, user = user, message_element = message_element)
                    else:
                         x = getattr(self, message_element.handler)
                         x(message = message,data = data, user = user, message_element = message_element)
            else:
                pass

        if data is not None:
            action = m.Command.objects.filter(action=data)
            action = action.first()
            if action is None:
                #frameuser = User.objects.filter(usernick = user, frame__isnull=False).exists()
                #if frameuser:
                #  userframe = User.objects.get(usernick = user).first()
                #  frames = User.objects.filter(name_functions = userframe.frame ).first()
                #  x = getattr(self, frames )
                #  x(message,data,user)

               #self.base_logic(message = message,data = data, user = user)
               pass
            else:       
                
                message_element = action.message_element
                if message_element.handler == None:
                    #bot.answer_callback_query(callback_query_id=call_id, text="")
                    self.base_logic(message = message, data = data, user = user, message_element = message_element)
                elif   message_element.handler != None:
                    #bot.answer_callback_query(callback_query_id=call_id, text="")
                    x = getattr(self, message_element.handler)
                    x(message = message,data = data, user = user, message_element = message_element, )
                if message_element.dophandler == True:
                    self.dophandler(message = message, data = data, user = user, message_element = message_element, call_id = call_id)
                
        
        elif user.role !='admin':
            if len(message.text) != 0:
                action = m.Command.objects.filter(action=message.text.lower()).first()
                waitmessage = m.User.objects.filter(waitmessage = True)
                if waitmessage:
                    frame_value = user.frame
                    x = getattr(self, frame_value)
                    x(message = message, data = None, user = user, message_element = None)
                if action is not None:
                    message_element = action.message_element
                    if message_element.handler == None:
                        self.base_logic(message = message, data = data, user = user, message_element = message_element)
                    else:
                        x = getattr(self, message_element.handler)
                        x(message = message,data = data, user = user, message_element = message_element)
                    if message_element.dophandler == True:
                        self.dophandler(message = message, data = data, user = user, message_element = message_element, call_id = call_id)
            
            #else:

            #    message_element = m.message_element.objects.filter(name = 'help_text')[0]
            #    self.base_logic(message = message, data = data, user = user, message_element = message_element)








bot = telebot.TeleBot('6067492832:AAHQS3M04prSw6gOmyaGnV6qJineUw6JZ0s')

#хороший тон, вызов функции после ее описания
@bot.message_handler(content_types = ['text'])
def Message(message):
    FMS().executor(message = message,data = None, user_id = message.from_user.id, call_id = None)

@bot.callback_query_handler(func=lambda call: True)
def Calldata(call):
    data = call.data
    data_id = call.id
    FMS().executor(message = None,data = data, user_id= call.from_user.id, call_id = data_id)

bot.polling(none_stop=True, interval=0)
# Не забыть про data = call.split(',')