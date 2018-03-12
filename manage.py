#!/usr/bin/env python

import os
from flask_script import Manager, Shell, Server
from main import create_app
from test import runtest

app=create_app()
manager = Manager(app)


def _make_context():
    return {'app':app}


@manager.command
def test():
    runtest()

manager.add_command('server', Server(host="0.0.0.0", port=5000))
manager.add_command('shell', Shell(make_context=_make_context))



if __name__ == '__main__':
    manager.run()