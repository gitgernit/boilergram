import aiogram.filters
import aiogram.dispatcher


demo_router = aiogram.Router()

command_router = aiogram.Router()
text_router = aiogram.Router()
other_types_router = aiogram.Router()

demo_router.include_routers(command_router, text_router, other_types_router)


@command_router.message(aiogram.filters.Command('start'))
async def start(message: aiogram.types.Message):
    await message.answer('Welcome to boilergram!')


@command_router.message(aiogram.filters.Command('dice'))
async def dice(message: aiogram.types.Message):
    await message.answer_dice()


@text_router.message(aiogram.F.text)
async def text(message: aiogram.types.Message):
    await message.answer(f'Gotcha, Mr. "{message}"!')


@other_types_router.message()
async def photo(message: aiogram.types.Message):
    match message.content_type:
        case 'photo':
            await message.answer('That\'s got to be a photo.')

        case 'voice':
            await message.answer('That\'s got to be a voice message.')

        case 'animation':
            await message.answer('That\'s got to be an animation.')

        case _:
            await message.answer('Not sure what that is.')
