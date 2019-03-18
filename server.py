import chat_bot
bot=chat_bot.telegram_chatbot("797382536:AAE7xX2VuyfzuCQaQlXlc5-syjwcJF0qU54")

update_id=None

def make_reply(message):
    reply="okay"
    return reply
while True:
    print("...")
    updates=bot.get_updates(offset=update_id)
    updates=updates["result"]
    if updates:
        for item in updates:

            update_id=item["update_id"]
            try:
                message=item["message"]["text"]
            except:
                message=None
            from_=item["message"]["from"]["id"]

            reply=make_reply(message)

            bot.sendMessage(reply,from_)