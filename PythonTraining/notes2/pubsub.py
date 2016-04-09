'Publisher subscriber model'

from time import time
from collections import namedtuple, deque, defaultdict
import hashlib
from itertools import islice
from heapq import merge

Post = namedtuple('Post', ['timestamp', 'user', 'text'])
UserInfo = namedtuple('UserInfo', 'displayname email hashed_password joined bio photo')

posts = deque()                     # arranged newest to oldest
user_posts = defaultdict(deque)     # user -> deque of that user's posts
following = defaultdict(set)        # user -> set of followed users
followers = defaultdict(set)        # user -> set of following users
users = dict()                      # user -> UserInfo
#reply = dict()                     # post -> another_post

def post_message(user, text, timestamp=None):
    user = intern(user)
    timestamp = timestamp or time()
    post = Post(-timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

def posts_by_user(user, limit=10):
    return list(islice(user_posts[user], limit))

def posts_for_user(user, limit=10):
    relevant = [user_posts[followed_user] for followed_user in following[user]]
    return list(islice(merge(*relevant), limit))

def latest_posts(limit=10):
    return list(islice(posts, limit))

def search(phrase, limit=10):
    # XXX This could benefit from caching common requests or preindexing the posts
    return list(islice((post for post in posts if phrase in post.text), limit))

def follow(user, followed_user):
    user = intern(user)
    followed_user = intern(followed_user)
    following[user].add(followed_user)
    followers[followed_user].add(user)

def who_you_follow(user):
    return sorted(following[user])

def who_follows_you(user):
    return sorted(followers[user])

def hash_password(user, email, joined, password):
    salt = 'will the red witch resurrect john snow and who will pay dearly'
    result = '\x1F'.join([user, email, str(joined), password, salt])
    for i in range(10000):
        result = hashlib.sha256(result + str(i)).digest()
    return result

def validate_strong(password):
    if not (len(password) >= 6
            and any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(c.isdigit() for c in password)):
        raise ValueError('Must be at least 6 letters, upper and lowercase with digits')

def set_user(user, email, password, displayname=None, bio=None, photo=None, joined=None):
    user = intern(user)
    validate_strong(password)
    displayname = displayname or user.title()
    joined = joined or time()
    hashed_password = hash_password(user, email, joined, password)
    users[user] = UserInfo(displayname, email, hashed_password, joined, bio, photo)

def update_user(user, email=None, password=None, displayname=None, bio=None,
                photo=None, joined=None):
    user = intern(user)
    info = users[user]
    if password or email or joined:
        if password is None:
            raise ValueError('Updating "email" or "joined" requires a new password')
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
    users[user] = UserInfo(displayname, email, hashed_password, joined, bio, photo)

def validate_user(user, password):
    info = users[user]
    hashed_password = hash_password(user, info.email, info.joined, password)
    if hashed_password != info.hashed_password:
        raise ValueError('Password not matched')

def get_user_info(user):
    return users[user]

if __name__ == '__main__':
    from pubsub_session import *
