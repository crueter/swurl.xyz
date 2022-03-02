'''
    Rudimentary wrapper around python-feedgen.
    This simply supports adding entries and publishing.
    The `fg` object is public, so you can simply
    modify that itself, to change feed title, link,
    or modify individual entries. Look at python-feedgen
    documentation for more info.

    Copyleft 2021-2022 Swurl
'''

from feedgen.feed import FeedGenerator
import pickle
from datetime import datetime

fg = None

def load_fg():
    global fg
    fg = None
    try:
        with open('feed.obj', 'rb') as f:
            fg = pickle.load(f)
    except:
        pass

    if fg == None:
        fg = FeedGenerator()
        fg.title('swirl')
        fg.subtitle('swirl\'s funny feed')
        fg.link([{'href': 'https://swurl.xyz'}, {'href': 'https://swurl.xyz/rss.xml'}])
        fg.language('en')

load_fg()

def add_entry(guid, title, *, categories=['updates'], link=[{'href': 'https://swurl.xyz'}], summary=''):
    fe = fg.add_entry()
    fe.guid(guid=guid)
    fe.title(title=title)
    fe.category(category=[{'term': c} for c in categories])
    fe.link(link=link)
    fe.summary(summary=summary)
    fe.published(published=datetime.astimezone(datetime.now()))
    print(f'added entry {title}')

def abort():
    load_fg()

def rss_str():
    print(fg.rss_str(pretty=True).decode())

def publish():
    fg.lastBuildDate(datetime.astimezone(datetime.now()))
    rss_str()
    choice = input('Does this look good? [Y/n] ')
    if choice.lower() in ['', 'y']:
        fg.rss_file('../rss.xml')
        with open('feed.obj', 'wb') as f:
            pickle.dump(fg, f)
        print('published changes')
    else:
        print('ok, run abort() to remove all changes')
