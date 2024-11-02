from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api =''
bot = Bot(token=api)

dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Рассчитать'),
        KeyboardButton(text='Информация')
        ],
        [
        KeyboardButton(text='Купить')
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

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_inl)

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for number in range(1,5):
        await message.answer(f'Название: Product{number} | Описание: описание{number} | Цена: {number * 100}')
        with open(f'files/{number}.jpg', 'rb') as img:
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
    await message.answer(f"Ваша норма калорий: {int(data['weight'])*10 + int(data['growth']) * 6.25 - 5 * int(data['age']) - 161}")
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)