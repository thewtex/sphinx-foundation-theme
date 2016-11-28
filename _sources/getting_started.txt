Getting Started
===============

Installation
------------

To install::

  pip install sphinx-foundation-theme


Configuration
-------------

In your project's Sphinx *conf.py* file, set the theme to ``foundation``::

    import sphinx_foundation_theme

    html_theme = 'foundation'

    html_theme_path = sphinx_foundation_theme.get_html_theme_path()

To modify the appearance, see the theme :ref:`customization` documentation.
