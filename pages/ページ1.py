import streamlit as st
import datetime

code = '''
import streamlit as st

st.title('ムサシアプリ')
'''
# 
st.code(code, language='python')

print('feature/aで修正しました')
print('feature/bの追加')