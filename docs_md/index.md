# SQLAlchemy-Nav

SQLAlchemy-Nav makes it easy to create and customize dynamic [Bootstrap 4 Navbars](https://getbootstrap.com/docs/4.5/components/navbar/) for web apps with a [SQLAlchemy](https://sqlalchemy.org) backend.

## Why SQLAlchemy-Nav

Unlike static Navbars, SQLAlchemy-Nav can create personalized Navbars for your users.

## Installation

```
$ pip install sqlalchemy-nav
```

## Quickstart

Run the following setup code.

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

Create and render a Navbar:

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

## Citation

```
@software{bowen2020sqlalchemy-nav,
  author = {Dillon Bowen},
  title = {SQLAlchemy-Nav},
  url = {https://dsbowen.github.io/sqlalchemy-nav/},
  date = {2020-06-10},
}
```

## License

Users must cite this package in any publications which use it.

It is licensed with the MIT [License](https://github.com/dsbowen/sqlalchemy-nav/blob/master/LICENSE).