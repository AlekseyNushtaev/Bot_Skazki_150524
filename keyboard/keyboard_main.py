from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

png = ("⌚️📱📲💻⌨️🖥🖨🖱🖲🕹🗜💽💾💿📀📼📷📸📹🎥📽🎞📞☎️📟📠📻🎙🎚🎛🧭⏱⏲⏰🕰⌛️⏳📡🔋🪫"
       "🔌💡🔦🕯🪔🧯🛢💸💵💴💶💷🪙💰💳🪪💎⚖️🪜🧰🪛🔧🔨⚒🛠⛏🪚🔩⚙️🆗🔙")

main_1 = InlineKeyboardButton(text="О разработчике ⚙️", callback_data="contacts")
main_2 = InlineKeyboardButton(text="Репка", callback_data="repka_1")
main_3 = InlineKeyboardButton(text="Три медведя", callback_data="bears_1")
main_4 = InlineKeyboardButton(text="Теремок", callback_data="terem_1")


main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [main_2],
        [main_3],
        [main_4],
        [main_1]
    ]
)
