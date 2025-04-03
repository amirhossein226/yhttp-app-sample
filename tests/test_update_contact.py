from bddrest import given, response, status


def test_update_contact(Given, mockup):

    data = {
        'name': 'Milad',
        'email': 'milad11@gmail.com',
        'phone': '0912 222 2222'
    }

    with Given('/contact/1', verb='PUT', form=data):
        pass
