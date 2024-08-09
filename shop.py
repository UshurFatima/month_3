from aiogram import F, Router, types
from aiogram.filters.command import Command


shop_router = Router()


@shop_router.message(Command('shop'))
async def shop_handler(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Детектив'),
                types.KeyboardButton(text='Роман')
            ],
            [
                types.KeyboardButton(text='Фэнтези'),
                types.KeyboardButton(text='Триллер')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Выберите жанр книг', reply_markup=kb)


@shop_router.message(F.text.lower() == 'детектив')  # F.text: text потому что инфа с сообщения
async def detective_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Книги жанра Детектив', reply_markup=kb)


@shop_router.message(F.text.lower() == 'роман')
async def novel_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Книги жанра Роман', reply_markup=kb)


@shop_router.message(F.text.lower() == 'фэнтези')
async def fantasy_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Книги жанра Фэнтези', reply_markup=kb)


@shop_router.message(F.text.lower() == 'триллер')
async def thriller_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Книги жанра Триллер', reply_markup=kb)

