Open up the `crud.py` file. Notice the `import` statements at the top involving
`sqlalchemy`. You'll need to add these to any file you make that uses
SQLAlchemy.

#### Exercise 1: Create
Write code in `crud.py` to add you and your partner to the database. Make
sure that you have five entries (Lorenzo, Michele, Omri, and the two of you)
by using `session.query(Person).all()`.

#### Exercise 2: Read
Write a function `find_nationality` in `crud.py` that takes a nationality
and returns a list of names of people in the database with that nationality.
For example, right now `find_people_with_nationality('American')` should
return `['Lorenzo', 'Michele']` (the order doesn't matter). Your code should
start like this:

    def find_nationality(nat):

#### Exercise 3: Update
Suppose Michele moves from Boston to Jerusalem. Update her location in the
database.

#### Exercise 4: Delete
Remove all the instructors from the database so that only students and TAs
are left.

