"""Getting started with SQLAlchemy-Nav"""

# 1. Import classes from sqlalchemy_nav
from sqlalchemy_nav import BrandMixin, DropdownitemMixin, NavbarMixin, NavitemMixin

# 2. Standard session creation
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()
Base = declarative_base()

# 3. Use the SQLAlchemy-Nav Mixins to create database models
class Navbar(NavbarMixin, Base):
    __tablename__ = 'navbar'

class Brand(BrandMixin, Base):
    __tablename__ = 'brand'

class Navitem(NavitemMixin, Base):
    __tablename__ = 'navitem'
    
class Dropdownitem(DropdownitemMixin, Base):
    __tablename__ = 'dropdownitem'

# 4. Create the database
Base.metadata.create_all(engine)

"""Example"""

bar = Navbar()
Brand(bar=bar, url='/my-brand', label='My Brand')
Navitem(bar=bar, url='/my-navitem', label='My Navitem')
item = Navitem(bar=bar, label='Dropdown')
Dropdownitem(item=item, url='/dropdown1', label='Dropdownitem 1')
Dropdownitem(item=item, url='/dropdown2', label='Dropdownitem 2')
bar.view_html()