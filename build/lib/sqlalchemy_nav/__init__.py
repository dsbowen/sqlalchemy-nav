"""Mixins for SQLAlchemy-Nav

SQLAlchemy-Nav Mixins can be used to create dynamic navigation bar models 
compatible with Bootstrap 4. Navigation bars can contain navigation 
items, dropdown items, and custom html.

All models store their HTML in a `MutableSoup` attribute, `body`. This is 
essentially a `BeautifulSoup` object which you can use to insert custom 
HTML.

`Navitem`s are nested in `Navbar`s, and `Dropdownitem`s are nested in 
`Navitem`s.
"""

from sqlalchemy_nav.navbar import NavbarMixin
from sqlalchemy_nav.navitem import NavitemMixin
from sqlalchemy_nav.dropdownitem import DropdownitemMixin