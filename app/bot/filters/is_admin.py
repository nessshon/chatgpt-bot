from aiogram.types import ChatType, Message
from aiogram.dispatcher.filters import BoundFilter


class IsAdmin(BoundFilter):

    async def check(self, message: Message) -> bool:
        admin_ids = message.bot.get("admin_ids")

        return str(message.chat.id) in admin_ids
