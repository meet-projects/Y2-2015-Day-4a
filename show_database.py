from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

if __name__ == '__main__':
    people = session.query(Person).all()

    columns = [str(c).split('.')[-1] for c in Person.__table__.columns]
    table = []
    for person in people:
        table.append([getattr(person, c) for c in columns])

    max_lengths = []

    for title, data in zip(columns, zip(*table)):
        max_lengths.append(max([len(repr(d)) for d in data]) + 2)
    row_format = ''.join(["{:>%d}" % length for length in max_lengths])

    print(row_format.format(*columns))
    print('-' * 15 * len(columns))
    for row in table:
        print(row_format.format(*row))
