from django import template
import locale
register = template.Library()

@register.filter(name='conversao')
def conversao(valor):
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    return locale.currency(valor)