from aiogram import Router, types, F
from aiogram.types import CallbackQuery

from keyboard.keyboard_creator import create_kb
from lexicon.lexicon_bears import bears_text

router =Router()


@router.callback_query(F.data == "bears_1")
async def bears_1(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_1.jpg"),
        caption=bears_text[1],
        reply_markup=create_kb(1, bears_2="Вперед", main="В главное меню")
    )


@router.callback_query(F.data == "bears_2")
async def bears_2(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_2.jpg"),
        caption=bears_text[2],
        reply_markup=create_kb(2, bears_1="Назад", bears_3="Вперед", main="В главное меню")
    )


@router.callback_query(F.data == "bears_3")
async def bears_3(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_3.jpg"),
        caption=bears_text[3],
        reply_markup=create_kb(2, bears_2="Назад", bears_4="Вперед", main="В главное меню")
    )


@router.callback_query(F.data == "bears_4")
async def bears_4(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_4.jpg"),
        caption=bears_text[4],
        reply_markup=create_kb(2, bears_3="Назад", bears_5="Вперед", main="В главное меню")
    )


@router.callback_query(F.data == "bears_5")
async def bears_5(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_5.jpg"),
        caption=bears_text[5],
        reply_markup=create_kb(2, bears_4="Назад", bears_6="Вперед", main="В главное меню")
    )


@router.callback_query(F.data == "bears_6")
async def bears_6(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_6.jpg"),
        caption=bears_text[6],
        reply_markup=create_kb(2, bears_5="Назад", bears_7="Вперед", main="В главное меню")
    )


@router.callback_query(F.data == "bears_7")
async def bears_7(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_7.jpg"),
        caption=bears_text[7],
        reply_markup=create_kb(2, bears_6="Назад", bears_8="Вперед", main="В главное меню")
    )


@router.callback_query(F.data == "bears_8")
async def bears_8(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_8.jpg"),
        caption=bears_text[8],
        reply_markup=create_kb(2, bears_7="Назад", bears_9="Вперед", main="В главное меню")
    )


@router.callback_query(F.data == "bears_9")
async def bears_9(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_9.jpg"),
        caption=bears_text[9],
        reply_markup=create_kb(2, bears_8="Назад", bears_10="Вперед", main="В главное меню")
    )


@router.callback_query(F.data == "bears_10")
async def bears_10(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_10.jpg"),
        caption=bears_text[10],
        reply_markup=create_kb(2, bears_9="Назад", bears_11="Вперед", main="В главное меню")
    )


@router.callback_query(F.data == "bears_11")
async def bears_11(cb: CallbackQuery):
    await cb.message.delete()
    await cb.message.answer_photo(
        types.FSInputFile(path="image/bears_11.jpg"),
        caption=bears_text[11],
        reply_markup=create_kb(1, bears_10="Назад", main="В главное меню")
    )
