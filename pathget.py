import requests
from bs4 import BeautifulSoup

# HTML de ejemplo
html = '<html><body><div class="myclass"><p>Hello, world!</p></div></body></html>'

url = "https://parascrapear.com/"

# Hacer la solicitud a la página web
response = requests.get(url)
# Cargar el HTML en BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar el elemento div con clase 'myclass'
div = soup.find('div', {'id': 'modals'})


# Obtener el xpath del elemento div
def get_xpath(element):
    """
    Función recursiva para obtener el xpath de un elemento
    """
    xpath = ''
    if element.parent.name == 'html':
        return '/html/' + element.name
    xpath = get_xpath(element.parent) + '/' + element.name
    if element.attrs:
        for key, value in element.attrs.items():
            if key == 'class':
                xpath += '[@class="' + ' '.join(value) + '"]'
            else:
                xpath += '[@' + key + '="' + value + '"]'
    return xpath


def get_path(element):
    """
    Obtener el XPath de un elemento utilizando BeautifulSoup.
    """
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name if 1 == len(siblings) else '%s[%d]' % (child.name, 1 + siblings.index(child))
        )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)


dpath = get_path(div)
xpath = get_xpath(div)

print(f"segunda funcion {dpath}")
print(f"Primera funcion {xpath}")
