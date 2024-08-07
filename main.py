import asyncio
# for async/await syntax
import logging
# store information, like which user or IP accessed
# the application. If an error occurs, then logs may
# provide (in terminal) useful insights by telling you
# the state of the program before the error and the line of code
# where it occurred.

from bot_config import bot, dp
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.echo import echo_router


async def main():
    # добавляем маршрутизаторы диспетчеру, чтобы соединить с файлами-обработчиками
    dp.include_routers(start_router, picture_router, echo_router)  # echo_router в самый конец
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # объем показанной информации
    asyncio.run(main())
