from aiogram import *
from decouple import config

bot = Bot(config('API_TOKEN'))
dp = Dispatcher(bot)
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
toys = types.ReplyKeyboardMarkup(resize_keyboard=True)
payment = types.ReplyKeyboardMarkup(resize_keyboard=True)
selected_items = {}  
item_prices = {  
    "🚗 Машинка 🚗": 100,
    "⚽ Мячик ⚽": 50,
    "🛡 Танк 🛡": 150,
    "🤖 Робот 🤖": 200,
}
total_price = 0  

keyboard.add(types.KeyboardButton(text="🎁 Покупка игрушек 🎁"), types.KeyboardButton(text="📞 Связь с администрацией 📞"))
keyboard.add(types.KeyboardButton(text="💰 Оплата 💰"), types.KeyboardButton(text="❗ Сбросить товары ❗"))
keyboard.add(types.KeyboardButton(text="💰 Цены на игрушки 💰"))
toys.add(types.KeyboardButton(text="🚗 Машинка 🚗"), types.KeyboardButton(text="⚽ Мячик ⚽"))
toys.add(types.KeyboardButton(text="🛡 Танк 🛡"), types.KeyboardButton(text="🤖 Робот 🤖"))
toys.add(types.KeyboardButton(text="👈 Назад 👈"))
payment.add(types.KeyboardButton(text="💰 Перейти до оплаты 💰"), types.KeyboardButton(text="👈 Назад 👈"))


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Добро пожаловать в Магазин игрушек 'Нагибатор'\nЧтобы купить игрушку нажмите ниже👇", reply_markup=keyboard)


@dp.message_handler(text=['📞 Связь с администрацией 📞'])
async def help(message: types.Message):
    await message.answer('Если вам нужна помощь, то обратитесь к администратору @viktor12800')


@dp.message_handler(text=['🎁 Покупка игрушек 🎁'])
async def toy(message: types.Message):
    await message.answer("Вот наши все игрушки\nВыберите игрушку, которую хотите купить👇", reply_markup=toys)


@dp.message_handler(lambda message: message.text in ["🚗 Машинка 🚗", "⚽ Мячик ⚽", "🛡 Танк 🛡", "🤖 Робот 🤖"])
async def process_selected_item(message: types.Message):
    item_name = message.text
    if item_name not in selected_items:
        selected_items[item_name] = 1
    else:
        selected_items[item_name] += 1
    global total_price  
    total_price += item_prices.get(item_name, 0)  

    await message.answer(f"Вы выбрали {item_name}. Текущее количество: {selected_items[item_name]}")


@dp.message_handler(text=['👈 Назад 👈'])
async def back(message: types.Message):
    await message.answer("❗ Главное меню ❗", reply_markup=keyboard)


@dp.message_handler(text=["💰 Оплата 💰"])
async def checkout(message: types.Message):
    checkout_text = "Ваш чек товаров:\n"
    for item_name, quantity in selected_items.items():
        checkout_text += f"{item_name} : {quantity} шт\n"
    checkout_text += f"Общая сумма: {total_price} грн\nХотите оплатить сейчас?"
    await message.answer(checkout_text, reply_markup=payment)


@dp.message_handler(text=['❗ Сбросить товары ❗'])
async def reset_items(message: types.Message):
    global total_price, selected_items
    total_price = 0
    selected_items = {}
    await message.answer("Все товары были сброшены.")

@dp.message_handler(text=["💰 Перейти до оплаты 💰"])
async def next(message: types.Message):
    link = "https://www.example.com"  
    await message.answer(f"Оплата ---> {link}")
    
@dp.message_handler(text=["💰 Цены на игрушки 💰"])
async def prices(message: types.Message):
    await message.answer("🚗 Машинка 🚗 -- 100 грн\n⚽ Мячик ⚽ -- 50 грн\n🛡 Танк 🛡 -- 150 грн\n🤖 Робот 🤖 -- 200грн")

    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    
    
    
    
    
    
    