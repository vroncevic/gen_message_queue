# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = u'gen_message_queue'
copyright = u'2018, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'1.0.0'
release = u'https://github.com/vroncevic/gen_message_queue/releases'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'gen_message_queuedoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'gen_message_queue.tex',
    u'gen\\_message\\_queue Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'gen_message_queue', u'gen_message_queue Documentation',
    [author], 1
)]
texinfo_documents = [(
    master_doc, 'gen_message_queue', u'gen_message_queue Documentation',
    author, 'gen_message_queue', 'One line description of project.',
    'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']