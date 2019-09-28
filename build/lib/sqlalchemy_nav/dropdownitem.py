"""Dropdownitem Mixin

Dropdownitem is attached to a Navitem. It contains a list of classes for the a 
tag.
"""

from .base import Base

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_mutable import MutableListType

DROPDOWN_HTML = '<a class="{html_class}" href="{href}">{label}</a>'


class DropdownitemMixin(Base):
    classes = Column(MutableListType)
    index = Column(Integer)
    
    @declared_attr
    def navitem_id(cls):
        return Column(Integer, ForeignKey('navitem.id'))
    
    def __init__(self, item=None, classes=None, *args, **kwargs):
        self.item = item
        self.classes = classes or ['dropdown-item']
        super().__init__(*args, **kwargs)
    
    def compile(self):
        return DROPDOWN_HTML.format(
            html_class=self.html_class, href=self.url, label=self.label)