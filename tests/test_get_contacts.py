from bddrest import status, response, when

from yhttp.bee.models import Contacts
from yhttp.bee import app


def test_get_contact(Given):

    def mockup():
        with app.db.session() as session:
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

    with Given('/contacts', 'GET'):
        assert status == 200
        assert response.json == []

        mockup()
        when()
        assert status == 200
        assert len(response.json) == 3
        assert response.json == [
            {
                'name': 'David',
                'email': 'david@gmail.com',
                'phone': '+09 453 3344'
            },
            {
                'name': 'Milad',
                'email': 'milad@gmail.com',
                'phone': '+98 912 222 3434'
            },
            {
                'name': 'Niki',
                'email': 'niki@gmail.com',
                'phone': '+74 98982333'
            }
        ]
    with Given('/contacts/1', 'GET'):
        assert status == 200
        assert response.json == {
            'name': 'David',
            'email': 'david@gmail.com',
            'phone': '+09 453 3344'
        }
        when('/contacts/2')
        assert status == 200
        assert response.json == {
            'name': 'Milad',
            'email': 'milad@gmail.com',
            'phone': '+98 912 222 3434'
        }

        when('/contacts/a22s')
        assert status == 404

        when('/contacts/22')
        assert status == 404
