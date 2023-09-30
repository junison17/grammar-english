
import streamlit as st
import openai
import os
import base64

# Setting up OpenAI API key
api_key = os.environ.get("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("OPENAI_API_KEY 환경 변수를 설정해주세요.")
openai.api_key = api_key

# Custom CSS for background image and styling
st.markdown(
    f'''
    <style>
        .reportview-container {{
            background: url(data:img.jpg;base64,{base64.b64encode(open("C:/grammar-english/img.jpg", "rb").read()).decode()}) no-repeat center center fixed;
            background-size: cover;
        }}
        .main .block-container {{
            background-color: rgba(34, 34, 34, 0.6);
            color: white;
            opacity: 0.8;
        }}
        textarea, input {{
            background-color: rgba(255, 255, 255, 0.8) !important;
        }}
        button {{
            background-color: #cf48d6 !important;
            color: white !important;
        }}
    </style>
    ''',
    unsafe_allow_html=True,
)

# Main Application
st.title("영어문제출제 사이트")
st.write("문제를 만드세요")
text = st.text_area("", height=200)

st.write("어느 문제 유형으로 만드겠습니까?")
language = st.text_input("")

if st.button("문제 만들기"):
    prompt = f"If you ask questions in Korean, translate them into English and understand it in English. Make an English grammar problem with the type of {text}\n\n You are a globally capable English teacher. You made and published TOEIC workbooks for middle school, high school, and college students in Korea.Make an English question, make a split line at the bottom, Write down the correct answer in the beginning of the explanation.translate the explanation into Korean and write it in detail.Write down" 
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "If you ask questions in Korean, translate them into English and understand it in English.You are an English grammar expert who makes TOEIC and TOEFL workbooks in Korea. And you are an English teacher who teaches high school students."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=2000,
    )
    result = response["choices"][0]["message"]["content"]
    st.write("결과물 보기")
    st.text_area("", value=result, height=200)
