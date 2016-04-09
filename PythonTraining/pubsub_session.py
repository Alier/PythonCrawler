from pubsub import *
from pprint import pprint

set_user('raymondh', email='python@rcn.com', password='Superman123',
         bio = 'Python trainer. Core Developer. Pilot. Soldier. Fashion Photographer. Familyman')
set_user('davin', email='davin@appliomics.com', password = 'LonelyHeartClub101',
         bio = 'Python trainer. CEO of startup. Phd in Chemistry. Familyman',
         displayname = 'Davin Potts')
set_user('barry', email='barry@python.org', password = 'TallTexan1962',
         bio = 'Python core developer. Musician',
         displayname = 'Funky Barry')

### TODO: make sure we can update the accounts
# set_user('raymondh',password='Batman456')
# set_user('davin', displayname='Davinator') 

post_message('raymondh','#python is the best')
post_message('davin','teaching #python today')
post_message('raymondh','#python news: pypy5.0 released today')
post_message('barry','it is fun to use #emacs')
post_message('davin','@barry, no, no, #vi rocks')
post_message('barry','@davin but #emacs can do anything')
post_message('davin','@barry but it turns my fingers into nuts')
post_message('raymondh','#python tip: always use namedtuples')
post_message('davin','#funfact: coriander and cilantro come from th same plant')

follow('davin',followed_user = 'raymondh')
follow('davin',followed_user = 'barry')
follow('raymondh',followed_user = 'barry')
#follow('barry',followed_user = 'raymondh')
#follow('barry',followed_user = 'davin')

pprint(list(posts))
pprint(dict(following))
pprint(dict(follower))
pprint(users)
#pprint(posts_by_user('raymondh'))
print 'Posts for davin'
pprint(posts_for_user('davin'))
print 'latest posts'
pprint(latest_posts(3))
print 'search for emacs'
pprint(search('emacs'))

print who_you_follow('raymondh')
print who_follows_you('raymondh')

print get_user_info('raymondh')

#validate_user('raymondh','Superman456')
update_user('raymondh',bio='Superman')
validate_user('raymondh','Superman123')
update_user('raymondh',displayname='Superman')
validate_user('raymondh','Superman123')
print get_user_info('raymondh')
