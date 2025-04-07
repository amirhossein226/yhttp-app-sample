from bddrest import response, status, when


def test_delete_contact(Given, mockup):
    with Given('/contacts/1', verb='delete'):
        assert status == 404

        mockup()
        when()
        assert status == 204

        when(verb='get')
        assert status == 404

    with Given('/contacts/', verb='get'):
        assert status == 200
        assert len(response.json) == 2

    with Given('/contacts/', verb='delete'):
        assert status == 400
