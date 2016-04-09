from pubsub import *
from pprint import pprint

set_user('raymondh', email='python@rcn.com', password='Superman123',
         bio = 'Python trainer. Core Developer. Pilot. Soldier. Fashion Photographer. Familyman')
set_user('davin', email='davin@appliomics.com', password='LonelyHeartsClub101',
         bio = 'Python trainer.  CEO of startup.  Phd in Chemistry.  Familyman',
         displayname='Davin Potts')
set_user('barry', email='barry@python.org', password='TallTexan1962',
         bio = 'Python core developer.  Musician',
         displayname='Funky Barry')         

post_message('raymondh', '#python is the best')
post_message('davin', 'teaching #python today')
post_message('raymondh', '#python news:  pypy5.0 released today')
post_message('barry', 'it is fun to use #emacs')
post_message('davin', '@barry no, no #vi rocks')
post_message('barry', '@davin but #emacs can do anything')
post_message('davin', '@barry but it turns my fingers into knots')
post_message('raymondh', '#python tip: always use namedtuples')
post_message('davin', '#funfact:  coriander and cilantro come from the same plant')

update_user('raymondh', password='Batman456')       # XXX make sure we can update the accounts
update_user('davin', displayname='Davinator')

validate_user('davin', 'LonelyHeartsClub101')
validate_user('raymondh', 'Batman456')
follow('davin', followed_user='raymondh')
follow('davin', followed_user='barry')
follow('davin', followed_user='barry')

pprint(list(posts))
pprint(dict(following))
pprint(dict(followers))
pprint(users)

pprint(posts_by_user('raymondh'))
pprint(posts_for_user('davin'))
pprint(latest_posts(limit=5))

print who_you_follow('davin')
print who_follows_you('barry')
print get_user_info('davin')
