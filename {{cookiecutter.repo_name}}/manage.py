#!/usr/bin/env python

import os

from flask.ext.script import Manager, Server
from flask.ext.script.commands import ShowUrls, Clean
from {{cookiecutter.repo_name}} import create_app
from {{cookiecutter.repo_name}}.models import db

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('{{cookiecutter.repo_name|upper}}_ENV', 'dev')
app = create_app('{{cookiecutter.repo_name}}.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """

    return dict(app=app, db=db)


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """

    db.create_all()

if __name__ == "__main__":
    manager.run()
