'Publisher subscriber model'
from time import time
from collections import namedtuple, deque, defaultdict
import hashlib
from itertools import islice
from heapq import merge

Post = namedtuple('Post',['timestamp','user', 'text'])              #takes the most memory in the whole program
UserInfo = namedtuple('UserInfo', 'displayname email hashed_password bio photo joined')

posts = deque()     #arranged newest to oldest
user_posts = defaultdict(deque)   # user -> deque of that user's posts
following = defaultdict(set)      # user -> list of following users
follower = defaultdict(set)       # user -> list of followers
users = dict()                    # user -> UserInfo
# TODO : add conversation / push notification
#reply = dict()                    # post -> another_post @
    
def post_message(user, text, timestamp=None):
    user = intern(user)             # save space. intern('abc') and intern('abc') would reuse the same location
    timestamp = timestamp or time() # will return timestamp if timestamp is not None
    post= Post(-timestamp, user, text)   # because sort would sort by the first data, so reverse the sign make sure the newest is first
    posts.appendleft(post)
    user_posts[user].appendleft(post)

def posts_by_user(user, limit=10):
    #return list(user_posts['raymondh'])[:10] # comsumes memory as it will create a list first then slice it
    return list(islice(user_posts[user], limit))  # more efficient as islice creates an iterator and only create as much elements as limit

# all posts from users followed by this user
def posts_for_user(user, limit=10):
    relevant = [user_posts[followed_user] for followed_user in following[user]]  # number of deques = number of following users
    # merge will return a generator. islice gets up to limit element from this generator
    return list(islice(merge(*relevant), limit))      #tuple sort by first element, merge sort by first element
                                                      #if you sort the merged result, you can reverse it, you're using more memory

def latest_posts(limit=10):
    return list(islice(posts,limit))

'''
>>> it = [10,20,30]
>>> type(it)
<type 'list'>
>>> type((for i in it if i < 20))
SyntaxError: invalid syntax
>>> t = [i for i in it if i<=20]
>>> type(t)
<type 'list'>
>>> m = (i for i in it if i<=20)
>>> type(m)
<type 'generator'>
'''
### Generator is more memory efficient than list
def search(phrase, limit=2):
    #TODO : This could benefit from caching common requests or preindexing the posts
    return list(islice((post for post in posts if phrase in post.text),limit))  #(post for xxx) creates a generator
    
def follow(user, followed_user):
    user = intern(user)
    followed_user = intern(followed_user)
    following[user].add(followed_user)
    follower[followed_user].add(user)

def who_you_follow(user):
    return sorted(following[user])

def who_follows_you(user):
    return sorted(follower[user])

def hash_password(user, email, joined, password):
    salt = 'will the red witch resurrect john snow and who will pay dearly'
    result = '\x1f'.join([user, email, str(joined), password, salt])  # \x1f is ascii 31, unprintable character, to make sure no hack string could be created to mimic these four fields
    for i in range(10000):                                       # TODO: make this larger
        result = hashlib.sha256(result + str(i)).hexdigest()       # TODO: change to sha256
    return result    

def validate_strong(password):
    # XXX Todo: Check to make sure the password variants isn't in common password
    if not (len(password) >=6
            and any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(c.isdigit() for c in password)):
        raise ValueError('Must be at least 6 letters, upper and lowercase with digits')

def set_user(user, email, password=None, displayname=None, bio=None, photo=None, joined=None):
    user = intern(user)     # intern is only done for immutable values. this place is not very needed as it's only called once for each user
    validate_strong(password)
    displayname = displayname or user.title()
    joined = joined or time()
    hashed_password = hash_password(user, email, joined, password)
    users[user] = UserInfo(displayname, email, hashed_password, bio, photo, joined)

def update_user(user, email=None, password=None, displayname=None, bio=None, photo=None, joined=None):
    user = intern(user)
    info = users[user]
    if password or email or joined:
        if password is None:
            raise valueError('Updating "email" or "joined" requires a new password')
        email = email or info.email
        joined = joined or info.joined
        hashed_password = hash_password(user, email, joined, password)
    else:
        email = info.email
        joined = info.joined
        hashed_password = info.hashed_password
    displayname = displayname or info.displayname
    bio = bio or info.bio
    photo = photo or info.photo
    users[user] = UserInfo(displayname, email, hashed_password, bio, photo, joined)
            
def get_user_info(user):
    return users[user]

def validate_user(user, password):
    info = users[user]
    hashed_password = hash_password(user, info.email, info.joined, password)
    if hashed_password != info.hashed_password:
        raise ValueError('Password not matched')

# to faciliated run pubsub from this file. Need to be removed later
if __name__ == '__main__':
    import pubsub_session
    
