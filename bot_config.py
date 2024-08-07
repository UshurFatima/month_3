from aiogram import Bot, Dispatcher
# диспетчер занимается приёмом событий от Telegram и раскидыванием их по хэндлерам через фильтры и мидлвари.
from dotenv import load_dotenv
# loads the environment variables from your . env file
from os import getenv
# retrieves(извлекает) these variables so that you can use them in your script


load_dotenv()  # чтоб все, что было в env стало доступным в коде
token = getenv('BOT_TOKEN')
# token is like login/password: is needed to know which bot is used
# По этому токену сервера Telegram будут понимать,
# какой именно бот к ним обращается.
bot = Bot(token=token)
dp = Dispatcher()
