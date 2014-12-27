#http://stackoverflow.com/questions/9766940/how-to-create-an-sql-view-with-sqlalchemy
# from stephan on stackoverflow
# custom view implementation in sqlalchemy

from sqlalchemy import Table
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Executable, ClauseElement

class CreateView(Executable, ClauseElement):
    def __init__(self, name, select):
        self.name = name
        self.select = select

@compiles(CreateView)
def visit_create_view(element, compiler, **kw):
    return "CREATE VIEW %s AS %s" % (
         element.name,
         compiler.process(element.select, literal_binds=True)
         )

# test data
from sqlalchemy import MetaData, Column, Integer
from sqlalchemy.engine import create_engine
engine = create_engine('sqlite://')
metadata = MetaData(engine)
t = Table('t',
          metadata,
          Column('id', Integer, primary_key=True),
          Column('number', Integer))
t.create()
engine.execute(t.insert().values(id=1, number=3))
engine.execute(t.insert().values(id=9, number=-3))

# create view
createview = CreateView('viewname', t.select().where(t.c.id>5))
engine.execute(createview)

# reflect view and print result
v = Table('viewname', metadata, autoload=True)
for r in engine.execute(v.select()):
    print r