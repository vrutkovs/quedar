from sqlalchemy_aio import ASYNCIO_STRATEGY
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, DateTime, Boolean
)

engine = create_engine(
    # In-memory sqlite database cannot be accessed from different
    # threads, use file.
    app.config['dsn'], strategy=ASYNCIO_STRATEGY
)

group = Table(
    'group', meta,

    Column('id', Integer, primary_key=True),
    Column('name', String(200), nullable=False),
    Column('description', String(600)),
    Column('country', String(20)),
    Column('city', String(60)),
    Column('creator',
           Integer,
           ForeignKey('user.id', ondelete='CASCADE', nullable=False)),
)

group_org = Table(
    'group_org', meta,

    Column('id', Integer, primary_key=True),
    Column('group',
           Integer,
           ForeignKey('group.id', nullable=False)),
    Column('user',
           Integer,
           ForeignKey('user.id', nullable=False)),
)

user = Table(
    'user', meta,

    Column('id', Integer, primary_key=True),
    Column('name', String(16), nullable=False),
    Column('password', String(20), nullable=False),
    Column('email_address', String(60)),
)

event = Table(
    'event', meta,

    Column('id', Integer, primary_key=True),
    Column('group',
           Integer,
           ForeignKey('group.id', ondelete='CASCADE', nullable=False)),
    Column('creator',
           Integer,
           ForeignKey('user.id', ondelete='CASCADE', nullable=False)),
    Column('name', String(20), nullable=False),
    Column('description', String(60)),
    Column('location', String(60), nullable=False),
    Column('starts_at', DateTime()),
    Column('ends_at', DateTime()),
)

attendee = Table(
    'attendee', meta,

    Column('id', Integer, primary_key=True),
    Column('user',
           Integer,
           ForeignKey('user.id', ondelete='CASCADE', nullable=False)),
    Column('event',
           Integer,
           ForeignKey('event.id', ondelete='CASCADE', nullable=False)),
    Column('rsvped_on', DateTime()),
    Column('rsvp_status', Boolean()),
)

async def init_engine(app):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[group, group_org, user, event, attendee])
    return engine
