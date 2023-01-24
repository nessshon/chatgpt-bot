import openai
from aiogram import Dispatcher
from aiogram.types import Message

from .filters.is_admin import IsAdmin


async def message_handler(message: Message):
    emoji = await message.answer("⌛️")

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
        await emoji.edit_text(text=response['choices'][0]['text'], parse_mode=None)

    except Exception as error:
        await emoji.edit_text(error.__str__())

def register(dp: Dispatcher):
    dp.register_message_handler(
        message_handler, IsAdmin(),
        content_types="text", state="*"
    )
