import streamlit as st
st.title('Web thử')
col1,col2,col3, = st.columns(3)
with col1:
    a = st.number_input('a')
with col2:
    op= st.radio('Phép toán',('\+','\-','x',':'),horizontal=True)
with col3:
    b = st.number_input('b')

res = st.number_input('Nhập kết quả')
if st.button('Kiểm tra'):
    if op == '\\+': result = a+b
    elif op == '\\-': result = a - b
    elif op == 'x': result = a*b
    elif op == ':': result = a/b
    if result == res:
        st.success('Chính xác')
        st.balloons()
    else:
        st.error(f'Sai, đáp án đúng là {result}')
        st.snow()
