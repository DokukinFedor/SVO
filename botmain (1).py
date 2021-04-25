import telebot
from telebot import types
import sys
sys.setrecursionlimit(10000)
bot = telebot.TeleBot('1758569238:AAFdWy30HMAbS2Ml5sp6yJ2OQZfnLSzsvHg')
@bot.message_handler(content_types='text')
def anquet(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Да", callback_data="NumberOne")
    but_2 = types.InlineKeyboardButton(text="Нет", callback_data="NumberTwo")
    key.add(but_1, but_2)
    bot.send_message(message.chat.id, 'Добрый день, вы спешите?', reply_markup=key)
@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    global vremmass
    global ans
    global sigma
    if c.data == 'NumberOne':
        bot.send_message(c.message.chat.id, 'Понятно, видмо вам надо подсказать дорогу? Тогда можете пройти на сайт нашего навигатора')
    if c.data == 'NumberTwo':
        bot.send_message(c.message.chat.id, 'Я бы хотел чтобы вы прошли пару тестов. Отвечайте на них + или -. Это сделать ваше времяпровождение максимально полезным')
        msg = bot.send_message(c.message.chat.id, 'хотите ли вы перекусить?')
        ans = []
        l = open('db.txt', 'r', encoding='utf-8')
        vremmass = l.readlines()
        f = 0
        sigma = []
        for i in range(len(vremmass)):
            f += 1
            vremmass[i] = vremmass[i].split('@@@')
            vremmass[i][1] = (''.join((list(vremmass[i][1]))[0:len(vremmass[i][1]) - 1])).split('___')
            for k in range(len(vremmass[i][1])):
                vremmass[i][1][k] = vremmass[i][1][k].split('***')
                sigma.append(vremmass[i][1][k])
        l.close()
        kep = []
        bot.register_next_step_handler(msg, q1)
@bot.message_handler(content_types='text')
def q1(message):
    global vremmass
    global ans
    global k
    global kep
    if message.text == '+':
        ans.append(vremmass[0])
        kep.append('eat')
    msg = bot.send_message(message.chat.id, 'вы Москвич или приезжий?(плюс, если приезжий, а минус - если вы живете в Москве или МО)')
    k = 0
    bot.register_next_step_handler(msg, q2)
@bot.message_handler(content_types='text')
def q2(message):
    global vremmass
    global ans
    global k
    global op
    global kep
    if message.text == '+':
        k = 1
        ans.append(vremmass[4])
        kep.append('souv')
    msg = bot.send_message(message.chat.id, 'У вас с собой все что нужно для телефона?')
    bot.register_next_step_handler(msg, q3)
@bot.message_handler(content_types='text')
def q3(message):
    global vremmass
    global ans
    global k
    global n
    global op
    global kep
    if message.text == '-':
        ans.append(vremmass[2])
        kep.append('dev')
    msg = bot.send_message(message.chat.id, 'Как ваше самочувствие?')
    bot.register_next_step_handler(msg, q4)
@bot.message_handler(content_types='text')
def q4(message):
    global vremmass
    global ans
    global k
    global n
    global f
    global sh
    global op
    global kep
    f = 1
    n = 0
    if message.text == '-':
        ans.append(vremmass[7])
        op.append('АэроАптека')
    sh = 1
    msg = bot.send_message(message.chat.id, 'Нужно ли вам посетить уборную?')
    bot.register_next_step_handler(msg, q5)
@bot.message_handler(content_types='text')
def q5(message):
    global op
    global vremmass
    global ans
    global k
    global kep
    global n
    global sh
    global f
    if message.text == '+' and n != 1 and sh != 0 or k != 0 and message.text == '+' or f != 0 and message.text == '+':
        ans.append('туалет')
        op.append('туалет')
        msg = bot.send_message(message.chat.id, 'У вас есть вся одежда для пребывания в комфорте на завтрашний день?')
        bot.register_next_step_handler(msg, q51)
        f = 1
    elif k != 0 and message.text == '-':
        msg = bot.send_message(message.chat.id, 'У вас есть вся одежда для пребывания в комфорте на завтрашний день?')
        bot.register_next_step_handler(msg, q51)
    elif f == 1:
        n = 1
        msg = bot.send_message(message.chat.id, 'Необходимо ли вам посетить банк или снять деньги?')
        bot.register_next_step_handler(msg, q5)
    elif n == 1 and message.text == '+':
        msg = bot.send_message(message.chat.id, 'Геобанк,Сбербанк, Промсвязьбанк, ВТБ, ВТБ-24, Тинькофф, Райффайзенбанк, НМБ, Райффайзенбанк - какой банк вы предпочитаете??(напишите название банка)')
        bot.register_next_step_handler(msg, q52)
    else:
        g = message.chat.id
        print(result(g))
@bot.message_handler(content_types='text')
def q51(message):
    global vremmass
    global ans
    global k
    global n
    global kep
    global f
    if message.text == '-':
        ans.append(vremmass[8])
        kep.append('wearing')
        msg = bot.send_message(message.chat.id, 'Необходимо ли вам посетить банк или снять деньги?')
        n = 1
        k = 0
        f = 0
        bot.register_next_step_handler(msg, q5)
    else:
        msg = bot.send_message(message.chat.id, 'Необходимо ли вам посетить банк или снять деньги?')
        n = 1
        k = 0
        f = 0
        bot.register_next_step_handler(msg, q5)
@bot.message_handler(content_types='text')
def q52(message):
    global vremmass
    global ans
    global k
    global n
    global kep
    global sh
    ans.append(message.text)
    n = 0
    sh = 0
    k = 0
    msg = bot.send_message(message.chat.id,
                           'пожалуйста, отправьте любое сообщение для продолжения')
    bot.register_next_step_handler(msg, q5)
def result(g):
    global vremmass
    global ans
    global kep
    global k
    global n
    global op
    op = []
    for t in ans:
        print(t)
        if type(t) != str:
            op.append(t[1])
        else:
            op.append(t)
    ans = []
    bot.send_message(g,
                           'Подождите, осталась всего пара вопросов.')

    bot.register_next_step_handler(msg, q21)
def q21(message):
    global kep
    global op
bot.polling()