from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# This queries the Person table
session.query(Person).all()


# Let's look at what's in the database
session.query(Person).filter_by(nationality = 'American').all()
session.query(Person).filter_by(nationality = 'American').first()

my_query = session.query(Person)
my_query.all()

american_male = my_query.filter_by(nationality = 'American', gender = 'male').first()

print(american_male.name)

# Let's update our data
lorenzo = american_male
lorenzo.hometown = 'Nazareth'
session.commit()

# Let's delete some data

session.delete(lorenzo)
session.commit()
