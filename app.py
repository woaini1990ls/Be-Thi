{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
\
# C\uc0\u7845 u h\'ecnh giao di\u7879 n trang web\
st.set_page_config(page_title="That Khe AI Shadowing Coach", page_icon="\uc0\u55356 \u57252 ", layout="centered")\
\
st.title("\uc0\u55356 \u57252  That Khe AI Shadowing Coach")\
st.subheader("Ng\'e1ch \uc0\u273 \u7883 a ph\u432 \u417 ng: Luy\u7879 n nh\u7841 i gi\u7885 ng ti\u7871 ng Anh A2 c\u7921 c vui nh\u7897 n")\
st.markdown("---")\
\
# N\uc0\u7897 i dung b\'e0i h\u7885 c (C\'e2u chuy\u7879 n c\u7911 a C\u432 \u7901 ng v\u7873  Th\u7907  phi\'ean)\
sentences = [\
    "Welcome to That Khe! My name is Cuong, and I live here.",\
    "Every morning, when the sun is still sleeping, Uncle Ba is already awake.",\
    "He drinks hot tea and eats a big bowl of pho for superpower.",\
    "He takes bags of star anise and bamboo shoots to the border gate.",\
    "Uncle Ba cannot speak Chinese, but he uses crazy body language to sell everything.",\
    "Sometimes the mountain roads are slippery, but he never gives up.",\
    "At 4:00 PM, he rides back home, tired but happy with his family."\
]\
\
# Giao di\uc0\u7879 n ch\u7885 n c\'e2u \u273 \u7875  luy\u7879 n Shadowing\
st.markdown("### \uc0\u55357 \u56540  Ch\u7885 n c\'e2u \u273 \u7875  luy\u7879 n t\u7853 p (Shadowing):")\
selected_sentence = st.selectbox("Ch\uc0\u7885 n m\u7897 t c\'e2u trong b\'e0i:", sentences)\
\
# Hi\uc0\u7875 n th\u7883  c\'e2u \u273 \u432 \u7907 c ch\u7885 n\
st.info(f"**C\'e2u hi\uc0\u7879 n t\u7841 i:** \{selected_sentence\}")\
\
# H\uc0\u432 \u7899 ng d\u7851 n luy\u7879 n t\u7853 p\
st.markdown("""\
**\uc0\u55357 \u56481  H\u432 \u7899 ng d\u7851 n c\'e1ch luy\u7879 n Shadowing 100% Free:**\
1. **Nghe m\uc0\u7851 u:** B\u7845 m n\'fat b\'ean d\u432 \u7899 i \u273 \u7875  nghe tr\'ecnh duy\u7879 t \u273 \u7885 c m\u7851 u c\'e2u.\
2. **Nh\uc0\u7841 i gi\u7885 ng:** \u272 \u7885 c to l\u7841 i c\'e2u \u273 \'f3 theo \u273 \'fang ng\u7919  \u273 i\u7879 u.\
""")\
\
# T\'edch h\uc0\u7907 p Web Speech API (Text-to-Speech) b\u7857 ng HTML/JS \u273 \u417 n gi\u7843 n nh\'fang trong Streamlit\
tts_html = f"""\
<div style="margin: 20px 0;">\
    <button onclick="speakText()" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">\uc0\u55357 \u56586  Nghe c\'e2u m\u7851 u (Listen)</button>\
</div>\
\
<script>\
function speakText() \{\{\
    const text = "\{selected_sentence\}";\
    const utterance = new SpeechSynthesisUtterance(text);\
    utterance.lang = 'en-US';\
    utterance.rate = 0.9; // T\uc0\u7889 c \u273 \u7897  ch\u7853 m v\u7915 a ph\u7843 i cho c\u7845 p \u273 \u7897  A2\
    window.speechSynthesis.speak(utterance);\
\}\}\
</script>\
"""\
\
st.markdown(tts_html, unsafe_allow_html=True)\
\
st.markdown("---")\
st.markdown("### \uc0\u55356 \u57241 \u65039  Ghi \'e2m gi\u7885 ng \u273 \u7885 c c\u7911 a b\u7841 n")\
st.markdown("B\uc0\u7841 n c\'f3 th\u7875  ghi \'e2m tr\u7921 c ti\u7871 p b\u7857 ng micro c\u7911 a \u273 i\u7879 n tho\u7841 i ho\u7863 c m\'e1y t\'ednh \u273 \u7875  ki\u7875 m tra ph\u7843 n x\u7841 :")\
\
# T\'ednh n\uc0\u259 ng ghi \'e2m t\'edch h\u7907 p s\u7861 n c\u7911 a Streamlit\
audio_value = st.audio_input("B\uc0\u7845 m v\'e0o micro \u273 \u7875  ghi \'e2m gi\u7885 ng c\u7911 a b\u7841 n:")\
\
if audio_value is not None:\
    st.success("\uc0\u10024  \u272 \'e3 ghi \'e2m th\'e0nh c\'f4ng! H\'e3y nghe l\u7841 i \u273 \u7875  so s\'e1nh v\u7899 i b\u7843 n g\u7889 c nh\'e9:")\
    st.audio(audio_value)\
\
st.markdown("---")\
st.markdown("<p style='text-align: center; color: gray;'>Ph\'e1t tri\uc0\u7875 n cho c\u7897 ng \u273 \u7891 ng gi\'e1o d\u7909 c Th\u7845 t Kh\'ea | 100% Free & No-Code</p>", unsafe_allow_html=True)}