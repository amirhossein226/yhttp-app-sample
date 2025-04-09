from bddcli import Application as CLIApplication, Given,\
    stdout, stderr, status, when
from sqlalchemy import select
import json


def test_custom_cli_command():
    cliapp = CLIApplication('bee', 'yhttp.bee:app.climain')

    with Given(cliapp, 'db --help'):
        assert status == 0

        when('db drop')
        when('db create')
        assert status == 0
        assert stdout == ''

        when('db objects create')
        assert status == 0
        assert stdout != ''

        from yhttp.bee.basedata import BASE_DATA
        when('db insert-mockup')
        assert status == 0
        assert stdout != ''

        inserted_content = json.loads(str(stdout))
        assert len(inserted_content) == len(BASE_DATA)

        for expected, actual in zip(BASE_DATA, inserted_content):
            assert expected['name'] == actual['name']
            assert expected['email'] == actual['email']
            assert expected['phone'] == actual['phone']

