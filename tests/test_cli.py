from bddcli import Application as CLIApplication, Given, stdout, stderr, status, when

def test_custom_cli_command():
    cliapp = CLIApplication('bee', 'yhttp.bee:app.climain')

    with Given(cliapp, 'db --help'):
        print(f"db --help: status={status}, stdout='{stdout}'")
        assert status == 0

        when('db drop')
        print(f"db drop: status={status}, stdout='{stdout}', stderr='{stderr}'")

        when('db create')
        print(f"db create: status={status}, stdout='{stdout}', stderr='{stderr}'")
        assert status == 0
        assert stdout == ''

        when('db objects create')
        print(f"db objects create: status={status}, stdout='{stdout}', stderr='{stderr}'")
        assert status == 0
        assert stdout != ''

        when('db insert-mockup')
        print(f"db insert-mockup: status={status}, stdout='{stdout}', stderr='{stderr}'")
        assert status == 0
        assert stdout == ''
