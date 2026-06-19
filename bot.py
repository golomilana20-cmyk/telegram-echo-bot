import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ВНИМАНИЕ: Сюда пользователь, который скачает ваш код, вставит свой токен
TOKEN = "ВАШ_ТЕЛЕГРАМ_ТОКЕН_ЗДЕСЬ"

# Сюда можно вставить свой цифровой ID из @userinfobot, чтобы получать копии сообщений
MY_ID = 0  

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я твой первый Телеграм-бот.")

# Обработчик всех текстовых сообщений
@dp.message()
async def echo_message(message: types.Message):
    # Бот отвечает пользователю
    await message.answer(f"Вы написали: {message.text}")
    
    # Если указан ID администратора, бот тайно пересылает сообщение ему
    if MY_ID != 0:
        text_to_admin = f"⚠️ Новое сообщение!\nОт: {message.from_user.first_name} (@{message.from_user.username})\nТекст: {message.text}"
        try:
            await bot.send_message(chat_id=MY_ID, text=text_to_admin)
        except Exception as e:
            print(f"Не удалось переслать сообщение админу: {e}")

# Главная функция запуска
async def main():
    print("Бот успешно запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
