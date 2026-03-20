import streamlit as st
import requests
import urllib3

# 학교 네트워크 보안 오류(SSL) 무시 설정
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. 페이지 설정 및 디자인 (태블릿 최적화)
st.set_page_config(page_title="나의 가치관 심층 리포트", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    /* 태블릿 전용 글씨 크기 설정: 질문과 선택지 크기 통일 */
    html, body, [class*="st-"] {
        font-size: 1.15rem !important; 
        font-family: 'Pretendard', sans-serif;
    }
    .stRadio [role=radiogroup]{gap: 15px;}
    .stRadio label {font-size: 1.15rem !important; line-height: 1.6;} /* 선택지 크기 */
    div.stMarkdown p {font-size: 1.15rem !important;} /* 질문 및 본문 크기 */
    
    /* 디자인 요소 */
    .stButton>button {
        background-color: #4A90E2; color: white; font-weight: bold; 
        width: 100%; height: 3.5em; border-radius: 15px; font-size: 1.2rem;
        margin-top: 20px;
    }
    .analysis-card {
        padding: 30px; border-radius: 25px; background-color: #ffffff; 
        border: 3px solid #4A90E2; margin-top: 25px; line-height: 1.8;
    }
    .score-box {
        background-color: #f8f9fa; padding: 15px; border-radius: 10px;
        border-left: 5px solid #4A90E2; margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📚 나의 가치관 심층 알아보기")
st.write("안녕 친구들! 6가지 상황을 통해 나의 '진짜 속마음'과 '도덕적 가치'를 분석해볼게요.")
st.divider()

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxkTPc56bkPvVfzcMLKAbtwfAQX59i6u5pLnrCRbQISWl52CEi5NiZMHwdEPXmiOAmhvQ/exec"

with st.container():
    st.subheader("📍 기본 정보")
    col1, col2 = st.columns(2)
    with col1:
        student_id = st.text_input("학번 (4자리)", placeholder="예: 2401", max_chars=4)
    with col2:
        name = st.text_input("이름", placeholder="이름을 입력하세요")

st.divider()

with st.form(key='ethics_test'):
    st.subheader("🕵️ STEP 1. 인물 분석")
    q1 = st.selectbox("1. 이 이야기에서 '가장 나쁜 사람'은 누구인가요?", 
                    ["선택하세요", "A(약속을 깬 연인)", "B(분노하며 떠난 연인)", "C(냉정한 뱃사공)", "D(유혹한 부자)", "E(비밀을 폭로한 친구)", "F(과거를 덮어준 짝사랑)"])
    q1_reason = st.text_area("그렇게 생각한 구체적인 이유는 무엇인가요? (아이패드로 자세히 적어보세요)")
    
    q2 = st.selectbox("2. 그나마 '가장 덜 나쁜(착한) 사람'은 누구인가요?", ["선택하세요", "A", "B", "C", "D", "E", "F"])

    st.divider()
    st.subheader("⚖️ STEP 2. 가치관 딜레마: 당신의 선택은?")
    
    d1 = st.radio("Q1. [단톡방 사건] 우리 반 단톡방에서 누군가 친구 한 명을 저격하며 비하하는 메시지를 올렸어요. 분위기는 순식간에 동조하는 쪽으로 흘러가는데...", 
                  ["나도 같이 동조하며 분위기에 맞춘다 (소외될까 봐)", "의리상 친구를 감싸주고 싶지만, 일단은 아무 말 없이 상황을 지켜본다 (방관)", "용기 있게 비하 발언을 멈추라고 말하며 친구를 방어한다 (정의)", "개인적으로 그 친구에게 연락해 위로하지만, 단톡방에서는 티 내지 않는다 (현실적 타협)"])
    
    d2 = st.radio("Q2. [AI 수행평가] 우리 모둠 친구가 AI를 써서 과제를 완벽하게 해왔어요. 덕분에 우리 모둠은 1등 확정이지만, 정직하게 한 다른 모둠은 감점을 받게 됩니다.", 
                  ["모둠의 이익이 먼저! 비밀로 하고 1등 점수를 받는다 (공동체 이익)", "친구의 노력이 가상하므로 인정해준다 (유연성)", "이건 공정하지 않다. 친구에게 다시 해오라고 설득하거나 선생님께 알린다 (절대 공정)", "찝찝하지만 내가 직접적인 잘못을 한 건 아니니 신경 쓰지 않는다 (무관심)"])
    
    d3 = st.radio("Q3. [절친의 뒷담화] 베프가 나에게만 비밀이라며 '다른 친구 뒷담화'를 했어요. 그런데 그 내용이 사실과 전혀 다른 오해라는 걸 내가 알고 있다면?", 
                  ["친구의 기분을 맞춰주기 위해 오해라는 걸 알면서도 맞장구쳐준다 (우정 우선)", "진실은 알려줘야지! 친구가 민망하지 않게 사실관계를 조심스레 정정해준다 (진실 우선)", "중간에서 난처해지기 싫으니 그냥 듣고만 있고 나중에 잊어버린다 (관계 유지)", "그 사실을 뒷담화 대상이었던 친구에게 알려 오해를 풀어준다 (정의 구현)"])

    d4 = st.radio("Q4. [편의점의 실수] 거스름돈을 15,000원이나 더 받았어요. 직원은 전혀 모르고 바빠 보인다면 당신의 행동은?",
                  ["말하지 않고 조용히 편의점을 나온다 (실익 우선)", "양심이 찔리지만 이미 나왔으니 그냥 쓴다 (합리화)", "나중에 직원이 곤란해질 수 있으니 즉시 돌려준다 (타인 배려)", "돈 계산은 정확해야지! 정해진 원칙대로 바로잡는다 (원칙 고수)"])

    d5 = st.radio("Q5. [급식 새치기] 너무 배가 고픈 점심시간, 내 앞의 친구가 자기 친한 무리 3명을 슬쩍 끼워줬어요. 뒤의 줄은 엄청 길고 다들 짜증 난 상태라면?",
                  ["친구들끼리 그럴 수 있지. 나도 내 친구를 내 앞에 끼운다 (동조)", "기분은 나쁘지만 싸우기 싫어서 꾹 참는다 (갈등 회피)", "큰 소리로 새치기하지 말라고 당당하게 말한다 (공정 추구)", "조용히 가서 친구에게 뒤로 가라고 눈치를 준다 (현실적 해결)"])

    d6 = st.radio("Q6. [SNS의 거짓말] 평소 나를 괴롭히던 애가 잘못하지도 않은 일로 SNS에서 마녀사냥을 당하고 있어요. 진실을 밝혀주면 그 애가 풀려날 수 있다면?",
                  ["쌤통이다! 가만히 있으면서 상황을 즐긴다 (인과응보)", "엮이기 싫다. 내가 나설 일은 아니라고 생각하며 무시한다 (개인주의)", "아무리 싫어도 거짓으로 욕먹는 건 아니지. 진실을 말해준다 (보편적 정의)", "나에게 사과하면 도와주겠다고 조건을 제시한다 (전략적 거래)"])

    submit = st.form_submit_button(label='📊 심층 가치관 분석 결과 확인하기')

if submit:
    if name and student_id and q1 != "선택하세요":
        # 인물 비중 데이터
        title_map = {"A": "신뢰", "B": "자존", "C": "원칙", "D": "순수", "E": "진실", "F": "책임"}
        user_title = title_map.get(q1[0], "자유")

        try:
            response = requests.post(WEB_APP_URL, json={"name": f"{student_id} {name}", "mbti": user_title, "intro": f"이유:{q1_reason}"}, verify=False)
            if response.status_code == 200:
                # 축하 효과 2종 세트
                st.balloons()
                st.snow()
                
                # 가치 점수 계산
                all_ans = [d1, d2, d3, d4, d5, d6]
                score_j = sum(1 for a in all_ans if any(x in a for x in ["정의", "정직", "공정", "진실", "원칙", "바로잡는다"]))
                score_f = sum(1 for a in all_ans if any(x in a for x in ["의리", "동조", "배려", "기분을 맞춰", "이해된다"]))
                score_p = sum(1 for a in all_ans if any(x in a for x in ["현실적", "실익", "방관", "무관심", "개이득", "합리화", "회피", "거래"]))

                # 6가지 심층 유형 로직 (STEP 2 결과 + STEP 1 인물 결합)
                if score_j >= 4:
                    type_name = "강철의 수호자 (Justice Knight)"
                    type_desc = f"{name}님은 어떤 상황에서도 '옳고 그름'을 가장 먼저 생각하는 사람입니다. 친구와의 우정이나 눈앞의 이익보다 보편적인 정의를 중요하게 여기는 성향이 매우 강하네요. 사회에 꼭 필요한 대나무 같은 성격이지만, 때로는 타인의 실수에도 조금 엄격할 수 있으니 한 번쯤 유연한 마음을 가져보는 것도 좋겠어요!"
                elif score_f >= 4:
                    type_name = "따뜻한 공감주의자 (Warm Empath)"
                    type_desc = f"{name}님은 사람의 마음과 관계를 세상에서 가장 소중히 여깁니다. 누군가 마음 상하는 것을 보기 힘들어하고, 갈등보다는 평화를 선택하는 편이네요. 주변에 친구가 많고 인기가 좋지만, 때로는 거절해야 할 때 거절하지 못해 스스로가 힘들 수 있으니 자신의 마음도 잘 챙겨주세요!"
                elif score_p >= 4:
                    type_name = "전략적 현실주의자 (Smart Realist)"
                    type_desc = f"{name}님은 상황을 매우 냉철하고 효율적으로 판단하는 능력이 있습니다. 불필요한 감정 소모보다는 가장 합리적인 해결책을 찾으려 노력하네요. 현실 감각이 뛰어나고 문제 해결 능력이 좋지만, 때로는 주변에서 차갑게 느낄 수 있으니 가끔은 감성적인 접근을 시도해보는 건 어떨까요?"
                elif score_j >= 2 and score_f >= 2:
                    type_name = "조화로운 균형가 (Balanced Leader)"
                    type_desc = f"{name}님은 원칙을 지키면서도 사람들의 마음을 잃지 않으려 노력하는 훌륭한 균형 감각을 가졌습니다. 정의와 우정 사이에서 끊임없이 고민하며 최선의 선택을 내리려 애쓰는 타입이군요. 이런 성향은 나중에 팀을 이끄는 리더로서 매우 큰 장점이 될 것입니다!"
                elif score_f >= 2 and score_p >= 2:
                    type_name = "유연한 중재자 (Flexible Mediator)"
                    type_desc = f"{name}님은 고정관념에 얽매이지 않고 사람과 상황에 따라 부드럽게 대처하는 능력이 있습니다. 갈등이 생겼을 때 실질적이면서도 모두가 만족할 만한 타협점을 찾아내는 데 능숙하시네요! 사회 생활에서 가장 적응력이 뛰어난 스타일입니다."
                else:
                    type_name = "자유로운 탐험가 (Free Spirit)"
                    type_desc = f"{name}님은 하나의 가치에 얽매이기보다 그때그때 자신의 직관과 가치에 따라 자유롭게 판단하는 분입니다. 틀에 박힌 생각보다는 자신만의 독특한 시선으로 세상을 바라보며, 남들이 생각하지 못한 창의적인 선택을 하기도 합니다."

                st.markdown(f"""
                <div class="analysis-card">
                    <h1 style='text-align: center;'>🕵️ {name}님의 가치관 리포트</h1>
                    <h2 style='color:#4A90E2; text-align: center;'>"{type_name}"</h2>
                    <p style='font-size: 1.2rem; color: #333;'>{type_desc}</p>
                    <hr>
                    <div class="score-box">
                        <p><b>📊 나의 가치관 지표 (6점 만점):</b></p>
                        <ul>
                            <li><b>정의와 원칙 (Justice):</b> {score_j}점</li>
                            <li><b>관계와 공감 (Empathy):</b> {score_f}점</li>
                            <li><b>현실과 실익 (Pragmatism):</b> {score_p}점</li>
                        </ul>
                    </div>
                    <p><b>🔍 이야기 속 인물과의 연결:</b><br>
                    {name}님은 <b>{q1}</b>을 가장 나쁘다고 선택하셨습니다. 이는 {name}님의 내면에 <b>[{user_title}]</b>이라는 가치가 매우 깊이 자리 잡고 있음을 뜻합니다. {user_title}이(가) 무너지는 상황을 볼 때 가장 큰 분노를 느끼는 것이죠.</p>
                    <hr>
                    <p style='color: #666; font-size: 1rem; text-align: center;'>
                        💡 결과는 참고용일 뿐! 중요한 것은 내가 '왜' 그런 선택을 했는지 스스로 돌아보는 과정입니다. 친구들과 리포트를 공유하며 대화해 보세요!
                    </p>
                </div>
                """, unsafe_allow_html=True)
        except:
            st.error("데이터 저장 중 오류가 발생했습니다.")
    else:
        st.warning("학번, 이름, 그리고 가장 나쁜 사람을 꼭 선택해 주세요!")