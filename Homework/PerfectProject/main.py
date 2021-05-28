from Erie.core.core import Core
from Erie.telegram_core.core import TelegramCore as TgCore

tg = TgCore(Core.GetTelegramToken())
tg.InitHandlers()