from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

png = ("⌚️📱📲💻⌨️🖥🖨🖱🖲🕹🗜💽💾💿📀📼📷📸📹🎥📽🎞📞☎️📟📠📻🎙🎚🎛🧭⏱⏲⏰🕰⌛️⏳📡🔋🪫"
       "🔌💡🔦🕯🪔🧯🛢💸💵💴💶💷🪙💰💳🪪💎⚖️🪜🧰🪛🔧🔨⚒🛠⛏🪚🔩⚙️🆗🔙")

main_1 = InlineKeyboardButton(text="Обратная связь ⚙️", callback_data="contacts")
main_2 = InlineKeyboardButton(text="Репка", callback_data="repka_1")
main_3 = InlineKeyboardButton(text="Три медведя", callback_data="bears_1")
main_4 = InlineKeyboardButton(text="Теремок", callback_data="terem_1")
back = InlineKeyboardButton(text="В главное меню", callback_data="main")
contact = InlineKeyboardButton(text="Отправить сообщение", url="https://t.me/alekseinushtaev")



main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [main_2],
        [main_3],
        [main_4],
        [main_1]
    ]
)

contact_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [contact],
        [back]
    ]
)
