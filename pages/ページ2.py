import streamlit as st
import datetime

with st.form(key='profile_form'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

#     # セレクトボックス
#     age_category = st.selectbox(
#         '年齢層',
#         ('子供(18才未満)','大人(18才以上)'))

    # ボタン
    age_category = st.radio(
        '年齢層',
        ('子供(18才未満)','大人(18才以上)'))

    # 複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ','読書','プログラミング','アニメ','釣り'))
    
    # チェックボックス
    mail_subscribe = st.checkbox('メールマガジンを購読する')

    # スライダー
    height = st.slider('身長', min_value=110, max_value=210)

    # 日付
    d = st.date_input('誕生日を入力してください。', datetime.date(1998, 2, 16))

    # カラーピッカー
    color = st.color_picker('テーマカラー', '#00f900')

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    
    if submit_btn:
            st.text(f'ようこそ！{name}さん！{address}に本を送りました')
            st.text(f'年齢層:{age_category}')
            st.text(f'趣味:{", ".join(hobby)}')
