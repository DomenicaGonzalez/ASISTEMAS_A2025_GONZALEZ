import re

# Lista de contraseñas a verificar
contraseñas = ["123456", "Password1", "admin", "Segura#2025", "qwerty", "Hola123!"]

def verificar_contraseña(contraseña):
    # Requisitos de seguridad
    longitud = len(contraseña) >= 8
    tiene_mayuscula = re.search(r"[A-Z]", contraseña)
    tiene_minuscula = re.search(r"[a-z]", contraseña)
    tiene_numero = re.search(r"[0-9]", contraseña)
    tiene_especial = re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña)

    if longitud and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        return "✔️ Segura"
    else:
        return "❌ Débil"

# Analizar cada contraseña
for pwd in contraseñas:
    resultado = verificar_contraseña(pwd)
    print(f"🔍 Contraseña: {pwd} → {resultado}")
