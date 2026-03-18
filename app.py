import streamlit as st
import requests
import urllib3

# 학교 네트워크 보안 오류(SSL) 무시 설정
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="나의 가치관 알아보기", page_icon="📚")

st.markdown("""
    <style>
    .stRadio [role=radiogroup]{gap: 10px;}
    .stButton>button {background-color: #4A90E2; color: white; font-weight: bold; height: 3em; border-radius: 10px;}
    .story-box {background-color: #f0f7ff; padding: 25px; border-radius: 15px; border-left: 8px solid #4A90E2; line-height: 1.8; font-size: 1.1em;}
    .analysis-card {padding: 25px; border-radius: 20px; background-color: #ffffff; border: 2px solid #e0e0e0; margin-top: 20px; line-height: 1.7;}
    .highlight {color: #4A90E2; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

st.title("📚 나의 가치관 알아보기")
st.write("안녕 친구들! 오늘 우리는 흥미로운 이야기를 통해 내 마음속 '진짜 우선순위'를 찾아볼 거예요.")
st.divider()

# 2. 선생님의 구글 배포 URL (기존 주소 그대로 사용)
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxkTPc56bkPvVfzcMLKAbtwfAQX59i6u5pLnrCRbQISWl52CEi5NiZMHwdEPXmiOAmhvQ/exec"

# 3. 입력 폼 시작
with st.container():
    st.subheader("📍 기본 정보")
    col1, col2 = st.columns(2)
    with col1:
        student_id = st.text_input("학번 (4자리)", placeholder="예: 2401", max_chars=4)
    with col2:
        name = st.text_input("이름", placeholder="이름을 입력하세요")

st.divider()

st.markdown("### 📖 오늘의 이야기: 어떤 선택")
st.markdown("""
<div class="story-box">
결혼을 약속한 연인 <b>A와 B</b>. B는 결혼 자금을 위해 섬으로 떠났지만 소식이 끊깁니다. 
걱정된 A는 섬에 가려 하지만 돈이 없었고, <b>뱃사공 C</b>는 "돈 없이는 절대 배를 태워줄 수 없다"며 외면합니다. 
이때 <b>부자 D</b>가 도움을 주는 조건으로 부적절한 제안을 하고, 절박한 A는 이를 받아들입니다. 
우여곡절 끝에 섬에서 B를 만난 A는 결혼 준비를 시작하지만, 비밀을 안 <b>친구 E</b>가 B에게 사실을 폭로합니다. 
분노한 B는 이별을 고하고 떠나버립니다. 
슬퍼하는 A 앞에 짝사랑하던 <b>F</b>가 나타나 "모든 것을 이해할 수 있다"며 고백하고, 둘은 연인이 됩니다.
</div>
""", unsafe_allow_html=True)

st.divider()

with st.form(key='ethics_test'):
    st.subheader("🕵️ STEP 1. 인물 분석")
    q1 = st.selectbox("1. 이 이야기에서 '가장 나쁜 사람'은 누구인가요?", 
                    ["선택하세요", "A(약속을 깬 연인)", "B(분노하며 떠난 연인)", "C(냉정한 뱃사공)", "D(유혹한 부자)", "E(비밀을 폭로한 친구)", "F(과거를 덮어준 짝사랑)"])
    q1_reason = st.text_area("그렇게 생각한 구체적인 이유는?")
    
    q2 = st.selectbox("2. 그나마 '가장 덜 나쁜(착한) 사람'은 누구인가요?", ["선택하세요", "A", "B", "C", "D", "E", "F"])
    
    st.divider()
    st.subheader("⚖️ STEP 2. 가치관 밸런스 게임")
    d1 = st.radio("Q1. 친구의 컨닝을 목격했다면?", ["우정을 위해 침묵한다", "정직을 위해 알린다"])
    d2 = st.radio("Q2. 굶주린 아이를 위한 도둑질은?", ["범죄이므로 절대 안 된다", "사정이 있으니 이해된다"])
    d3 = st.radio("Q3. 조별 과제 무임승차 친구의 이름은?", ["팀워크를 위해 넣는다", "공정성을 위해 뺀다"])
    d4 = st.radio("Q4. 친구와의 약속 vs 큰 돈을 벌 기회?", ["약속이 우선이다", "실익이 우선이다"])
    d5 = st.radio("Q5. 좋은 결과를 위해서라면 작은 거짓말은?", ["결과가 중요하다", "정직한 과정이 중요하다"])

    submit = st.form_submit_button(label='📊 심층 분석 결과 확인하기')

# 4. 분석 결과 및 데이터 전송
if submit:
    if name and student_id and q1 != "선택하세요":
        data = {"name": f"{student_id} {name}", "mbti": q1[0], "intro": f"이유:{q1_reason}"}
        
        try:
            requests.post(WEB_APP_URL, json=data, verify=False)
            st.balloons()
            
            # --- 심층 분석 로직 시작 ---
            st.markdown("---")
            st.header(f"🕵️ {name}님의 가치관 리포트")
            
            # 인물별 상세 분석 데이터
            analysis_data = {
                "A": {
                    "title": "사랑과 신뢰의 수호자",
                    "desc": "당신은 인간관계에서 **'변치 않는 믿음'**을 가장 고귀한 가치로 여깁니다. 아무리 절박한 상황이라도 사랑하는 사람과의 약속을 깬 A의 행동을 용납하지 못하는군요. 당신은 '결과가 수단을 정당화할 수 없다'고 믿는 원칙주의적인 면모를 가지고 있습니다.",
                    "advice": "주변 사람들에게 신뢰받는 타입이지만, 때로는 타인의 피치 못할 사정에 조금 더 유연해질 필요가 있어요."
                },
                "B": {
                    "title": "명예와 자부심의 수호자",
                    "desc": "당신은 **'자신의 당당함'**과 명예를 생명처럼 소중히 여깁니다. 결과적으로는 도움을 받았더라도, 그 과정에서 수치심을 느끼게 된 B의 분노에 깊이 공감하고 있네요. 당신은 내면의 자존감을 지키는 일을 인생의 최우선 순위에 두는 분입니다.",
                    "advice": "스스로에게 엄격한 만큼 타인에게도 엄격할 수 있어요. 가끔은 '완벽하지 않은 모습'도 수용해 보세요."
                },
                "C": {
                    "title": "공정과 원칙의 관리자",
                    "desc": "당신은 **'정당한 대가와 규칙'**이 사회를 지탱하는 힘이라고 믿습니다. 사적인 감정이나 안타까운 사정 때문에 원칙(뱃값)을 어기는 것을 가장 큰 무질서로 보시는군요. 당신은 매우 이성적이고 공사 구분이 확실한 리더 타입입니다.",
                    "advice": "차가워 보일 수 있지만 누구보다 공정합니다. 따뜻한 공감 한마디를 섞어준다면 최고의 리더가 될 거예요."
                },
                "D": {
                    "title": "숭고한 도덕성의 감시자",
                    "desc": "당신은 **'도덕적 결백'**과 인간다운 도리를 가장 중시합니다. 힘든 처지에 놓인 사람을 돕기는커녕 자신의 이익(유혹)을 위해 이용한 D의 행동에 가장 큰 혐오감을 느끼는군요. 당신은 정의감이 매우 강하며 약자를 보호하고자 하는 따뜻한 심장을 가졌습니다.",
                    "advice": "세상의 부조리에 상처받기 쉽지만, 당신 같은 사람이 있어 세상이 더 깨끗해집니다."
                },
                "E": {
                    "title": "우정과 진실의 감별사",
                    "desc": "당신은 **'진실한 관계'**를 무엇보다 소중하게 생각합니다. 설령 그것이 아픈 진실일지라도 감추는 것은 배신이라고 느끼는군요. 하지만 친구의 비밀을 폭로한 E를 가장 나쁘게 보았다면, 당신은 '의리'를 '진실'보다 더 상위의 가치로 두는 사람입니다.",
                    "advice": "입이 무겁고 의리가 강해 친구들이 믿고 의지하는 사람입니다. 정직과 배려 사이의 균형을 잘 잡아보세요."
                },
                "F": {
                    "title": "정의와 인과응보의 실현자",
                    "desc": "당신은 **'잘못에 대한 책임'**을 명확히 하는 것이 진정한 정의라고 믿습니다. 잘못을 저지른 사람(A)이 아무런 대가 없이 새로운 행복을 찾는 것을 공정하지 않다고 느끼시는군요. 당신은 논리적이며 인과관계를 중요하게 생각하는 분석가 타입입니다.",
                    "advice": "과거보다는 미래의 가능성에 조금 더 무게를 두어 보는 연습을 하면 마음이 한결 편해질 거예요."
                }
            }

            p_code = q1[0]
            res = analysis_data.get(p_code, {"title": "자유로운 영혼", "desc": "자신만의 독특한 가치관을 가지고 있습니다.", "advice": ""})

            st.markdown(f"""
            <div class="analysis-card">
                <h2 style='color:#4A90E2;'>✨ 당신은 [{res['title']}] 입니다.</h2>
                <p>{res['desc']}</p>
                <hr>
                <p><b>🔍 심층 분석 결과:</b></p>
                <ul>
                    <li>선택한 '가장 나쁜 인물'({q1})을 통해 볼 때, 당신은 <b>사회의 공정함</b>보다는 <b>개인의 진실성</b>에 더 높은 가치를 둡니다.</li>
                    <li>당신은 겉으로 보이는 결과보다 <b>'왜 그런 행동을 했는가?'</b>라는 동기를 중요하게 생각하는 경향이 있습니다.</li>
                </ul>
                <p style='font-style: italic; color: #666;'>💡 조언: {res['advice']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("분석 완료! 이 결과가 나의 평소 생각과 비슷한가요? 친구들과 비교해 봅시다!")

        except Exception as e:
            st.error(f"데이터 저장 중 오류가 발생했습니다: {e}")
    else:
        st.warning("학번, 이름, 그리고 '가장 나쁜 사람'을 꼭 선택해 주세요!")