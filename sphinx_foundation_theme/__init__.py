"""Sphinx Foundation Theme

A Sphinx HTML theme that uses Zurb foundation-sites.
"""

__version__ = '0.4.0'

import os

def get_html_theme_path():
    """Return the `html_theme_path` in a list for use in a project's Sphinx
    conf.py."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return [cur_dir]
