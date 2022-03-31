import telebot,random,os,requests
from telebot import types
ttoken = os.environ['TOKEN']
bot = telebot.TeleBot(ttoken)

# Github: https://github.com/PluginX
# Telegram: https://t.me/Plugin

@bot.message_handler(commands=['start'])
def send_welcome(message):


            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text='Channel', url='https://t.me/CodeLeak')
            b2 = types.InlineKeyboardButton(text='apis.red', url='https://apis.red')

            key.add(b1)
            key.add(b2)

            bot.send_photo(message.chat.id, 'https://t.me/thuuu/8',
                           caption=f'Hi {first}.\nWelcome to our free python host bot\nMade By: @Plugin\n\nPlease see the photo!\n*Send your python file first!*\n\n/help\n *To get the help page*\n\n/pip + Library name\n *To install a Library*\n\n/run + Your file Id\n *To run your bot!*',
                           parse_mode='markdown', reply_markup=key)


@bot.message_handler(func=lambda m: True)
def Get(message):

    msg = message.text
    first = message.chat.first_name

    if msg.startswith('/pip'):
                try:

                    data = str(msg).split(' ')
                    the_pip = data[1]

                    if 'telebot' in the_pip:
                        bot.send_message(message.chat.id, text="Installed by the developer ✅")

                    elif 'pyTelegramBotAPI' in the_pip:
                        bot.send_message(message.chat.id, text="Installed by the developer ✅")

                    elif 'requests' in the_pip:
                        bot.send_message(message.chat.id, text="Installed by the developer ✅")

                    elif 'selenium' in the_pip:
                        bot.send_message(message.chat.id, text="Selenium blocked by the developer 🚫")

                    else:
                        os.system(f"pip install {the_pip}")
                        bot.send_message(message.chat.id, text="Install success! ✅")

                except:
                    bot.send_message(message.chat.id,
                                     text=f"sorry! you leave something empty!\nOr you are missing some requires\nPlease see the photo in /start ")

    elif msg.startswith('/run'):
                try:

                    data = str(msg).split(' ')
                    the_file_name = data[1]

                    os.startfile(f"bots\{the_file_name}.py")
                    bot.send_message(message.chat.id, text="Your Bot hosted success! ✅")

                except:
                    bot.send_message(message.chat.id,
                                     text=f"sorry! you leave something empty!\nOr you are missing some requires\nPlease see the photo in /start ")

    elif msg.startswith('/help'):
                try:

                    key = types.InlineKeyboardMarkup()
                    b1 = types.InlineKeyboardButton(text='Coder', url='https://t.me/Plugin')
                    key.add(b1)

                    bot.send_message(message.chat.id, text="*Help Page* 📑\n1- Drag your python file to the bot\n2- Then the bot will give you *File ID*\n\n3- Then install your Librarys\n 🔍 using /pip + *library name*\n\n4- Run your bot\n 🔍 using /run + *File iD*\n\n*Contact*: @Plugin", parse_mode='markdown', reply_markup=key)

                except:
                    bot.send_message(message.chat.id,text=f"sorry! you leave something empty!\nOr you are missing some requires\nPlease see the photo in /start ")

    else:
                bot.send_message(message.chat.id, text=f"Sorry!, I cant understand what the hell you want!, {msg}")



@bot.message_handler(content_types=['document'])
def save(message):

    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    ran = 'a'+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)

    with open('bots/'+ran+'.py', 'wb') as new_file:
        new_file.write(downloaded_file)

    try:
        with open('bots/'+ran+'.py', 'r',encoding='utf-8') as check_file:
            for line in check_file:
                if 'os' in line:
                    bot.reply_to(message, text=f'You cant use *Os* Library 🚫\nFile Removed! ', parse_mode='markdown')
                    check_file.close()
                    os.remove('bots/'+ran+'.py')
                    break
                elif 'input' in line:
                    bot.reply_to(message, text=f'You cant use *Inputs!* 🚫\nFile Removed!',
                                 parse_mode='markdown')
                    check_file.close()
                    os.remove('bots/' + ran + '.py')
                    break
                elif 'marshal' in line:
                    bot.reply_to(message, text=f'You file is *encrypted* 🚫\nFile Removed!',
                                 parse_mode='markdown')
                    check_file.close()
                    os.remove('bots/' + ran + '.py')
                    break
                elif 'base64' in line:
                    bot.reply_to(message, text=f'You file is *encrypted* 🚫\nFile Removed!',
                                 parse_mode='markdown')
                    check_file.close()
                    os.remove('bots/' + ran + '.py')
                    break
                elif 'bot.py' in line:
                    bot.reply_to(message, text=f'You cant use *bot.py* in your file 🚫\nFile Removed!',
                                 parse_mode='markdown')
                    check_file.close()
                    os.remove('bots/' + ran + '.py')
                    break

                else:
                    bot.send_message(message.chat.id, text=f'*File upload success* ✅\n\n *Your File ID*:\n{ran}',parse_mode='markdown')
                    break
    except:
        bot.send_message(message.chat.id, text=f'*File upload disabled by the coder* 🚫\nPlease try again later',parse_mode='markdown')


bot.polling(True)
