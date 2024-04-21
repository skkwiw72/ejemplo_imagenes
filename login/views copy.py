from django.contrib.auth.models import User

def imprimir_usuarios_y_contraseñas():
    # Obtener todos los objetos de usuario en la base de datos
    usuarios = User.objects.all()

    # Iterar sobre cada usuario y imprimir su nombre de usuario y contraseña
    for usuario in usuarios:
        print("Nombre de usuario:", usuario.username)
        print("Contraseña:", usuario.password)  # Ten en cuenta que este campo contiene la contraseña cifrada
        print("--------------------")

# Llamar a la función para imprimir los usuarios y contraseñas
imprimir_usuarios_y_contraseñas()
