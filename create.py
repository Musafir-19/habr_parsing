from scrap import habr
from models import *
from config import app


def create():
    for item in habr:
        post = Post(url=item['url'], title=item['title'],
                    author=item['author'], time=item['time'],
                    comments=item['comments'],)
        db.session.add(post)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        create()

