from reverend.thomas import Bayes
import re

phrases = '''\
all the leaves are brown and the sky is grey
de colored, de colored,  todo los colores
jingle bell, jingle bell, jingle all the way, oh what fun it is to ride
casa belles casca belles hoy est navidad, es un dia de allergia y felicidad
'''.splitlines()

## Step 1: Make and train a language classifier ##########
language = Bayes()

for lang, samplefile in [
    ('English','notes3/proverbs_en.txt'),
    ('Spanish','notes3/proverbs_es.txt')
]:
    with open(samplefile) as f:
        language.train(lang,f.read())

## Step 2: Apply the classifier on new data ###############
for phrase in phrases:
    lang = language.guess(phrase)
    print lang, '-->', phrase
