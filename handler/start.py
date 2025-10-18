from aiogram import types, Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm import state
from aiogram.fsm.context import FSMContext

from keyboard.default_keyboard import main_keyboard, back_keyboard
from states.user import PartnerState

router = Router()


@router.message(Command('start'))
async def send_message(message: types.Message):
    await message.answer("""Assalom alaykum Abu_weyh1
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""",
                         reply_markup=main_keyboard())


@router.message(F.text == 'Sherik kerak')
async def send_message(message: types.Message, state: FSMContext):
    await message.answer("""<b>Sherik topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""",
                         reply_markup=back_keyboard(),
                         parse_mode="HTML")
    await message.answer("Ismingizni kiriting?")
    await state.set_state(PartnerState.fullname)


@router.message(StateFilter(PartnerState.fullname))
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    await message.answer(text="""📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#""")

    await state.set_state(PartnerState.job)

    @router.message(StateFilter(PartnerState.job))
    async def get_name(message: types.Message, state: FSMContext):
        await state.update_data(job=message.text)
        await message.answer(text="""📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""")

        await state.set_state(PartnerState.contact)

        @router.message(StateFilter(PartnerState.contact))
        async def get_name(message: types.Message, state: FSMContext):
            await state.update_data(contact=message.text)
            await message.answer(text="""🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")

            await state.set_state(PartnerState.address)

        await state.set_state(PartnerState.address)

        @router.message(StateFilter(PartnerState.address))
        async def get_name(message: types.Message, state: FSMContext):
            await state.update_data(address=message.text)
            await message.answer(text="""💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")

            await state.set_state(PartnerState.price)

            @router.message(StateFilter(PartnerState.price))
            async def get_name(message: types.Message, state: FSMContext):
                await state.update_data(price=message.text)
                await message.answer(text="""👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba""")

                await state.set_state(PartnerState.study_or_work)

                @router.message(StateFilter(PartnerState.study_or_work))
                async def get_name(message: types.Message, state: FSMContext):
                    await state.update_data(study_or_work=message.text)
                    await message.answer(text="""🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")

                    await state.set_state(PartnerState.goal)

                    @router.message(StateFilter(PartnerState.goal))
                    async def get_address(message: types.Message, state: FSMContext):
                        data = await state.get_data()
                        fullname = data.get("fullname")
                        job = data.get("job")
                        contact = data.get("contact")
                        address = data.get("address")
                        price = data.get("price")
                        study_or_work = data.get("study_or_work")
                        time = data.get("time")
                        goal = message.text

                        await state.clear()

                        await message.answer(text=f"""Sherik kerak:

🏅 Sherik: {fullname} 
📚 Texnologiya: {job}
🇺🇿 Telegram: {message.from_user.username}
📞 Aloqa: {contact}
🌐 Hudud: {address}
💰 Narxi: {price} 
👨🏻‍💻 Kasbi:  {study_or_work}
🕰 Murojaat qilish vaqti: {time}
🔎 Maqsad: o'ldirish {goal}

#sherik #{job} #{address}""",
                                             reply_markup=main_keyboard())
