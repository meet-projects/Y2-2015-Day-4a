from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

### These are the commands you just saw live.

lorenzo = Person(
        name = 'Lorenzo Brown',
        gender = 'male',
        nationality = 'American',
        hometown = 'San Francisco')

michele = Person(
        name = 'Michele Pratusevich',
        gender = 'female',
        nationality = 'American',
        hometown = 'Boston')

omri = Person(
        name = 'Omri Doron',
        gender = 'male',
        nationality = 'Israeli',
        hometown = 'Jerusalem')

# This deletes everything in your database.
session.query(Person).delete()
session.commit()

# This adds some rows to the database. Make sure you `commit` after `add`ing!
session.add(lorenzo)
session.add(michele)
session.add(omri)
session.commit()

