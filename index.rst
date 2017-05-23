.. Test Documentation documentation master file, created by
   sphinx-quickstart on Tue May 23 14:23:37 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Test Documentation
==================

.. highlight:: python

Tutorial: http://www.sphinx-doc.org/en/stable/tutorial.html

Restructured text into: http://www.sphinx-doc.org/en/stable/rest.html

Getting Started
---------------

#. Defaults in ``sphinx-quickstart`` are fine, just make sure you enable ``autodoc`` to "automatically insert docstrings from modules".

#. Edit conf.py to include in the header::

    import os
    import sys
    sys.path.insert(0, 'path/to/your/code') 

#. Add ``sphinx.ext.napoleon`` to the list of extensions to enable numpy-style docstrings (optional).

#. Add to your rst file::

    .. automodule:: name_of_your_python_module
        :members:

   *Note that sphinx must be able to import your python module from somewhere in the python system path.*

#. Run ``make html``. When you update your python code, re-run ``make html``.


Table of contents:

.. toctree::
   :maxdepth: 2

   code

.. Indices and tables
.. ==================
.. 
.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
