"""
4단계: 레이아웃과 컨테이너
학습 목표: 페이지 구조를 체계적으로 구성하기
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="레이아웃 배우기",
    page_icon="🎨",
    layout="wide"  # "centered" 또는 "wide"
)

st.title("🎨 레이아웃 구성하기")

# ============================================
# 1. 사이드바
# ============================================
st.sidebar.title("⚙️ 설정 패널")
st.sidebar.write("사이드바는 설정이나 필터를 배치하기 좋습니다.")

sidebar_option = st.sidebar.selectbox(
    "옵션 선택:",
    ["옵션 1", "옵션 2", "옵션 3"]
)

sidebar_slider = st.sidebar.slider(
    "값 조정:",
    0, 100, 50
)

st.sidebar.divider()
st.sidebar.info(f"""
**현재 설정**
- 선택: {sidebar_option}
- 값: {sidebar_slider}
""")

# ============================================
# 2. 컬럼 레이아웃
# ============================================
st.header("1. 컬럼 레이아웃")

st.subheader("2개 컬럼 (1:1 비율)")
col1, col2 = st.columns(2)

with col1:
    st.write("**왼쪽 컬럼**")
    st.button("버튼 1", use_container_width=True, key="left_btn1")
    st.button("버튼 1", use_container_width=True, key="left_btn2")
with col2:
    st.write("**오른쪽 컬럼**")
    st.button("버튼 2", use_container_width=True, key="right_btn1")
    st.button("버튼 2", use_container_width=True, key="right_btn2")


# 구분선
st.divider()

st.subheader("3개 컬럼 (1:2:1 비율)")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.metric("사용자", "1,234", "+12%")

with col2:
    st.write("중앙 컬럼은 넓게!")
    st.progress(0.7)

with col3:
    st.metric("매출", "₩5M", "+8%")

# ============================================
# 3. 탭
# ============================================
st.divider()
st.header("2. 탭 레이아웃")

tab1, tab2, tab3  = st.tabs(["⚙️ 설정", "ℹ️ 정보", "다운"])

with tab1:
    st.subheader("설정 탭")
    
    theme = st.selectbox("테마:", ["라이트", "다크"])
    language = st.selectbox("언어:", ["한국어", "English"])
    
    if st.button("설정 저장"):
        st.success("설정이 저장되었습니다!")

with tab2:
    st.subheader("정보 탭")
    st.info("""
    **버전**: 1.0.0  
    **개발자**: Streamlit Team  
    **라이선스**: MIT
    """)

# ============================================
# 4. 확장 가능한 섹션 (Expander)
# ============================================
st.divider()
st.header("3. 확장 섹션 (Expander)")

with st.expander("📖 더 자세히 보기"):
    st.write("""
    여기는 기본적으로 숨겨져 있는 내용입니다.
    클릭하면 펼쳐집니다!
    """)
    st.code("""
    def hello():
        return "Hello, World!"
    """, language="python")

with st.expander("📊 통계 데이터", expanded=True):
    st.write("expanded=True로 설정하면 기본으로 펼쳐져 있습니다.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("방문자", "1,234")
    col2.metric("페이지뷰", "5,678")
    col3.metric("전환율", "3.2%")

# ============================================
# 5. Empty (동적 업데이트)
# ============================================
st.divider()
st.header("5. Empty (동적 업데이트)")

import time

placeholder = st.empty()

if st.button("카운트다운 시작"):
    for i in range(5, 0, -1):
        placeholder.write(f"⏰ {i}초 남았습니다...")
        time.sleep(1) # 1초 기다리기
    placeholder.success("✅ 완료!")

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")

st.markdown("""
### 과제 1: 제품 상세 페이지 만들기

다음 레이아웃으로 제품 상세 페이지를 만드세요:

**구조:**
1. 사이드바: 카테고리 선택, 가격 범위 필터
2. 메인 영역:
   - 2개 컬럼 (1:1): 왼쪽에 이미지, 오른쪽에 상품 정보
   - 탭: 상세설명, 리뷰, 배송정보
   - Expander: FAQ
""")


import streamlit as st

st.set_page_config(
    page_title="제품 상세 페이지",
    page_icon="🛒",
    layout="wide"
)

# -------------------
# 1. 사이드바: 필터 영역
# -------------------
st.sidebar.title("필터")

# 카테고리 선택
category = st.sidebar.selectbox(
    "카테고리 선택",
    ["전체", "전자기기", "패션", "생활용품", "도서"]
)

# 가격 범위 필터 (슬라이더)
price_min, price_max = st.sidebar.slider(
    "가격 범위 설정 (원)",
    min_value=0,
    max_value=1_000_000,
    value=(100_000, 500_000),
    step=10_000
)

st.sidebar.markdown("---")
st.sidebar.subheader("현재 필터")
st.sidebar.write(f"카테고리: **{category}**")
st.sidebar.write(f"가격: **{price_min:,}원 ~ {price_max:,}원**")

# -------------------
# 2. 메인 영역
# -------------------
st.title("프리미엄 무선 헤드폰")

# 2개 컬럼 (1:1)
col1, col2 = st.columns(2)

# 왼쪽: 제품 이미지
with col1:
    # 예시 이미지 URL (원하면 자신의 이미지로 교체)
    st.image(
        "data:image/jpeg;base64,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",
       
    )

# 오른쪽: 상품 정보
with col2:
    st.subheader("제품 정보")

    st.markdown("""
    **제품명**: 프리미엄 무선 노이즈캔슬링 헤드폰  
    **브랜드**: SoundMax  
    **가격**: **299,000원**  
    **카테고리**: 전자기기
    """)

    st.markdown("##### 주요 특징")
    st.markdown("""
    - 하이브리드 액티브 노이즈 캔슬링
    - 최대 40시간 연속 재생
    - 블루투스 5.2 지원
    - 멀티포인트(2대 동시 연결) 지원
    - 접이식 디자인 및 전용 케이스 포함
    """)

    # 옵션 선택 (색상, 수량 등)
    color = st.selectbox("색상 선택", ["블랙", "화이트", "네이비"])
    quantity = st.number_input("수량", min_value=1, max_value=10, value=1, step=1)

    st.markdown("---")
    # 구매 버튼 영역
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        if st.button("🛒 장바구니 담기"):
            st.success(f"{color} 색상 {quantity}개가 장바구니에 담겼습니다.")
    with col_btn2:
        if st.button("✅ 바로 구매"):
            st.info("구매 페이지로 이동합니다... (실서비스에서는 결제 페이지 연결)")

# -------------------
# 탭: 상세설명, 리뷰, 배송정보
# -------------------
st.markdown("---")
tab1, tab2, tab3 = st.tabs(["📄 상세설명", "💬 리뷰", "🚚 배송정보"])

with tab1:
    st.subheader("제품 상세 설명")
    st.markdown("""
    이 프리미엄 무선 노이즈캔슬링 헤드폰은  
    장시간 착용에도 편안한 인체공학적 디자인과  
    몰입감을 극대화하는 하이브리드 노이즈 캔슬링 기술을 탑재했습니다.

    **상세 스펙**
    - 드라이버: 40mm 다이내믹 드라이버
    - 주파수 응답: 20Hz ~ 20kHz
    - 블루투스 버전: 5.2
    - 코덱: SBC, AAC
    - 배터리 사용 시간: 최대 40시간 (ANC OFF 기준)
    - 충전 포트: USB-C
    - 무게: 260g
    """)

    with st.expander("기술적 특징 더 보기"):
        st.markdown("""
        - 듀얼 마이크 노이즈 감소 알고리즘으로 통화 품질 개선  
        - 환경에 따라 자동으로 노이즈 캔슬링 강도 조절  
        - 전용 앱에서 EQ(이퀄라이저) 및 버튼 동작 커스터마이징 가능
        """)

with tab2:
    st.subheader("사용자 리뷰")

    # 간단한 평균 평점 표시
    st.markdown("**평균 평점: 4.6 / 5.0 (125개 리뷰)**")
    st.progress(92)  # 예시로 평점 비율 같은 느낌으로 사용

    # 예시 리뷰들
    st.markdown("---")
    st.markdown("**user01** - ⭐⭐⭐⭐⭐")
    st.write("노이즈캔슬링 성능이 정말 좋아요. 지하철에서도 음악 소리에만 집중할 수 있습니다.")

    st.markdown("---")
    st.markdown("**music_lover** - ⭐⭐⭐⭐☆")
    st.write("음질은 좋은데, 약간 타이트하게 눌리는 느낌이 있어요. 장시간 사용시 귀가 조금 아픕니다.")

    st.markdown("---")
    st.markdown("**office_worker** - ⭐⭐⭐⭐⭐")
    st.write("재택근무용으로 최고입니다. 통화 품질도 좋고, 배터리가 오래가요.")

    st.markdown("---")
    st.markdown("리뷰 작성하기")
    new_rating = st.slider("평점", 1, 5, 5)
    new_review = st.text_area("리뷰 내용")
    if st.button("리뷰 등록"):
        if new_review.strip():
            st.success("리뷰가 등록되었습니다. (데모에서는 실제 저장은 되지 않습니다)")
        else:
            st.warning("리뷰 내용을 입력해주세요.")

with tab3:
    st.subheader("배송 정보")
    st.markdown("""
    - **배송 방법**: 택배 (CJ대한통운 / 로젠택배)
    - **배송비**: 3,000원 (50,000원 이상 구매 시 무료배송)
    - **출고일**: 영업일 기준 1~2일 이내 출고
    - **배송기간**: 출고 후 평균 1~3일 소요

    **교환/반품 안내**
    - 제품 수령 후 7일 이내 교환/반품 신청 가능
    - 단순 변심의 경우 왕복 배송비는 고객 부담
    - 제품 불량 또는 오배송 시 배송비는 판매자 부담
    """)

# -------------------
# Expander: FAQ
# -------------------
st.markdown("---")
with st.expander("❓ 자주 묻는 질문 (FAQ)"):
    st.markdown("""
    **Q1. 유선 연결도 가능한가요?**  
    A1. 네, 동봉된 3.5mm 오디오 케이블로 유선 연결도 가능합니다.

    **Q2. 여러 기기(노트북 + 스마트폰)에 동시에 연결되나요?**  
    A2. 네, 멀티포인트 기능을 지원하여 최대 2대 기기까지 동시 연결됩니다.

    **Q3. 방수 기능이 있나요?**  
    A3. 생활 방수(IPX4) 수준으로, 가벼운 빗방울이나 땀 정도는 견딜 수 있습니다.  
    다만 샤워, 수영 등의 환경에서는 사용을 권장하지 않습니다.

    **Q4. 펌웨어 업데이트는 어떻게 하나요?**  
    A4. 전용 모바일 앱을 통해 펌웨어 업데이트가 가능합니다.
    """)





# 예시 답안
with st.expander("💡 과제 1 예시 답안"):
    st.subheader("제품 상세 페이지")
    
    # 2컬럼 레이아웃
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ96jQ9W4bT93OXaPYPMiX3hSW3ioFRp-2mCA&s", use_container_width=True)
    
    with col2:
        st.write("### 🎧 무선 헤드폰 Pro")
        st.write("**₩299,000**")
        st.write("⭐⭐⭐⭐⭐ (4.8) - 리뷰 324개")
        st.write("---")
        st.write("고급 노이즈 캔슬링 기능이 탑재된 프리미엄 무선 헤드폰")
        
        quantity = st.number_input("수량:", min_value=1, value=1)
        col_a, col_b = st.columns(2)
        col_a.button("🛒 장바구니", use_container_width=True)
        col_b.button("💳 바로 구매", type="primary", use_container_width=True)
    
    # 탭
    tab1, tab2, tab3 = st.tabs(["📋 상세설명", "⭐ 리뷰", "🚚 배송정보"])
    
    with tab1:
        st.write("**주요 특징**")
        st.write("- 최대 30시간 재생")
        st.write("- 고급 노이즈 캔슬링")
        st.write("- 블루투스 5.0")
    
    with tab2:
        st.write("평균 평점: ⭐ 4.8/5.0")
        st.write("---")
        st.write("**김철수**: ⭐⭐⭐⭐⭐")
        st.write("정말 좋아요!")
    
    with tab3:
        st.info("무료 배송 (2-3일 소요)")
    
    # FAQ
    with st.expander("❓ 자주 묻는 질문"):
        st.write("**Q: 배송은 얼마나 걸리나요?**")
        st.write("A: 보통 2-3일 소요됩니다.")

with st.expander("💡 과제 2 예시 답안"):
    st.subheader("데이터 분석 대시보드")
    
    # 상단 메트릭
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("총 방문자", "12,345", "+8%")
    m2.metric("페이지뷰", "45,678", "+12%")
    m3.metric("전환율", "3.2%", "-0.3%")
    m4.metric("평균 체류", "5:23", "+15s")
    
    # 중단
    left, right = st.columns([2, 1])
    
    with left:
        st.write("**방문자 추이**")
        data = pd.DataFrame(
            np.random.randint(100, 200, 30),
            columns=['방문자']
        )
        st.line_chart(data)
    
    with right:
        st.write("**필터**")
        period = st.selectbox("기간:", ["오늘", "7일", "30일", "90일"])
        source = st.multiselect("소스:", ["검색", "SNS", "직접", "광고"])
        st.button("적용", type="primary", use_container_width=True)
    
    # 하단 탭
    t1, t2, t3 = st.tabs(["📊 데이터", "📈 통계", "⚙️ 설정"])
    
    with t1:
        sample_df = pd.DataFrame({
            '날짜': pd.date_range('2026-01-01', periods=5),
            '방문자': [120, 145, 132, 156, 143]
        })
        st.dataframe(sample_df, use_container_width=True)
    
    with t2:
        st.write("평균 방문자:", data['방문자'].mean())
        st.write("최대값:", data['방문자'].max())
        st.write("최소값:", data['방문자'].min())
    
    with t3:
        st.write("대시보드 설정")
        st.checkbox("자동 새로고침")
        st.selectbox("새로고침 간격:", ["1분", "5분", "10분"])
