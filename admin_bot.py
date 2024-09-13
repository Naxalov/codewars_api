import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import handlers

load_dotenv()
def main():
    TOKEN = os.getenv('TOKEN')

    # Application obyekti yaratish
    application = Application.builder().token(TOKEN).build()
    
    # Handlerlarni ro'yxatdan o'tkazish
    application.add_handler(CommandHandler("start", handlers.start))
    application.add_handler(CommandHandler("sendResults", handlers.results_type))
    application.add_handler(CallbackQueryHandler(handlers.send_results_to_image, pattern='type:'))

    # Botni ishga tushirish
    application.run_polling()

if __name__ == '__main__':
    main()
