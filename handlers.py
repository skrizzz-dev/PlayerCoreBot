from aiogram.types import Message
from aiogram.filters import Command
from keyboards import start_keyboard, genre_keyboard, lenght_keyboard, type_keyboard

def register_handlers(dp):
    @dp.message(Command("start"))
    async def cmd_start(message: Message):
        await message.answer("Хочешь подбирать игру?", reply_markup=start_keyboard)
        
