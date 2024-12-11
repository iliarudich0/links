
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')  # Insert your Telegram bot token here
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Create the main menu
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
button_books = KeyboardButton('📚 Список книг')
main_menu.add(button_books)

# Dictionary to store book links
books = {
    "Книга 1": "https://drive.google.com/file/d/your_link_1/view?usp=sharing",
    "Книга 2": "https://drive.google.com/file/d/your_link_2/view?usp=sharing",
    "Книга 3": "https://drive.google.com/file/d/your_link_3/view?usp=sharing",
    # Add more books here as needed
}

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Send a welcome message and show the main menu."""
    await message.reply(
        "Привет! Я бот, который поможет тебе получить доступ к книгам. "
        "Нажми на кнопку списка книг, чтобы просмотреть доступные файлы.", 
        reply_markup=main_menu
    )

@dp.message_handler(lambda message: message.text == '📚 Список книг')
async def send_book_list(message: types.Message):
    """Send the list of available books as clickable links."""
    response = "Доступные книги:\n\n"
    for book_name, book_link in books.items():
        response += f"<a href=\"{book_link}\">{book_name}</a>\n"
    await message.reply(response, parse_mode="HTML")

@dp.message_handler()
async def handle_unknown_message(message: types.Message):
    """Handle unknown messages."""
    await message.reply(
        "Пожалуйста, выберите один из доступных вариантов меню.", 
        reply_markup=main_menu
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
