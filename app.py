import streamlit as st
from openai import OpenAI

st.title("📖 쉬어읽기 변환기")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

text = st.text_area("문장을 입력하세요")

if st.button("변환하기"):
    if text.strip() == "":
        st.warning("문장을 입력해주세요.")
    else:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": f"""
다음 문장을 쉬어읽기 단위로 '/'로 나눠주세요:

{text}
"""}
            ]
        )
        result = response.choices[0].message.content
        st.write(result)