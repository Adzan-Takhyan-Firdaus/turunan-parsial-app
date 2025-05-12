import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def tampilkan_turunan_2var():
    st.title("📘 Aplikasi Turunan Parsial 2 Variabel")

    fungsi_str = st.text_input("Masukkan fungsi f(x, y):", "x**2 + y**2")
    x, y = sp.symbols('x y')

    try:
        f = sp.sympify(fungsi_str)
        fx = sp.diff(f, x)
        fy = sp.diff(f, y)

        st.latex(f"f(x, y) = {sp.latex(f)}")
        st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(fx)}")
        st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(fy)}")

        x0 = st.number_input("Nilai x₀", value=1.0)
        y0 = st.number_input("Nilai y₀", value=1.0)

        f_val = f.subs({x: x0, y: y0})
        fx_val = fx.subs({x: x0, y: y0})
        fy_val = fy.subs({x: x0, y: y0})

        st.write(f"f({x0}, {y0}) = {f_val}")
        st.write(f"Gradien: ({fx_val}, {fy_val})")

        if st.session_state.get("trial"):
            st.session_state["trial_count"] += 1
            sisa = 3 - st.session_state["trial_count"]
            st.info(f"Sisa penggunaan trial: {sisa}")

        x_vals = np.linspace(x0 - 2, x0 + 2, 50)
        y_vals = np.linspace(y0 - 2, y0 + 2, 50)
        X, Y = np.meshgrid(x_vals, y_vals)
        Z = sp.lambdify((x, y), f, 'numpy')(X, Y)
        Z_tangent = float(f_val) + float(fx_val)*(X - x0) + float(fy_val)*(Y - y0)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')
        ax.plot_surface(X, Y, Z_tangent, alpha=0.5, color='red')
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
