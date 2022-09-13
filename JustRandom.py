"""
Licensed under GNU General Public License v3:
https://github.com/lapismyt/hikka_mods/blob/main/LICENSE
"""

# meta developer: @LapisMods

__version__ = (1, 0, 5)

import logging
import random
from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class JustRandomMod(loader.Module):

    """Module for get random numbers from list"""

    strings = {
        "name": "JustRandom",
        "answer_randint": "<b>🎰 Random number is... ",
        "error": "<b>😢 Oops... I tried to help you, but error breaked my plans...</b>\n\n",
        "args_error": "<b>😢 Sorry, but this command accept only {0} args.</b>"}

    strings_ru = {
        "answer_randint": "<b>🎰 И выпадает число... ",
        "error": "<b>😢 Упс... Я попытался помочь вам, но ошибка помешала моим планам...</b>\n\n",
        "args_error": "<b>😢 Простите, но данная команда принимает только {0} аргумент(а/ов).</b>"
    }

    def __init__(self):
        self.name = self.strings["name"]

    @loader.command(ru_doc="<от: число> <до: число> - Случайное число из диапазона")
    @loader.ratelimit
    async def randintcmd(self, message):
        """<from: int> <to: int> - Random number from range"""

        try:
            args = utils.get_args(message)
            if len(args) == 2:
                result = random.randint(int(args[0]), int(args[1]))
                await utils.answer(message, self.strings["answer_randint"] + str(result) + "</b>")
            else:
                await utils.answer(message, self.strings["args_error"].format("2"))
        except (BaseException) as err:
            await utils.answer(message, self.strings["error"] + "```" + str(err) + "```")
