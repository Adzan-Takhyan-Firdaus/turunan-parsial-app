import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def tampilkan_turunan_3var():
    st.title("📗 Aplikasi Turunan Parsial 3 Variabel")

    fungsi_str = st.text_input("Masukkan fungsi f(x, y, z):", "x*y + z**2")
    x, y, z = sp.symbols('x y z')

    try:
        f = sp.sympify(fungsi_str)
        fx = sp.diff(f, x)
        fy = sp.diff(f, y)
        fz = sp.diff(f, z)

        st.latex(f"f(x, y, z) = {sp.latex(f)}")
        st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(fx)}")
        st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(fy)}")
        st.latex(f"\\frac{{\\partial f}}{{\\partial z}} = {sp.latex(fz)}")

        x0 = st.number_input("Nilai x₀", value=1.0)
        y0 = st.number_input("Nilai y₀", value=1.0)
        z0 = st.number_input("Nilai z₀", value=1.0)

        f_val = f.subs({x: x0, y: y0, z: z0})
        fx_val = fx.subs({x: x0, y: y0, z: z0})
        fy_val = fy.subs({x: x0, y: y0, z: z0})
        fz_val = fz.subs({x: x0, y: y0, z: z0})

        st.write(f"f({x0}, {y0}, {z0}) = {f_val}")
        st.write(f"Gradien: ({fx_val}, {fy_val}, {fz_val})")

        if st.session_state.get("trial"):
            st.session_state["trial_count"] += 1
            sisa = 3 - st.session_state["trial_count"]
            st.info(f"Sisa penggunaan trial: {sisa}")

        # Grafik batang 2D
        st.subheader("📊 Grafik Batang 2D: Nilai f(x, y, z) dan Turunan Parsial")
        labels = ['f(x, y, z)', '∂f/∂x', '∂f/∂y', '∂f/∂z']
        values = [float(f_val), float(fx_val), float(fy_val), float(fz_val)]
        bar_colors = ['royalblue', 'tomato', 'orange', 'seagreen']

        fig, ax = plt.subplots()
        ax.bar(labels, values, color=bar_colors)
        ax.set_ylabel("Nilai")
        ax.set_title("Hasil Evaluasi di Titik (x₀, y₀, z₀)")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
