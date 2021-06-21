from app import ath

from app import db
from app.models import User, Post

@ath.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__=='__main__':
    ath.run(debug=True)