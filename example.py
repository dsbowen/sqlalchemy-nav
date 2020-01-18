"""Getting started with SQLAlchemy-Nav"""

# 1. Import bases from sqlalchemy_nav
from sqlalchemy_nav import NavbarMixin, NavitemMixin, DropdownitemMixin

# 2. Standard session creation
from sqlalchemy import create_engine
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

class Navitem(NavitemMixin, Base):
    __tablename__ = 'navitem'
    
class Dropdownitem(DropdownitemMixin, Base):
    __tablename__ = 'dropdownitem'

# 4. Create the database
Base.metadata.create_all(engine)


print('\nExample 1: Basic use')
navbar = Navbar(label='Home', href='https://dsbowen.github.io')
# Navbars are fixed to the top by default; we remove it here for demonstration
navbar.body.select_one('nav')['class'].remove('fixed-top')
Navitem(navbar, label='About', href='/about')
navitem = Navitem(navbar, dropdown=True, label='Projects')
Dropdownitem(navitem, label='Flask-Worker', href='/flask-worker')
Dropdownitem(navitem, label='SQLAlchemy-Mutable', href='/sqlalchemy-mutable')
session.add(navbar)
session.commit()
print(navbar.render().prettify())


print('\nExample 2: Customization')

from bs4 import BeautifulSoup

searchbar_html = '''
<form class="form-inline">
    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
</form>
'''
searchbar = BeautifulSoup(searchbar_html, 'html.parser')
navbar.body.select_one('nav').append(searchbar)
navbar.body.changed() # See SQLAlchemy-MutableSoup for details
session.commit()
print(navbar.render().prettify())