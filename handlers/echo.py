from aiogram import Router, types
# Роутер определяет путь, по которому следует передать данные
# Данные перемещаются по любой сети в виде пакетов данных

echo_router = Router()


# декоратор вызывает функции при наступлении определенных событий
# чтоб бот определял как отвечать на какие команды
@echo_router.message()
async def echo_handler(message: types.Message):  # handler - обработчик
    await message.reply(message.text)  # текст полученного сообщения

