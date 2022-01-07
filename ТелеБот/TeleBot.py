import telebot, wikipedia, re
from telebot import types

bot = telebot.TeleBot("5069454947:AAGuUPECHlPwd_hJzLjLVaJ5Ke1pelOc_UM")
wikipedia.set_lang("ru")


# Чистим текст статьи в Wikipedia и ограничиваем
def getwiki(s):
    try:
        ny = wikipedia.page(s)

        wikitext = ny.content[:3500]
        # Разделяем по точкам
        wikimas = wikitext.split('.')
        # Отбрасывает недописанную хрень
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not ('==' in x):
                # Делаем так, что бы в сторке было минимум 3 символа.
                if (len((x.strip())) >= 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception:
        return 'В энциклопедии нет информации об этом'
while True:
    try:

        # /help
        @bot.message_handler(commands=["help"])
        def help(message):
            bot.send_message(message.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')

        # Кнопки
        @bot.message_handler(content_types=["text"])
        def handle_text(message):
            markup1 = types.InlineKeyboardMarkup()
            search_results = wikipedia.search(message.text, results=2)
            mar1 = types.InlineKeyboardButton(text=search_results[0], callback_data='first')
            mar2 = types.InlineKeyboardButton(text=search_results[1], callback_data='second')
            markup1.add(mar1, mar2)
            bot.send_message(message.chat.id, 'Выберите:', reply_markup=markup1)


        # Поиск ссылки
        @bot.callback_query_handler(func=lambda call: True)
        def answer(call):
            if call.data == 'first':
                bot.send_message(call.message.chat.id, getwiki(call.message.json['reply_markup']['inline_keyboard'][0][0]['text']))
            if call.data == 'second':
                bot.send_message(call.message.chat.id, getwiki(call.message.json['reply_markup']['inline_keyboard'][0][1]['text']))

        bot.polling(none_stop=True, interval=0)
    except Exception:
        continue
    else:
        break
