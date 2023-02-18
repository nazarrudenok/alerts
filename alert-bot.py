import telebot
import requests

bot = telebot.TeleBot("5672716533:AAFej1J84UUwbQ5Q22eRN3xg5IdRvlQ4Pqw")

@bot.message_handler(commands=['start'])
def start(message):
    headers = {'X-API-Key': '52b9d358bcb491a92d2ba114fd07dde825961358'}
    response = requests.get('https://alerts.com.ua/api/states', headers = headers)
    
    alarm_json = response.json()
    
    alarm_vinnytsia = alarm_json['states'][0]['alert']
    alarm_volyn = alarm_json['states'][1]['alert']
    alarm_dnipro = alarm_json['states'][2]['alert']
    alarm_donbas = alarm_json['states'][3]['alert']
    alarm_zhytomyr = alarm_json['states'][4]['alert']
    alarm_karpaty = alarm_json['states'][5]['alert']
    alarm_zaporizhya = alarm_json['states'][6]['alert']
    alarm_franik = alarm_json['states'][7]['alert']
    alarm_kyiv_obl = alarm_json['states'][8]['alert']
    alarm_kirovograd = alarm_json['states'][9]['alert']
    alarm_lugansk = alarm_json['states'][10]['alert']
    alarm_lviv = alarm_json['states'][11]['alert']
    alarm_mykolaiv = alarm_json['states'][12]['alert']
    alarm_odessa = alarm_json['states'][13]['alert']
    alarm_poltava = alarm_json['states'][14]['alert']
    alarm_rivne = alarm_json['states'][15]['alert']
    alarm_sumy = alarm_json['states'][16]['alert']
    alarm_ternopil = alarm_json['states'][17]['alert']
    alarm_kharkiv = alarm_json['states'][18]['alert']
    alarm_kherson = alarm_json['states'][19]['alert']
    alarm_khmel = alarm_json['states'][20]['alert']
    alarm_cherkasy = alarm_json['states'][21]['alert']
    alarm_chernivtsy = alarm_json['states'][22]['alert']
    alarm_chernihiv = alarm_json['states'][23]['alert']
    alarm_kyiv = alarm_json['states'][24]['alert']


    if alarm_vinnytsia:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][0]['name'])
    if alarm_volyn:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][1]['name'])
    if alarm_dnipro:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][2]['name'])
    if alarm_donbas:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][3]['name'])
    if alarm_zhytomyr:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][4]['name'])
    if alarm_karpaty:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][5]['name'])
    if alarm_zaporizhya:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][6]['name'])
    if alarm_franik:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][7]['name'])
    if alarm_kyiv_obl:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][8]['name'])
    if alarm_kirovograd:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][9]['name'])
    if alarm_lugansk:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][10]['name'])
    if alarm_lviv:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][11]['name'])
    if alarm_mykolaiv:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][12]['name'])
    if alarm_odessa:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][13]['name'])
    if alarm_poltava:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][14]['name'])
    if alarm_rivne:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][15]['name'])
    if alarm_sumy:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][16]['name'])
    if alarm_ternopil:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][17]['name'])
    if alarm_kharkiv:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][18]['name'])
    if alarm_kherson:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][19]['name'])
    if alarm_khmel:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][20]['name'])
    if alarm_cherkasy:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][21]['name'])
    if alarm_chernivtsy:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][22]['name'])
    if alarm_chernihiv:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][23]['name'])
    if alarm_kyiv:
        bot.send_message(message.chat.id, '🚨 Повітряна тривога зараз у ' + alarm_json['states'][24]['name'])
        

bot.polling(none_stop=True)