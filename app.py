import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(page_title="쉬어읽기 변환기", page_icon="📖", layout="centered")

# 디자인 개선을 위한 CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 AI 쉬어읽기 변환기")
st.info("문장을 입력하면 AI가 자연스럽게 쉬어 읽을 부분을 '/'로 표시해 드립니다.")

# 1. API 키 설정
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("⚠️ Streamlit Secrets에 'GOOGLE_API_KEY'가 설정되지 않았습니다. 설정 후 다시 시도해주세요.")
    st.stop()

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # 404 에러 방지를 위해 가장 보편적인 명칭 사용
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"설정 오류가 발생했습니다: {e}")
    st.stop()

# 2. 사용자 입력부
text = st.text_area("변환할 문장을 입력하세요", 
                   placeholder="예: 아버지가 방에 들어가신다.", 
                   height=200)

# 3. 실행 버튼
if st.button("AI 분석 및 변환 시작"):
    if not text.strip():
        st.warning("내용을 입력해 주세요!")
    else:
        with st.spinner("AI가 문장을 분석하고 있습니다..."):
            try:
                # AI에게 전달할 명확한 지시문
                prompt = (
                    "너는 한국어 낭독 및 아나운싱 전문가야. "
                    "전달된 문장을 의미 단위로 끊어서, 읽
