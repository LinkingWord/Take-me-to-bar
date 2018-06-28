import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import bot_settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {
	'proxy_url': 'socks5://t1.learn.python.ru:1080',
	'urllib3_proxy_kwargs': {
		'username': 'learn', 
		'password': 'python'
	}
}

def start_bot(bot, update):
	# print(update)
	first_greeting = 'Привет, {}!'.format(update.message.chat.first_name, '/start')

	update.message.reply_text(first_greeting)


# def chat(bot, update):
# 	user_text = update.message.text
# 	logging.info(user_text)
# 	update.message.reply_text('Привет, {}!').format(update.message.chat.first_name)


def  main():
	mybot = Updater(bot_settings.TAKE_ME_BOT_APIKEY, request_kwargs=PROXY)
	mybot.dispatcher.add_handler(CommandHandler('start', start_bot))
	mybot.dispatcher.add_handler(MessageHandler(Filters.text, chat))
	mybot.start_polling()
	mybot.idle()	


if __name__ == '__main__':
	logging.info('Bot started')
	main()