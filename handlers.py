from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.filters import Command
from aiogram import F
from database import add_favorite, get_favorites, remove_favorite
from keyboards import start_keyboard, genre_keyboard, length_keyboard, type_keyboard, favorite_keyboard, remove_keyboard
import json, random


user_data = {}

def register_handlers(dp):
    @dp.message(Command("start"))
    async def cmd_start(message: Message):
        await message.answer("Хочешь подбирать игру?", reply_markup=start_keyboard)
        
    @dp.callback_query(F.data == "start_search") 
    async def start_search(callback: CallbackQuery): 
        await callback.answer() 
        await callback.message.answer("Выбери жанр:", reply_markup=genre_keyboard)
    
    @dp.callback_query(F.data.startswith("add_"))
    async def add_to_favorite(callback: CallbackQuery):
        title = callback.data.replace("add_", "")
        result = add_favorite(callback.from_user.id, title)
        if result == "ok":
            await callback.answer("Добавлено в избранное ❤️")
        elif result == "limit":
            await callback.answer("Больше 5 игр нельзя добавлять в избранное")
        elif result == "exists":
            await callback.answer("Эта игра уже в избранном 👾")
            
    @dp.message(Command("favorites"))
    async def show_favorites(message: Message):
        favorites = get_favorites(message.from_user.id)
        if not favorites:
            await message.answer("Избранное пуста, добавляй игры 🎮")
        else:
            for title in favorites:
                await message.answer(title, reply_markup=remove_keyboard(title))
            
    @dp.callback_query(F.data.startswith("remove_"))
    async def remove_from_favorite(callback: CallbackQuery):
        title = callback.data.replace("remove_", "")
        remove_favorite(callback.from_user.id, title)
        await callback.answer(f"'{title}' Удалено ❌")
        
 
    @dp.callback_query(F.data.startswith("genre_"))
    async def genre_selected(callback: CallbackQuery):
        await callback.answer()
        genre = callback.data.replace("genre_", "")
        user_data[callback.from_user.id] = {"genre": genre} 
        await callback.message.answer("Выбери длительность прохождения игры", reply_markup=length_keyboard)
        
    @dp.callback_query(F.data.startswith("length_"))
    async def length_selected(callback: CallbackQuery):
        await callback.answer()
        length= callback.data.replace("length_", "")
        user_data[callback.from_user.id]["length"] = length
        await callback.message.answer("Выбери тип игры", reply_markup=type_keyboard)
        
    @dp.callback_query(F.data.startswith("type_"))
    async def type_selected(callback: CallbackQuery):
        await callback.answer()
        game_type = callback.data.replace("type_", "")
        user_data[callback.from_user.id]["type"] = game_type
        data = user_data.get(callback.from_user.id, {})
        with open("games.json", "r", encoding="utf-8") as f:
            games = json.load(f)
        matches = [g for g in games if g["genre"] == data["genre"] and g["length"] == data["length"] and g["type"].lower() == data["type"]]
        game = random.choice(matches)
        if matches:
            await callback.message.answer_photo(
                photo=FSInputFile(game["image"]),
                caption=f"Название: {game['title']}\n\n{game['description']}",
                reply_markup=favorite_keyboard(game["title"]) 
            )
        else:
            await callback.message.answer("игр не нашлось 🤔 \n\nпопробуй заново\n\n/start")