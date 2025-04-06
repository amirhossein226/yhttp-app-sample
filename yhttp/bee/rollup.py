from yhttp.core import Application
from yhttp.ext import sqlalchemy as saext, dbmanager
from .models import Base
from .cli.insert_mockup import InsertMockData

app = Application()


# Add builtin settings here
app.settings.merge('''
db:
  url: postgresql://postgres:postgres@localhost/bee

auth:
  redis:
    host: localhost
    port: 6379
    db: 0

  token:
    algorithm: HS256
    secret: foobar

  refresh:
    key: yhttp-refresh-token
    algorithm: HS256
    secret: quxquux
    secure: true
    httponly: true
    maxage: 2592000  # 1 Month
    domain: example.com
''')

dbmanager.install(app, cliarguments=[
    InsertMockData
])

saext.install(app, Base)


@app.when
def ready(app):
    from . import __version__
    app.version = __version__


# http handlers
from . import handlers
