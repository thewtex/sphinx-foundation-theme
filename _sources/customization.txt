.. _customization:

Customization
=============

Topbar
------

A responsive `topbar <http://foundation.zurb.com/sites/docs/top-bar.html>`_ is included
to provide an overview and assist navigation.

Topbar Site Navigation
^^^^^^^^^^^^^^^^^^^^^^

The topbar includes a menu to navigate the site table of contents.  The name
of this menu is *Site* by default. To change it, set the ``topbar_site_name``
option::

  html_theme_options = { 'topbar_site_name': 'Site Navigation' }

To adjust the number of levels in the topbar site menu, set the
``topbar_site_depth`` option. The default value, *-1*, shows all levels.

Topbar Page Navigation
^^^^^^^^^^^^^^^^^^^^^^

By default, the topbar also includes a menu to navigate the page table of
contents. To disable this menu altogether, set the ``topbar_page`` option to
``False``.

The name of the topbar page menu is *Page* by default. To change it, set the
``topbar_page_name`` option.

Topbar Relations
^^^^^^^^^^^^^^^^

Be default, links to the previous and next pages are included by default on
the right side of the topbar. To disable these pagination links, set the
``topbar_relations`` option to ``False``.


Sidebars
--------

Sidebar Contents
^^^^^^^^^^^^^^^^

By default, the sidebar is empty. Add sidebar contents by populating the
*conf.py* `html_sidebars
<http://www.sphinx-doc.org/en/1.4.9/config.html?highlight=html_sidebars>`_ option.
For example::

  # Custom sidebar templates, maps document names to template names.
  html_sidebars = {'**': ['localtoc.html',
          'relations.html',
          'sourcelink.html'],
      'index': [
          'globaltoc.html']
      }

Sidebar Location
^^^^^^^^^^^^^^^^

To move the sidebar to the right, set the ``rightsidebar`` boolean in
*conf.py*::

  html_theme_options = { 'rightsidebar': True }


Colorscheme
-----------

To use your own colorscheme,

1. `Install Node/NPM <https://nodejs.org/en/download/>`_
2. ``npm install -g foundation-cli``
3. ``foundation new --framework sites --template basic``
4. ``cd projectname``
5. Run ``npm start``
6. Edit ``scss/_settings.scss`` to the desired settings
7. Copy ``css/app.css`` to the ``_static`` directory of your Sphinx sources
8. Set the ``stylesheet`` key in the *conf.py* ``html_theme_options``.

For example::

  html_theme_options = { 'stylesheet': 'myfoundationstyle.css' }

The `pygments_style
<http://www.sphinx-doc.org/en/1.4.9/config.html#confval-pygments_style>`_
can be changed to a `style that matches your theme <https://help.farbox.com/pygments.html>`_.
