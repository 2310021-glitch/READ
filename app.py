import streamlit as st
from openai import OpenAI

# 페이지 제목 설정
st.title("📖 쉬어읽기 변환기")

# 스트림릿 Secrets에서 API 키를 불러와 OpenAI 클라이언트를 설정합니다.
# (설정창에 OPENAI_API_KEY가 반드시 등록되어 있어야 합니다!)
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except KeyError:
    st.error("API 키를 찾을 수 없습니다. Streamlit Settings의 Secrets에 'OPENAI_API_KEY'를 등록해주세요.")
    st.stop()

# 사용자로부터 텍스트 입력 받기
text = st.text_area("변환할 문장을 입력하세요", placeholder="예: 오늘날 인공지능 기술은 다양한 산업 분야에서 빠르게 확산되고 있습니다.")

if st.button("변환하기"):
    if not text.strip():
        st.warning("문장을 입력해주세요.")
    else:
        with st.spinner("AI가 문장을 분석 중입니다..."):
            try:
                # 에러의 원인이었던 모델명을 'gpt-4o-mini'로 수정했습니다.
                response = client.chat.completions.create(
                    model="gpt-4o-mini", 
                    messages=[
                        {"role": "system", "content": "당신은 한국어 독해 전문가입니다. 입력된 문장을 의미 단위로 끊어 읽기 좋게 '/' 표시를 넣어 변환해 주세요."},
                        {"role": "user", "content": f"다음 문장을 쉬어읽기 단위로 '/'로 나눠주세요:\n\n{text}"}
                    ]
                )
                
                # 결과 출력
                result = response.choices[0].message.content
                st.subheader("✅ 변환 결과")
                st.success(result)
                
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
                st.info("OpenAI 계정에 잔액(Credit)이 충분한지 확인해 보세요.")
