#1 - Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования


from datetime import datetime


def log_to_file(temp, result):
    with open('log.csv', 'a') as file:
        file.write(f'{datetime.today()}; {temp[0]}; {temp[2]};{temp[1]};{result}; \n')

#2 - Перенести игру в конфеты на интерфейс телеграма
import telebot 

token = '5728793661:AAGWT9H1QcrBy4VE5vGck3vGqmHX1j5JGQA'

bot = telebot (TOKEN)

@bot.message_handler(commands=['start'])
def stsrt_answer (msg: telebot.types.Message):
    bot.send_message (chat_id=msg.from_user.id, text = f'Вы прислали команду: {msg.text}')


@bot.message_handler()
def answer (msg: telebot.types.Message):
    bot.send_message (chat_id=msg.from_user.id, text = f'Вы прислали: {msg.text}')


bot.polling ()
