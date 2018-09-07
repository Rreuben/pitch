from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app import create_app, DB

# instances for the create_app
APP = create_app('development')


MANAGER = Manager(APP)
MANAGER.add_command('server', Server)

MIGRATE = Migrate(APP, DB)
MANAGER.add_command('db', MigrateCommand)

@MANAGER.shell
def make_shell_context():
    return dict(app=APP, db=DB,)

@MANAGER.command
def test():
    '''
    Run the unit test
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    MANAGER.run()
