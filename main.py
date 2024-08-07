import asyncio
# for async/await syntax
import logging
# store information, like which user or IP accessed
# the application. If an error occurs, then logs may
# provide (in terminal) useful insights by telling you
# the state of the program before the error and the line of code
# where it occurred.

<<<<<<< HEAD
from bot_config import bot, dp
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.echo import echo_router
=======

load_dotenv()  # чтоб все, что было в env стало доступным в коде
token = getenv('BOT_TOKEN')
# token is like login/password: is needed to know which bot is used
# По этому токену сервера Telegram будут понимать,
# какой именно бот к ним обращается.
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_handler(message: types.Message):  # handler - обработчик
    print(vars(message.from_user))  # информация о пользователе
    await message.answer(f'Привет, {message.from_user.first_name}! '
                         f'Я первый бот Фатимы!')


@dp.message(Command('picture'))
async def picture_handler(message: types.Message):
    image = types.FSInputFile('images/cat.jpg')
    # file system input file: to retrieve image
    await message.answer_photo(
        photo=image,
        caption='Крутой кот'
    )


# декоратор вызывает функции при наступлении определенных событий
# чтоб бот определял как отвечать на какие команды
@dp.message()
async def echo_handler(message: types.Message):  # handler - обработчик
    await message.reply(message.text)  # текст полученного сообщения
>>>>>>> a6f518c416500ea5efd19606b3a1b43c2fea3fb1


async def main():
    # добавляем маршрутизаторы диспетчеру, чтобы соединить с файлами-обработчиками
    dp.include_routers(start_router, picture_router, echo_router)  # echo_router в самый конец
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # объем показанной информации
    asyncio.run(main())
