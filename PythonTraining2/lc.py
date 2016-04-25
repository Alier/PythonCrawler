from reverend.thomas import Bayes

# Step 1:  Make and train a language classifier ###############
language = Bayes()
for lang, samplefile in [
    ('English', 'notes3/proverbs_en.txt'),
    ('Spanish', 'notes3/proverbs_es.txt'),
]:
    with open(samplefile) as f:
        language.train(lang, f.read())

# Step 2:  Apply the classifier to new data ###################
phrases = '''\
all the leaves are brown and the sky is grey
de colored, de colored, todo los colores
jingle bells, jingle bells, jingle all the way, oh what fun it is to ride
casca belles casca belles hoy es navidad, es un dia de allegria y felicidad
'''.splitlines()

for phrase in phrases:
    lang = language.guess(phrase)[0][0]
    print lang, '-->', phrase

## Test your skill with follow-up exercises ##################################################
    
# Five minutes:
# -------------
# CSDMC2010_SPAM.zip  <-- unzip this
# Supervised learning:  SPAMTrain.label has preclassified the email into 0-spam and 1-ham
# Loop over the 1st 4000 emails and use the label file to train the classifier
# Loop over the next 326 and guess whether they are spam or ham.  Compare your results to the label.



# Twenty minutes:
# ---------------
# https://www.gutenberg.org/browse/languages/ro <== Romanian
# https://www.gutenberg.org/files/11756/11756-0.txt
# From the gutenberg site, pick 20 languages and for each choose 10 books.
# Loop over them and train the language guessers.
# Test with a sample not in the 10 training books
