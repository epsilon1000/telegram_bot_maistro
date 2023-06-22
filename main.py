import os
import openai
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
bot = Bot(token=os.getenv("TELEGRAM_BOT_KEY"))

dp = Dispatcher(bot)

first_prompt = 'You are an useful assistant called "Maistro", you are programmed to answer any questions the user asks'



@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
    await message.reply('¡Hola! Soy el Maistro, un bot que sabe cosas. ¿En qué puedo ayudarte?')


@dp.message_handler()
async def gpt(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    await message.reply(response.choices[0].text)


if __name__ == "__main__":
    executor.start_polling(dp)
