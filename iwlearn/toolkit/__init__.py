# -*- extra stuff goes here -*-

from plone.i18n.locales.languages import _languagelist

_languagelist[u'me'] = {u'native' : 'Crnogorski jezik', u'name' : 'Montenegrin'}

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
