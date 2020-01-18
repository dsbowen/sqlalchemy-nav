# SQLAlchemy-Nav

SQLAlchemy-Nav provides [SQLAlchemy Mixins](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html) for creating navigation bars compatible with [Bootstrap 4](https://getbootstrap.com/docs/4.4/components/navbar/). Its Mixins are:

1. ```NavbarMixin``` for creating navigation bars
2. ```NavitemMixin``` for adding nav-items to the navbar
3. ```DropdownitemMixin``` for adding dropdown-items to nav-items

## Example

After setup, we can create nav-bars as follows:

```python
navbar = Navbar(label='Home', href='https://dsbowen.github.io')
Navitem(navbar, label='About', href='/about')
navitem = Navitem(navbar, dropdown=True, label='Projects')
Dropdownitem(navitem, label='Flask-Worker', href='/flask-worker')
Dropdownitem(navitem, label='SQLAlchemy-Mutable', href='/sqlalchemy-mutable')
session.add(navbar)
session.commit()
print(navbar.render().prettify())
```

## Documentation

You can find the latest documentation at [https://dsbowen.github.io/sqlalchemy-nav](https://dsbowen.github.io/sqlalchemy-nav).

## License

Publications which use this software should include the following citation for SQLAlchemy-Nav, as well as its dependencies [SQLAlchemy-MutableSoup](https://dsbowen.github.io/sqlalchemy-mutablesoup) and [SQLAlchemy-OrderingItem](https://dsbowen.github.io/sqlalchemy-orderingitem):

Bowen, D.S. (2019). SQLAlchemy-Nav \[Computer software\]. [https://github.com/dsbowen/sqlalchemy-nav](https://dsbowen.github.io/sqlalchemy-nav).

Bowen, D.S. (2020). SQLAlchemy-MutableSoup [Computer software]. [https://dsbowen.github.io/sqlalchemy-mutablesoup](https://dsbowen.github.io/sqlalchemy-mutablesoup).

Bowen, D.S. (2019). SQLAlchemy-OrderingItem [Computer software]. [https://dsbowen.github.io/sqlalchemy-orderingitem](https://dsbowen.github.io/sqlalchemy-orderingitem).

This project is licensed under the MIT License [LICENSE](https://github.com/dsbowen/sqlalchemy-nav/blob/master/LICENSE).