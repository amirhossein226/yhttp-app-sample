from bddrest import response, status, when, given


def test_update_contact(Given, mockup):

    data = {
        'name': 'Milad',
        'email': 'milad11@gmail.com',
        'phone': '0912 222 2222'
    }

    with Given('/contacts/2', verb='update', form=data):
        assert status == 404

        mockup()
        when()
        assert status == 200
        assert response.json == {
            'name': 'Milad',
            'email': 'milad11@gmail.com',
            'phone': '0912 222 2222'
        }

        when(form = given - 'name')
        assert status == 200

    with Given('/contacts/1', verb='update', form=data):
        assert status == '409 The object with name Milad already exists!'
