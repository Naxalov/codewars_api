import os
from telegram import Update
from telegram.ext import  CallbackContext
from codewars import User, Users
import keyboards
import csv


GROUP_CHAT_ID =-1002169190245

async def start(update: Update, context: CallbackContext) -> None:
    first_name = update.message.chat.first_name
    chat_id = update.effective_chat.id
    
    await context.bot.send_message(chat_id=chat_id, text=f"Assalomu aleykum {first_name}. Siz bu bot orqali codewars saytidan ishlangan masallar sonini ko'rishingiz mumkin!!!")

async def results_type(update: Update, context: CallbackContext):
    await update.message.reply_text(text='Total Completed problem type?', reply_markup=keyboards.inline_keyboard)

async def send_results_to_image(update: Update, context: CallbackContext) -> None:
    type_completeat = update.callback_query.data.split(":")[1]
    group ='codewars'
    users_data = []
    with open(f'group/{group}.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users_data.append({
                'username': row['username'],
                'fullname': row['fullname']
            })
    users = Users(users_data)
    results_competeAt = users.get_total_date(date_type=type_completeat)
    result_image_path = 'total_completed_'+ str(type_completeat) + '.jpg'
    users.get_users_html_convert(results_competeAt, result_image_path, type_completeat)
    await context.bot.send_photo(chat_id=GROUP_CHAT_ID, photo=result_image_path, message_thread_id=5)
    