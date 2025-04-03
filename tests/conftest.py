import functools
from yhttp.dev.fixtures import freshdb, cicd

import pytest
import bddrest

from yhttp import bee
from yhttp.bee.models import Contacts

@pytest.fixture
def mockup():
    with bee.app.db.session() as session:
        contacts = [
            Contacts(
                name='David',
                email='david@gmail.com',
                phone='+09 453 3344'
            ),
            Contacts(
                name='Milad',
                email='milad@gmail.com',
                phone='+98 912 222 3434'
            ),
            Contacts(
                name='Niki',
                email='niki@gmail.com',
                phone='+74 98982333'
            )
        ]
        session.add_all(contacts)
        session.commit()


@pytest.fixture
def Given(freshdb):

    bee.app.settings.merge(f'''
      db:
        url: {freshdb}
    ''')
    bee.app.ready()
    bee.app.db.create_objects()
    yield functools.partial(bddrest.Given, bee.app)
    bee.app.shutdown()
