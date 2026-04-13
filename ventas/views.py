from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User, Group


# 1. LOGIN: Filtra quién entra y lo manda a 'cliente' o a 'home'
def login_view(request):
    if request.method == "POST":
        usuario = request.POST.get("username")
        clave = request.POST.get("password")
        user = authenticate(request, username=usuario, password=clave)

        if user is not None:
            login(request, user)
            # REGLA: Si pertenece al grupo Cliente, va a la vista cliente
            if user.groups.filter(name="Cliente").exists():
                return redirect("cliente")  # <-- CAMBIADO DE 'ventas' A 'cliente'
            else:
                return redirect("home")  # Tú (Master) vas al House
        else:
            messages.error(request, "Credenciales incorrectas.")

    return render(request, "ventas/login.html")


# 2. REGISTRO: Crea al usuario y lo tira a la vista de cliente
def registro_view(request):
    if request.method == "POST":
        usuario = request.POST.get("username")
        correo = request.POST.get("email")
        clave = request.POST.get("password")

        if User.objects.filter(username=usuario).exists():
            messages.error(request, "Ese nombre de usuario ya existe.")
            return redirect("registro")

        nuevo_usuario = User.objects.create_user(
            username=usuario, email=correo, password=clave
        )

        try:
            grupo = Group.objects.get(name="Cliente")
            nuevo_usuario.groups.add(grupo)
        except Group.DoesNotExist:
            pass

        login(request, nuevo_usuario)
        messages.success(request, f"¡Bienvenido {usuario}!")

        # SALTO DIRECTO A CLIENTE
        return redirect("cliente")  # <-- CAMBIADO DE 'ventas' A 'cliente'

    return render(request, "ventas/registro.html")


# 3. EL HOUSE (Panel administrativo)
def home_view(request):
    es_cliente = request.user.groups.filter(name="Cliente").exists()
    return render(request, "ventas/home.html", {"es_cliente": es_cliente})


## 4. LA VISTA DE BIENVENIDA EXCLUSIVA PARA EL CLIENTE
def cliente_view(request):
    # Solo permitimos que entren los que son del grupo 'Cliente'
    if request.user.groups.filter(name="Cliente").exists():
        return render(request, "ventas/cliente.html")
    else:
        # Si un Master intenta entrar aquí, lo mandamos al home
        return redirect("home")


# 5. EL POS (Lo dejamos aparte solo para el Master)
def pos_view(request):
    return render(request, "ventas/pos.html")
