from flask_script import Manager

from c_meet import app
from c_meet.scripts.db import CreateGroup, InitDB, DemoDB

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    manager.add_command('demo_db', DemoDB())
    manager.add_command('create_group', CreateGroup())
    manager.run()
