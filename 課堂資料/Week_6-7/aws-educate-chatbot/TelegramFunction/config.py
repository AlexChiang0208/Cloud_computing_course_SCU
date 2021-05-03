# Request Link and Long Polling Use
TELEGRAM_TOKEN = ''
WEBHOOK_URL = ''
TELEGRAM_BASE = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}'
TELEGRAM_WEBHOOK_URL = TELEGRAM_BASE + f'/setWebhook?url={WEBHOOK_URL}'
