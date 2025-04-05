from bddrest import status, response, when


def test_get_contact(Given, mockup):
    with Given('/contacts/', 'GET'):
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
