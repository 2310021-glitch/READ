import streamlit as st
import google.generativeai as genai

st.title("📖 쉬어읽기 변환기")

# 구글 API 키 설정
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # 모델 이름을 가장 기본형인 'gemini-1.5-flash'로 설정합니다.
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"설정 오류: {e}")
    st.stop()

text = st.text_area("문장을 입력하세요", placeholder="여기에 문장을 입력하고 변환하기를 눌러주세요.")

if st.button("변환하기"):
    if not text.strip():
        st.warning("문장을 입력해주세요.")
    else:
        with st.spinner("AI가 분석 중입니다..."):
            try:
                # 여기서 에러가 나면 모델명을 'gemini-pro'로 바꿔서 시도해 볼 수도 있습니다.
                response = model.generate_content(f"다음 문장을 쉬어읽기 단위로 '/'로 나눠주세요: {text}")
                st.success(response.text)
            except Exception as e:
                st.error("오류가 발생했습니다. 모델 설정을 다시 확인 중입니다...")
                st.info(f"에러 상세내용: {e}")
