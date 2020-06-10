"""# API"""

from flask import request
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import backref, relationship
from sqlalchemy_modelid import ModelIdBase
from sqlalchemy_mutablesoup import MutableSoupType
from sqlalchemy_orderingitem import OrderingItem

import os


class Base(OrderingItem, ModelIdBase):
    """
    All SQLAlchemy-Nav mixins inherit from this base.

    Parameters
    ----------
    template : str
        Relative path to the html template file. Users should not pass this 
        argument; it is passed automatically by mixins.

    label : str
        Label (text) of the first `<a>` tag.

    href : str
        Hyperref of the first `<a>` tag.

    Attributes
    ----------
    id : int
        Model identifier.

    index : int
        Order of the model in its parent's list. e.g. the 0th `Navitem` in a 
        `Navbar` has an `index` of 0.

    body : sqlalchemy_mutablesoup.MutableSoup
        The body of the object. This is converted to html when the object is 
        rendered.

    a : bs4.Tag
        First `<a>` html tag in `body`.

    label : str
        Text of `a`. Set from the `label` parameter.

    href : str
        Hyperref of `a`. Set from the `href` parameter.
    """
    id = Column(Integer, primary_key=True)
    index = Column(Integer)
    body = Column(MutableSoupType)

    def __init__(self, template, label=None, href=None, *args, **kwargs):
        path = os.path.dirname(os.path.realpath(__file__))
        self.body = open(os.path.join(path, template)).read()
        self.label = label
        self.href = href
        super().__init__(*args, **kwargs)

    @property
    def a(self):
        return self.body.select_one('a')

    @property
    def label(self):
        return self.a.text

    @label.setter
    def label(self, val):
        self.body.set_element('a', val)

    @property
    def href(self):
        return self.a.attrs.get('href')

    @href.setter
    def href(self, val):
        self.a['href'] = val
        self.body.changed()
    
    def is_active(self):
        """        
        Returns
        -------
        is_active : bool
            Indicates that the object's href is active.
        """
        try:
            return self.href == str(request.url_rule)
        except: # Exception will occur outside app context
            return False

    def render(self, body=None):
        """
        Prepares a `bs4.BeautifulSoup` object for rendering into html.

        Parameters
        ----------
        body : sqlalchemy_mutablesoup.MutableSoup or None, default=None
            Object to render. If `None`, a copy of `self.body` is used.

        Returns
        -------
        body : sqlalchemy_mutablesoup.MutableSoup
            Prepared for rendering into html.
        """
        return self._render(body)


class NavbarMixin(Base):
    """
    Navigation bar mixin.

    Parameters
    ----------
    name : str
        Name of the navigation bar. This facilitates finding the navigation 
        bar when querying the database.

    \*args, \*\*kwargs :
        Additional arguments and keyword arguments are passed to 
        `Base.__init__`.

    Attributes
    ----------
    name : str
        Set from the `name` parameter.

    navitems : sqlalchemy.ext.orderinglist.OrderingList
        List of `Navitem` objects ordered by `index`.
    """
    name = Column(String)

    @declared_attr
    def navitems(cls):
        return relationship(
            'Navitem',
            backref='navbar',
            order_by='Navitem.index',
            collection_class=ordering_list('index')
        )

    def __init__(self, name=None, *args, **kwargs):
        self.name = name
        super().__init__('navbar.html', *args, **kwargs)
    
    def _render(self, body=None):
        body = body or self.body.copy()
        btn = body.select_one('button.navbar-toggler')
        btn['data-target'] = '#'+self.model_id
        btn['aria-controls'] = self.model_id
        body.select_one('div.navbar-collapse')['id'] = self.model_id
        ul = body.select_one('ul')
        [ul.append(item.render()) for item in self.navitems]
        return body


class NavitemMixin(Base):
    """
    Navigation item mixin.

    Parameters
    ----------
    navbar : sqlalchemy_nav.NavbarMixin or None, default=None
        Navigation bar with which this navigation item is associated.

    dropdown : bool, default=False
        Indicates that this navitem will contain dropdown items.

    \*args, \*\*kwargs : :
        Additional arguments and keyword arguments are passed to `Base.__init__`.

    Attributes
    ----------
    navbar : sqlalchemy_nav.NavbarMixin or None
        Set from the `navbar` parameter.

    dropdownitems : sqlalchemy.ext.orderinglist.OrderingList
        List of `Dropdownitem` objects ordered by `index`.
    """
    @declared_attr
    def _navbar_id(self):
        return Column(ForeignKey('navbar.id'))

    @declared_attr
    def dropdownitems(cls):
        return relationship(
            'Dropdownitem',
            backref='navitem',
            order_by='Dropdownitem.index',
            collection_class=ordering_list('index')
        )

    def __init__(self, navbar=None, dropdown=False, *args, **kwargs):
        self.navbar = navbar
        template = 'navitemdropdown.html' if dropdown else 'navitem.html'
        super().__init__(template, *args, **kwargs)  

    def _render(self, body=None):
        body = body or self.body.copy()
        if self.is_active(): # add 'active' class to `a` Tag
            li = body.select_one('li')
            if li.attrs.get('class') is None:
                li['class'] = []
            body.select_one('li')['class'].append('active')
        if self.dropdownitems:
            body.select_one('a')['id'] = self.model_id
            div = body.select_one('.dropdown-menu')
            div['aria-labelledby'] = self.model_id
            [div.append(item.render()) for item in self.dropdownitems]
        return body


class DropdownitemMixin(Base):
    """
    Dropdown item mixin.

    Parameters
    ----------
    navitem : sqlalchemy_nav.NavitemMixin or None, default=None
        Navigation item with which this dropdown item is associated.

    \*args, \*\*kwargs : :
        Additional arguments and keyword arguments are passed to 
        `Base.__init__`.

    Attributes
    ----------
    navitem : sqlalchemy_nav.NavitemMixin or None
        Set from the `navitem` parameter.
    """
    @declared_attr
    def _navitem_id(cls):
        return Column(Integer, ForeignKey('navitem.id'))

    def __init__(self, navitem=None, *args, **kwargs):
        self.navitem = navitem
        super().__init__('dropdownitem.html', *args, **kwargs)    

    def _render(self, body=None):
        body = body or self.body.copy()
        if self.is_active(): # add 'active' class to `a` Tag
            a = body.select_one('a')
            if a.attrs.get('class') is None:
                a['class'] = []
            body.select_one('a')['class'].append('active')
        return body