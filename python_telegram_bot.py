from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater, Filters, MessageHandler, CallbackContext
import os
TOKEN = os.environ['token']
import database

def like(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    count = database.Count(chat_id)
    txt = update.message.text
    bot = context.bot
    like = InlineKeyboardButton(f'👍 {count.like}', callback_data='👍')
    dislike = InlineKeyboardButton(f'👎 {count.dislike}', callback_data='👎')
    reply = InlineKeyboardMarkup([[like, dislike]])
    update.message.reply_text('text', reply_markup=reply)
    
def get_queary(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.from_user.id
    count = database.Count(chat_id)
    count.add(query.data)
    bot = context.bot
    print(count.like, count.dislike)
    like = InlineKeyboardButton(f'👍 {count.like}', callback_data='👍')
    dislike = InlineKeyboardButton(f'👎 {count.dislike}', callback_data='👎')
    reply = InlineKeyboardMarkup([[like, dislike]])
    query.edit_message_text('text', reply_markup=reply)
    
updater= Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', like))
updater.dispatcher.add_handler(CallbackQueryHandler(get_queary))

updater.start_polling()
updater.idle()