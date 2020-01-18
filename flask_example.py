"""Flask example

This toy example uses SQLAlchemy-Nav to create a dynamic navigation bar. 

We begin with a standard setup, then create the `Navbar` instance before 
the first app request. I name the navigation bar so that we can find it 
later using `query.filter_by(name='name')`. Finally, we use the navbar to 
keep a tally of how many times each link on the dropdown menu was visited.
"""

# 1. Import Mixins from sqlalchemy_nav
from sqlalchemy_nav import NavbarMixin, NavitemMixin, DropdownitemMixin

# 2. Import Flask classes, methods, and extensions and initialize app
from flask import Flask, Markup, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 3. Use the SQLAlchemy-Nav Mixins to create database models
class Navbar(NavbarMixin, db.Model):
    def render(self):
        return Markup(str(super().render()))

class Navitem(NavitemMixin, db.Model):
    pass

class Dropdownitem(DropdownitemMixin, db.Model):
    pass

# 4. Create a Navbar instance before the first app request
@app.before_first_request
def before_first_request():
    db.create_all()
    navbar = Navbar(name='my-navbar', label='Home', href='https://dsbowen.github.io')
    navbar.body.select_one('nav')['class'].remove('fixed-top')
    Navitem(navbar, label='Index ', href='/')
    navitem = Navitem(navbar, label='Pages', dropdown=True)
    Dropdownitem(navitem, label='Page 1 ', href='/page1')
    Dropdownitem(navitem, label='Page 2 ', href='/page2')
    db.session.add(navbar)
    db.session.commit()
    
@app.route('/')
def index():
    # 5. Recover the Navbar instance by name
    navbar = Navbar.query.filter_by(name='my-navbar').first()
    # 6. Tally visits to the index route
    index_item = navbar.navitems[0]
    index_item.label = index_item.label + 'x'
    db.session.commit()
    # 7. Pass the Navbar instance to the html template
    return render_template('index.html', navbar=navbar, content='Index page')

@app.route('/page1')
def page1():
    navbar = Navbar.query.filter_by(name='my-navbar').first()
    page1_item = navbar.navitems[1].dropdownitems[0]
    page1_item.label = page1_item.label + 'x'
    db.session.commit()
    return render_template('index.html', navbar=navbar, content='Page 1')

@app.route('/page2')
def page2():
    navbar = Navbar.query.filter_by(name='my-navbar').first()
    page2_item = navbar.navitems[1].dropdownitems[1]
    page2_item.label = page2_item.label + 'x'
    db.session.commit()
    return render_template('index.html', navbar=navbar, content='Page 2')

if __name__ == '__main__':
    app.run(debug=True)