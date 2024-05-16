from aiogram import Router, types, F
from aiogram.types import CallbackQuery

from keyboard.keyboard_repka import *
from lexicon.lexicon_repka import *

router =Router()


@router.callback_query(F.data == "repka_1")
async def repka_1(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/repka_1.jpg"),
        caption=repka_1_text,
        reply_markup=repka_1_kb
    )
@router.callback_query(F.data == "repka_2")
async def repka_2(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/repka_2.jpg"),
        caption=repka_2_text,
        reply_markup=repka_2_kb
    )
@router.callback_query(F.data == "repka_3")
async def repka_3(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/repka_3.jpg"),
        caption=repka_3_text,
        reply_markup=repka_3_kb
    )
@router.callback_query(F.data == "repka_4")
async def repka_4(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/repka_4.jpg"),
        caption=repka_4_text,
        reply_markup=repka_4_kb
    )
@router.callback_query(F.data == "repka_5")
async def repka_5(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/repka_5.jpg"),
        caption=repka_5_text,
        reply_markup=repka_5_kb
    )
@router.callback_query(F.data == "repka_6")
async def repka_6(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/repka_6.jpg"),
        caption=repka_6_text,
        reply_markup=repka_6_kb
    )
@router.callback_query(F.data == "repka_7")
async def repka_7(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/repka_7.jpg"),
        caption=repka_7_text,
        reply_markup=repka_7_kb
    )
@router.callback_query(F.data == "repka_8")
async def repka_8(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/repka_8.jpg"),
        caption=repka_8_text,
        reply_markup=repka_8_kb
    )
