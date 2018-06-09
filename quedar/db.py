from sqlalchemy_aio import ASYNCIO_STRATEGY
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, DateTime, Boolean,
    create_engine
)
from datetime import datetime

meta = MetaData()

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

async def init_db(app):
    engine = create_engine(
        # In-memory sqlite database cannot be accessed from different
        # threads, use file.
        app.config['dsn'], strategy=ASYNCIO_STRATEGY
    )
    meta.create_all(bind=engine, tables=[user, group, group_org, event, attendee])
    app['engine'] = engine

async def sample_data(engine):
    conn = await engine.connect()
    await conn.execute(user.insert().values(
        name='Test user',
        password='password',
        email_address='someone@example.com',
    ))
    await conn.execute(group.insert().values(
        name='Test group',
        description='Test group description',
        country='Czech Republic',
        city='Brno',
        creator=1,
    ))
    await conn.execute(group_org.insert().values(
        group=1,
        user=1,
    ))
    await conn.execute(event.insert().values(
        group=1,
        creator=1,
        name="Test event",
        description="Test description",
        location="The Place",
        starts_at=datetime(1,1,1,1,1,0),
        ends_at=datetime(1,1,1,1,30,0),
    ))
    await conn.execute(attendee.insert().values(
        user=1,
        event=1,
        rsvped_on=datetime(1,1,1,0,1,0),
        rsvp_status=True,
    ))

    await conn.close()
