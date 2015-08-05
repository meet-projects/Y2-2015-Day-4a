Start by opening a terminal. Type the following commands:

    cd Desktop
    git clone https://github.com/meet-projects/Y2-2015-Day-4a
    cd Y2-2015-Day-4a

Now, set up Python. Here's what you run the first time after you log in:

    exec bash
    wget http://tinyurl.com/MEETpython
    source MEETpython

If you have already run the code above but you've opened a new terminal window,
please run:

    exec bash
    source ~/y2-venv/bin/activate

Now, set up the database. *Warning: if you already have people in the
database, this command will delete all of them and reset it to Lorenzo,
Michele, Omri, and Mustafa.* You can use this any time if you mess up the
database or add too many people.

    python initialize.py

For this lab, you'll write your code either interactively in Python, or in
`add_to_database.py`. When working interactively, copy-paste in the code at
the top of `add_to_database.py`

#### Exercise 1: Create
Write code in `add_to_database.py` to add you and your partner to the database.
Make sure that you have six entries (Lorenzo, Michele, Omri, Mustafa, and the
two of you) by using `session.query(Person).all()`.

#### Exercise 2: Read
First, *at the Python shell*, write code to find Mustafa in the database and print
his hometown.

Then, write a function `find_nationality` in `add_to_database.py` that takes a
nationality and returns a list of names of people in the database with that
nationality. For example, right now `find_nationality('American')`
should return `['Lorenzo Brown', 'Michele Pratusevich']` (the order doesn't
matter). Your code should start like this:

    def find_nationality(nat):

Make sure your code works with `find_nationality('Israeli')` and
`find_nationality('Palestinian')` too. If your results don't have you
and your partner, then make sure you have the right spelling
and capitalization.

#### Exercise 3: Update
Suppose Michele moves from Boston to Jerusalem. *At the Python shell*, update
her location in the database.

#### Exercise 4: Delete
*At the Python shell*, remove all the instructors and staff from the database
so that only students and TAs are left.

