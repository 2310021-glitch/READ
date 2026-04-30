import streamlit as st
import google.generativeai as genai

st.title("📖 쉬어읽기 변환기 (무료 버전)")

# 구글 API 키 설정
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
   model = genai.GenerativeModel('models/gemini-1.5-flash')
except:
    st.error("Secrets에 'GOOGLE_API_KEY'를 등록해주세요.")
    st.stop()

text = st.text_area("문장을 입력하세요")

if st.button("변환하기"):
    if not text.strip():
        st.warning("문장을 입력해주세요.")
    else:
        with st.spinner("제미나이가 분석 중..."):
            response = model.generate_content(f"다음 문장을 쉬어읽기 단위로 '/'로 나눠주세요: {text}")
            st.success(response.text)
