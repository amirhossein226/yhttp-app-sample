from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, select

import datetime as dt


class DuplicateObjectError(Exception):
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
    phone:  Mapped[str] = mapped_column(String(20))
    created_at: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now(dt.UTC))
    updated_at: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now(dt.UTC))

    @classmethod
    def create(cls, name, email, phone, overwrite=False):
        from .rollup import app
        with app.db.session() as session:
            contact = session.scalar(select(cls).where(cls.name == name))
            if not contact:
                contact = cls(
                    name=name,
                    email=email,
                    phone=phone
                )
                session.add(contact)
                session.commit()

            elif not overwrite:
                raise DuplicateObjectError(
                    f'The object already exists: {name}'
                )

            else:
                contact.name = name
                contact.email = email
                contact.phone = phone
                session.commit()
            return contact.to_dict()
