from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, select

import datetime as dt


class DuplicateObjectError(Exception):
    pass


class ObjectNotFound(Exception):
    pass


class Base(DeclarativeBase):
    pass


def to_dict(self):
    exclude_ = [
        'id',
        'created_at',
        'updated_at'
    ]
    data = dict()
    for column in self.__table__.columns:
        if column.name not in exclude_:
            data[column.name] = getattr(self, column.name)
    return data


Base.to_dict = to_dict


class Contacts(Base):
    __tablename__ = 'contacts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    email: Mapped[str] = mapped_column(String(254))
    phone: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now(dt.UTC))
    updated_at: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now(dt.UTC))

    @classmethod
    def create(cls, name, email, phone):
        from .rollup import app
        with app.db.session() as session:
            contact = session.scalar(select(cls).where(cls.name == name))

            if contact:
                raise DuplicateObjectError(
                    f'The object with name `{name}` already exists!'
                )

            else:
                contact = cls(
                    name=name,
                    email=email,
                    phone=phone
                )
                session.add(contact)
                session.commit()

                return contact.to_dict()

    @classmethod
    def update(cls, id, **data):
        from .rollup import app

        with app.db.session() as session:
            contact = session.get(cls, id)
            if not contact:
                raise ObjectNotFound('Object not exists!')

            if data.get('name'):
                conflict_contact = session.scalar(
                    select(cls)
                    .where(cls.id != id)
                    .where(cls.name == data['name'])
                )

                if conflict_contact:
                    raise DuplicateObjectError(
                        f'The object with name \
`{data["name"]}` already exists!'
                    )
            contact.name = data.get('name') or contact.name
            contact.email = data.get('email') or contact.email
            contact.phone = data.get('phone') or contact.phone
            session.commit()

            return contact.to_dict()

    @classmethod
    def delete(cls, id):
        from .rollup import app

        with app.db.session() as session:

            obj_to_delete = session.get(cls, id)
            print(obj_to_delete, '+++++++++++++++++++++++++++++++++++++++++++')
            if not obj_to_delete:
                raise ObjectNotFound

            session.delete(obj_to_delete)
            session.commit()
