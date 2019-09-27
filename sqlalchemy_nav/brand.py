"""Brand Mixin"""

from .base import Base

from sqlalchemy import Column
from sqlalchemy_mutable import MutableListType

BRAND = (
"""<a class="{html_class}" href="{href}">{label}</a>"""
)


class BrandMixin(Base):
    classes = Column(MutableListType)
    
    def __init__(self, bar=None, classes=None, *args, **kwargs):
        self.bar = bar
        self.classes = classes or ['navbar-brand']
        super().__init__(*args, **kwargs)
    
    def compile(self):
        return BRAND.format(
            html_class=self.html_class, href=self.url, label=self.label)