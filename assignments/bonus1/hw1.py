from cProfile import label
import streamlit as st
from snownlp import SnowNLP

# audio_file = open('myaudio.ogg', 'rb')
# audio_bytes = audio_file.read()

# st.audio(audio_bytes, format='audio/ogg', )



st.title('情感分析器')
st.write('請任意寫下一串中文字，機器會自動告訴您這句話的情感分數')
st.image('emotion.png',width = 350)

menu = ['Home', 'About']
choice = st.sidebar.selectbox("Menu", menu)

if choice == 'Home':
    st.subheader('Home')
    with st.form(key = 'nlpForm'):
        raw_text = st.text_area('輸入您的文字')
        submit_button = st.form_submit_button(label = '分析')

    if submit_button:
        st.info('Results')
        sentiment = SnowNLP(raw_text).sentiments
        # sentiment = Textblob(raw_text).sentiment
        st.write('情感分數： '+str(sentiment))
        if sentiment > 0.6:
            st.markdown('你是正向的 :smiley: ')
            st.balloons()
        elif (sentiment > 0.4) and (sentiment <= 0.6):
            st.markdown('你是中立的 😐 ')
        else: 
            st.markdown('你是負面的 :angry: ')
            st.snow()