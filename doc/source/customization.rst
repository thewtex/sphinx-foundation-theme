.. _customization:

Customization
=============

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


Sidebars
--------

.. todo:: Sidebar contents
By default, the sidebar is emtpy. Add sidebar contents by populating the
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

.. todo:: Sidebar location
