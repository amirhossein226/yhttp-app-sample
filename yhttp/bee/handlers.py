from yhttp.core import json, text, statuscode, statuses, guard as g
from .models import Contacts, DuplicateObjectError, ObjectNotFound
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
        )
        return contact

    except DuplicateObjectError:
        raise statuses.conflict()

    return contact


@app.route(r'/contacts/(\d+)?')
@json
@statuscode(statuses.ok)
def update(req, contact_id):
    with app.db.session() as session:
        c = session.get(Contacts, int(contact_id))

    if not c:
        return statuses.notfound()
    data = req.getform()

    try:
        contact = Contacts.update(
            id=int(contact_id),
            **data
        )
    except DuplicateObjectError:
        raise statuses.status(
            409, f'The object with name {data["name"]} already exists!'
        )

    return contact


@app.route(r'/contacts/(\d+)?')
@text
@statuscode(statuses.nocontent)
def delete(req, contact_id):
    try:
        Contacts.delete(int(contact_id))
    except ObjectNotFound:
        raise statuses.notfound()
