import streamlit as st
import requests
import urllib3
import urllib.parse

# 학교 네트워크 보안 오류(SSL) 무시 설정
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. 페이지 설정 및 디자인 (선생님 원본 유지)
st.set_page_config(page_title="나의 가치관 심층 리포트", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="st-"] {
        font-size: 1.15rem !important; 
        font-family: 'Pretendard', sans-serif;
    }
    .stRadio [role=radiogroup]{gap: 15px;}
    .stRadio label {font-size: 1.15rem !important; line-height: 1.6;} 
    div.stMarkdown p {font-size: 1.15rem !important;} 
    .stButton>button {
        background-color: #4A90E2; color: white; font-weight: bold; 
        width: 100%; height: 3.5em; border-radius: 15px; font-size: 1.2rem;
        margin-top: 20px;
    }
    .story-box {
        background-color: #f0f7ff; padding: 25px; border-radius: 15px; 
        border-left: 8px solid #4A90E2; line-height: 1.9; font-size: 1.1rem;
        margin-bottom: 30px;
    }
    .analysis-card {
        padding: 30px; border-radius: 25px; background-color: #ffffff; 
        border: 3px solid #4A90E2; margin-top: 25px; line-height: 1.8;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📚 나의 가치관 심층 알아보기")
st.write("도덕시간 가치관 심리테스트! 결과를 보고 교과서 15페이지 활동1번을 작성합니다.")
st.divider()

# 2. 이야기 본문 (선생님 원본 100% 동일)
st.subheader("📖 [읽기 자료] 어느 연인의 이야기")
st.markdown("""
<div class="story-box">
    결혼을 약속한 연인 <b>A와 B</b>. B는 결혼 자금을 위해 섬으로 떠났지만 소식이 끊깁니다.
걱정된 A는 섬에 가려 하지만 돈이 없었고, <b>뱃사공 C</b>는 "돈 없이는 절대 배를 태워줄 수 없다"며 외면합니다.
이때 <b>부자 D</b>가 도움을 주는 조건으로 부적절한 제안을 하고, 절박한 A는 이를 받아들입니다.
우여곡절 끝에 섬에서 B를 만난 A는 결혼 준비를 시작하지만, 비밀을 안 <b>친구 E</b>가 B에게 사실을 폭로합니다.
분노한 B는 이별을 고하고 떠나버립니다. 슬퍼하는 A 앞에 짝사랑하던 <b>F</b>가 나타나 "모든 것을 이해할 수 있다"며 고백하고, 둘은 연인이 됩니다.
</div>
""", unsafe_allow_html=True)

# 구글 앱스 스크립트 배포 URL (선생님 것으로 교체 확인)
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwf4gA-TqELeI5vXSx5tLsUkavu1xWEfpNOScaElDf-w1N59hzlcNWq4kaCHfHHsORaXw/exec"

# 3. 설문 폼 (선생님 질문지 구성 100% 동일)
with st.form(key='ethics_test_final_v4'):
    st.subheader("📍 기본 정보 입력")
    col1, col2 = st.columns(2)
    with col1:
        student_id = st.text_input("학번 (4자리)", placeholder="예: 2401", max_chars=4)
    with col2:
        name = st.text_input("이름", placeholder="이름을 입력하세요")

    st.divider()
    st.subheader("🕵️ STEP 1. 인물 분석")
    q1_choice = st.selectbox("1. 이 이야기에서 '가장 나쁜 사람'은 누구인가요?", 
                    ["선택하세요", "A(약속을 깬 연인)", "B(분노하며 떠난 연인)", "C(냉정한 뱃사공)", "D(유혹한 부자)", "E(비밀을 폭로한 친구)", "F(과거를 덮어준 짝사랑)"])
    q1_reason = st.text_area("그렇게 생각한 구체적인 이유는 무엇인가요?")
    q2_choice = st.selectbox("2. 그나마 '가장 덜 나쁜(착한) 사람'은 누구인가요?", ["선택하세요", "A", "B", "C", "D", "E", "F"])

    st.divider()
    st.subheader("⚖️ STEP 2. 가치관 딜레마: 당신의 선택은?")
    
    d1 = st.radio("Q1. [단톡방 사건] 단톡방에 나랑 조금 친한 어떤 친구를 비하하는 분위기가 형성되었다면?", ["나도 같이 동조하며 분위기에 맞춘다", "의리상 친구를 감싸주고 싶지만, 일단은 아무 말 없이 지켜본다", "용기 있게 비하 발언을 멈추라고 말하며 친구를 방어한다"])
    d2 = st.radio("Q2. [AI 수행평가] 우리 모둠 친구가 AI로 과제를 해왔다. 선생님은 모르지만, 나는 알고 있는 상황이라면?", ["모둠의 이익이 먼저! 비밀로 하고 1등 점수를 받는다", "친구의 노력이 가상하므로 그냥 인정해준다", "이건 공정하지 않다. 친구에게 다시 해오라고 설득하거나 선생님께 알린다"])
    d3 = st.radio("Q3. [절친의 뒷담화] 베프가 사실과 전혀 다른 오해로 나에게 다른 친구의 뒷담화를 한다면?", ["친구의 기분을 맞춰주기 위해 알면서도 맞장구쳐준다", "중간에서 난처해지기 싫으니 그냥 듣고만 있는다", "진실은 알려줘야지! 친구가 민망하지 않게 사실관계를 정정해준다"])
    d4 = st.radio("Q4. [카드 결제 오류] 8,000원 결제가 800원만 된 것을 알게 되었다면?", ["운이 좋았다고 생각하며 그냥 넘어간다", "귀찮기도 하고 이미 멀리 왔으니 다음에 기회 되면 말한다", "가게 주인이 손해를 보게 되므로 다시 가서 결제한다"])
    d5 = st.radio("Q5. [급식 새치기] 급식줄을 서 있는데 내 앞의 친구가 자신의 친구 무리를 슬쩍 끼워줬다면?", ["친구들끼리 그럴 수 있지. 나도 내 친구를 내 앞에 끼운다", "기분은 나쁘지만 싸우기 싫어서 꾹 참는다", "큰 소리로 새치기하지 말라고 당당하게 말한다"])
    d6 = st.radio("Q6. [SNS의 거짓말] 나를 초등학교때 괴롭히던 애가 잘못 없는 일로 마녀사냥을 당하고 있다면?", ["쌤통이다! 가만히 있으면서 상황을 즐긴다", "엮이기 싫다. 내가 나설 일은 아니라고 생각하며 무시한다", "아무리 싫어도 거짓으로 욕먹는 건 아니지. 진실을 말해준다"])

    submit = st.form_submit_button(label='📊 결과 확인 및 제출하기')

if submit:
    if name and student_id and q1_choice != "선택하세요":
        worst_char = q1_choice[0]
        best_char = q2_choice[0] if q2_choice != "선택하세요" else "X"
        score_j = sum(1 for a in [d1, d2, d3, d4, d5, d6] if any(x in a for x in ["방어한다", "공정하지", "정정해준다", "다시 가서", "당당하게", "진실을 말해준다"]))
        
        title_map = {"A": "사랑과 신뢰", "B": "명예와 자존", "C": "원칙과 공정", "D": "도덕적 순수", "E": "의리와 진실", "F": "헌신과 책임"}
        user_title = title_map.get(worst_char, "자유로운 영혼")

        # ✅ [수정] 학번과 이름을 분리하여 전송
        params = {
            "student_id": student_id,  # 학번 단독 전송
            "name": name,              # 이름 단독 전송
            "worst": worst_char,
            "best": best_char,
            "reason": q1_reason,
            "score_j": score_j
        }
        
        final_url = f"{WEB_APP_URL}?{urllib.parse.urlencode(params)}"

        try:
            requests.get(final_url, verify=False, timeout=5) # POST 대신 GET 전송
            st.balloons()
            st.snow()

            # ✅ 심층 분석 강화 (700바이트 내외 상세 버전)
            if score_j >= 5:
                type_name = "🛡️ 강철의 정의 수호자"
                type_desc = f"{name}님은 어떤 유혹이나 압박 속에서도 '옳음'을 지켜내는 대나무 같은 사람입니다. 친구와의 의리나 눈앞의 이익보다 보편적인 정의와 정직을 최우선 가치로 여기시네요. 이러한 성격은 공동체에서 신뢰의 상징이 되지만, 때로는 자신의 기준이 너무 엄격하여 스스로나 타인을 지치게 할 수도 있습니다. 원칙을 지키는 그 당당함에 타인의 서툰 실수를 감싸줄 수 있는 너그러움을 한 뼘만 더한다면, 모두가 믿고 따르는 진정한 리더가 될 것입니다."
            elif score_j >= 4:
                type_name = "⚖️ 조화로운 균형가"
                type_desc = f"{name}님은 원칙과 인간관계 사이에서 최선의 답을 찾아내려 노력하는 합리적인 판단가입니다. 무조건적인 규칙 준수보다는 상황의 맥락을 살피고, 공동체에 가장 이로운 방향이 무엇인지 고민하는 균형 잡힌 시각을 가졌습니다. 갈등 상황에서도 감정에 휘둘리기보다 객관적인 사실을 바탕으로 중재하려는 태도는 주변을 편안하게 만듭니다. 지금처럼 공정함을 잃지 않으면서도 사람들의 마음을 다독이는 따뜻한 시선을 유지한다면 어디서든 환영받는 존재가 될 것입니다."
            elif score_j >= 2:
                type_name = "🤝 따뜻한 공감주의자"
                type_desc = f"{name}님은 차가운 규칙의 잣대보다 사람의 마음과 관계의 온기를 세상에서 가장 소중히 여깁니다. 누군가 마음 상하는 일을 방지하기 위해 때로는 손해를 감수하기도 하며, 타인의 아픔에 깊이 공감하고 위로하는 능력이 탁월하시네요. 주변 친구들이 {name}님 곁에서 편안함을 느끼는 이유이기도 합니다. 다만, 타인을 배려하느라 정작 중요한 원칙이나 자신의 정당한 권리를 놓칠 때가 있으니, 가끔은 '아닌 것'에 대해 당당하게 목소리를 내는 연습을 통해 스스로를 보호하는 힘을 길러보세요!"
            elif score_j == 1:
                type_name = "💡 전략적 현실주의자"
                type_desc = f"{name}님은 상황을 매우 냉철하고 효율적으로 판단하며 실질적인 해결책을 찾는 능력이 돋보입니다. 불필요한 도덕적 갈등에 에너지를 쏟기보다 현재 상황에서 가장 합리적인 이익이나 결과를 도출하는 데 집중하는 현실 감각을 갖추셨군요. 문제 해결 속도가 빠르고 실수가 적어 조직에서 매우 유능한 인재로 평가받을 것입니다. 다만, 효율성만을 쫓다 보면 주변 사람들의 감정을 간과할 수 있으니, 결과만큼이나 '과정의 정당성'과 '사람의 마음'에도 조금 더 관심을 기울여보시길 권합니다."
            else:
                type_name = "🌈 자유로운 탐험가"
                type_desc = f"{name}님은 틀에 박힌 생각이나 사회적 편견에 얽매이지 않고, 자신만의 독특하고 창의적인 시선으로 세상을 바라보는 분입니다. 고정관념에서 벗어난 {name}님의 판단은 때로 주변을 놀라게 하지만, 그것이 새로운 변화를 만드는 씨앗이 되기도 합니다. 규범보다는 자신의 직관과 상황에 따른 유연함을 믿는 모습은 매우 자유롭고 당당해 보입니다. 나만의 개성 있는 가치관을 소중히 가꾸어 나가되, 타인과 함께 살아가는 데 필요한 최소한의 약속들을 존중하는 마음을 더한다면 더 넓은 세상을 자유롭게 탐험할 수 있을 것입니다."

            st.markdown(f"""
            <div class="analysis-card">
                <h1 style='text-align: center;'>🕵️ {name}님의 가치관 리포트</h1>
                <hr>
                <h2 style='color:#4A90E2; text-align: center;'>"{type_name}"</h2>
                <div style='background-color: #f9f9f9; padding: 20px; border-radius: 15px;'>
                    <p style='font-size: 1.15rem; line-height: 1.8; text-align: justify;'>{type_desc}</p>
                </div>
                <hr>
                <p><b>🔍 인물 분석 기반 결과:</b><br>
                당신은 <b>{q1_choice}</b>를 가장 나쁜 인물로 꼽았습니다. 이는 삶에서 <b>[{user_title}]</b> 가치가 훼손되는 것을 가장 견디기 힘들어하기 때문입니다.</p>
                <p style='color: #666; font-size: 1rem; font-style: italic;'><b>" {q1_reason} "</b></p>
                <hr>
                <p style='text-align: center; color: #4A90E2; font-weight: bold;'>📊 나의 원칙 준수 지수: {score_j} / 6점</p>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"전송 시도 중 오류가 발생했습니다: {e}")
    else:
        st.warning("⚠️ 학번, 이름, 그리고 '가장 나쁜 사람' 선택은 필수입니다!")