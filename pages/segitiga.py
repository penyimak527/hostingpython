import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
  Ini adalah aplikasi menghitung luas segitiga sederhana
         """)

alas = st.number_input('masukkan alas ', 0);
tinggi = st.number_input('masukkan tinggi' , 0)
hitung = st.button("hitung luas");

if(hitung):
    luassegitiga = 1/2 * alas * tinggi
    st.success(f"luasnya adalah {luassegitiga} cm" )
    st.balloons();

