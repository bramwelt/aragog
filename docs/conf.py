extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Aragog'
copyright = u'2014, Trevor Bramwell'

version = '0.1.0'
release = '0.1.0'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'Aragogdoc'

latex_elements = {}

latex_documents = [
    ('index', 'Aragog.tex', u'Aragog Documentation',
     u'Trevor Bramwell', 'manual'),
]

man_pages = [
    ('index', 'aragog', u'Aragog Documentation',
     [u'Trevor Bramwell'], 1)
]

texinfo_documents = [
    ('index', 'Aragog', u'Aragog Documentation',
     u'Trevor Bramwell', 'Aragog', 'One line description of project.',
     'Miscellaneous'),
]

intersphinx_mapping = {'http://docs.python.org/': None}
