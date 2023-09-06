from aiogram import *
from decouple import config 


bot = Bot(config('API_TOKEN'))
dp = Dispatcher(bot)
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
toys = types.ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.add(types.KeyboardButton(text="🎁 Покупка игрушек 🎁"),types.KeyboardButton(text="📞 Связь с администрацией 📞"))
toys.add(types.KeyboardButton(text="🚗 Машинка 🚗"),types.KeyboardButton(text="⚽ Мячик ⚽"))
toys.add(types.KeyboardButton(text="🛡 Танк 🛡"),types.KeyboardButton(text="🤖 Робот 🤖"))
toys.add(types.KeyboardButton(text="👈 Назад 👈"))

@dp.message_handler(commands=['start'])
async def start(messege: types.Message):
    await messege.answer("Добро пожаловать в Магазин игрушек 'Нагибатор'\nЧтобы купить игрушку нажмите ниже👇",reply_markup=keyboard)
    
    
@dp.message_handler(text=['📞 Связь с администрацией 📞'])
async def help(messege: types.Message):
    await messege.answer('Если вам нужна помощь то обратитесь к администратору @viktor12800')
    
    
@dp.message_handler(text=['🎁 Покупка игрушек 🎁'])
async def toy(messege: types.Message):
    await messege.answer("Вот нашы все игрушки\nВыберете игрушку которую хотите купить👇",reply_markup=toys)
    
@dp.message_handler(text=['👈 Назад 👈'])
async def back(messege: types.Message):    
    await messege.answer("❗ Главное меню ❗",reply_markup=keyboard)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)