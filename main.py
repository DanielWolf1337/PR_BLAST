import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiohttp import web

# ТОКЕН (ТВОЙ НОВЫЙ)
TOKEN = "8717487273:AAHJyn3ajIW8Xo2khmQu1hyoKFI8sHmsbpY"
BOT_NAME = "PR BLAST"

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("✅ Бот работает! ID: " + str(message.from_user.id))

# Веб-сервер для Render
async def web_server():
    app = web.Application()
    app.router.add_get('/', lambda r: web.Response(text=f"{BOT_NAME} is running!"))
    port = int(os.environ.get('PORT', 10000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"✅ Веб-сервер на порту {port}")

# Главная функция
async def main():
    print(f"🚀 {BOT_NAME} запуск...")
    asyncio.create_task(web_server())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
