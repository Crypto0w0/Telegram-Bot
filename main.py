import requests
from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)
res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Odessa&appid={WHEATHER_API_KEY}&units=metric')

res = res.json()

#def getTemp(res):
  #return res['weather']['temp']

@dp.message_handler(commands='start')
async def start(message: types.Message):
  await message.answer("Hello")

@dp.message_handler(commands='test')
async def start(message: types.Message):
  await message.answer("This is test")

executor.start_polling(res['weather']['temp'])
