"""Flask example

This toy example uses SQLAlchemy-Nav to create a dynamic navigation bar. We 
begin by creating the navigation bar instance before the first app request. 
I name the navigation bar so that we can find it later using 
query.filter_by(name='name').

We then use the navbar to keep a tally of how many times each link on the 
dropdown menu was visited.
"""

from sqlalchemy_nav import BrandMixin, DropdownitemMixin, NavbarMixin, NavitemMixin

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class Navbar(NavbarMixin, db.Model):
    pass

class Brand(BrandMixin, db.Model):
    pass

class Navitem(NavitemMixin, db.Model):
    pass

class Dropdownitem(DropdownitemMixin, db.Model):
    pass

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
    bar = Navbar.query.filter_by(name='my navbar').first()
    bar.navitems[0].label += 'x'
    db.session.commit()
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