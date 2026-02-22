from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать поиск 👾", callback_data="start_search")]
    ]
)

genre_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Экшен ⚡️", callback_data="genre_action")],
        [InlineKeyboardButton(text="Хоррор 👻", callback_data="genre_horror")],
        [InlineKeyboardButton(text="Шутер 🔫", callback_data="genre_shooter")],
        [InlineKeyboardButton(text="Файтинг 👊", callback_data="genre_fighting")],
        [InlineKeyboardButton(text="Гонки", callback_data="genre_racing")]
    ]
)

length_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Короткая 💨", callback_data="length_short")],
        [InlineKeyboardButton(text="Средняя 🕹", callback_data="length_medium")],
        [InlineKeyboardButton(text="Долгая ⏳", callback_data="length_long")]
    ]
)

type_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ААА 🏆", callback_data="type_aaa")],
        [InlineKeyboardButton(text="Инди ⌨️", callback_data="type_indie")]
    ]
)

def favorite_keyboard(title):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="В избранное ❤️", callback_data=f"add_{title}")]
        ]
    )