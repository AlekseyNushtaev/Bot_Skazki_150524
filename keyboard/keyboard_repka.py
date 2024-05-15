from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


to_main = InlineKeyboardButton(text="В главное меню", callback_data="main")
repka_1_forward = InlineKeyboardButton(text="Вперед", callback_data="repka_2")
repka_2_back = InlineKeyboardButton(text="Назад", callback_data="repka_1")
repka_2_forward = InlineKeyboardButton(text="Вперед", callback_data="repka_3")
repka_3_back = InlineKeyboardButton(text="Назад", callback_data="repka_2")
repka_3_forward = InlineKeyboardButton(text="Вперед", callback_data="repka_4")
repka_4_back = InlineKeyboardButton(text="Назад", callback_data="repka_3")
repka_4_forward = InlineKeyboardButton(text="Вперед", callback_data="repka_5")
repka_5_back = InlineKeyboardButton(text="Назад", callback_data="repka_4")
repka_5_forward = InlineKeyboardButton(text="Вперед", callback_data="repka_6")
repka_6_back = InlineKeyboardButton(text="Назад", callback_data="repka_5")
repka_6_forward = InlineKeyboardButton(text="Вперед", callback_data="repka_7")
repka_7_back = InlineKeyboardButton(text="Назад", callback_data="repka_6")
repka_7_forward = InlineKeyboardButton(text="Вперед", callback_data="repka_8")
repka_8_back = InlineKeyboardButton(text="Вперед", callback_data="repka_7")


repka_1_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [repka_1_forward],
        [to_main]
    ]
)
repka_2_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [repka_2_back, repka_2_forward],
        [to_main]
    ]
)
repka_3_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [repka_3_back, repka_3_forward],
        [to_main]
    ]
)
repka_4_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [repka_4_back, repka_4_forward],
        [to_main]
    ]
)
repka_5_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [repka_5_back, repka_5_forward],
        [to_main]
    ]
)
repka_6_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [repka_6_back, repka_6_forward],
        [to_main]
    ]
)
repka_7_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [repka_7_back, repka_7_forward],
        [to_main]
    ]
)
repka_8_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [repka_8_back],
        [to_main]
    ]
)
