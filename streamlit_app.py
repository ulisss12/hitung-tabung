import streamlit as st
import math, time

st.title("menghitung :blue[volume tabung] :rocket:")


r = st.number_input("masukan jari - jari (cm):",0)
t = st.number_input("masukan tinggi (cm):",0)

if st.button("hitung volume", type="primary"):
  loading = st.progres(0)
  for i in range(100):
    time.sleep(0.01)
    loading.prgres(i+1)
    
  v = math.pi*(r**2)*t
  st.success(f"volume tabung adalah (v:.2f)")
  
