import telebot
from telebot import types
import random
import const

token = "900094219:AAEmlUtyX-VLOLpsoY0CcmQhCu_EUmotXYA"
bot = telebot.TeleBot(token)


#----------------
# Команда /phrase
#----------------


@bot.message_handler(commands=['phrase'])

def phrase(message):
    
    bot.send_message(message.chat.id, "Угадай пропущенные слова:\n\nНа три вещи можно смотреть бесконечно - На огонь, на воду и на...\n\n1 - Меня\n2 - Воздух")
    bot.register_next_step_handler(message, answer_phrase)


def answer_phrase(message):

    if message.text == '1':
        bot.send_message(message.chat.id, "Молодец\nТебе +1 к Харизме\n\nПродолжить /phrase")
    else:
        bot.send_message(message.chat.id, "Неправильно\nТебе -1 к Харизме\n\nПравильный ответ: \"Меня\"\nПродолжить /phrase")

    bot.register_next_step_handler(message, phrase_2)
           

def phrase_2(message):

    bot.send_message(message.chat.id, "Угадай пропущенные слова:\n\nАльфредо - доктор...\n\n1 - Наук\n2 - Просто доктор\n3 - Философии\n4 - Харизматичных наук")
    bot.register_next_step_handler(message, answer_phrase_2)


def answer_phrase_2(message):

    if message.text == '4':
        bot.send_message(message.chat.id, "Молодец\nТебе ещё +1 к Харизме\n\nК сожалению у меня переизбыток фраз, можешь больше не писать эту команду :c")
    else:
        bot.send_message(message.chat.id, "Неправильно\nТебе -1 к Харизме\n\nПравильный ответ: \"4 - Харизматичных наук\"\n\nК сожалению у меня переизбыток фраз, можешь больше не писать эту команду :c")


#----------------
# Команда /video
#----------------


@bot.message_handler(commands = ['video'])

def videos(message):
    videos = const.videos_array
    rand = random.choice(videos)
    bot.send_message(message.chat.id, f"Держи видео\nНе забывай про like\n{rand}")


#----------------
# Команда /lastvideo
#----------------


@bot.message_handler(commands = ['lastvideo']) 

def last(message):
    last = 'https://www.instagram.com/p/B1YuFMplFCg6IuOtbXXAavimU1WtX3jIuLyOnM0/'
    bot.send_message(message.chat.id, "Держи самое свежее видео\nНе забудь про like\n" + last)


#----------------
# Команда /gif
#----------------


@bot.message_handler(commands = ['gif'])

def gif(message):
    file_id = ["CgADAgAD3AQAApO64UqPDF6p5hjyURYE",
               "CgADAgAD3gQAApO64Ups3tNPY3viNBYE",
               "CgADAgAD3wQAApO64UpJRZpYxQYsCRYE",
               "CgADAgADdwMAAjsB8Erihgo1HRNhrBYE",
               "CgADAgADVAQAAkeE6EqfPDqRhdrWJRYE",
               "CgADAgADVgQAAkeE6Epw_NNgyYkWVBYE"
              ]
               
    random_gif = random.choice(file_id)
    bot.send_document(message.chat.id, random_gif)


#----------------
# Команда /level
#----------------


@bot.message_handler(commands = ['level'])

def check(message):
    global c
    c = 0
    if c > 0:
        bot.send_message(message.chat.id, "Тебе здесь больше нечего делать\nТы познал свою харизму")
    else:
        bot.register_next_step_handler(message, level)

def level(message):
    bot.send_message(message.chat.id, "Отправь мне своё фото и я скажу насколько ты харизматичен\n\nВперёд 🔥")
    bot.register_next_step_handler(message, user_photo)

def user_photo(message):
    global c

    if isinstance(message.text, (str, int, float)):
        bot.send_message(message.chat.id, "Отправь свое фото\n\nПропиши /level ещё раз")
    else:
        c += 1
        random_integer = random.randint(1, 100)
        bot.send_message(message.chat.id, f"Ты харизматичен на {random_integer}% из 100\n\nРекорд: Alfredo Auditore - 101%")

        if random_integer >= 70:
            bot.send_message(message.chat.id, "Поздравляю, но до меня тебе далеко")
        else:
            bot.send_message(message.chat.id, "Твоему запасу харизмы не позавидуешь..")
        

    

#----------------
# Команда /choice
#----------------


chek = 0

@bot.message_handler(commands = ['choice'])

def check_choice(message):
    global chek
    if chek > 2:
        bot.send_message(message.chat.id, "Хватит тебе на сегодня")
    else:
        bot.register_next_step_handler(message, inline)

def inline(message):
    global chek
    global rand_choice
    rand_choice = random.randint(1, 12)

    if rand_choice == 1:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Челентано", callback_data="Челентано")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 2:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Ди Каприо", callback_data="Ди Каприо")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 3:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 4:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Железный Арни", callback_data="Железный Арни")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 5:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Железный человек", callback_data="Железный человек")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 6:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Супермен", callback_data="Супермен")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 7:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Стив Джобс", callback_data="Стив Джобс")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 8:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Билл Гейтс", callback_data="Билл Гейтс")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 9:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Бенедикт Камбербэтч", callback_data="Бенедикт Камбербэтч")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 10:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Илон Маск", callback_data="Илон Маск")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 11:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Владимир Путин", callback_data="Владимир Путин")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)

    elif rand_choice == 12:
        
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Альфредо", callback_data="Альфредо")
        but_2 = types.InlineKeyboardButton(text="Егор Крид", callback_data="Егор Крид")
        key.add(but_1, but_2)
        bot.send_message(message.chat.id, "Кто же твой кумир?", reply_markup=key)
    
        


@bot.callback_query_handler(func=lambda c:True)

def inlin(c):
    global chek
    global rand_choice

    if rand_choice == 1:
        
        if c.data == 'Альфредо':
            
            bot.send_message(c.message.chat.id, "На сегодня ты сделал правильный выбор\n\nПродолжить /choice")
        elif c.data == 'Челентано':
            bot.send_message(c.message.chat.id, "Не в этот раз..\n\nПродолжить /choice")
        chek += 1

    elif rand_choice == 2:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, "На сегодня ты сделал правильный выбор\n\nПродолжить /choice")
        elif c.data == 'Ди Каприо':
            bot.send_message(c.message.chat.id, "Альфредо блестит ярче, чем его оскар\n\nПродолжить /choice")
        chek += 1

    elif rand_choice == 3:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Извини, они не сравнимы...\n\nПродолжить /choice')
        elif c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Извини, они не сравнимы...\n\nПродолжить /choice')
        chek += 1

    elif rand_choice == 4:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Харизма побеждает железо\n\nПродолжить /choice')
        elif c.data == 'Железный Арни':
            bot.send_message(c.message.chat.id, 'Он хоть и железный, но не достаточно харизматичный\n\nПродолжить /choice')
        chek += 1

    elif rand_choice == 5:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Извини, они не сравнимы...\n\nПродолжить /choice')
        elif c.data == 'Железный человек':
            bot.send_message(c.message.chat.id, 'Извини, они не сравнимы...\n\nПродолжить /choice')
        chek += 1

    elif rand_choice == 6:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Наилучший выбор\nАльфредо и есть Супермен\n\nПродолжить /choice')
        elif c.data == 'Супермен':
            bot.send_message(c.message.chat.id, 'Супермен здесь только Альфредо\n\nПродолжить /choice')
        chek += 1

    elif rand_choice == 7:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Джобс создал iPhone, но не харизму\n\nПродолжить /choice')
        elif c.data == 'Стив Джобс':
            bot.send_message(c.message.chat.id, 'Создал iPhone, но не эталон харизмы\n\nПродолжить /choice')
        chek += 1
            
    elif rand_choice == 8:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Правильно\n\nПродолжить /choice')
        elif c.data == 'Билл Гейтс':
            bot.send_message(c.message.chat.id, 'Он конечно создал майкрософт, но не харизму\n\nПродолжить /choice')
        chek += 1

    elif rand_choice == 9:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Сомнений нет\n\nПродолжить /choice')
        elif c.data == 'Бенедикт Камбэрбэтч':
            bot.send_message(c.message.chat.id, 'Не в этот раз..\n\nПродолжить /choice')
        chek += 1

    elif rand_choice == 10:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Правильно, харизма Альфредо добралась до марса раньше Илона\n\nПродолжить /choice')
        elif c.data == 'Илон Маск':
            bot.send_message(c.message.chat.id, 'Харизма Альфредо добралась до марса раньше Илона\n\nПродолжить /choice')
        chek += 1

    elif rand_choice == 11:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Это опасный выбор, но всё же он правильный\n\nПродолжить /choice')
        elif c.data == 'Владимир Путин':
            bot.send_message(c.message.chat.id, 'Владимир Путин конечно молодец, но не Альфредо\n\nПродолжить /choice')
        chek += 1

    elif rand_choice == 12:
        
        if c.data == 'Альфредо':
            bot.send_message(c.message.chat.id, 'Без комментариев\n\nПродолжить /choice')
        elif c.data == 'Егор Крид':
            bot.send_message(c.message.chat.id, 'Без комментариев\n\nПродолжить /choice')
        chek += 1
  


    
#----------------
# Команда /rang
#----------------


points = 0
rang = 'Отброс 🧔'


@bot.message_handler(commands = ['rang'])

def rangs(message):
    
    global points
    global rang

    if points >= 30 and points < 100:
        rang = "Начинающий 🔰"
        bot.send_message(message.chat.id, "Поздравляю, ты достиг уровня Начинающий 🔰")
    elif points >= 100 and points < 150:
        rang = "Детектив Харизма 🕵"
        bot.send_message(message.chat.id, "Поздравляю, ты достиг уровня: Детектив Харизма 🕵")
    elif points >= 150 and points < 200:
        rang = "Сын маминой подруги 😎"
        bot.send_message(message.chat.id, "Поздравляю, ты удостоен уровня: Сын маминой подруги 😎")
    elif points >= 200 and points < 300:
        rang = "Лидер Харизматичной мафии 🧛‍"
        bot.send_message(message.chat.id, "Поздравляю, ты достиг уровня: Лидер Харизматичной Мафии 🧛‍")
    elif points >= 300:
        rang = "Властелин харизмы 🧙‍"
        bot.send_message(message.chat.id, "Поздравляю, ты удостоен последнего ранга: Властелина Харизмы 🧙‍\n\nКто же ты черт побери такой..")
    else:
        rang == "Да кто же ты такой черт побери.."

    bot.send_message(message.chat.id, f"""Ранги:
    
1 - Отброс 🧔 [0 баллов]
2 - Начинающий 🔰 [30 баллов]
3 - Детектив Харизма 🕵 [100 баллов]
4 - Сын маминой подруги 😎 [150 баллов]
5 - Лидер Харизматичной мафии 🧛‍ [200 баллов]
6 - Властелин Харизмы 🧙‍ [300 баллов]

Твой ранг: {rang}
Баллов: {points}

Чтобы зарабатывать баллы используй команду /points""")


#----------------
# Команда /start
#----------------


@bot.message_handler(commands = ['start', 'help'])

def keyboard_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Список команд')
    user_markup.row('Баллы харизмы' , 'Ранг')
    bot.send_message(message.chat.id, 'Источник харизмы активирован🔥', reply_markup = user_markup)
    bot.register_next_step_handler(message, answer_start)
    
def answer_start(message):
    global points
    global rang
    if message.text == 'Список команд':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, """Тебя приветствует самый харизматичный бот на планете\n\nСписок доступных команд:\n
/sticker  -  Получить стикеры с Альфредо
/points  -  Зарабатывай баллы Харизмы
/rang  -  Просмотреть Ранг
/level  -  Узнай уровень харизмы
/video  -  Рандомное видео
/gif  -  Харизматичная гифка
/choice  -  Выбери 1 из 2
/phrase  -  Угадай фразу дня
/lastvideo  -  Последнее видео
/help  -  Получить помощь

Идеи по улучшению кидать сюда 👇
                                                         @darklight2456

Общайся со мной и прокачивай харизму 💪""", reply_markup = hide_markup)
        
    elif message.text == 'Баллы харизмы':
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, f"Баланс очков: {points}", reply_markup = hide_markup)
    elif message.text == "Ранг":
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, f"""Ранги:
    
1 - Отброс 🧔 [0 баллов]
2 - Начинающий 🔰 [30 баллов]
3 - Детектив Харизма 🕵 [100 баллов]
4 - Сын маминой подруги 😎 [150 баллов]
5 - Лидер Харизматичной мафии 🧛‍ [200 баллов]
6 - Властелин Харизмы 🧙‍ [300 баллов]

Твой ранг: {rang}
Баллов: {points}

Чтобы зарабатывать баллы используй команду /points""", reply_markup = hide_markup)


#-----------------
# Команда /points
#-----------------


@bot.message_handler(commands = ['points'])

def questions(message):

    global rang
    if rang == "Властелин харизмы 🧙‍":
        bot.send_message(message.chat.id, "Ты уже слишком харизматичный, большего твоё тело не выдержит..")
        bot.register_next_step_handler(message, keyboard_start)

    global count
    count = random.randint(1, 40)

    if count == 1:
        bot.send_message(message.chat.id, "Какой навык круче?\n\n1 - Харизма\n2 - Красота\n\n")
      
    elif count == 2:
        bot.send_message(message.chat.id, "Не откладывай на завтра то, что..\n\n1 - Можно сделать сегодня\n2 - Нельзя сделать")

    elif count == 3:
        bot.send_message(message.chat.id, "Выбирай\n\n1 - Антипикап\n2 - Пикап")

    elif count == 4:
        bot.send_message(message.chat.id, "Какая медаль была вручена Гагарину за полёт в космос\n\n1 - Золотая звезда\n2 - Харизматичная звезда\n3 - За освоение целинных земель")
    
    elif count == 5:
        bot.send_message(message.chat.id, "Веришь в призраков?\n\n1 - Да\n2 - Нет")

    elif count == 6:
        bot.send_message(message.chat.id, "Сколько лет Челентано?\n\n1 - Больше 80\n2 - Больше 60\n3 - Он умер")

    elif count == 7:
        bot.send_message(message.chat.id, "Если бы здесь проходил конкурс красоты, он бы..\n\n1 - Ушел\n2 - Пришел\n3 - Отошёл\n4 - Прошел мимо вас")
 
    elif count == 8:
        bot.send_message(message.chat.id, "Существует ли харизма в космосе?\n\n1 - Конечно\n2 - Нет")

    elif count == 9:
        bot.send_message(message.chat.id, "Что быстрее?\n\n1 - Скорость звука\n2 - Скорость света")

    elif count == 10:
        bot.send_message(message.chat.id, "Что изобрёл Альфред Нобель?\n\n1 - Телефон\n2 - Динамит\n3 - Харизму\n4 - Телефон")

    elif count == 11:
        bot.send_message(message.chat.id, "Кто изобрел интернет?\n\n1 - Тим Бернерс Ли\n2 - Джордж Мини\n3 - Чарльз Бэббидж")

    elif count == 12:
        bot.send_message(message.chat.id, "Ходят слухи, что Альфредо родился с максимальным уровнем харизмы по данным S.P.E.C.I.A.L.\nЭто правда?\n\n1 - Сомнений нет\n2 - Нет")

    elif count == 13:
        bot.send_message(message.chat.id, "Сколько патрон заряжается в магазин АК-47?\n\n1 - 40\n2 - 27\n3 - 30")

    elif count == 14:
        bot.send_message(message.chat.id, "Из какой стали делают лучшие ножи?\n\n1 - Из дамасской\n2 - Из нержавеющей")

    elif count == 15:
        bot.send_message(message.chat.id, "Фраза Цезаря:\n\n1 - Невелик тот, кто невелик, а велик тот, кто велик\n2 - И ты брут\n3 - Элементарно")

    elif count == 16:
        bot.send_message(message.chat.id, "Какой воздух тяжелее?\n\n1 - Горячий\n2 - Холодный")

    elif count == 17:
        bot.send_message(message.chat.id, "Чем прославился Ленин?\n\n1 - Убил цезаря\n2 - Был императором\n3 - Организовал революцию против императора России")

    elif count == 18:
        bot.send_message(message.chat.id, "Столица Бразилии\n\n1 - Сингапур\n2 - Рио-де-Жанейро\n3 - Бразиллиа")

    elif count == 19:
        bot.send_message(message.chat.id, "Как называли Викингов в Древней Руси\n\n1 - Викинги\n2 - Варяги\n3 - Коррупционеры\n4 - Разбойники")

    elif count == 20:
        bot.send_message(message.chat.id, "Сколько Актёров играли Человека-паука?\n\n1 - Четыре\n2 - Один\n3 - Два\n4 - Три")

    elif count == 21:
        bot.send_message(message.chat.id, "В честь кого назвали 1 из Черепашек-ниндзя - Леонардо\n\n1 - Леонардо да Винчи\n2 - Леопард Лео\n3 - Леонардо ди Каприо")

    elif count == 22:
        bot.send_message(message.chat.id, "Кто первым изобрел лампочку?\n\n1 - Никола Тесла\n2 - Томас Эдисон\n3 - Ломоносов")

    elif count == 23:
        bot.send_message(message.chat.id, "Страна с самым большим уровнем населения?\n\n1 - Россия\n2 - США\n3 - Китай")

    elif count == 24:
        bot.send_message(message.chat.id, "Кто основал Microsoft?\n\n1 - Билл Гейтс\n2 - Стив Джобс\n3 - Марк Цукерберг")

    elif count == 25:
        bot.send_message(message.chat.id, "Первая в мире Социальная Сеть?\n\n1 - Instagram\n2 - VK\n3 - Facebook")

    elif count == 26:
        bot.send_message(message.chat.id, "Самое популярное слово в мире?\n\n1 - Привет\n2 - OK")

    elif count == 27:
        bot.send_message(message.chat.id, "Где в реках нет воды?\n\n1 - В Африке\n2 - На карте")

    elif count == 28:
        bot.send_message(message.chat.id, "Самая богатая компания в мире?\n\n1 - Google\n2 - Apple\n3 - Samsung\n4 - Amazon")

    elif count == 29:
        bot.send_message(message.chat.id, "Сколько океанов на планете?\n\n1 - Пять\n2 - Четыре\n3 - Три")

    elif count == 30:
        bot.send_message(message.chat.id, "В чём измеряется сила?\n\n1 - Ньютоны\n2 - Вольт\n3 - Ватт")

    elif count == 31:
        bot.send_message(message.chat.id, "Сколько хромосом в геноме нормального человека?\n\n1 - 46\n2 - 42\n3 - 44")

    elif count == 32:
        bot.send_message(message.chat.id, "Столица Италии?\n\n1 - Рим\n2 - Барселона\n3 - Лиссабон")

    elif count == 33:
        bot.send_message(message.chat.id, "Сколько планет в солнечной системе?\n\n1 - 6\n2 - 7\n 3 - 8")

    elif count == 34:
        bot.send_message(message.chat.id, "Самое опасное животное в мире?\n\n1 - Москит\n2 - Черная мамба\n3 - Белая акула")

    elif count == 35:
        bot.send_message(message.chat.id, "Сколько лет живет кот?\n\n1 - 9-10 лет\n2 - 11-13 лет\n3 - 12-15 лет")

    elif count == 36:
        bot.send_message(message.chat.id, "Какое лекарство изобрели случайно?\n\n1 - Анальгин\n2 - Пенициллин\n3 - Гидроперит")

    elif count == 37:
        bot.send_message(message.chat.id, "Какая страна подарила США статую свободы?\n\n1 - Германия\n2 - Аргентина\n3 - Англия\n4 - Франция")

    elif count == 38:
        bot.send_message(message.chat.id, "Что Дарт Вейдер сказал Люку Скайокеру?\n\n1 - Люк, я твой отец\n2 - Люк, я твой брат\n3 - Люк, я твоя мама\n4 - Люк, я твой люк")

    elif count == 39:
        bot.send_message(message.chat.id, "Сколько животных было в ковчеге Моисея?\n\n1 - 3000\n2 - Ковчег был у Ноя\n3 - 2500")

    elif count == 40:
        bot.send_message(message.chat.id, "В какой стране первыми появились пластиковые деньги?\n\n1 - Россия\n2 - США\n3 - Австралия\n4 - Канада")

    
    bot.register_next_step_handler(message, answers)


def answers(message):

    global count
    global points

    if count == 1:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Верно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это не харизматично с твоей стороны :c\nПопробуй ещё\n\nПродолжить /points")
            

    elif count == 2:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Верно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")       
        else:
            bot.send_message(message.chat.id, "Это не харизматично с твоей стороны :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 3:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Достойно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, f"Это не харизматично с твоей стороны :c\n\nПродолжить /points")


    elif count == 4:
        if message.text == "3":
            points += 10
            bot.send_message(message.chat.id, f"Правильно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Неправильно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 5:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Разумно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это не разумно :c\nПопробуй ещё\n\nПродолжить /points")

    
    elif count == 6:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Верно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 7:
        if message.text == "4":
            points += 10
            bot.send_message(message.chat.id, f"Харизматично, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 8:
        if message.text == "4":
            points += 10
            bot.send_message(message.chat.id, f"Харизма Альфредо уже давно живет на марсе и в космосе\nТы получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 9:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Молодец, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")

    
    elif count == 10:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Харизматично, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        elif message.text == "3":
            bot.send_message(message.chat.id, "Нобель не создавал Альфредо..\nЭто неверно, попробуй ещё\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно\nПопробуй ещё\n\nПродолжить /points")


    elif count == 11:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Правильно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно\nПопробуй ещё\n\nПродолжить /points")


    elif count == 12:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Сомнений быть не должно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это была правда..\nПопробуй ещё\n\nПродолжить /points")


    elif count == 13:
        if message.text == "3":
            points += 10
            bot.send_message(message.chat.id, f"В точку, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Неправильно\nПопробуй ещё\n\nПродолжить /points")


    elif count == 14:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Правильно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неправильно\nПопробуй ещё\n\nПродолжить /points")

    
    elif count == 15:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Харизматично, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Нет, брут!\nПопробуй ещё\n\nПродолжить /points")

        
    elif count == 16:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Правильно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно\nПопробуй ещё\n\nПродолжить /points")


    elif count == 17:
        if message.text == "3":
            points += 10
            bot.send_message(message.chat.id, f"Это правда, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно, он организовал революцию\nПопробуй ещё\n\nПродолжить /points")


    elif count == 18:
        if message.text == "3":
            points += 10
            bot.send_message(message.chat.id, f"Alright, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")

    
    elif count == 19:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Правильно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Правильный ответ \"Варяги\"\nПопробуй ещё\n\nПродолжить /points")

    
    elif count == 20:
        if message.text == "4":
            points += 10
            bot.send_message(message.chat.id, f"Верно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно, всего 3\nПопробуй ещё\n\nПродолжить /points")


    elif count == 21:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Правильно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно\nПопробуй ещё\n\nПродолжить /points")


    elif count == 22:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Лампу сделал Эдисон, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Её изобрел Эдисон\nПопробуй ещё\n\nПродолжить /points")


    elif count == 23:
        if message.text == "3":
            points += 10
            bot.send_message(message.chat.id, f"Харизматично, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 24:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Харизматично, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 25:
        if message.text == "3":
            points += 10
            bot.send_message(message.chat.id, f"Харизматично, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 26:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Ок, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это ОК\nПопробуй ещё\n\nПродолжить /points")


    elif count == 27:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Логично, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Ты серьёзно?\nПопробуй ещё\n\nПродолжить /points")


    elif count == 28:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Это так, (1 трлн.$ ), ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это Apple (1 трлн.$)\nПопробуй ещё\n\nПродолжить /points")


    elif count == 29:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Правильно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Их всего четыре\nПопробуй ещё\n\nПродолжить /points")


    elif count == 30:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Правильный ответ, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Она измеряется в ньютонах, где ты был на уроках физики?\nПопробуй ещё\n\nПродолжить /points")


    elif count == 31:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Верно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно, их 46 (23 пары)\nПопробуй ещё\n\nПродолжить /points")


    elif count == 32:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"И это верный ответ, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 33:
        if message.text == "3":
            points += 10
            bot.send_message(message.chat.id, f"Молодец, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 34:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Ну естесственно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 35:
        if message.text == "3":
            points += 10
            bot.send_message(message.chat.id, f"Правильно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это не так\nПопробуй ещё\n\nПродолжить /points")


    elif count == 36:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Садись, 5 по химии, еще ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 37:
        if message.text == "4":
            points += 10
            bot.send_message(message.chat.id, f"Отлично, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неправильно\nПопробуй ещё\n\nПродолжить /points")


    elif count == 38:
        if message.text == "1":
            points += 10
            bot.send_message(message.chat.id, f"Белиссимо, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 39:
        if message.text == "2":
            points += 10
            bot.send_message(message.chat.id, f"Верно, ковчег был у Ноя, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")


    elif count == 40:
        if message.text == "3":
            points += 10
            bot.send_message(message.chat.id, f"Молодец, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /points")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /points")




#----------------
# Команда /sticker
#----------------


@bot.message_handler(commands = ['sticker'])

def sticker(message):
    bot.send_message(message.chat.id, "Ещё не готово)")


#----------------
# Обработчик текста
#----------------


@bot.message_handler(content_types = ['text'])

def message_handler(message):
    bot.send_message(message.chat.id, "Я принимаю только команды\n\nСписок команд ты можешь узнать командой\n/help")
    




bot.polling(none_stop=True, interval=0)