import telebot
from telebot import types

from telebot.types import KeyboardButton

bot = telebot.TeleBot('6432345446:AAFJmbKnA2MXpdkyvnuZuq_8aZjUwWx2_Ck')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("☎️ ️Наши контакты")
    btn2 = types.KeyboardButton("❓  Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text='Шалом, {0.first_name}!\nЯ чат-бот ИКЦ "Натив" Москва. \nОтвечу на часто задаваемые вопросы о Центре изучения иврита ✅ '.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "☎️ ️Наши контакты":
        bot.send_message(message.chat.id, text="Сайт: \nhttp://il4u.org.il/"
                                               '\n\nE-mail: \nmoscow@il4u.org.il'
                                               '\n\nТелефон: \n+7(495)645-00-75'
                                               '\n\nTelegram: \nt.me/iccmoscow'
                                               '\n\nАдрес: \n<a href="https://yandex.ru/maps/-/CCUo5LedgD">Москва, Стремянный переулок, 38, БЦ "Плеханов Плаза", 4 этаж</a>', parse_mode="html", disable_web_page_preview=True)
    elif message.text == "❓  Задать вопрос":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1️⃣ Что представляют из себя курсы иврита?")
        markup.row(btn1)
        btn2 = types.KeyboardButton("2️⃣ Как записаться на курсы?")
        markup.row(btn2)
        btn3 = types.KeyboardButton("3️⃣ Сколько времени проходит с момента подачи заявки до получения письма с приглашением в группу?")
        markup.row(btn3)
        back = types.KeyboardButton("Вернуться в главное меню")
        next_q = types.KeyboardButton("➡️")
        markup.add(back, next_q)
        bot.send_message(message.chat.id, text="Список популярных вопросов", reply_markup=markup)


    elif message.text == "1️⃣ Что представляют из себя курсы иврита?":
        bot.send_message(message.chat.id, text="В Центре изучения иврита «Натив» представлены три уровня обучения. Каждый уровень рассчитан на 70 академических часов. "
                                               "В зависимости от интенсивности группы курс включает в себя 18 или 24 занятия (2 и 3 месяца соответственно). Занятия бесплатные, проходят в формате онлайн."
                                               "\n <i>*Академический час - 45 минут</i>", parse_mode='html')
    elif message.text == "2️⃣ Как записаться на курсы?":
        bot.send_message(message.chat.id, text='В связи с большим вниманием к курсам иврита, для записи в группы мы работаем с заявками через лист ожидания.'
                                               '\nДля получения актуальной информации о наборе в группы по изучению иврита запишитесь в лист ожидания и укажите удобное для вас время занятий и уровень обучения. '
                                               '\nТем, кто регистрируется в листе ожидания, мы в приоритетном порядке отправляем информацию об открытии новых групп.'
                                               '\n\n Ссылка на лист ожидания 1 уровня:\n <a href="https://icc-moscow.timepad.ru/event/2803474/">Записаться</a>'
                                               '\n Ссылка на 2 и 3 уровни:\n <a href="https://icc-moscow.timepad.ru/event/2562457/">Записаться</a>', parse_mode="html", disable_web_page_preview=True)
    elif message.text == "3️⃣ Сколько времени проходит с момента подачи заявки до получения письма с приглашением в группу?":
        bot.send_message(message.chat.id, text="Для утренних групп ожидание составляет около 1-2 месяцев, для вечерних групп – 3-6 месяцев.",)
    elif message.text == "4️⃣ Как я узнаю, что до меня дошла очередь?":
        bot.send_message(message.chat.id, text="Вам придет письмо с приглашением записаться в одну из ближайших открывающихся групп. Рекомендуем также проверять папку “Спам”.",)
    elif message.text == "5️⃣ Какие учебные пособия используются, нужно ли их покупать или скачивать?":
        bot.send_message(message.chat.id, text="Занятия ведутся по авторским материалам преподавателей Центра, предоставляемых их в электронном виде.",)
    elif message.text == "6️⃣ В какое время проходят занятия?":
        bot.send_message(message.chat.id, text="Утром, днем и вечером. Каждое занятие - 3 или 4 академических часа.",)
    elif message.text == "7️⃣ Бывают ли группы выходного дня?":
        bot.send_message(message.chat.id, text="Да, у нас бывают группы по воскресеньям, но крайне редко. Бóльшая часть занятий проходит в будние дни.",)
    elif message.text == "8️⃣ Какой уровень иврита будет у меня по окончании курса?":
        bot.send_message(message.chat.id, text="В Израиле уровень «Алеф»* рассчитан на 500 часов. При прохождении 3-х ступеней в нашем Центре, вы овладеете частью уровня «Алеф»."
                                                '\n *<i><b>«Алеф»</b> — начальный уровень обучения в Израиле</i>', parse_mode="html")
    elif message.text == "9️⃣ Заранее хотел(а) зарегистрироваться на следующий уровень,но платформа Timepad отказывает (такой пользователь существует).":
        bot.send_message(message.chat.id, text='Для записи на 2 и 3 уровени у нас существует отдельный лист ожидания:'
                                               '\n\n<a href="https://icc-moscow.timepad.ru/event/2562457/">Записаться</a>'
                                               '\n\nЕсли все же не удается зарегистрироваться, попробуйте сделать это с другой электронной почты.', parse_mode="html", disable_web_page_preview=True)
    elif message.text == "🔟 Как происходит переход на следующий уровень?":
        bot.send_message(message.chat.id, text='Ученики получают приглашение на следующий уровень с ссылкой на регистрацию. При заполнении анкеты, обязательно укажите номер группы, которую закончили.'
                                                '\n Новым участникам мы предлагаем пройти тест, чтобы определить уровень подготовки, и уже после выбрать комфортный курс обучения.')
    elif message.text == "1️⃣1️⃣ Могу ли я пойти на 2 (3) уровень к другому преподавателю?":
        bot.send_message(message.chat.id, text='Да, если у преподавателя откроется соответствующая группа.')
    elif message.text == "1️⃣2️⃣ Как я узнаю, одобрена ли моя заявка?":
        bot.send_message(message.chat.id, text='В случае одобрения заявки всем участникам приходит подтверждение от платформы TimePad. Заявки одобряются в течение 7 рабочих дней.')
    elif message.text == "1️⃣3️⃣ А что вы мне можете предложить, пока я жду начала обучения?":
        bot.send_message(message.chat.id, text='В Израильском культурном центре «Натив» есть сообщество студентов и выпускников ульпана. Вы можете получить приглашение в него, заполнив форму:'
                                               '\n\n<a href="https://docs.google.com/forms/d/e/1FAIpQLSf_xyl4AmH-9B3fAWEHTtSEclJJwT9RUFwkHrvtHagBehtAYQ/viewform">Заполнить форму приглашения</a>'
                                               '\n\nТакже, Центр проводит мероприятия и вебинары на различные темы, способствующие сближению и знакомству с культурой и традициями Израиля. Подробнее вы можете узнать на нашем сайте: \n\nhttps://iccmoscow.tilda.ws/', parse_mode="html", disable_web_page_preview=True)
    elif message.text == "1️⃣4️⃣ Остались вопросы?":
        bot.send_message(message.chat.id, text='Мы всегда на связи.'
                                               '\nВы можете обратиться к нам по номеру телефона:\n+7(495)645-00-75 \nили по email:\nmoscow@il4u.org.il')
    elif message.text == '➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("4️⃣ Как я узнаю, что до меня дошла очередь?")
        markup.row(btn4)
        btn5 = types.KeyboardButton("5️⃣ Какие учебные пособия используются, нужно ли их покупать или скачивать?")
        markup.row(btn5)
        btn6 = types.KeyboardButton("6️⃣ В какое время проходят занятия?")
        markup.row(btn6)
        bot.delete_message(message.chat.id, message.id)
        next_w = types.KeyboardButton("➡️➡️")
        back = types.KeyboardButton("⬅️⬅️")
        markup.add(back, next_w)
        bot.send_message(message.chat.id, text="Выбери из списка вопрос", reply_markup=markup)

    elif message.text == '➡️➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn7 = types.KeyboardButton("7️⃣ Бывают ли группы выходного дня?")
        markup.row(btn7)
        btn8 = types.KeyboardButton("8️⃣ Какой уровень иврита будет у меня по окончании курса?")
        markup.row(btn8)
        btn9 = types.KeyboardButton("9️⃣ Заранее хотел(а) зарегистрироваться на следующий уровень,но платформа Timepad отказывает (такой пользователь существует).")
        markup.row(btn9)
        bot.delete_message(message.chat.id, message.id)
        next_q = types.KeyboardButton("➡️➡️➡️")
        prev = types.KeyboardButton("⬅️⬅️⬅️")
        markup.add(prev, next_q)
        bot.send_message(message.chat.id, text="Выбери из списка вопрос", reply_markup=markup)

    elif message.text == '➡️➡️➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn10 = types.KeyboardButton("🔟 Как происходит переход на следующий уровень?")
        markup.row(btn10)
        btn11 = types.KeyboardButton("1️⃣1️⃣ Могу ли я пойти на 2 (3) уровень к другому преподавателю?")
        markup.row(btn11)
        btn12 = types.KeyboardButton("1️⃣2️⃣ Как я узнаю, одобрена ли моя заявка?")
        markup.row(btn12)
        bot.delete_message(message.chat.id, message.id)
        next_q = types.KeyboardButton("➡️➡️➡️➡️")
        prev = types.KeyboardButton("⬅️⬅️⬅️⬅️")
        markup.add(prev, next_q)
        bot.send_message(message.chat.id, text="Выбери из списка вопрос", reply_markup=markup)

    elif message.text == '⬅️⬅️⬅️⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn7 = types.KeyboardButton("7️⃣ Бывают ли группы выходного дня?")
        markup.row(btn7)
        btn8 = types.KeyboardButton("8️⃣ Какой уровень иврита будет у меня по окончании курса?")
        markup.row(btn8)
        btn9 = types.KeyboardButton("9️⃣ Заранее хотел(а) зарегистрироваться на следующий уровень,но платформа Timepad отказывает (такой пользователь существует).")
        markup.row(btn9)
        bot.delete_message(message.chat.id, message.id)
        next_q = types.KeyboardButton("➡️➡️➡️")
        prev = types.KeyboardButton("⬅️⬅️⬅️")
        markup.add(prev, next_q)
        bot.send_message(message.chat.id, text="Выбери из списка вопрос", reply_markup=markup)

    elif message.text == '➡️➡️➡️➡️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn13 = types.KeyboardButton("1️⃣3️⃣ А что вы мне можете предложить, пока я жду начала обучения?")
        markup.row(btn13)
        btn14 = types.KeyboardButton("1️⃣4️⃣ Остались вопросы?")
        markup.row(btn14)
        bot.delete_message(message.chat.id, message.id)
        prev = types.KeyboardButton("Вернуться в главное меню")
        markup.add(prev)
        bot.send_message(message.chat.id, text="Выбери из списка вопрос", reply_markup=markup)

    elif message.text == '⬅️⬅️⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("4️⃣ Как я узнаю, что до меня дошла очередь?")
        markup.row(btn4)
        btn5 = types.KeyboardButton("5️⃣ Какие учебные пособия используются, нужно ли их покупать или скачивать?")
        markup.row(btn5)
        btn6 = types.KeyboardButton("6️⃣ В какое время проходят занятия?")
        markup.row(btn6)
        bot.delete_message(message.chat.id, message.id)
        next_w = types.KeyboardButton("➡️➡️")
        back = types.KeyboardButton("⬅️⬅️")
        markup.add(back, next_w)
        bot.send_message(message.chat.id, text="Выбери из списка вопрос", reply_markup=markup)

    elif message.text == "⬅️⬅️":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1️⃣ Что представляют из себя курсы иврита?")
        markup.row(btn1)
        btn2 = types.KeyboardButton("2️⃣ Как записаться на курсы?")
        markup.row(btn2)
        btn3 = types.KeyboardButton("3️⃣ Сколько времени проходит с момента подачи заявки до получения письма с приглашением в группу?")
        markup.row(btn3)
        bot.delete_message(message.chat.id, message.id)
        next_q = types.KeyboardButton("➡️")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back, next_q)
        bot.send_message(message.chat.id, text="Список популярных вопросов", reply_markup=markup)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("☎️ ️Наши контакты")
        button2 = types.KeyboardButton("❓  Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="И снова шалом!", reply_markup=markup)

bot.polling(none_stop=True)
