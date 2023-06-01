from django.http import HttpResponse


def bienvenida(request):
    html_content = """
          <html>
              <head>
                  <title>Django</title>
              </head>
              <body>
                  <h1>Bienvenido  APP Django!</h1>
                  <p>Aplicación de prueba Django!</p>
              </body>
          </html>
          """
    return HttpResponse(html_content)


def despedida(request):
    html_content = """
          <html>
              <head>
                  <title>Django</title>
              </head>
              <body>
                  <h1>Despedida  APP Django!</h1>
                  <p>Aplicación de prueba Django!</p>
              </body>
          </html>
          """
    return HttpResponse(html_content)


# con parametros

def usuario(request, name):
    html_content = f"""
              <html>
                  <head>
                      <title>Django</title>
                  </head>
                  <body>
                      <h1>Bienvenido  APP Django!</h1>
                      <p>Señor {name}</p>
                  </body>
              </html>
              """
    # saludo = f"<h1>Bienvenido señor {name}</h1>"
    return HttpResponse(html_content)


def datos(request, name, ape, edad):
    html_content = f"""
              <html>
                  <head>
                      <title>Django</title>
                  </head>
                  <body>
                      <h1>Bienvenido  APP Django!</h1>
                      <p>Señor {name} {ape} tiene {edad} años.</p>
                  </body>
              </html>
              """
    # saludo = f"<h1>Bienvenido señor {name}</h1>"
    return HttpResponse(html_content)