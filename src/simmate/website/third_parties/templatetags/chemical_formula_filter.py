# -*- coding: utf-8 -*-

# For adding new filters to django, look at...
# https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/

from django import template
from django.utils.safestring import mark_safe

# We need a registration instance in order to configure everything with Django
register = template.Library()

def formula_to_html(formula_str):
    """
    Converts a chemical formula to html format by wrapping numbers with a
    subscript tag. For example, "Y2CF2" will be turned into "Y<sub>2</sub>CF<sub>2</sub>"
    so that it looks nice in a webpage
    """
    
    # start with an empty string that we build off of
    new_formula_str = ""
    
    for character in formula_str:
        # if it's a number, we wrap it in <sub> tags
        if character.isnumeric():
            character = f"<sub>{character}</sub>"
        # now add it to our result
        new_formula_str += character
    
    # Because we added new html to our script, we need to have Django check it
    # ensure it safe before returning. Read more about this here:
    # https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/#filters-and-auto-escaping
    return mark_safe(new_formula_str)

# now register the new filter with django
register.filter('chemical_formula', formula_to_html)