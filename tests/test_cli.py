from bddcli import Application as CLIApplication, Given, stdout, status, when


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

        when('db insert-mockup')
        assert status == 0
        assert stdout == ''
