from docstr_md.python import PySoup, compile_md
from docstr_md.src_href import Github

src_href = Github('https://github.com/dsbowen/sqlalchemy-nav/blob/master')
path = 'sqlalchemy_nav/__init__.py'
soup = PySoup(path=path, parser='sklearn', src_href=src_href)
soup.rm_properties()
for obj in soup.objects:
    if hasattr(obj, 'name'):
        if obj.name == 'NavbarMixin':
            obj.rm_methods('navitems')
        elif obj.name == 'NavitemMixin':
            obj.rm_methods('dropdownitems')
compile_md(soup, compiler='sklearn', outfile='docs_md/api.md')