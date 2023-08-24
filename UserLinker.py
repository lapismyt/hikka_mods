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
    def getuseridcmd(self, message):
        """<reply> - Get user ID"""
        if (hasattr(message, "reply_to")) and (message.reply_to is not None):
            utils.answer(message, self.strings["answer_getid"].format(str(message.reply_to_peer_id.user_id)))
        else:
            utils.answer(message, self.strings["error"].format("No reply!"))

    @loader.command(ru_doc="<id пользователя> <текст> - Отправить ссылку на пользователя")
    @loader.ratelimit
    def userlinkcmd(self, message):
        """<user_id> <text> - Make link for user"""
        args = utils.get_args(message)
        if len(args) == 2:
            utils.answer(message, self.strings["answer"].format(args[0], args[1]))
        else:
            utils.answer(message, self.strings["error"].format("Args count must be 2"))
