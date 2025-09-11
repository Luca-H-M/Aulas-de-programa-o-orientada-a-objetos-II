import streamlit as st
from Retangulo import retangulo

class retanguloUI:
    def main():
        st.header("Cálculos com Retângulo")
        base = st.text_input("Valor da base")
        altura = st.text_input("Valor da altura")
        if st.button("Calcular"):
            x = float(base)
            y = float(altura)
            z = retangulo(x, y)

            st.write(retangulo.__str__())
