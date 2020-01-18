"""Navitem Mixin

A `Navitem` has a `Navbar` parent and `Dropdownitem` children.
"""

from sqlalchemy_nav.base import Base

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import relationship


class NavitemMixin(Base):
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
        """
        Set `dropdown` to `True` to indicate that this `Navitem` will 
        contain `Dropdownitem`s.
        """
        self.navbar = navbar
        template = 'navitemdropdown.html' if dropdown else 'navitem.html'
        super().__init__(template, *args, **kwargs)  

    def render(self, body=None):
        """Render MutableSoup

        If this `Navitem` contains `Dropdownitem`s, render them and append 
        to the dropdown menu. Additionally, set the appropriate 'id' and 
        'aria-labelledby' attributes.
        """
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