"""
Licensed under GNU General Public License v3:
https://github.com/lapismyt/hikka_mods/blob/main/LICENSE
"""

# meta developer: @LapisMods

__version__ = (1, 0, 0)

import logging
from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class UserLinkerMod(loader.Module):
    
    strings = {
        "name": "UserLinker",
        "error": "<b>❗️Error!\n{0}</b>",
        "answer_getid": "User ID: <pre>{0}</pre>",
        "answer_userlink": "<a href=\"tg://user?id={0}\">{1}</a>"
    }

    strings_ru = {
        "error": "<b>❗️ Ошибка!\n{0}</b>",
        "answer_getid": "ID пользователя: <pre>{0}</pre>"
    }

    def __init__(self):
        self.name = self.strings["name"]

    @loader.command(ru_doc="<reply> - Узнать ID пользователя")
    @loader.ratelimit
    async def getuseridcmd(self, message):
        """<reply> - Get user ID"""
        if hasattr(message, "reply_to"):
            user_id = (await message.get_reply_message()).sender.id
            await utils.answer(message, self.strings["answer_getid"].format(str(user_id)))
        else:
            await utils.answer(message, self.strings["error"].format("No reply!"))

    @loader.command(ru_doc="<id пользователя> <текст> - Отправить ссылку на пользователя")
    @loader.ratelimit
    async def userlinkcmd(self, message):
        """<user_id> <text> - Make link for user"""
        args = await utils.get_args_raw(message)
        user_id = args[0]
        text = args[1:]
        if len(args) == 2:
            await utils.answer(message, self.strings["answer"].format(user_id, text))
        else:
            await utils.answer(message, self.strings["error"].format("Args count must be 2"))
