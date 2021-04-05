import random
import string
import telebot
USERS = []

bot = telebot.TeleBot('1708020452:AAFQCmIKVxgUbZu9YhKxxcdE12Vh2uF3cVE');


@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id,'Команды:' + '\n' + '/pass (генерация пароля)' + '\n' + '/all (все ваши пароли')

@bot.message_handler(commands=['start'])
def start(message):
	if message.chat.id not in USERS:
		bot.send_message(message.chat.id, 'Привет! Это бот по генерации паролей!' + '\n' + 'Подробнее - /help', parse_mode='html')
		USERS.append(message.chat.id)
	else:
		bot.send_message(message.chat.id, 'Извини, ты уже его активировал')


@bot.message_handler(commands=['pass'])
def pas(message):
	rand_string = '12345467890qwertyuiopasdfghjklzxcvbnm'
	ls = list(rand_string)
	random.shuffle(ls)
	ls = ls[:(random.randint(6, 15))]
	print("".join(ls))
	my_file = open(str(message.chat.id) + '.txt', "a+")
	my_file.write("".join(ls) + '\n')
	my_file.close()
	bot.send_message(message.chat.id,"".join(ls))


@bot.message_handler(commands=['all'])
def all(message):
	# sendDocument
	doc = open(str(message.chat.id) + '.txt', 'rb')
	bot.send_document(message.chat.id, doc)
	bot.send_document(message.chat.id, "FILEID") 


if __name__ == '__main__':
	bot.polling(none_stop=True)