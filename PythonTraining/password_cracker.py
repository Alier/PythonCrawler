from pprint import pprint
import hashlib
import itertools

## Security Code #######################################################

userpass = {}       # Usually this is in a file

def digest(password):
    salt = 'the life expectancy of a stark, targyrian, or lannister is very short'   #destroy the exist/built rainbow table
    result = password + salt
    for i in range(100000):                                                             # make the hashfunction slower
        result = hashlib.md5(result + str(i)).hexdigest()
        # new bcrypt, scrypt, slower and takes more memory, targetting to throw crackers off.
    return result

def is_strong(password):
    # XXX Todo: Check to make sure the password variants isn't in common password
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

### Cracker code ####################################################

def make_rainbow():
    rainbow = {}        # md5: password

    with open('notes2/common_passwords.txt') as f:
        for line in f:
            password = line.split(',')[0]
            hashpass = digest(password)
            rainbow[hashpass] = password
    return rainbow

def cracker(username, rainbow):
    for username, hashpass in userpass.items():
        if hashpass in rainbow:
            print username, rainbow[hashpass]

def search_common(userpass):
    passuser = {hashpass: username for username, hashpass in userpass.items()}
    pre_num_variants = map(str, range(10))+['']
    post_num_variants = map(str,range(1000))+['']
    with open('notes2/common_passwords.txt') as f:
        for line in f:
            password = line.split(',')[0]
            case_variants = [password.lower(),password.upper(),password.title()]
            for parts in itertools.product(pre_num_variants, case_variants, post_num_variants):
                password = ''.join(parts)
                hashpass = digest(password)
                if hashpass in passuser:
                    print passuser[hashpass], password
                
if __name__ == '__main__':
    new_account('raymond','Superman1')
    new_account('jeff','Cisco1')
    new_account('denis','Sharapova123')
    new_account('ai','1Brazil')
    new_account('steven','Seahawks123')
    
    print verify('jeff','Cisco1')
    print verify('steven','Seahawks123')

    search_common(userpass)
    #cracker(userpass,make_rainbow())
