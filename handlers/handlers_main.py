from aiogram import Router, types, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from keyboard.keyboard_main import main_kb

router =Router()


@router.message(CommandStart())
async def process_start_command(mes: Message):
    await mes.answer_photo(
        types.FSInputFile(path="image/main.jpg"),
        caption="Добро пожаловать в мир сказок!\nВыберите сказку для чтения.",
        reply_markup=main_kb
    )


@router.callback_query(F.data == "main")
async def main_menu(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/main.jpg"),
        caption="Добро пожаловать в мир сказок!\nВыберите сказку для чтения.",
        reply_markup=main_kb
    )


@router.message()
async def other_answer(mes: Message):
    await mes.delete()