from random import randint
from time import sleep

from webbot import Browser

BASE_URL = "https://test-edu.ru/"

web = Browser()
web.go_to(BASE_URL)

input("Готово?")

web.click("начать тестирование")
web.click("+")
web.click("+")

web.click("мужской")

web.click("следующий вопрос")

for _ in range(77):
    n = randint(1, 4)
    web.click(tag="input", classname="answers__label", number=n)
    sleep(5)
    web.click("следующий вопрос")
