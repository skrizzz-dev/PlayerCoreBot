from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram import F
from keyboards import start_keyboard, genre_keyboard, lenght_keyboard, type_keyboard

def register_handlers(dp):
    @dp.message(Command("start"))
    async def cmd_start(message: Message):
        await message.answer("Хочешь подбирать игру?", reply_markup=start_keyboard)
        
    @dp.callback_query(F.data == "start_search") 
    async def start_search(callback: CallbackQuery): 
        await callback.answer() 
        await callback.message.answer("Выбери жанр:", reply_markup=genre_keyboard)
    
    @dp.callback_query(F.data.startswith("genre_"))
    async def genre_selected(callback: CallbackQuery):
        await callback.answer() 
        await callback.message.answer("Выбери длительность прохождения игры", reply_markup=lenght_keyboard)
        
    @dp.callback_query(F.data.startswith("lenght_"))
    async def lenght_selected(callback: CallbackQuery):
        await callback.answer() 
        await callback.message.answer("Выбери тип игры", reply_markup=type_keyboard)