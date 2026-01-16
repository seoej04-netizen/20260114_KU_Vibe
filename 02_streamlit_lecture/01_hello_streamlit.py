"""
1단계: Streamlit 소개 및 첫 번째 앱
학습 목표: Streamlit의 기본 구조 이해하기
"""

import streamlit as st

# 브라우저창 텝을 보면 아이콘과 페이지 타이틀이 바뀌어있는것을 볼 수 있다.
st.set_page_config(
    page_title="스트림릿과의 만남",
    page_icon="🎨",
    layout="wide"  # "centered" 또는 "wide"
)

# 제목 표시
st.title("🎉 나의 첫 Streamlit 앱")

# 간단한 텍스트 출력
st.write("안녕하세요! Streamlit에 오신 것을 환영합니다.")

# 구분선
st.divider()

# 자기소개 섹션
st.header("자기소개")
st.write("이름: 서은진")
st.write("직업: 대학생")
st.write("관심사: 신기한 거 전부")

# 구분선
st.divider()

# 간단한 인터랙션
st.subheader("버튼을 눌러보세요!")
if st.button("인사하기"):
    st.balloons()  # 풍선 애니메이션
    st.success("반갑습니다! 🎊")

import streamlit as st
import random

st.title("오늘의 랜덤 행운 🍀")

# 보여줄 행운 문구 리스트
luck_messages = [
    "오늘은 새로운 시작을 하기 딱 좋은 날이에요!",
    "생각지도 못한 좋은 소식을 듣게 될 거예요.",
    "당신의 노력이 곧 눈에 띄는 성과로 돌아올 거예요.",
    "오래 고민하던 일이 좋은 방향으로 풀릴 거예요.",
    "오늘 만나는 사람 중 하나가 큰 도움이 될 거예요.",
    "작은 선택이 큰 행운으로 이어질 거예요.",
    "웃는 얼굴이 오늘의 행운을 더 끌어당길 거예요.",
    "놓쳤다고 생각했던 기회가 다시 돌아올지도 몰라요.",
    "당신의 진심이 꼭 전달될 거예요.",
    "기분 좋은 우연이 오늘 당신을 기다리고 있어요."
]

st.write("아래 버튼을 눌러 오늘의 행운을 확인해보세요!")

# 버튼
if st.button("행운 뽑기"):
    message = random.choice(luck_messages)
    st.success(message)


# 정보 박스
st.info("💡 팁: 코드를 수정하고 저장하면 자동으로 새로고침됩니다!")

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")
st.markdown("""
1. 제목을 자신의 이름으로 변경해보세요
2. 자기소개 내용을 본인의 정보로 바꿔보세요
3. 새로운 버튼을 추가하고, 클릭 시 다른 메시지가 나오도록 해보세요
4. `st.warning()` 또는 `st.error()` 함수를 사용해보세요
""")
