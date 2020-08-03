# Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.

import string


def txt(words):
    lst = words.lower().split()
    table = str.maketrans('', '', string.punctuation)
    words_lst = [w.translate(table) for w in lst]
    often_words = [words_lst.count(w) for w in words_lst]
    length_words = [len(w) for w in words_lst]
    return words_lst[often_words.index(max(often_words))], words_lst[length_words.index(max(length_words))]


text = 'OmegaLil одолела EXTREMUM, а Cyber Legacy победила Khan в групповом этапе закрытой квалификации на OMEGA ' \
       'League по Dota 2. Обе встречи завершились со счетом 2:0. В следующем раунде группового этапа Cyber Legacy ' \
       'сразится с Team Empire, а команда Ильи Lil Ильюка сыграет с HellRaisers. Следить за ходом квалификации можно ' \
       'в нашем репортаже. Закрытые отборочные на OMEGA League для Европы проходят 1–9 августа в онлайне. 16 команд ' \
       'разыгрывают слоты в дивизионах Immortal и Divine. Первые матчи основной стадии турнира запланированы на 14 ' \
       'августа. '
print(txt(text))


