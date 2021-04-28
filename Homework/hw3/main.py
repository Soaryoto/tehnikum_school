# Soaryoto
import time
import core.base as Base
import core.image as Images
import core.localization as Localization

Base.FullScreen() # На весь экран
Base.CleareConsole() # Чистим консоль


Base.PrintTextWithImage("Привет", "img2")
Base.SetViewBlockForInput()
time.sleep(1)


Base.CleareConsole() # Чистим консоль

Base.PrintTextWithImage("Как дела?", "img1")
Base.SetViewBlockForInput()
time.sleep(1)


Base.CleareConsole() # Чистим консоль

Base.PrintTextWithImage("Как мне надоело программировать", "img3")
Base.SetViewBlockForInput()
time.sleep(1)



Base.CleareConsole() # Чистим консоль

Base.PrintTextWithImage("Люди очень скучные", "img4")
Base.GetInputUsersText()
time.sleep(1)