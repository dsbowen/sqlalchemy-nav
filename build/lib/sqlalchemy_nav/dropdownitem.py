"""Dropdownitem Mixin

A `Dropdownitem` has a `Navitem` parent.
"""

from sqlalchemy_nav.base import Base

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declared_attr


class DropdownitemMixin(Base):
    @declared_attr
    def _navitem_id(cls):
        return Column(Integer, ForeignKey('navitem.id'))

    def __init__(self, navitem=None, *args, **kwargs):
        self.navitem = navitem
        super().__init__('dropdownitem.html', *args, **kwargs)    

    def render(self, body=None):
        body = body or self.body.copy()
        if self.is_active(): # add 'active' class to `a` Tag
            a = body.select_one('a')
            if a.attrs.get('class') is None:
                a['class'] = []
            body.select_one('a')['class'].append('active')
        return body