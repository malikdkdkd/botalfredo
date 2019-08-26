
videos_array = ['https://www.instagram.com/p/B08ZD3yl2Yf/', 'https://www.instagram.com/p/BzVl6QwipDY/', 
              'https://www.instagram.com/p/B0ld5uKiIV1/', 'https://www.instagram.com/p/By-JtedFpuC/',
              'https://www.instagram.com/p/ByVLtZClKYi/', 'https://www.instagram.com/p/BwSBQiGCx5O/',
              'https://www.instagram.com/p/BwCEw_4oFDq/', 'https://www.instagram.com/p/BvmFXV7o_Mw/',
              'https://www.instagram.com/p/Bu840dPFOV4/', 'https://www.instagram.com/p/BueB23mlyZ_/',
              'https://www.instagram.com/p/BuOmHPLl75E/', 'https://www.instagram.com/p/BuBxrpHFAw5/',
              'https://www.instagram.com/p/BtlUrwlFTGD/', 'https://www.instagram.com/p/BtGjLxnFNL7/',
              'https://www.instagram.com/p/Bs5gd7PFzwZ/', 'https://www.instagram.com/p/Bsf8bSblUhk/',
              'https://www.instagram.com/p/BsDGyholnSR/', 'https://www.instagram.com/p/BrudsDXlw7c/',
              'https://www.instagram.com/p/Brfcc27lc1_/', 'https://www.instagram.com/p/BrDQxLJlkEM/',
              'https://www.instagram.com/p/BqpkcV2FegA/', 'https://www.instagram.com/p/BqM76N-FE_Q/',
              'https://www.instagram.com/p/BqFMh0lFM2q/', 'https://www.instagram.com/p/BpjjydQliQJ/',
              'https://www.instagram.com/p/BpKV0XlF9z5/', 'https://www.instagram.com/p/BpFHHExgjsW/',
              'https://www.instagram.com/p/Bo9USz2gpLd/', 'https://www.instagram.com/p/BooQ_sFA4pJ/',
              'https://www.instagram.com/p/BoHLUXEgEoy/', 'https://www.instagram.com/p/Bn_ZinUA3j8/',
              'https://www.instagram.com/p/Bn0yMTmApNf/', 'https://www.instagram.com/p/BnlVvi4AV2g/',
              'https://www.instagram.com/p/BnJtDwXAAln/', 'https://www.instagram.com/p/Bm_VoC2AIt_/',
              'https://www.instagram.com/p/BmbLCEkAcpB/', 'https://www.instagram.com/p/BmJDGXxjWr-/',
              'https://www.instagram.com/p/Bl27ilEnFud/', 'https://www.instagram.com/p/BllBo5egPKb/',
              'https://www.instagram.com/p/BlS89oxjAC-/', 'https://www.instagram.com/p/BlLmF8AlLpm/',
              'https://www.instagram.com/p/BlC6koBAXWa/', 'https://www.instagram.com/p/Bkz_lr7AlSO/',
              'https://www.instagram.com/p/BknNbibA4Hz/', 'https://www.instagram.com/p/BkfwwxuA9uC/',
              'https://www.instagram.com/p/BkSqvmcAC_L/', 'https://www.instagram.com/p/BkKycwKgMQd/',
              'https://www.instagram.com/p/BkDISfdgAGF/', 'https://www.instagram.com/p/Bj7VbECAEr9/',
              'https://www.instagram.com/p/BjzZzm9A279/', 'https://www.instagram.com/p/BjpbsbBAF_4/',
              'https://www.instagram.com/p/BjfEd7oAk6x/', 'https://www.instagram.com/p/BjZr2KRAFZW/',
              'https://www.instagram.com/p/BjPp1BQgzzJ/', 'https://www.instagram.com/p/BjH74c1ApVH/',
              'https://www.instagram.com/p/BjATzhqgxRA/', 'https://www.instagram.com/p/Bi4dhZfgutL/',
              'https://www.instagram.com/p/Bi1tPnJgFrC/', 'https://www.instagram.com/p/BizJvaMgWYQ/',
              'https://www.instagram.com/p/Biw16umAUU5/', 'https://www.instagram.com/p/B1YuFMplFCg6IuOtbXXAavimU1WtX3jIuLyOnM0/']

stri = """
if count == 1:
    def point_question(message):
        bot.send_message(message.chat.id, "Привет, за 1 правильный ответ ты будешь получать 10 баллов\n\nКакой фильм лучше?\n\n1 - 50 оттенков серого\n2 - Крестный отец\n\nОтвет нужно дать цифрой")
        bot.register_next_step_handler(message, ques_answer)

    def ques_answer(message):
        if message.text == "2":
            global points
            points += 10
            bot.send_message(message.chat.id, f"Верно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /point\nОстановить /exit")
        else:
            bot.send_message(message.chat.id, "Неправильно\nПопробуй ещё\n\nПродолжить /point\nОстановить /exit")

elif count == 2:

    def point_question_2(message):
        if message.text == "/exit":
            bot.send_message(message.chat.id, "Ты остановил игру")
            exit()
        else:
            bot.send_message(message.chat.id, "Какая медаль была вручена Гагарину за полёт в космос\n\n1 - Золотая звезда\n2 - Харизматичная звезда\n3 - За освоение целинных земель")
            bot.register_next_step_handler(message, ques_answer_2)

    def ques_answer_2(message):
        if message.text == "3":
            global points
            points += 10
            bot.send_message(message.chat.id, f"Правильно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /point\nОстановить /exit")
        else:
            bot.send_message(message.chat.id, "Неправильно :c\nПопробуй ещё\n\nПродолжить /point\nОстановить /exit")


elif count == 3:

    def point_question_3(message):
        if message.text == "/exit":
            bot.send_message(message.chat.id, "Ты остановил игру")
            exit()
        else:
            bot.send_message(message.chat.id, "Выбирай\n\n1 - Антипикап\n2 - Пикап")
            bot.register_next_step_handler(message, ques_answer_3)

    def ques_answer_3(message):
        if message.text == "1":
            global points
            points += 10
            bot.send_message(message.chat.id, f"Достойно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /point\nОстановить /exit")
        else:
            bot.send_message(message.chat.id, "Это не харизматично с твоей стороны :c\nПопробуй ещё\n\nПродолжить /point\nОстановить /exit")



elif count == 4:

    def point_question_4(message):
        if message.text == "/exit":
            bot.send_message(message.chat.id, "Ты остановил игру")
            exit()
        else:
            bot.send_message(message.chat.id, "Не откладывай на завтра то, что..\n\n1 - Можно сделать сегодня\n2 - Нельзя сделать")
            bot.register_next_step_handler(message, ques_answer_4)

    def ques_answer_4(message):
        if message.text == "1":
            global points
            points += 10
            bot.send_message(message.chat.id, f"Верно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /point\nОстановить /exit")
        else:
            bot.send_message(message.chat.id, "Это не харизматично с твоей стороны :c\nПопробуй ещё\n\nПродолжить /point\nОстановить /exit")


elif count == 5:

    def point_question_5(message):
        if message.text == "/exit":
            bot.send_message(message.chat.id, "Ты остановил игру")
            exit()
        else:
            bot.send_message(message.chat.id, "Веришь в призраков?\n\n1 - Да\n2 - Нет")
            bot.register_next_step_handler(message, ques_answer_6)

    def ques_answer_5(message):
        if message.text == "2":
            global points
            points += 10
            bot.send_message(message.chat.id, f"Разумно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /point\nОстановить /exit")
        else:
            bot.send_message(message.chat.id, "Это не разумно :c\nПопробуй ещё\n\nПродолжить /point\nОстановить /exit")


elif count == 6:

    def point_question_6(message):
        if message.text == "/exit":
            bot.send_message(message.chat.id, "Ты остановил игру")
            exit()
        else:
            bot.send_message(message.chat.id, "Для чего ставят хэштег?\n\n1 - Для понтов\n2 - Просто так\n3 - Для сообщений по теме")
            bot.register_next_step_handler(message, ques_answer_6)

    def ques_answer_6(message):
        if message.text == "3":
            global points
            points += 10
            bot.send_message(message.chat.id, f"Верно, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /point\nОстановить /exit")
        else:
            bot.send_message(message.chat.id, "Это неправильно :c\nПопробуй ещё\n\nПродолжить /point\nОстановить /exit")


elif count == 7:

    def point_question_7(message):
        if message.text == "/exit":
            bot.send_message(message.chat.id, "Ты остановил игру")
            exit()
        else:
            bot.send_message(message.chat.id, "Сколько лет Челентано?\n\n1 - Больше 80\n2 - Больше 60\n3 - Он умер")
            bot.register_next_step_handler(message, ques_answer_7)

    def ques_answer_7(message):
        if message.text == "2":
            global points
            points += 10
            bot.send_message(message.chat.id, f"Харизматично, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /point\nОстановить /exit")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /point\nОстановить /exit")


elif count == 8:

    def point_question_8(message):
        if message.text == "/exit":
            bot.send_message(message.chat.id, "Ты остановил игру")
            exit()
        else:
            bot.send_message(message.chat.id, "Если бы здесь проходил конкурс красоты, он бы..\n\n1 - Ушел\n2 - Пришел\n3 - Отошёл\n4 - Прошел мимо вас")
            bot.register_next_step_handler(message, ques_answer_8)

    def ques_answer_8(message):
        if message.text == "4":
            global points
            points += 10
            bot.send_message(message.chat.id, f"Харизматично, ты получаешь 10 очков!\nБаланс: {points} очков Харизмы\n\nПродолжить /point\nОстановить /exit")
        else:
            bot.send_message(message.chat.id, "Это неверно :c\nПопробуй ещё\n\nПродолжить /point\nОстановить /exit")

"""