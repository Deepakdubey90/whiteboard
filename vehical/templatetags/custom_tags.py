 # -*- encoding: utf-8 -*-
import six
import sys
from django.template import Node, TemplateSyntaxError, Library
from django.conf import settings

register = Library()

class CurrentURLNode(Node):

    def __init__(self, asvar=None):
        self.asvar = asvar

    def render(self, context):
        request = context['request']
        from django.core.urlresolvers import reverse, NoReverseMatch
        url = ''
        try:
            url = reverse(request.resolver_match.view_name, args=request.resolver_match.args, kwargs=request.resolver_match.kwargs, current_app=context.current_app)
        except NoReverseMatch:
            exc_info = sys.exc_info()
            if settings.SETTINGS_MODULE:
                project_name = settings.SETTINGS_MODULE.split('.')[0]
                try:
                    url = reverse(project_name + '.' + request.resolver_match.view_name,
                          args=request.resolver_match.args, kwargs=request.resolver_match.kwargs,
                          current_app=context.current_app)
                except NoReverseMatch:
                    if self.asvar is None:                      
                        six.reraise(*exc_info)
            else:
                if self.asvar is None:
                    raise

        if self.asvar:
            context[self.asvar] = url
            return ''
        else:
            return url

@register.tag
def current_url(parser, token):
    bits = token.split_contents()
    bits = bits[1:]
    asvar = None
    if len(bits) >= 2 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]
    if len(bits):
        raise TemplateSyntaxError("Unexpected arguments to current_url tag")
    return CurrentURLNode(asvar)
