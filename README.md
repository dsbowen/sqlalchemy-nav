# SQLAlchemy-Nav

SQLAlchemy-Nav provides [SQLAlchemy Mixins](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html) for creating navigation bars compatible with [Bootstrap](https://getbootstrap.com/docs/4.3/components/navbar/). Its Mixins are:

1. ```NavbarMixin``` for creating navigation bars
2. ```BrandMixin``` for adding a brand to the navbar
3. ```NavitemMixin``` for adding nav-items to the navbar
4. ```DropdownitemMixin``` for adding dropdown-items to nav-items

## License

Publications which use this software should include the following citation for SQLAlchemy-Nav and its dependency, [SQLAlchemy-Mutable](https://pypi.org/project/sqlalchemy-mutable/):

Bowen, D.S. (2019). SQLAlchemy-Nav \[Computer software\]. [https://github.com/dsbowen/sqlalchemy-nav](https://github.com/dsbowen/sqlalchemy-nav)

Bowen, D.S. (2019). SQLAlchemy-Mutable \[Computer software\]. [https://github.com/dsbowen/sqlalchemy-mutable](https://github.com/dsbowen/sqlalchemy-mutable)

This project is licensed under the MIT License [LICENSE](https://github.com/dsbowen/sqlalchemy-nav/blob/master/LICENSE).

## Getting started

### Installation

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
```

## Examples

### Example 1. Use with SQLAlchemy

This example generates html for a Bootstrap Navbar using the SQLAlchemy setup above. You can find the full setup and example [here](https://github.com/dsbowen/sqlalchemy-nav/blob/master/example.py)

```python
bar = Navbar()
Brand(bar=bar, url='/my-brand', label='My Brand')
Navitem(bar=bar, url='/my-navitem', label='My Navitem')
item = Navitem(bar=bar, label='Dropdown')
Dropdownitem(item=item, url='/dropdown1', label='Dropdownitem 1')
Dropdownitem(item=item, url='/dropdown2', label='Dropdownitem 2')
bar.view_html()
```

Outputs:

```html
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
```

## Example 2: Toy web app with Flask-SQLAlchemy

This example shows how to use SQLAlchemy-Nav to create dynamic navigation bars in web apps. You can find the full setup and example [here](https://github.com/dsbowen/sqlalchemy-nav/blob/master/flask_example.py).

Our web app uses [Flask](http://flask.palletsprojects.com/en/1.1.x/), [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/), and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/).

### Python file

We begin by creating the ```Navbar``` instance before the first app request. I name the navigation bar so that we can find it later using ```query.filter_by(name='name')```. We then use the navbar to keep a tally of how many times each link on the dropdown menu was visited.
 
```python
# 1. Import Mixins from sqlalchemy_nav
from sqlalchemy_nav import BrandMixin, DropdownitemMixin, NavbarMixin, NavitemMixin

# 2. Import Flask classes, methods, and extensions and initialize app
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# 3. Use the SQLAlchemy-Nav Mixins to create database models
class Navbar(NavbarMixin, db.Model):
    pass

class Brand(BrandMixin, db.Model):
    pass

class Navitem(NavitemMixin, db.Model):
    pass

class Dropdownitem(DropdownitemMixin, db.Model):
    pass

# 4. Create a Navbar instance before the first app request
@app.before_first_request
def before_first_request():
    db.create_all()
    bar = Navbar(name='my navbar')
    Brand(bar=bar, label='SQLAlchemy-Nav')
    Navitem(bar=bar, url=url_for('index'), label='Index ')
    item = Navitem(bar=bar, label='Dropdown')
    Dropdownitem(item=item, url=url_for('page1'), label='Page 1 ')
    Dropdownitem(item=item, url=url_for('page2'), label='Page 2 ')
    db.session.add(bar)
    db.session.commit()
    
@app.route('/')
def index():
    # 5. Recover the Navbar instance by name
    bar = Navbar.query.filter_by(name='my navbar').first()
    # 6. Tally visits to the index route
    bar.navitems[0].label += 'x'
    db.session.commit()
    # 7. Pass the Navbar instance to the html template
    return render_template('index.html', bar=bar, content='Index page')

@app.route('/page1')
def page1():
    bar = Navbar.query.filter_by(name='my navbar').first()
    bar.navitems[1].dropdownitems[0].label += 'x'
    db.session.commit()
    return render_template('index.html', bar=bar, content='Page 1')

@app.route('/page2')
def page2():
    bar = Navbar.query.filter_by(name='my navbar').first()
    bar.navitems[1].dropdownitems[1].label += 'x'
    db.session.commit()
    return render_template('index.html', bar=bar, content='Page 2')

if __name__ == '__main__':
    app.run()
```

### Html template

Next, we create an ```index.html``` file in our templates folder. The index template must:
1. Extend the bootstrap base template.
2. Execute ```{{ bar.render() }}``` in the ```navbar``` block.

Recall that ```bar``` is the ```Navbar``` instance we passed to the index template in step 7.

```html
{% extends "bootstrap/base.html" %}

{% block navbar %}
{{ bar.render() }}
{% endblock %}

{% block content %}
<h3>{{ content }}</h3>
{% endblock %}
```

### View the example

To see this example at work, set your ```FLASK_APP``` environment variable to your Python file and run it.

Alternatively, you can clone the SQLAlchemy-Nav repo and run ```flask_example.py```.

```
$ git clone https://github.com/dsbowen/sqlalchemy-nav.git
$ cd sqlalchemy-nav
$ python flask_example.py
```

Then open ```http://localhost:5000``` in your browser.