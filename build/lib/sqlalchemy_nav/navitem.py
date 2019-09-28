"""Navitem Mixin

Navitem is attachced to a Navbar. It contains a list of classes for the li 
tag, and may contain a list of dropdown items.
"""

from .base import Base

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import relationship
from sqlalchemy_mutable import MutableListType

LI = """
<li class="{html_class}">
    {a}
    {dropdown_div}
</li>
"""


A = """     
<a class="{a_class}" href="{href}" {dropdown_attrs}>
    {label}
</a>
"""


DROPDOWN_ATTRS = """
id="navbarDropdown{id}" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"
"""

DROPDOWN_DIV = """     
<div class="dropdown-menu" aria-labelledby="navbarDropdown{id}">
    {dropdownitems}
</div>
"""


class NavitemMixin(Base):
    classes = Column(MutableListType)
    index = Column(Integer)
    
    @declared_attr
    def navbar_id(cls):
        return Column(Integer, ForeignKey('navbar.id'))
    
    @declared_attr
    def dropdownitems(cls):
        return relationship(
            'Dropdownitem',
            backref='item',
            order_by='Dropdownitem.index',
            collection_class=ordering_list('index')
            )
    
    def __init__(
            self, bar=None, dropdownitems=[], classes=None, *args, **kwargs):
        self.bar = bar
        self.dropdownitems = dropdownitems
        self.classes = classes or ['nav-item']
        super().__init__(*args, **kwargs)
    
    def compile(self):
        html_class = self.html_class
        a_class = 'nav-link'
        if self.dropdownitems:
            html_class += ' dropdown'
            a_class += ' dropdown-toggle'
            dropdown_attrs = DROPDOWN_ATTRS.format(id=self.id)
            dropdownitems = ''.join(
                [i.compile() for i in self.dropdownitems])
            dropdown_div = DROPDOWN_DIV.format(
                id=self.id, dropdownitems=dropdownitems)
        else:
            dropdown_attrs = dropdown_div = ''
        a = A.format(
            a_class=a_class, href=self.url, dropdown_attrs=dropdown_attrs,
            label=self.label)
        return LI.format(
            html_class=self.html_class, href=self.url, a=a, 
            dropdown_div=dropdown_div)