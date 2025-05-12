import streamlit as st
from menu_pilihan import tampilkan_menu_pilihan

users = {
    "adzan": "ganteng",
    "admin": "admin"
}

if "login" not in st.session_state:
    st.session_state["login"] = False
if "trial" not in st.session_state:
    st.session_state["trial"] = False
if "trial_count" not in st.session_state:
    st.session_state["trial_count"] = 0

if not st.session_state["login"] and not st.session_state["trial"]:
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            if username in users and users[username] == password:
                st.session_state["login"] = True
                st.success(f"Selamat datang, {username}!")
            else:
                st.error("Username atau password salah!")
    with col2:
        if st.button("Coba Sebagai Trial"):
            st.session_state["trial"] = True
            st.session_state["trial_count"] = 0
            st.warning("Mode trial diaktifkan. Maksimal 3x perhitungan.")

if st.session_state["login"] or st.session_state["trial"]:
    tampilkan_menu_pilihan()
