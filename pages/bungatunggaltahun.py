import streamlit as st
st.write("""
         # Selamat Datang di Project kedua 
         Penghitung Bunga Tunggal
         """);
# variable
uang = st.number_input("Masukkan sejumlah Uang", 0)
bunga = st.number_input("Masukkan bunga (%)", 0)
tahun = st.number_input("Masukkan tahun nya", 1)
btn = st.button("Hitung")

if(btn):
    hitung = uang * (bunga/100) * tahun
    total_formatted = f"{round(hitung):,}".replace(",", ".")

    st.success(f"hasil bunga tunggal dalam {tahun} adalah Rp {total_formatted}")
    st.balloons();


# halaman_lain = st.button("Hitung luas segitiga ?")
# if(halaman_lain):
#     st.session_state["halaman"] = "segitiga"