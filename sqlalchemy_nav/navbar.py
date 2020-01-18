"""Navbar Mixin

A `Navbar` has `Navitem` children. Use the `name` attribute with 
query.filter_by(name=name) to retrieve the `Navbar` across sessions.
"""

from sqlalchemy_nav.base import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import backref, relationship


class NavbarMixin(Base):
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
    
    def render(self, body=None):
        """Render `body` MutableSoup

        Set the appropriate 'id', 'data-target', and 'aria-controls' 
        attributes. Then append the `Navitems` as HTML list elements.
        """
        body = body or self.body.copy()
        btn = body.select_one('button.navbar-toggler')
        btn['data-target'] = '#'+self.model_id
        btn['aria-controls'] = self.model_id
        body.select_one('div.navbar-collapse')['id'] = self.model_id
        ul = body.select_one('ul')
        [ul.append(item.render()) for item in self.navitems]
        return body