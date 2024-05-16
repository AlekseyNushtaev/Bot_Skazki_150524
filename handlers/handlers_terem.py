from aiogram import Router, types, F
from aiogram.types import CallbackQuery

from keyboard.keyboard_creator import create_kb
from lexicon.lexicon_terem import terem_text

router =Router()


@router.callback_query(F.data == "terem_1")
async def terem_1(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/terem_1.jpg"),
        caption=terem_text[1],
        reply_markup=create_kb(1, terem_2="Вперед", main="В главное меню")
    )


@router.callback_query(lambda call: call.data in [f"terem_{i}" for i in range(2,7)])
async def terem(cb: CallbackQuery):
    await cb.message.delete()
    back = int(cb.data[-1]) - 1
    fwd = back + 2
    dct = {
        cb.data[:-1] + str(back): "Назад",
        cb.data[:-1] + str(fwd): "Вперед",
    }
    await cb.message.answer_photo(
        types.FSInputFile(path=f"image/{cb.data}.jpg"),
        caption=terem_text[int(cb.data[-1])],
        reply_markup=create_kb(2, **dct, main="В главное меню")
    )


@router.callback_query(F.data == "terem_7")
async def terem_7(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/terem_7.jpg"),
        caption=terem_text[7],
        reply_markup=create_kb(1, terem_6="Назад", main="В главное меню")
    )