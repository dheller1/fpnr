from fpnr import create_app
from fpnr.model import User, db

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)
