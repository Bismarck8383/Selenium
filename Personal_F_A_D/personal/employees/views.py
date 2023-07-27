import json

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "index.html")


def new_employee(request):
    return render(request, "add_employee.html")


@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8007/api/create_employee'

        # Parse the request body as JSON and convert to Python dictionary
        data = json.loads(request.body.decode('utf-8'))

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        # Convert the data dictionary back to a JSON string
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code in [200, 201]:
            return JsonResponse(response.json(), safe=False, status=200)
        else:
            return JsonResponse(
                {'error': 'Ha ocurrido un error al crear el empleado.', 'original_error': response.text},
                status=response.status_code)


def employees_list(request):
    # Hacer la solicitud GET al endpoint de la API
    response = requests.get('http://127.0.0.1:8007/api/all_employees')

    if response.status_code == 200:
        employees = response.json()
    else:
        employees = []

    # Pasar los empleados al contexto de la plantilla
    context = {
        'employees': employees
    }

    return render(request, "index.html", context)


def get_employee_by_id(request, employee_id):
    url = f"http://127.0.0.1:8007/api/employees/{employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        error_message = response.json().get('error', 'Error desconocido')
        return JsonResponse({'error': error_message}, status=500)


def delete_employee_id(request, employee_id):
    # Verificar si el ID del empleado existe
    check_url = f"http://127.0.0.1:8007/api/employees/{employee_id}"
    check_response = requests.get(check_url)

    if check_response.status_code == 404:
        return JsonResponse({"error": "Empleado no encontrado"}, status=404)

    # Realizar la eliminación del empleado
    delete_url = f"http://127.0.0.1:8007/api/delete_employee/{employee_id}"
    delete_response = requests.delete(delete_url)

    if delete_response.status_code == 200:
        return JsonResponse({"message": "Registro eliminado exitosamente"}, status=200)
    else:
        try:
            error_message = delete_response.json().get('error', 'Error desconocido')
        except ValueError:
            error_message = 'Error desconocido'

        return JsonResponse({"error": f"Error al eliminar el registro: {error_message}"}, status=500)


@csrf_exempt
def update_employee(request, employee_id):
    try:
        # Verificar si el ID del empleado existe
        check_url = f"http://127.0.0.1:8007/api/employees/{employee_id}"
        check_response = requests.get(check_url)

        if check_response.status_code == 404:
            return JsonResponse({"error": "Empleado no encontrado"}, status=404)

        if request.method == 'PUT':
            try:
                # Obtener los nuevos datos del empleado del cuerpo de la solicitud PUT
                data = json.loads(request.body)
                print(f"recibi {data}")

                # Asegurarte de que todos los campos necesarios están presentes en data
                required_fields = ["name", "edad", "cargo", "genero", "salario", "email", "direccion",
                                   "fecha_contratacion",
                                   "telefono"]
                if all(field in data for field in required_fields):
                    print("Los datos son correctos y están todos los campos requeridos presentes.")
                else:
                    return JsonResponse({"error": "Faltan campos requeridos en los datos del empleado"}, status=400)

                # Si 'salario' es un número entero, lo convertimos a float con dos decimales
                if isinstance(data['salario'], int) or isinstance(data['salario'], float):
                    data['salario'] = float("{:.2f}".format(data['salario']))
                print(f"Salario convertido a {data['salario']}")

            except json.JSONDecodeError:
                return JsonResponse({"error": "Los datos del empleado proporcionados no son válidos"}, status=400)

            # Realizar la actualización del empleado
            update_url = f"http://127.0.0.1:8007/api/employee_update/{employee_id}"
            update_response = requests.put(update_url, json=data)
            print(update_response)

            if update_response.status_code == 200:
                return JsonResponse({"success": "Empleado actualizado exitosamente."}, status=200)

            else:
                try:
                    error_message = update_response.json().get('error', 'Error desconocido')
                except ValueError:
                    error_message = 'Error desconocido' + update_response.text

                return JsonResponse({"error": f"Error al actualizar el registro: {error_message}"}, status=500)
        else:
            return JsonResponse({"error": "Método no permitido"}, status=405)

    except Exception as e:
        import traceback
        return JsonResponse({"error": f"Error desconocido: {str(e)}. Traceback: {traceback.format_exc()}"}, status=500)


def bootstrap_prueba(request):
    return render(request, "bootstrap.html")
