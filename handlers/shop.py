from aiogram import F, Router, types
from aiogram.filters.command import Command

from keyboards import genres_keyboard
from bot_config import database

shop_router = Router()


@shop_router.message(Command('shop'))
async def shop_handler(message: types.Message):
    await message.answer('Выберите жанр книг', reply_markup=genres_keyboard())


genres = {'детектив', 'роман', 'фантастика', 'хоррор'}


@shop_router.message(F.text.lower().in_(genres))
async def genres_handler(message: types.Message):
    genre = message.text
    print(genre)
    kb = types.ReplyKeyboardRemove()
    # запрос в БД -> пользователь отправил название жанра,
    # и по названию жанра ищем книги
    books = database.fetch(
        '''
        SELECT * FROM books JOIN
        genres ON books.genre_id = genres.id
        WHERE genres.name = ?
        ''',
        (genre.capitalize(),)
    )
    if not books:
        await message.answer(f'Книг жанра {genre} нет в продаже')
        return

    # pprint(books)
    await message.answer(
        f'Книги жанра {genre}: ',
        reply_markup=kb
    )
    for book in books:
        cover = types.FSInputFile(book.get('cover'))
        await message.answer_photo(photo=cover, caption=f'Название: {book.get('name')}\n'
                                                        f'Цена: {book.get('price')} сом')
