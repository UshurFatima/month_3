import asyncio
# for async/await syntax
import logging
# store information, like which user or IP accessed
# the application. If an error occurs, then logs may
# provide (in terminal) useful insights by telling you
# the state of the program before the error and the line of code
# where it occurred.

 
from bot_config import bot, dp, set_bot_commands, database
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.echo import echo_router
from shop import shop_router
from handlers.book_survey import survey_router


async def on_startup(bot):
    print('Бот запустился')
    database.create_tables()


async def main():
    await set_bot_commands()
    # добавляем маршрутизаторы диспетчеру, чтобы соединить с файлами-обработчиками
    dp.include_routers(start_router, picture_router,
                       survey_router, shop_router,
                       echo_router)  # echo_router в самый конец

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # объем показанной информации
    asyncio.run(main())
