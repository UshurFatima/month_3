from aiogram import Router, types, F  # F - magic filter
from aiogram.filters.command import Command


start_router = Router()


@start_router.message(Command('start'))
async def echo_handler(message: types.Message):  # handler - обработчик
    # print(vars(message.from_user))  # информация о пользователе
    kb = types.InlineKeyboardMarkup(  # markup - разметка кнопок
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Наш сайт', url='https://online.geeks.kg'),
                types.InlineKeyboardButton(text='Наш инстаграм', url='https://instagram.com/geeks_edu')
            ],  # расположение кнопок зависит от списка
            [
                types.InlineKeyboardButton(text='Информация о нас', callback_data='about_us')
            ],
            [
                types.InlineKeyboardButton(text='Вакансии', callback_data='vacancies')
            ]
        ]
    )
    await message.answer(f'Привет, {message.from_user.first_name}! '
                         f'Я первый бот Фатимы!', reply_markup=kb)


# @start_router.callback_query(lambda callback: callback.data='about_us')
#             так как тут ответ не на сообщение, а на кнопку
@start_router.callback_query(F.data == 'about_us')  # сокращенная версия
async def aboutus_handler(callback: types.CallbackQuery):  # функция принимает в себя вызов кнопки
    # await callback.answer('hi, didn`t expect me?')
    await callback.message.answer('Тут будет о нас')


@start_router.callback_query(F.data == 'vacancies')  # F.data: data потому что инфа с кнопки
async def vacancies_handler(callback: types.CallbackQuery):
    await callback.message.answer('Тут будут вакансии')
