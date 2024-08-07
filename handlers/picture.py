from aiogram import Router, types
# router как замена диспетчеру
from aiogram.filters.command import Command
# чтобы бот распознавал команды


picture_router = Router()  # создание объекта класса роутер
# чтобы использовать в main.py


@picture_router.message(Command('picture'))
# меняем dp на объект роутера
async def picture_handler(message: types.Message):
    image = types.FSInputFile('images/cat.jpg')
    # file system input file: to retrieve image
    await message.answer_photo(
        photo=image,
        caption='Крутой кот'
    )
