from django import template

def currency_gourde(value):
    return f"{value:.6} HTG"

def productimage(value):
      return f"https://raw.github.com/jeanoxeant/oma-distribution/main/products/{value}"

register = template.Library()

register.filter("currency_gourde", currency_gourde) # name of the filter, function
register.simple_tag(productimage)