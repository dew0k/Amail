#
import telebot
import config

bot = telebot.TeleBot(config.API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.from_user.id, 'Amail - это бот для отправки и получения анонимных писем.\nДля получения писем от анонов нужно только запустить бота.\nДля отправки же нужно знать id пользователя.\nБолее подробно в /help')

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.from_user.id, 'Формат отправки сообщения:\n/send айди_получателя текст_сообщения\nПример:\n/send 12345678 Привет! Это Amail.')

@bot.message_handler(commands=['send'])
def send(message):
	sender = message.from_user.id
	geter = int(message.text.split(maxsplit=2)[1])
	text = message.text.split(maxsplit=2)[-1]

	try:
		bot.send_message(geter, f'Для вас анонимное письмо:\n{text}')
		bot.send_message(sender, 'Письмо отправленно')
	except:
		bot.send_message(sender, 'Не удалось отправить письмо')

if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        pass