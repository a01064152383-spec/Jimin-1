import streamlit as st

# --- 1. 앱 구성 및 제목 ---
st.title("➗ 유리함수의 역함수 학습 앱")
st.markdown("유리함수의 역함수의 **정의와 개념**을 이해하고, **문제를 풀어보는** 앱입니다.")

# --- 2. 유리함수 역함수의 정의 및 개념 학습 섹션 ---

st.header("1. 유리함수 역함수의 정의와 개념")

st.subheader("1.1. 역함수의 정의")
st.markdown(
    """
    함수 $y = f(x)$에 대하여 **$x$와 $y$의 값을 서로 바꾼** 관계를 만족하는 함수 $x = g(y)$를
    $f(x)$의 **역함수**라고 하며, $f^{-1}(x)$로 나타냅니다.
    
    * **핵심:** 역함수를 구하는 과정은 원래 함수의 **$x$와 $y$를 바꾸어** 새로운 함수식을 구하는 것입니다.
    """
)

st.subheader("1.2. 유리함수의 형태")
st.markdown(
    """
    일반적인 유리함수의 형태는 다음과 같습니다.
    $$
    y = \\frac{ax + b}{cx + d} \quad (단, c \\neq 0, ad - bc \\neq 0)
    $$
    """
)

st.subheader("1.3. 유리함수의 역함수 구하기")
st.markdown(
    """
    $y = \\frac{ax + b}{cx + d}$의 역함수를 구하는 순서는 다음과 같습니다.
    
    1.  **$x$와 $y$를 서로 바꾼다.**
        $$
        x = \\frac{ay + b}{cy + d}
        $$
    2.  **$y$에 대하여 정리한다.**
        * 양변에 $(cy + d)$를 곱합니다:
            $$x(cy + d) = ay + b$$
            $$cxy + dx = ay + b$$
        * $y$를 포함하는 항을 한쪽으로 모읍니다:
            $$cxy - ay = b - dx$$
            $$y(cx - a) = -dx + b$$
        * 따라서, $y$에 대하여 정리하면 역함수는 다음과 같습니다.
            $$
            y = \\frac{-dx + b}{cx - a}
            $$
    """
)
st.markdown(
    """
    
    
    * **결론 (공식):** $y = \\frac{ax + b}{cx + d}$ 의 역함수는 $y = \\frac{-dx + b}{cx - a}$ 입니다.
        * **핵심 변화:** 원래 함수의 분자 $x$의 계수 $a$와 분모의 상수항 $d$가 **자리를 바꾸고 부호가 반대로** 바뀝니다. ($-d$와 $a$가 $-a$와 $-d$로)
    """
)

st.write("---")

# --- 3. 문제 풀이 섹션 ---

st.header("2. 역함수 문제 풀이")
st.markdown("아래 유리함수의 역함수를 구하고 답을 입력해 보세요.")

# 문제 설정 (예시)
a_val, b_val, c_val, d_val = 3, -1, 2, 4
problem_func = f"y = \\frac{{ {a_val}x + ({b_val}) }}{{ {c_val}x + {d_val} }}"

# 정답 계산 (공식 적용)
# y = (-dx + b) / (cx - a)
# y = (-4x + (-1)) / (2x - 3)
correct_numerator = f"-{d_val}x + ({b_val})"
correct_denominator = f"{c_val}x - {a_val}"
correct_answer = f"\\frac{{ {correct_numerator} }}{{ {correct_denominator} }}"

st.latex(problem_func)

# 사용자 입력
user_numerator = st.text_input("분자 (예: -4x-1)", key="num")
user_denominator = st.text_input("분모 (예: 2x-3)", key="den")

# 채점 버튼
if st.button("답안 제출 및 확인"):
    # 입력 정리 및 비교 (공백, 괄호 등 제거하고 비교)
    def clean_input(text):
        return text.replace(" ", "").replace("(", "").replace(")", "").strip()

    cleaned_user_num = clean_input(user_numerator)
    cleaned_user_den = clean_input(user_denominator)

    # 정답 텍스트 (공식 형태)
    clean_correct_num = clean_input(f"-{d_val}x{b_val}") # -4x-1
    clean_correct_den = clean_input(f"{c_val}x-{a_val}") # 2x-3
    
    # 정답 텍스트 (분자/분모 부호 반대 형태도 허용)
    clean_alt_num = clean_input(f"{d_val}x{-b_val}") # 4x+1
    clean_alt_den = clean_input(f"-{c_val}x+{a_val}") # -2x+3

    is_correct = False
    
    # 기본 정답 형태와 일치하는지 확인
    if cleaned_user_num == clean_correct_num and cleaned_user_den == clean_correct_den:
        is_correct = True
    # 분자/분모 모두에 -1을 곱한 형태와 일치하는지 확인 (수학적으로 동등)
    elif cleaned_user_num == clean_alt_num and cleaned_user_den == clean_alt_den:
        is_correct = True
        
    if is_correct:
        st.success("✅ **정답입니다!**")
        st.balloons()
    else:
        st.error("❌ **다시 시도해 보세요.**")
        
    st.info(
        f"""
        **풀이:**
        원래 함수 $y = \\frac{3x - 1}{2x + 4}$ 에서 $a=3$, $b=-1$, $c=2$, $d=4$ 입니다.
        
        공식 $y = \\frac{-dx + b}{cx - a}$ 에 대입하면,
        $$
        y = \\frac{-4x + (-1)}{2x - 3} = \\frac{-4x - 1}{2x - 3}
        $$
        (또는 분자, 분모에 $-1$을 곱한 $\\frac{4x + 1}{-2x + 3}$ 도 정답입니다.)
        """
    )
