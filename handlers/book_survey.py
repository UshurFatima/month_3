from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
# for organizing bot behavior into distinct states and
# managing transitions between them;  to simulate sequential
# logic, or, in other words, to represent and control execution flow
from aiogram.fsm.context import FSMContext
from bot_config import database

survey_router = Router()


class BookSurvey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    genre = State()


@survey_router.message(Command('opros'))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.name)
    await message.answer('Как Вас зовут?')


@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookSurvey.age)
    await message.answer('Сколько Вам лет?')


@survey_router.message(BookSurvey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer('Вводите только цифры')
        return
    age = int(age)
    if 12 < age > 100:
        await message.answer('Вводите возраст от 12 до 100')
        return
    await state.update_data(age=age)
    await state.set_state(BookSurvey.gender)
    await message.answer('Какого вы пола?')


@survey_router.message(BookSurvey.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(BookSurvey.genre)
    await message.answer('Ваш любимый жанр книг?')


@survey_router.message(BookSurvey.genre)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)

    await message.answer('Спасибо за пройженный опрос!')
    data = await state.get_data()
    print(data)

    database.execute(query='''INSERT INTO book_survey (name, age, gender, genre) VALUES 
    (?, ?, ?, ?)''', params=(
        data.get('name'),
        data.get('age'),
        data.get('gender'),
        data.get('genre')
    )
                     )

    # чтобы бот не ожидал больше ответа; очищаем данные и состояния
    await state.clear()
