"""Base for SQLAlchemy-Nav Mixins"""

from bs4 import BeautifulSoup
from flask import request
from sqlalchemy import Column, Integer, String


class Base():
    id = Column(Integer, primary_key=True)    
    _label = Column(String)
    _url = Column(String)
    
    @property
    def html_class(self):
        """Convert class list to a string"""
        html_class = ' '.join(self.classes) if self.classes else ''
        html_class += ' active' if self.isactive() else ''
        return html_class
    
    @property
    def label(self):
        return '' if self._label is None else self._label
    
    @label.setter
    def label(self, label):
        self._label = label
    
    @property
    def url(self):
        return self._url or '#'
    
    @url.setter
    def url(self, url):
        self._url = url
    
    def __init__(self, url=None, label=None):
        self.url = url
        self.label = label
    
    def isactive(self):
        """Test if object URL is active"""
        try:
            return self.url == str(request.url_rule)
        except: # Exception will occur in shell
            return False
    
    def view_html(self):
        """For debugging"""
        soup = BeautifulSoup(self.compile(), 'html.parser')
        print(soup.prettify())