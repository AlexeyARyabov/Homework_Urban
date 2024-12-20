from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *


products = get_all_products()
api ='7761000920:AAH49PJrIf4LJb0HvMBcP8QOdfGLEB2w2MM'
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Рассчитать'),
        KeyboardButton(text='Информация')
        ],
        [
        KeyboardButton(text='Купить'),
        KeyboardButton(text='Регистрация')
        ]
    ],
    resize_keyboard=True)


kb_inl = InlineKeyboardMarkup(resize_keyboard=True)
btn_calc = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
btn_form = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inl.row(btn_calc, btn_form)

product_kb = InlineKeyboardMarkup(
    inline_keyboard=[
      [
          InlineKeyboardButton(text='Product1', callback_data='product_buying'),
          InlineKeyboardButton(text='Product2', callback_data='product_buying'),
          InlineKeyboardButton(text='Product3', callback_data='product_buying'),
          InlineKeyboardButton(text='Product4', callback_data='product_buying')
      ]
    ],
    resize_keyboard=True)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inl)

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for product in products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена:{product[3]}')
        with open(f'files/{product[0]}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=product_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()

# Расчет калорий по параметрам (возраст, рост, вес)
@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост в см:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f"Ваша норма калорий: {int(data['weight'])*10 + int(data['growth']) * 6.25 - 5 * int(data['age']) - 161}",
                         reply_markup=kb)
    await state.finish()

# Регистрация пользователя
@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно', reply_markup=kb)
    await state.finish()

# Реакция на произвольный текст
@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)