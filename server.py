from chat_bot import telegram_chatbot
bot=telegram_chatbot()

update_id=None

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