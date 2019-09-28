"""Navbar Mixin

The Navbar Mixin contains a list of classes for the nav tag, a Brand, a list 
of Navitems, custom html, and a name. Custom html is inserted after the 
Navitems and may be used for search buttons or other miscellaneous 
functions. The Navbar name can be used with query.filter_by to retrieve a 
Navbar in different sessions.
"""

from .base import Base

from bs4 import BeautifulSoup
from flask import Markup
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import backref, relationship
from sqlalchemy_mutable import MutableListType

NAVBAR_CLASSES = ['navbar', 'navbar-expand-lg', 'navbar-dark', 'bg-dark']

NAV = """
<nav class="{html_class}">
    {brand}
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            {navitems}
        </ul>
    {custom_html}
    </div>
</nav>
"""


class NavbarMixin(Base):
    classes = Column(MutableListType)
    custom_html = Column(Text)
    name = Column(String)
    
    @declared_attr
    def brand_id(cls):
        return Column(Integer, ForeignKey('brand.id'))
    
    @declared_attr
    def brand(cls):
        return relationship('Brand', backref=backref('bar', uselist=False))
    
    @declared_attr
    def navitems(cls):
        return relationship(
            'Navitem',
            backref='bar',
            order_by='Navitem.index',
            collection_class=ordering_list('index')
            )
    
    def __init__(
            self, brand=None, navitems=[], classes=None, custom_html=None,
            name=None, *args, **kwargs):
        self.brand = brand
        self.navitems = navitems
        self.classes = classes or NAVBAR_CLASSES
        self.custom_html = custom_html
        self.name = name
        super().__init__(*args, **kwargs)
        
    def compile(self):
        brand = '' if self.brand is None else self.brand.compile()
        navitems = ''.join(
            [i.compile() for i in self.navitems])
        custom_html = '' if self.custom_html is None else self.custom_html
        return NAV.format(
            html_class=self.html_class, brand=brand, navitems=navitems,
            custom_html=custom_html)
    
    def render(self):
        soup = BeautifulSoup(self.compile(), 'html.parser')
        return Markup(str(soup.prettify()))