import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiohttp import web

TOKEN = "8717487273:AAHJyn3ajIW8Xo2khmQu1hyoKFI8sHmsbpY"
BOT_NAME = "PR BLAST"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("✅ Бот работает! Твой ID: " + str(message.from_user.id))

async def web_server():
    app = web.Application()
    app.router.add_get('/', lambda r: web.Response(text=f"{BOT_NAME} is running!"))
    port = int(os.environ.get('PORT', 10000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"✅ Веб-сервер на порту {port}")

async def main():
    print(f"🚀 {BOT_NAME} запуск...")
    print(f"✅ Токен загружен: {TOKEN[:10]}...")
    asyncio.create_task(web_server())
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
if __name__ == "__main__":
    asyncio.run(main())
