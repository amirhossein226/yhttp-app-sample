import json
import easycli

from ..models import Contacts
from ..basedata import BASE_DATA


class InsertMockData(easycli.SubCommand):
    __command__ = 'insert-mockup'

    def __call__(self, args):
        from ..rollup import app
        app.db.connect()

        created_contacts = []
        with app.db.session() as session:
            for c in BASE_DATA:
                contact = Contacts(
                    name=c['name'],
                    email=c['email'],
                    phone=c['phone']
                )
                session.add(contact)
                created_contacts.append(contact.to_dict())
            session.commit()
            print(json.dumps(created_contacts, indent=2))
