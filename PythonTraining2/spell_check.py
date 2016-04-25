import re
from bloomfilter import BloomFilter
import pickle       # for serializing data into string/file
 
def make_checker(correct_words):
    # use pickle to save expensive data structures you make to save on time/memory
    # in this case: making BloomFilter is taking the most of the time running this program
    try:
        with open('words.pcl','r') as f:
            return pickle.load(f)
    except IOError:
        pass
    
    with open('notes3/words.txt') as f:
        correct_words = f.read().lower().split()

    bf = BloomFilter(correct_words, population=4000000, probes=10)
    
    with open('words.pcl','wb') as f:
        pickle.dump(bf, f)
    return bf

def spell_check(text, checker):
    print 'Misspelled words:'
    print '-----------------'
    words = re.findall(r"[a-z\']+", text.lower())
    for word in words:
        if word not in checker:
            print word

if __name__ == '__main__':

    correct_words = '''
        a aid all an army assistance bad be
        beautiful by child children come country
        flag for from go going good help is later
        man many men my no now of our some state
        the their to ugly was with woman women
    '''

    text = '''
            Now, iss the tymme for all
            guhd men tooo comee to the
            ayd of thur country and city.
    '''

    checker = make_checker(correct_words)
    #with open('notes3/the_great_gatsby.txt') as f:
    #   text = f.read()
    spell_check(text, checker)
