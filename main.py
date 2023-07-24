from googletrans import Translator, constants
import os

translator = Translator()
words = [
    "APPROVED",
    "NONE",
    "AMOUNT",
    "CANCEL_OR_ENTER",
    "CARD_ERROR",
    "TRY_AGAIN",
    "PLEASE_ENTER_YOUR_PIN",
    "NOT_AUTHORIZED",
    "SELECT_APPLICATION",
    "CONFIRM_APPLICATION",
    "SELECT_LANGUAGE",
    "CONTINUE",
    "PIN_ENTER",
    "PIN_CANCEL",
    ]
# all the languages supports by the library
languages = ['af', 'am', 'ar', 'az', 'be', 'bg', 'bn', 'bs', 'ca',
             'ceb', 'co', 'cs', 'cy', 'da', 'de', 'el', 'en', 'eo',
             'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy', 'ga', 'gd', 'gl',
             'gu', 'ha', 'haw', 'he', 'hi', 'hmn', 'hr', 'ht', 'hu', 'hy',
             'id', 'ig', 'is', 'it', 'iw', 'ja', 'jw', 'ka', 'kk', 'km', 'kn',
             'ko', 'ku', 'ky', 'la', 'lb', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk',
             'ml', 'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'no', 'ny', 'or', 'pa',
             'pl', 'ps', 'pt', 'ro', 'ru', 'sd', 'si', 'sk', 'sl', 'sm', 'sn', 'so',
             'sq', 'sr', 'st', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tl', 'tr',
             'ug', 'uk', 'ur', 'uz', 'vi', 'xh', 'yi', 'yo', 'zh-cn', 'zh-tw', 'zu'
             ]


start = '<?xml version="1.0" encoding="utf-8"?> \n<resources>\n'
end = '</resources>'
file_extension = '.xml'
for lan in languages:
    No = 0
    path = f'./Translation/VALUES-{lan}'
    os.mkdir(path)
    with open(f'{path}/strings{file_extension}', 'w', newline='') as f:
        f.write(start)
        for name in words:
            rep = name.replace("_"," ")

            if rep == "PIN ENTER":
                rep = "ENTER"

            elif rep == "PIN CANCEL":
                rep = "CANCEL"

            # default source in 'en' language
            translate_name = translator.translate(rep, dest= lan).text
            print(f'({lan}) No:{No} \t {rep}  ==> {translate_name.title()}...')

            f.write(f'\t <string name="{name}">{translate_name.title()}</string>\n')
            No += 1
        f.write(end)
    print(f'{lan} Done... ----------------------------')
