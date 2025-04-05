from bddrest import response, status, when, given


def test_create_contact(Given):
    data = {
        'name': 'Amir',
        'email': 'amir@gmail.com',
        'phone': '09199199191'
    }

    with Given('/contacts', verb='CREATE', form=data):
        assert status == 201
        assert response.json == {
            'name': 'Amir',
            'email': 'amir@gmail.com',
            'phone': '09199199191'
        }

        when()
        assert status == 409

        when(form=given - 'name')
        assert status == '400 name: Required'

        when(form=given - 'email')
        assert status == '400 email: Required'

        when(form=given - 'phone')
        assert status == '400 phone: Required'

        when(form={})
        assert status == '400 name: Required'

    with Given('/contacts', verb='CREATE', form=data):
        assert status == 409

    with Given('/contacts/', verb='CREATE', form=data):
        assert status == 404
