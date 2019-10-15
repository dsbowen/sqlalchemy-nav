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
Brand(bar=bar, url='/', label='dsbowen.github.io')
Navitem(bar=bar, url='/about', label='About')
item = Navitem(bar=bar, label='Projects')
Dropdownitem(item=item, url='/flask-worker', label='Flask-Worker')
Dropdownitem(item=item, url='/sqlalchemy-mutable', label='SQLAlchemy-Mutable')
Dropdownitem(item=item, url='/sqlalchemy-nav', label='SQLAlchemy-Nav')
bar.classes.remove('navbar-dark')
bar.classes.remove('bg-dark')
bar.classes.append('navbar-light')
bar.classes.append('bg-light')
bar.custom_html = """
<form class="form-inline">
    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
</form>
"""
bar.view_html()