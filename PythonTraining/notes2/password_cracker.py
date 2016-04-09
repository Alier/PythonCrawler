from pprint import pprint
import hashlib
from itertools import product

### Security Code ##################################################

userpass = {}             # Usually this is in a file

def digest(password):
    # XXX Todo:  Add the user specific salt to prevent chosen plaintext attacks
    salt = 'the life expectancy of a stark, targaryan, or lannister is very short'
    result = password + salt
    for i in range(100000):
        result = hashlib.sha512(result + str(i)).hexdigest()
    return result

def is_strong(password):
    # XXX Todo: Check to make sure the password variants aren't in common password file
    if len(password) < 6:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

def new_account(username, password):
    if not is_strong(password):
        raise ValueError('Passwords must be at least 6 letters, upper and lower and digits')
    hashpass = digest(password)
    userpass[username] = hashpass

def verify(username, password):
    hashpass = digest(password)
    return userpass[username] == hashpass

### Cracker code ##################################

def make_rainbow():
    rainbow = {}
    with open('notes2/common_passwords.txt') as f:
        for line in f:
            password, count = line.split(',')
            hashpass = digest(password)
            rainbow[hashpass] = password
    return rainbow

def cracker(userpass, rainbow):
    for username, hashpass in userpass.items():
        if hashpass in rainbow:
            print username, rainbow[hashpass]

def search_common(userpass):
    passuser = {hashpass: user for user, hashpass in userpass.items()}
    short_num_variants = map(str, range(10)) + ['']
    num_variants = map(str, range(1000)) + ['']
    with open('notes2/common_passwords.txt') as f:
        for line in f:
            password, count = line.split(',')
            case_variants = [password.lower(), password.upper(), password.title()]
            for parts in product(short_num_variants, case_variants, num_variants):
                password = ''.join(parts)
                hashpass = digest(password)
                if hashpass in passuser:
                    print passuser[hashpass], password

if __name__ == '__main__':
    new_account('raymondh', 'Superman7')
    new_account('jeff', 'Cisco1'),
    new_account('denis', '1Sharapova')
    new_account('ai', '1Brazil')
    new_account('steven', 'Seahawks12')

    print verify('jeff', 'Cisco1')
    print verify('steven', 'Seahawks12')

    # cracker(userpass, make_rainbow())
    search_common(userpass)

