from TelegramFunction.config import TELEGRAM_WEBHOOK_URL
from TelegramFunction.features import Tool as tl
from processor import TelegramBot

tl.webhook_init(TELEGRAM_WEBHOOK_URL)
bot = TelegramBot()

def lambda_handler(event, context):
    print(event)
    bot.run_process(event)
    return bot.run_data()