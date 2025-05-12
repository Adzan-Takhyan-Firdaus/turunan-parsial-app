import streamlit as st
from turunan_parsial_2var_app import tampilkan_turunan_2var
from turunan_parsial_3var_app import tampilkan_turunan_3var

def tampilkan_menu_pilihan():
    st.title("🧠 Pilih Jenis Turunan Parsial")

    st.markdown("Silakan pilih jenis fungsi yang ingin dihitung:")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📘 2 Variabel")
        st.markdown("Gunakan untuk fungsi seperti `f(x, y)`")
        if st.button("Masuk ke Aplikasi 2 Variabel"):
            st.session_state["mode"] = "2var"

    with col2:
        st.subheader("📗 3 Variabel")
        st.markdown("Gunakan untuk fungsi seperti `f(x, y, z)`")
        if st.button("Masuk ke Aplikasi 3 Variabel"):
            st.session_state["mode"] = "3var"

    if "mode" in st.session_state:
        if st.session_state["trial"] and st.session_state["trial_count"] >= 3:
            st.error("❌ Sesi trial habis. Silakan login.")
            



        if st.session_state["mode"] == "2var":
            tampilkan_turunan_2var()
        elif st.session_state["mode"] == "3var":
            tampilkan_turunan_3var()
