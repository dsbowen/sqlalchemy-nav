<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" type="text/css" />

<style>
    a.src-href {
        float: right;
    }
    p.attr {
        margin-top: 0.5em;
        margin-left: 1em;
    }
    p.func-header {
        background-color: gainsboro;
        border-radius: 0.1em;
        padding: 0.5em;
        padding-left: 1em;
    }
    table.field-table {
        border-radius: 0.1em
    }
</style># API

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##sqlalchemy_nav.**Base**

<p class="func-header">
    <i>class</i> sqlalchemy_nav.<b>Base</b>(<i>template, label=None, href=None, *args, **kwargs</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/sqlalchemy-nav/blob/master/sqlalchemy_nav/__init__.py#L15">[source]</a>
</p>

All SQLAlchemy-Nav mixins inherit from this base.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>template : <i>str</i></b>
<p class="attr">
    Relative path to the html template file. Users should not pass this argument; it is passed automatically by mixins.
</p>
<b>label : <i>str</i></b>
<p class="attr">
    Label (text) of the first <code>&lt;a&gt;</code> tag.
</p>
<b>href : <i>str</i></b>
<p class="attr">
    Hyperref of the first <code>&lt;a&gt;</code> tag.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>id : <i>int</i></b>
<p class="attr">
    Model identifier.
</p>
<b>index : <i>int</i></b>
<p class="attr">
    Order of the model in its parent's list. e.g. the 0th <code>Navitem</code> in a <code>Navbar</code> has an <code>index</code> of 0.
</p>
<b>body : <i>sqlalchemy_mutablesoup.MutableSoup</i></b>
<p class="attr">
    The body of the object. This is converted to html when the object is rendered.
</p>
<b>a : <i>bs4.Tag</i></b>
<p class="attr">
    First <code>&lt;a&gt;</code> html tag in <code>body</code>.
</p>
<b>label : <i>str</i></b>
<p class="attr">
    Text of <code>a</code>. Set from the <code>label</code> parameter.
</p>
<b>href : <i>str</i></b>
<p class="attr">
    Hyperref of <code>a</code>. Set from the <code>href</code> parameter.
</p></td>
</tr>
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>is_active</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/sqlalchemy-nav/blob/master/sqlalchemy_nav/__init__.py#L85">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>is_active : <i>bool</i></b>
<p class="attr">
    Indicates that the object's href is active.
</p></td>
</tr>
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>render</b>(<i>self, body=None</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/sqlalchemy-nav/blob/master/sqlalchemy_nav/__init__.py#L97">[source]</a>
</p>

Prepares a `bs4.BeautifulSoup` object for rendering into html.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>body : <i>sqlalchemy_mutablesoup.MutableSoup or None, default=None</i></b>
<p class="attr">
    Object to render. If <code>None</code>, a copy of <code>self.body</code> is used.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>body : <i>sqlalchemy_mutablesoup.MutableSoup</i></b>
<p class="attr">
    Prepared for rendering into html.
</p></td>
</tr>
    </tbody>
</table>



##sqlalchemy_nav.**NavbarMixin**

<p class="func-header">
    <i>class</i> sqlalchemy_nav.<b>NavbarMixin</b>(<i>name=None, *args, **kwargs</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/sqlalchemy-nav/blob/master/sqlalchemy_nav/__init__.py#L114">[source]</a>
</p>

Navigation bar mixin.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>name : <i>str</i></b>
<p class="attr">
    Name of the navigation bar. This facilitates finding the navigation bar when querying the database.
</p>
<b>*args, **kwargs : <i></i></b>
<p class="attr">
    Additional arguments and keyword arguments are passed to <code>Base.__init__</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>name : <i>str</i></b>
<p class="attr">
    Set from the <code>name</code> parameter.
</p>
<b>navitems : <i>sqlalchemy.ext.orderinglist.OrderingList</i></b>
<p class="attr">
    List of <code>Navitem</code> objects ordered by <code>index</code>.
</p></td>
</tr>
    </tbody>
</table>





##sqlalchemy_nav.**NavitemMixin**

<p class="func-header">
    <i>class</i> sqlalchemy_nav.<b>NavitemMixin</b>(<i>navbar=None, dropdown=False, *args, **kwargs</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/sqlalchemy-nav/blob/master/sqlalchemy_nav/__init__.py#L162">[source]</a>
</p>

Navigation item mixin.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>navbar : <i>sqlalchemy_nav.NavbarMixin or None, default=None</i></b>
<p class="attr">
    Navigation bar with which this navigation item is associated.
</p>
<b>dropdown : <i>bool, default=False</i></b>
<p class="attr">
    Indicates that this navitem will contain dropdown items.
</p>
<b>*args, **kwargs : <i></i></b>
<p class="attr">
    Additional arguments and keyword arguments are passed to <code>Base.__init__</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>navbar : <i>sqlalchemy_nav.NavbarMixin or None</i></b>
<p class="attr">
    Set from the <code>navbar</code> parameter.
</p>
<b>dropdownitems : <i>sqlalchemy.ext.orderinglist.OrderingList</i></b>
<p class="attr">
    List of <code>Dropdownitem</code> objects ordered by <code>index</code>.
</p></td>
</tr>
    </tbody>
</table>





##sqlalchemy_nav.**DropdownitemMixin**

<p class="func-header">
    <i>class</i> sqlalchemy_nav.<b>DropdownitemMixin</b>(<i>navitem=None, *args, **kwargs</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/sqlalchemy-nav/blob/master/sqlalchemy_nav/__init__.py#L218">[source]</a>
</p>

Dropdown item mixin.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>navitem : <i>sqlalchemy_nav.NavitemMixin or None, default=None</i></b>
<p class="attr">
    Navigation item with which this dropdown item is associated.
</p>
<b>*args, **kwargs : <i></i></b>
<p class="attr">
    Additional arguments and keyword arguments are passed to <code>Base.__init__</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>navitem : <i>sqlalchemy_nav.NavitemMixin or None</i></b>
<p class="attr">
    Set from the <code>navitem</code> parameter.
</p></td>
</tr>
    </tbody>
</table>



