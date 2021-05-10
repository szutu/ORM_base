import base
from sqlalchemy.orm import sessionmaker
# Creating new sesssion
Session = sessionmaker(bind=base.engine)
session = Session()

# adding records
for i in range(3, 4):
    # inv is an instance of Investors class
    inv = base.Investors(i, "Jack", "Kowalski", 1000)
    #adding to a session next instances of Investors
    session.add(inv)

opr = base.Operations(2, '2010-12-11', 'Google', 150)
session.add(opr)
# save above changes in database
session.commit()



