"""
setup.py: Scripts to run to set up our database
"""

from datetime import datetime
from model import db, User, Task
from passlib.hash import pbkdf2_sha256


# Create the database tables for our model
db.connect()
db.drop_tables([User, Task])
db.create_tables([User, Task])


User(name="admin", password=pbkdf2_sha256.hash("password")).save()
User(name="bob", password=pbkdf2_sha256.hash("bobbob")).save()

Task(name="Do the laundry.").save()
Task(name="Do the dishes.", performed=datetime.now()).save()