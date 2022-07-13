import requests
from .models import TeleSettings

# token = '5542030224:AAGJjLycbSMKlTm7s9GivEpNKccc_Q4z3JI'
# chat_id = '-732349017'
# text = 'Test_2'


def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_massage)

    # a = text.find('{')
    # b = text.find('}')
    # c = text.rfind('{')
    # d = text.rfind('}')
        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}')+1: text.rfind('{')]
            part_3 = text[text.rfind('}'):-1]

            text_slise = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
            text_slise =  text
        try:
            url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text_slise
            results = requests.post(url_req)
        except:
            pass
        finally:
            if results.status_code != 200:
                print("Fatall EROR 200")
            elif results.status_code == 500:
                print("Fatall EROR 500")
            else:

                print("Nice")
    # print(results.json())
    else:
        pass



# def sendTelegram():
#     api = 'https://api.telegram.org/bot'
#     method = api + token + '/sendMassage?chat_id='

    # req = requests.post(method, data={
    #     'chat_id': chat_id,
    #     'x': x,
    #     'text': text,
    #
    # })

