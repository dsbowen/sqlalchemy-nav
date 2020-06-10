# Examples

View examples of [Bootstrap 4 Navbars](https://getbootstrap.com/docs/4.5/components/navbar/).

## Setup

Run the following setup to use with [SQLAlchemy](https://sqlalchemy.org).

```python
from sqlalchemy_nav import NavbarMixin, NavitemMixin, DropdownitemMixin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# session creation (standard)
engine = create_engine('sqlite:///:memory:')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()
Base = declarative_base()

# use the SQLAlchemy-Nav Mixins to create database models
class Navbar(NavbarMixin, Base):
    __tablename__ = 'navbar'

class Navitem(NavitemMixin, Base):
    __tablename__ = 'navitem'
    
class Dropdownitem(DropdownitemMixin, Base):
    __tablename__ = 'dropdownitem'

# create the database (standard)
Base.metadata.create_all(engine)
```

Alternatively, run the following setup to use with [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/).

```python
from sqlalchemy_nav import NavbarMixin, NavitemMixin, DropdownitemMixin

from flask import Flask, Markup, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

# create session (standard)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# use the SQLAlchemy-Nav Mixins to create database models
class Navbar(NavbarMixin, db.Model):
    pass

class Navitem(NavitemMixin, db.Model):
    pass

class Dropdownitem(DropdownitemMixin, db.Model):
    pass

# create the database (standard)
db.create_all()
session = db.session
```

## Basic use

```python
navbar = Navbar(label='Home', href='https://my-home-page')
Navitem(navbar, label='About', href='/about')
navitem = Navitem(navbar, dropdown=True, label='Dropdown')
Dropdownitem(navitem, label='Item0', href='/item0')
Dropdownitem(navitem, label='Item1', href='/item1')
session.add(navbar)
session.commit()
print(navbar.render().prettify())
```

Out:

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
 <a class="navbar-brand" href="https://my-home-page">
  Home
 </a>
 <button aria-controls="navbar-1" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#navbar-1" data-toggle="collapse" type="button">
  <span class="navbar-toggler-icon">
  </span>
 </button>
 <div class="collapse navbar-collapse" id="navbar-1">
  <ul class="navbar-nav mr-auto">
   <li class="nav-item">
    <a class="nav-link" href="/about">
     About
    </a>
   </li>
   <li class="nav-item dropdown">
    <a aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" href="" id="navitem-2" role="button">
     Dropdown
    </a>
    <div aria-labelledby="navitem-2" class="dropdown-menu">
     <a class="dropdown-item" href="/item0">
      Item0
     </a>
     <a class="dropdown-item" href="/item1">
      Item1
     </a>
    </div>
   </li>
  </ul>
 </div>
</nav>
```

## Customization

We can manipulate the [SQLAlchemy-MutableSoup](https://dsbowen.github.io/sqlalchemy-mutablesoup) object for further customization. In this example, we add a search bar.

```python
from bs4 import BeautifulSoup

navbar = Navbar(label='Home', href='https://my-home-page')
session.add(navbar)
session.commit()

searchbar_html = '''
<form class="form-inline">
    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
</form>
'''
searchbar = BeautifulSoup(searchbar_html, 'html.parser')
navbar.body.select_one('nav').append(searchbar)
navbar.body.changed()
print(navbar.render().prettify())
```

Out:

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
 <a class="navbar-brand" href="https://my-home-page">
  Home
 </a>
 <button aria-controls="navbar-2" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#navbar-2" data-toggle="collapse" type="button">
  <span class="navbar-toggler-icon">
  </span>
 </button>
 <div class="collapse navbar-collapse" id="navbar-2">
  <ul class="navbar-nav mr-auto">
  </ul>
 </div>
 <form class="form-inline">
  <input aria-label="Search" class="form-control mr-sm-2" placeholder="Search" type="search"/>
  <button class="btn btn-outline-success my-2 my-sm-0" type="submit">
   Search
  </button>
 </form>
</nav>
```