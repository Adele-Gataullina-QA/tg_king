import random

import telebot

bot = telebot.TeleBot('ВСТАВИТЬ СВОЙ ТОКЕН')

from telebot import types

@bot.message_handler(commands=['start', 'help'])
def menu(message):
    keyboard_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_1_1 = types.KeyboardButton('Выбрать раздел')
    keyboard_menu.add(key_1_1)
    bot.reply_to(message, "Привет! Этот бот поможет тебе сориентироваться в обширном творчестве Стивена Кинга и выбрать книгу, которая придется по душе.", reply_markup=keyboard_menu)

Best_novels = ['https://www.livelib.ru/book/1002360916-kerri-stiven-king', 'https://www.livelib.ru/book/1002091774-siyanie-stiven-king', 'https://www.livelib.ru/book/1006891573-protivostoyanie-stiven-king', 'https://www.livelib.ru/book/1006055533-klatbische-domashnih-zhyvotnyh-stiven-king', 'https://www.livelib.ru/book/1002091795-ono-stiven-king', 'https://www.livelib.ru/book/1006039126-mizeri-stiven-king', 'https://www.livelib.ru/book/1000664440-pod-kupolom-stiven-king', 'https://www.livelib.ru/book/1001645289-zeljonaya-milya-stiven-king']
Longest_novels = ['https://www.livelib.ru/book/1006891573-protivostoyanie-stiven-king', 'https://www.livelib.ru/book/1002091795-ono-stiven-king', 'https://www.livelib.ru/book/1000664440-pod-kupolom-stiven-king', 'https://www.livelib.ru/book/1001506883-112263-stiven-king']
Series = ['https://www.livelib.ru/series/532740-temnaya-bashnya', 'https://www.livelib.ru/series/749243-trilogiya-billa-hodzhesa']
Richard_Bachman = ['https://www.livelib.ru/book/1000003142-yarost-stiven-king', 'https://www.livelib.ru/book/1001493784-dolgaya-progulka-richard-bahman', 'https://www.livelib.ru/book/1001532033-dorozhnye-raboty-richard-bahman', 'https://www.livelib.ru/book/1001317182-beguschij-chelovek-richard-bahman', 'https://www.livelib.ru/book/1001286159-hudeyuschij-stiven-king', 'https://www.livelib.ru/book/1003172009-regulyatory-richard-bahman', 'https://www.livelib.ru/book/1006866853-blejz-sbornik-richard-bahman']
Coauthorship = ['https://www.livelib.ru/book/1001280487-talisman-stiven-king', 'https://www.livelib.ru/book/1001475424-chjornyj-dom-stiven-king', 'https://www.livelib.ru/book/1005595081-spyaschie-krasavitsy-stiven-king', 'https://www.livelib.ru/book/1002726285-gvendi-i-ejo-shkatulka-stiven-king']
Nonmystic = ['https://www.livelib.ru/book/1000003142-yarost-stiven-king', 'https://www.livelib.ru/book/1001493784-dolgaya-progulka-richard-bahman', 'https://www.livelib.ru/book/1001532033-dorozhnye-raboty-richard-bahman', 'https://www.livelib.ru/book/1001317182-beguschij-chelovek-richard-bahman', 'https://www.livelib.ru/book/1006866853-blejz-sbornik-richard-bahman', 'https://www.livelib.ru/book/1002986515-kudzho-stiven-king', 'https://www.livelib.ru/book/1006039126-mizeri-stiven-king', 'https://www.livelib.ru/book/1001402445-igra-dzheralda-stiven-king', 'https://www.livelib.ru/book/1000945257-dolores-klejborn-stiven-king', 'https://www.livelib.ru/book/1002772446-devochka-kotoraya-lyubila-toma-gordona-stiven-king', 'https://www.livelib.ru/book/1007053543-billi-sammers-stiven-king', 'https://www.livelib.ru/book/1001515917-paren-iz-kolorado-stiven-king']
Madness = ['https://www.livelib.ru/book/1002975275-temnaya-polovina-stiven-king', 'https://www.livelib.ru/book/1006039126-mizeri-stiven-king', 'https://www.livelib.ru/book/1000003142-yarost-stiven-king', 'https://www.livelib.ru/book/1001402445-igra-dzheralda-stiven-king', 'https://www.livelib.ru/book/1001453989-roza-marena-stiven-king', 'https://www.livelib.ru/book/1002986515-kudzho-stiven-king', 'https://www.livelib.ru/book/1001514402-istoriya-lizi-stiven-king', 'https://www.livelib.ru/series/749243-trilogiya-billa-hodzhesa', 'https://www.livelib.ru/book/1002053145-beznadjoga-stiven-king', 'https://www.livelib.ru/book/1002091774-siyanie-stiven-king']
Superpowers = ['https://www.livelib.ru/book/1002092465-vosplamenyayuschaya-stiven-king', 'https://www.livelib.ru/book/1002360916-kerri-stiven-king', 'https://www.livelib.ru/book/1003834562-institut-stiven-king', 'https://www.livelib.ru/book/1002091774-siyanie-stiven-king', 'https://www.livelib.ru/book/1006205419-pozzhe-stiven-king', 'https://www.livelib.ru/book/1006178797-doktor-son-stiven-king']
Crime_fiction = ['https://www.livelib.ru/series/749243-trilogiya-billa-hodzhesa', 'https://www.livelib.ru/book/1005757309-chuzhak-stiven-king', 'https://www.livelib.ru/book/1007053543-billi-sammers-stiven-king', 'https://www.livelib.ru/book/1001515917-paren-iz-kolorado-stiven-king']
Fantasy = ['https://www.livelib.ru/series/532740-temnaya-bashnya', 'https://www.livelib.ru/book/1003053080-glaza-drakona-stiven-king']
Derry = ['https://www.livelib.ru/book/1002091795-ono-stiven-king', 'https://www.livelib.ru/book/1000828486-bessonnitsa-stiven-king', 'https://www.livelib.ru/book/1000722430-lovets-snov-stiven-king']
Castle_Rock = ['https://www.livelib.ru/book/1000745920-mjortvaya-zona-stiven-king', 'https://www.livelib.ru/book/1002986515-kudzho-stiven-king', 'https://www.livelib.ru/book/1002975275-temnaya-polovina-stiven-king', 'https://www.livelib.ru/book/1001427345-nuzhnye-veschi-stiven-king', 'https://www.livelib.ru/book/1001402445-igra-dzheralda-stiven-king', 'https://www.livelib.ru/book/1002751720-meshok-s-kostyami-stiven-king']
Alliens = ['https://www.livelib.ru/book/1002103067-tomminokery-stiven-king', 'https://www.livelib.ru/book/1000722430-lovets-snov-stiven-king']
Tech = ['https://www.livelib.ru/book/1006217845-mobilnik-stiven-king', 'https://www.livelib.ru/book/1005651223-kristina-stiven-king', 'https://www.livelib.ru/book/1001034270-pochti-kak-byuik-stiven-king']
Short_fiction = ['https://www.livelib.ru/book/1002978888-chetyre-sezona-sbornik-stiven-king', 'https://www.livelib.ru/book/1000658766-chetyre-posle-polunochi-sbornik-stiven-king', 'https://www.livelib.ru/book/1001393885-serdtsa-v-atlantide-sbornik-stiven-king', 'https://www.livelib.ru/book/1007554378-tma-i-bolshe-nichego-sbornik-stiven-king', 'https://www.livelib.ru/book/1005508483-budet-krov-sbornik-stiven-king', 'https://www.livelib.ru/book/1001398511-nochnaya-smena-sbornik-stiven-king', 'https://www.livelib.ru/book/1002995221-komanda-skeletov-sbornik-stiven-king', 'https://www.livelib.ru/book/1002344171-nochnye-koshmary-i-fantasticheskie-videniya-stiven-king', 'https://www.livelib.ru/book/1003749874-vsjo-predelno-sbornik-stiven-king', 'https://www.livelib.ru/book/1000474970-posle-zakata-sbornik-stiven-king', 'https://www.livelib.ru/book/1003191348-lavka-durnyh-snov-sbornik-stiven-king']
Nonfiction = ['https://www.livelib.ru/book/1002868277-plyaska-smerti-stiven-king', 'https://www.livelib.ru/book/1002514026-kak-pisat-knigi-stiven-king']
Favorites = ['https://www.livelib.ru/book/1002091774-siyanie-stiven-king', 'https://www.livelib.ru/book/1006891573-protivostoyanie-stiven-king', 'https://www.livelib.ru/book/1002986515-kudzho-stiven-king', 'https://www.livelib.ru/book/1006055533-klatbische-domashnih-zhyvotnyh-stiven-king', 'https://www.livelib.ru/book/1002091795-ono-stiven-king', 'https://www.livelib.ru/book/1002103067-tomminokery-stiven-king', 'https://www.livelib.ru/book/1006039126-mizeri-stiven-king', 'https://www.livelib.ru/book/1002111884-dyumaki-stiven-king', 'https://www.livelib.ru/series/532740-temnaya-bashnya']
Other = ['https://www.livelib.ru/book/1001137235-zhrebij-salema-stiven-king', 'https://www.livelib.ru/book/1002111884-dyumaki-stiven-king', 'https://www.livelib.ru/book/1003711626-strana-radosti-stiven-king', 'https://www.livelib.ru/book/1002178798-vozrozhdenie-stiven-king']
Lucky_choise = [Best_novels, Longest_novels, Series, Richard_Bachman, Coauthorship, Nonmystic, Madness, Superpowers, Crime_fiction,Fantasy, Derry, Castle_Rock, Alliens, Tech, Short_fiction, Nonfiction, Other]

@bot.message_handler(content_types=['text'])
def options(message):
    if message.text == "Выбрать раздел":
        keyboard_options = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_2_1 = types.KeyboardButton('Знаковые романы')
        keyboard_options.add(key_2_1)
        key_2_2 = types.KeyboardButton('Большие романы')
        keyboard_options.add(key_2_2)
        key_2_3 = types.KeyboardButton('Циклы')
        keyboard_options.add(key_2_3)
        key_2_4 = types.KeyboardButton('Под псевдонимом Ричард Бахман')
        keyboard_options.add(key_2_4)
        key_2_5 = types.KeyboardButton('Соавторство')
        keyboard_options.add(key_2_5)
        key_2_6 = types.KeyboardButton('Без мистики')
        keyboard_options.add(key_2_6)
        key_2_7 = types.KeyboardButton('Безумный антагонист')
        keyboard_options.add(key_2_7)
        key_2_8 = types.KeyboardButton('Сверхспособности')
        keyboard_options.add(key_2_8)
        key_2_9 = types.KeyboardButton('Детективы')
        keyboard_options.add(key_2_9)
        key_2_10 = types.KeyboardButton('Фэнтези')
        keyboard_options.add(key_2_10)
        key_2_11 = types.KeyboardButton('Дерри')
        keyboard_options.add(key_2_11)
        key_2_12 = types.KeyboardButton('Касл-Рок')
        keyboard_options.add(key_2_12)
        key_2_13 = types.KeyboardButton('Пришельцы')
        keyboard_options.add(key_2_13)
        key_2_14 = types.KeyboardButton('Зловещая техника')
        keyboard_options.add(key_2_14)
        key_2_15 = types.KeyboardButton('Сборники малой прозы')
        keyboard_options.add(key_2_15)
        key_2_16 = types.KeyboardButton('Нон-фикшн')
        keyboard_options.add(key_2_16)
        key_2_17 = types.KeyboardButton('Божественный рандом')
        keyboard_options.add(key_2_17)
        key_2_18 = types.KeyboardButton('Любимое 🖤')
        keyboard_options.add(key_2_18)
        bot.send_message(message.chat.id, 'Выбери интересующий раздел', reply_markup=keyboard_options)
    elif message.text == "Знаковые романы":
        bot.send_message(message.chat.id, random.choice(Best_novels))
    elif message.text == "Большие романы":
        bot.send_message(message.chat.id, random.choice(Longest_novels))
    elif message.text == "Циклы":
        bot.send_message(message.chat.id, random.choice(Series))
    elif message.text == "Под псевдонимом Ричард Бахман":
        bot.send_message(message.chat.id, random.choice(Richard_Bachman))
    elif message.text == "Соавторство":
        bot.send_message(message.chat.id, random.choice(Coauthorship))
    elif message.text == "Без мистики":
        bot.send_message(message.chat.id, random.choice(Nonmystic))
    elif message.text == "Безумный антагонист":
        bot.send_message(message.chat.id, random.choice(Madness))
    elif message.text == "Сверхспособности":
        bot.send_message(message.chat.id, random.choice(Superpowers))
    elif message.text == "Детективы":
        bot.send_message(message.chat.id, random.choice(Crime_fiction))
    elif message.text == "Фэнтези":
        bot.send_message(message.chat.id, random.choice(Fantasy))
    elif message.text == "Дерри":
        bot.send_message(message.chat.id, random.choice(Derry))
    elif message.text == "Касл-Рок":
        bot.send_message(message.chat.id, random.choice(Castle_Rock))
    elif message.text == "Пришельцы":
        bot.send_message(message.chat.id, random.choice(Alliens))
    elif message.text == "Зловещая техника":
        bot.send_message(message.chat.id, random.choice(Tech))
    elif message.text == "Сборники малой прозы":
        bot.send_message(message.chat.id, random.choice(Short_fiction))
    elif message.text == "Нон-фикшн":
        bot.send_message(message.chat.id, random.choice(Nonfiction))
    elif message.text == "Божественный рандом":
        bot.send_message(message.chat.id, random.choice(Lucky_choise))
    elif message.text == "Любимое 🖤":
        bot.send_message(message.chat.id, random.choice(Favorites))
    else:
        bot.send_message(message.chat.id, "К сожалению, я тебя не понимаю 😞 Пожалуйста, выбери раздел.")

def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()
