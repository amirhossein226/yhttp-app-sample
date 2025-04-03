from yhttp.core import json, statuscode, statuses, guard as g
from .models import Contacts, DuplicateObjectError
from .rollup import app

from sqlalchemy import select


@app.route(r'/contacts/(\d+)?')
@json
@statuscode(statuses.ok)
def get(req, contact_id=None):

    with app.db.session() as session:
        if contact_id:
            contact_id = int(contact_id)
            contact = session.get(Contacts, contact_id)

            if not contact:
                raise statuses.notfound()

            return contact.to_dict()

        else:
            result = []
            query_ = session.scalars(select(Contacts)).all()
            for c in query_:
                result.append(c.to_dict())
            return result


@app.route(r'/contacts')
@app.bodyguard(strict=False, fields=(
    g.String('name', length=(1, 100)),
    g.String('email', length=(1, 254)),
    g.String('phone',
             length=(1, 20),
             pattern=r'^(\+98|0098|0)?[ -]?(9\d{2})[ -]?\d{3}[ -]?\d{4}$')))
@json
@statuscode(statuses.created)
def create(req):
    data = req.getform()

    try:
        contact = Contacts.create(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            overwrite=False
        )
        return contact

    except DuplicateObjectError:
        raise statuses.conflict()

    return {'message': 'something went wrong'}
