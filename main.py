import re

f = open('steam_description_data.csv',  encoding='utf8')
words = 0
symbols = 0
symbols_without_space = 0
symbols_without_comma = 0
symbols_without_dot = 0
symbols_without_marks = 0
symbols_without_exclamatiom_mark = 0
symbols_without_colon = 0
comma = 0
dot = 0
comma = 0
exclamatiom_mark = 0
colon = 0
sentence = 0
for line in f:
    wordlist5 = re.split(r'[,\!]', line)
    wordlist4 = line.split(':')
    wordlist3 = line.split('!')
    wordlist = line.split()
    wordlist1 = line.split(',')
    wordlist2 = line.split('.')
    symbols = symbols + len(line)
    words = words + len(wordlist)
    symbols_without_space += sum(len(word) for word in wordlist)
    symbols_without_comma += sum(len(word) for word in wordlist1)
    symbols_without_dot += sum(len(word) for word in wordlist2)
    symbols_without_exclamatiom_mark += sum(len(word) for word in wordlist3)
    symbols_without_colon += sum(len(word) for word in wordlist4)
    sentence = sentence + len(wordlist5)
colon = symbols - symbols_without_colon
exclamatiom_mark = symbols -symbols_without_exclamatiom_mark
dot = symbols - symbols_without_dot
comma = symbols - symbols_without_comma
symbols_without_marks = symbols - dot - comma - exclamatiom_mark - colon
print('Кол-во символов без знаков препинания',symbols_without_marks ,
'Кол-во слов',
words,
'Кол-во символов',
symbols,
'Кол-во симоволов без пробелов',
symbols_without_space,
'Кол-во предложений',
sentence)
f.close()
