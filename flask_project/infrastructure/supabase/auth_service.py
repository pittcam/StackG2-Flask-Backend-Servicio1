import requests
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


def register_user_with_supabase(email, password, username, name):
    email = str(email).replace("'", "").replace('"', "").strip()
    password = str(password).replace("'", "").replace('"', "").strip()
    username = str(username).replace("'", "").replace('"', "").strip()
    name = str(name).replace("'", "").replace('"', "").strip()

    print("Registrando usuario con Supabase Auth:")
    print(f"  Email: {email}")
    print(f"  Password: {password}")
    print(f"  Username: {username}")
    print(f"  Name: {name}")

    # 📡 Paso 1: Registrar en Supabase Auth
    res = requests.post(
        f"{SUPABASE_URL}/auth/v1/signup",
        headers={
            "apikey": SUPABASE_KEY,
            "Content-Type": "application/json"
        },
        json={
            "email": email,
            "password": password
        }
    )

    print("Supabase Auth response:", res.status_code, res.text)

    if res.status_code != 200:
        raise Exception("Error en registro Supabase")

    data = res.json()
    token = data.get("access_token")
    user_id = data.get("user", {}).get("id")

    if not token or not user_id:
        print("Datos inválidos recibidos de Supabase:", data)
        raise Exception("Error: token o user_id no recibido")

    # 📡 Paso 2: Guardar datos adicionales en tabla 'usuarios'
    r2 = requests.post(
        f"{SUPABASE_URL}/rest/v1/usuarios",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        },
        json={
            "user_id": user_id,
            "username": username,
            "name": name
        }
    )

    print("Supabase DB response:", r2.status_code, r2.text)

    if r2.status_code not in [200, 201]:
        raise Exception("Error al guardar datos en Supabase")

    return {
        "id": user_id,
        "email": email,
        "token": token
    }

def login_user_with_supabase(email, password):
    email = str(email).replace("'", "").replace('"', "").strip()
    password = str(password).replace("'", "").replace('"', "").strip()

    print("Login Supabase Auth")
    print(f"Email: {email}")
    print(f"Password: {password}")

    res = requests.post(
        f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
        headers={
            "apikey": SUPABASE_KEY,
            "Content-Type": "application/json"
        },
        json={
            "email": email,
            "password": password
        }
    )

    print("Login response:", res.status_code, res.text)

    if res.status_code != 200:
        raise Exception("Error al iniciar sesión")

    data = res.json()
    return {
        "token": data.get("access_token"),
        "email": email,
        "id": data.get("user", {}).get("id")
    }
