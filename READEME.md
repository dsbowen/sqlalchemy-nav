# SQLAlchemy-Nav

SQLAlchemy-Nav provied [SQLAlchemy Mixins](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html) for creating navigation bars compatible with [Bootstrap](https://getbootstrap.com/docs/4.3/components/navbar/). Its Mixins are:

1. NavbarMixin for creating navigation bars
2. BrandMixin for adding a brand to the navbar
3. NavitemMixin for adding navitems to the navbar
4. DropdownitemMixin for adding dropdownitems to navitems

## License

Publications which use this software should include the following citations:

Bowen, D.S. (2019). SQLAlchemy-Nav \[Computer software\]. [https://github.com/dsbowen/sqlalchemy-nav](https://github.com/dsbowen/sqlalchemy-nav)

Bowen, D.S. (2019). SQLAlchemy-Mutable \[Computer software\]. [https://github.com/dsbowen/sqlalchemy-mutable](https://github.com/dsbowen/sqlalchemy-mutable)

This project is licensed under the MIT License [LICENSE](https://github.com/dsbowen/sqlalchemy-nav/blob/master/LICENSE).

## Getting started

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart):

```
$ pip install -U sqlalchemy-nav
```

### Setup

The following code will get you started with SQLAlchemy-Nav as quickly as possible:

```python
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
```

Outputs:

<html>
<head>
<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
</head>

<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
 <a class="navbar-brand" href="/my-brand">
  My Brand
 </a>
 <button aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#navbarSupportedContent" data-toggle="collapse" type="button">
  <span class="navbar-toggler-icon">
  </span>
 </button>
 <div class="collapse navbar-collapse" id="navbarSupportedContent">
  <ul class="navbar-nav mr-auto">
   <li class="nav-item">
    <a class="nav-link" href="/my-navitem">
     My Navitem
    </a>
   </li>
   <li class="nav-item">
    <a aria-expanded="false" aria-haspopup="true" class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" id="navbarDropdownNone" role="button">
     Dropdown
    </a>
    <div aria-labelledby="navbarDropdownNone" class="dropdown-menu">
     <a class="dropdown-item" href="/dropdown1">
      Dropdownitem 1
     </a>
     <a class="dropdown-item" href="/dropdown2">
      Dropdownitem 2
     </a>
    </div>
   </li>
  </ul>
 </div>
</nav>
</body>
</html>