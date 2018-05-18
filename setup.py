from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='iwlearn.toolkit',
      version=version,
      description="IW:LEARN website toolkit policy product",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['iwlearn'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
            'plone.app.caching',
            'Solgema.fullcalendar',
            'Products.feedfeeder',
            'collective.portletpage',
        # tagging
        #    'Products.PloneKeywordManager',
        #    'collective.keywordwidgetreplacer',
        #    'collective.taghelper',
        # link management
            'plone.app.redirector',
            'Products.RedirectionTool',
            'collective.videolink',
        #zgeo spatial annotations
            'collective.geo.contentlocations',
            'collective.geo.kml',
            'collective.geo.flexitopic',
            'collective.geo.file',
        #    'collective.geo.opensearch',

        # tools to interact with (anonymous) users
        #    plone.contentratings
        #    contentratings
        #    plone.app.discussion
        #    'Products.PlonePopoll',
            'Products.EasyNewsletter',
        #   Products.PloneSurvey
            'collective.captcha',
            'z3c.jbot',
        #    collective.recaptcha
        # iwlearn specific stuff and required dependencies
            'collective.ots',
            'iwlearn.theme',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
