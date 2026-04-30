import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="쉬어읽기 변환기", page_icon="📖")
st.title("📖 쉬어읽기 변환기")

# 1. API 키 설정 및 모델 로드
try:
    if "GOOGLE_API_KEY" not in st.secrets:
        st.error("Streamlit Secrets에 'GOOGLE_API_KEY'가 설정되지 않았습니다.")
        st.stop()
        
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    # 모델명 앞에 'models/'를 명시적으로 붙여주는 것이 가장 확실합니다.
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error(f"설정 중 오류가 발생했습니다: {e}")
    st.stop()

# 2. UI 구성
text = st.text_area("문장을 입력하세요", placeholder="여기에 문장을 입력하고 변환하기를 눌러주세요.", height=200)

if st.button("변환하기", type="primary"):
    if not text.strip():
        st.warning("문장을 입력해주세요.")
    else:
        with st.spinner("AI가 분석 중입니다..."):
            try:
                # 프롬프트를 더 명확하게 수정
                prompt = f"너는 한국어 낭독 전문가야. 다음 문장을 숨이 차지 않게 의미 단위로 끊어서 '/' 표시를 넣어줘:\n\n{text}"
                response = model.generate_content(prompt)
                
                st.subheader("변환 결과")
                st.success(response.text)
            except Exception as e:
                # 404 에러가 계속나면 여기서 모델을 'gemini-1.5-pro'로 바꿔보라는 안내가 뜰 것입니다.
                st.error("AI 모델 응답 중 오류가 발생했습니다.")
                st.info(f"에러 상세: {e}")
