import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import register_handlers
from database import init_db


bot = Bot(token=TOKEN)
dp = Dispatcher()
init_db()

register_handlers(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())