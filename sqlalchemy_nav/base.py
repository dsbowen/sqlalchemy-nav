"""Base for SQLAlchemy-Nav Mixins

All SQLAlchemy-Nav Mixins have the following attributes:
1. `body`: A `MutableSoup` object containing the HTML associated with the object.
2. `label`: The object label
3. `href`: The object's link
"""

from flask import request
from sqlalchemy import Column, Integer
from sqlalchemy_modelid import ModelIdBase
from sqlalchemy_mutablesoup import MutableSoupType
from sqlalchemy_orderingitem import OrderingItem

import os


class Base(OrderingItem, ModelIdBase):
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
        """Test if object href is active"""
        try:
            return self.href == str(request.url_rule)
        except: # Exception will occur in shell
            return False