import streamlit as st
import requests

# 1. 페이지 설정
st.set_page_config(page_title="도덕 수행평가: 가치관 테스트", page_icon="⚖️")

# 디자인 (중학생들이 좋아할 만한 깔끔한 스타일)
st.markdown("""
    <style>
    .stRadio [role=radiogroup]{gap: 15px;}
    .stButton>button {background-color: #4CAF50; color: white; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

st.title("🔍 '나'를 찾는 가치관 탐구")
st.write("우리 반 친구들, 반가워요! 평소 나의 생각은 어떤지 솔직하게 답해봅시다.")
st.divider()

# 2. 선생님의 구글 배포 URL (정확히 입력됨)
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxkTPc56bkPvVfzcMLKAbtwfAQX59i6u5pLnrCRbQISWl52CEi5NiZMHwdEPXmiOAmhvQ/exec"

# 3. 입력 폼 시작
with st.form(key='psych_test'):
    st.subheader("📍 기본 정보")
    col1, col2 = st.columns(2)
    with col1:
        student_id = st.text_input("학번 (예: 20101)", placeholder="5자리 숫자")
    with col2:
        name = st.text_input("이름", placeholder="이름을 입력하세요")
    
    st.divider()
    
    st.subheader("STEP 1. 인물 분석")
    st.info("우리가 수업 시간에 본 6명의 인물(A~F) 중 선택하세요.")
    
    q1 = st.selectbox("1. 행동이 가장 나빠서 도저히 이해가 안 가는 사람은?", ["선택하세요", "A", "B", "C", "D", "E", "F"])
    q2 = st.selectbox("2. 상황이 어찌 되었든 마음씨가 가장 착한 사람은?", ["선택하세요", "A", "B", "C", "D", "E", "F"])
    
    st.write("**3. 내가 만약 주인공이라면, 가장 공감되는 인물은?**")
    q4 = st.radio("공감되는 사람 선택", ["A", "B", "C", "D", "E", "F"], horizontal=True, label_visibility="collapsed")
    
    q5 = st.text_input("4. 내가 1번 인물(가장 나쁜 사람)을 선택한 결정적인 이유는?")
    
    st.divider()
    
    st.subheader("STEP 2. 최후의 선택 (하나만 골라보세요!)")
    
    st.write("**💡 질문 1. 결과와 과정**")
    d1 = st.radio("친구를 돕기 위해 거짓말을 해서 결국 도와줬다면?", 
                ["도와줬으니 결과적으로 잘한 일이다", "아무리 도와주려 했어도 거짓말은 잘못이다"])
    
    st.write("**💡 질문 2. 개인과 우리**")
    d2 = st.radio("조별 과제에서 한 친구가 아파서 빠졌을 때, 우리 조의 점수는?", 
                ["아픈 건 어쩔 수 없으니 다 같이 점수를 낮게 받아도 된다", "아프더라도 맡은 일은 해야 다른 조원들이 피해를 안 본다"])
    
    st.write("**💡 질문 3. 규칙과 사정 (중2 눈높이)**")
    d3 = st.radio("배가 너무 고파서 빵을 훔친 아이, 경찰관인 당신은?", 
                ["법은 모두에게 공평해야 하므로 잘못한 만큼 벌을 주어야 한다", "배고픈 사정이 딱하니 이번 한 번은 훈계만 하고 보내준다"])

    submit = st.form_submit_button(label='📊 결과 확인 및 제출하기')

# 4. 분석 로직 및 전송
if submit:
    if name and student_id and q1 != "선택하세요" and q2 != "선택하세요":
        # 구글 시트로 보낼 데이터
        data = {
            "name": f"{student_id} {name}", # 학번과 이름을 합쳐서 '성함'칸에 넣음
            "mbti": f"나쁨:{q1}/착함:{q2}", 
            "intro": f"이유:{q5} / 딜레마:{d1}, {d2}, {d3}"
        }
        
        try:
            response = requests.post(WEB_APP_URL, json=data)
            if response.status_code == 200:
                st.balloons()
                st.success(f"{name} 학생, 답변이 잘 저장되었습니다!")
                
                # --- 가치관 분석 결과창 ---
                st.markdown("---")
                st.header(f"📑 {name}님의 가치관 분석 결과")
                
                # 분석 멘트 생성 (간단한 로직)
                analysis_text = ""
                if d3 == "법은 모두에게 공평해야 하므로 잘못한 만큼 벌을 주어야 한다":
                    analysis_text += "당신은 사회의 **'공공의 규칙과 정의'**를 아주 소중하게 생각하는 원칙주의자입니다. "
                else:
                    analysis_text += "당신은 사람의 **'따뜻한 마음과 상황'**을 먼저 살피는 공감 능력이 뛰어난 사람입니다. "
                
                if d1 == "아무리 도와주려 했어도 거짓말은 잘못이다":
                    analysis_text += "또한, 결과보다는 **'옳은 과정'**이 인생에서 더 중요하다고 믿고 있네요."
                else:
                    analysis_text += "또한, 목적을 이루기 위한 **'실용적인 결과'**를 중요하게 생각하는 편입니다."
                
                st.subheader(f"당신은 '{analysis_text}'")
                st.info(f"선택하신 {q1}번 인물에 대한 생각과 {q2}번 인물에 대한 지향점은 다음 수업 시간에 친구들과 함께 이야기 나눠봅시다!")
            else:
                st.error("전송에 실패했습니다. 선생님께 말씀드려주세요.")
        except Exception as e:
            st.error(f"연결 오류: {e}")
    else:
        st.warning("학번, 이름, 그리고 선택 질문들에 빠짐없이 답해주세요!")