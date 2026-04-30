import streamlit as st
import google.generativeai as genai

st.title("📖 쉬어읽기 변환기")

# 구글 API 키 설정
try:
    # 이 부분들의 줄 맞춤(들여쓰기)이 정확해야 합니다.
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Secrets 설정 혹은 API 키를 확인해주세요.")
    st.stop()

text = st.text_area("문장을 입력하세요")

if st.button("변환하기"):
    if not text.strip():
        st.warning("문장을 입력해주세요.")
    else:
        with st.spinner("AI가 분석 중입니다..."):
            try:
                response = model.generate_content(f"다음 문장을 쉬어읽기 단위로 '/'로 나눠주세요: {text}")
                st.success(response.text)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
