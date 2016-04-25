'Goal: show typical patterns for accessing REST APIs using the requests module'

import requests

# Github REST API documented at : https://developer.github.com/v3/
# http://bit.ly/python-sj141

def show_user_info(user):
    " Print a Github user's name, company and contact information"
    info = requests.get('https://api.github.com/users/'+user).json()
    print 'Mr %(name)s works for %(company)s. Contact at %(email)s' % info


if __name__ == '__main__':
    print show_user_info('raymondh')
    print show_user_info('Alier')