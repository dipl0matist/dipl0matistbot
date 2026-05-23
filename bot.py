import telebot
import requests

TOKEN = "8340018362:AAH_gUix_7YsivBvSBPFXNEAJgKm8nLM7AU"
API_KEY = "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"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def ai(message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": message.text
            }
        ]
    }

    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    answer = r.json()['choices'][0]['message']['content']

    bot.reply_to(message, answer)

print("AI Bot ishladi")

bot.infinity_polling()