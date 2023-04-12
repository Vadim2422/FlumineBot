import random
from aiogram import Bot, Dispatcher, executor, types
from magic_filter import F
from config_data.config import load_config, Config
config: Config = load_config()
bot: Bot = Bot(config.tg_bot.token)
dp = Dispatcher(bot)
play: bool = False
num: int



def custom_filter(some_list: list) -> bool:
    sum = 0
    for i in some_list:
        if isinstance(i, int) and i % 7 == 0:
            sum += i
    if sum <= 83:
        return True
    return False


anonymous_filter = lambda str: str.count('я') + str.count('Я') >= 23


def on_start_up():
    print("Bot is up")


async def start(message: types.Message):
    global num, play
    if play:
        await message.answer("Игра уже идет")
        return
    num = random.randint(1, 100)
    play = True
    await message.answer("Отгадай число")


async def message(message: types.Message):
    global play, num
    print(num)
    if play:
        if int(message.text) == num:
            await message.answer("Угадал")
            play = False
        elif int(message.text) < num:
            await message.answer("Больше")
        else:
            await message.answer("Меньше")


dp.register_message_handler(start, commands=['start'])
dp.register_message_handler(message, F.cont)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_start_up(), skip_updates=True)
