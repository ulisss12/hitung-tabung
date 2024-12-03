import streamlit as st

st.title("menghitung :blue[volume tabung] :rocket:")


r = st.number_input("masukan jari - jari (cm):",0)
t = st.number_input("masukan tinggi (cm):",0)

if st.button("menghitung volume", type="primary"):
  v = math.pi*(r**2)*t
  st.success(f"volume tabung adalah (v:.2f)")
  
