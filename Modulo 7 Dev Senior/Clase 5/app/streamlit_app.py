# Importa la biblioteca Streamlit para crear interfaces gráficas web
import streamlit as st

# Importa requests para hacer llamadas HTTP a la API FastAPI
import requests

# Dirección base de la API local de FastAPI
API_BASE_URL = "http://localhost:8000"

# Configura el título y el ícono de la pestaña del navegador
st.set_page_config(page_title="Gestión de Cuentas", page_icon="🔐")

# Título principal de la página
st.title("Sistema de Gestión de Cuentas")

# Menú lateral para seleccionar entre Registro y Login
menu = ["Registro", "Login"]
choice = st.sidebar.selectbox("Menú", menu)

# Variables de sesión para manejar login persistente
if "token" not in st.session_state:
    st.session_state.token = None
if "user" not in st.session_state:
    st.session_state.user = None

# --- REGISTRO DE USUARIOS ---
if choice == "Registro":
    st.subheader("Crear nuevo usuario")
    
    # Formulario para registrar nuevos usuarios
    with st.form("register_form", clear_on_submit=True):
        username = st.text_input("Usuario", help="4-20 caracteres")
        password = st.text_input("Contraseña", type="password", help="Mínimo 6 caracteres")
        role = st.selectbox("Rol", ["user", "admin"])
        submit = st.form_submit_button("Registrar")
        
        if submit:
            # Validaciones mínimas antes de enviar al backend
            if len(username) < 4 or len(username) > 20:
                st.error("El usuario debe tener entre 4 y 20 caracteres")
            elif len(password) < 6:
                st.error("La contraseña debe tener al menos 6 caracteres")
            else:
                # Datos a enviar a la API para crear usuario
                data = {"username": username, "password": password, "role": role}
                try:
                    # Enviar POST a /auth/register
                    r = requests.post(f"{API_BASE_URL}/auth/register", json=data)
                    if r.status_code == 200:
                        st.success(f"✅ Usuario '{username}' creado correctamente")
                    else:
                        st.error(f"❌ Error: {r.json().get('detail', r.text)}")
                except Exception as e:
                    st.error(f"❌ Error de conexión: {e}")

# --- LOGIN DE USUARIOS ---
if choice == "Login":
    st.subheader("Iniciar sesión")
    
    # Formulario para ingresar usuario y contraseña
    with st.form("login_form", clear_on_submit=True):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        submit = st.form_submit_button("Entrar")
        
        if submit:
            # Validación básica
            if not username or not password:
                st.warning("⚠️ Completa usuario y contraseña")
            else:
                # Datos a enviar al endpoint /auth/login
                data = {"username": username, "password": password}
                try:
                    # Login usando x-www-form-urlencoded (OAuth2PasswordRequestForm)
                    r = requests.post(f"{API_BASE_URL}/auth/login", data=data)
                    if r.status_code == 200:
                        # Guarda el token JWT en sesión
                        token = r.json()["access_token"]
                        st.session_state.token = token
                        st.success("✅ Login exitoso")
                        
                        # Llama a /auth/me para obtener los datos del usuario
                        headers = {"Authorization": f"Bearer {token}"}
                        r2 = requests.get(f"{API_BASE_URL}/auth/me", headers=headers)
                        if r2.status_code == 200:
                            st.session_state.user = r2.json()
                        else:
                            st.session_state.user = None
                    else:
                        st.error("❌ Credenciales inválidas")
                except Exception as e:
                    st.error(f"❌ Error de conexión: {e}")

    # Mostrar información del usuario si está autenticado
    if st.session_state.token and st.session_state.user:
        st.success(f"👋 Bienvenido, {st.session_state.user['username']} (rol: {st.session_state.user['role']})")
        
        # Botón para cerrar sesión
        if st.button("🚪 Cerrar Sesión"):
            st.session_state.token = None
            st.session_state.user = None
            st.success("✅ Sesión cerrada correctamente")
            st.rerun()
        
        # Si el usuario es admin, intenta acceder a ruta protegida para administradores
        if st.session_state.user["role"] == "admin":
            headers = {"Authorization": f"Bearer {st.session_state.token}"}
            r = requests.get(f"{API_BASE_URL}/auth/admin", headers=headers)
            if r.status_code == 200:
                st.info("🔐 Tienes acceso a la ruta de administrador.")
            else:
                st.warning("⚠️ No tienes acceso a la ruta de administrador.")
        else:
            st.info("👤 Eres un usuario estándar.")