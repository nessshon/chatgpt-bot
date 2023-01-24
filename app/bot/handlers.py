import openai
from aiogram import Dispatcher
from aiogram.types import Message

from .filters.is_admin import IsAdmin


async def message_handler(message: Message):
    emoji = await message.answer("⌛️")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    await emoji.edit_text(text=response['choices'][0]['text'])


def register(dp: Dispatcher):
    dp.register_message_handler(
        message_handler, IsAdmin(),
        content_types="text", state="*"
    )
