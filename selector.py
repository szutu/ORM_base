import base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=base.engine)
session = Session()

# show table Operations
for s in session.query(base.Operations).all():
    print(s.operation_id)

# show selected records from table Operations
for s in session.query(base.Operations).filter(base.Operations.operation_id > 5):
    print(s.operation_id)


def updater():

    # table updater
    id = input('Write ID of investor who is about to change: ')
    x = session.query(base.Investors).get(id)
    if x in [None]:
        raise ValueError("Given id doesn't exist ")
    print('name: '+x.name, ' surname:: '+x.surname, ' capital: '+str(x.capital))
    x.name = input('Type name: ')
    x.surname = input('Type surname: ')
    x.capital = int(input('Type capital: '))
    session.commit()
    print('Updated data : \n'+'name: ' + x.name, 'surname: ' + x.surname, 'capital: ' + str(x.capital))


if __name__ == "__main__":
    updater()
