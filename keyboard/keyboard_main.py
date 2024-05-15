from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

png = ("⌚️📱📲💻⌨️🖥🖨🖱🖲🕹🗜💽💾💿📀📼📷📸📹🎥📽🎞📞☎️📟📠📻🎙🎚🎛🧭⏱⏲⏰🕰⌛️⏳📡🔋🪫"
       "🔌💡🔦🕯🪔🧯🛢💸💵💴💶💷🪙💰💳🪪💎⚖️🪜🧰🪛🔧🔨⚒🛠⛏🪚🔩⚙️🆗🔙")

main_1 = InlineKeyboardButton(text="О разработчике ⚙️", callback_data="contacts")
main_2 = InlineKeyboardButton(text="Репка", callback_data="repka_1")


main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [main_2],
        [main_1]
    ]
)
