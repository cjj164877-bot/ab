import streamlit as st

n_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def dec_to_base(num, n):
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        result = n_map[num % n] + result
        num //= n
    return result

def base_to_dec(num, n):
    result = 0
    for char in num:
        if char not in n_map[:n]:
            return f"잘못된 문자: {char}"
        value = n_map.find(char)
        result = result * n + value
    return result

st.title("🔢 진법 변환기")

mode = st.radio(
    "변환 방식 선택",
    ("10진수 → n진수", "n진수 → 10진수")
)

n = st.number_input("진법 입력 (2 ~ 36)", min_value=2, max_value=36, step=1)

input_value = st.text_input("값 입력")

if st.button("변환"):
    if input_value == "":
        st.warning("값을 입력하세요.")
    else:
        if mode == "10진수 → n진수":
            try:
                num = int(input_value)
                result = dec_to_base(num, n)
                st.success(f"결과: {result}")
            except ValueError:
                st.error("10진수를 올바르게 입력하세요.")
        else:
            result = base_to_dec(input_value.upper(), n)
            if isinstance(result, str):
                st.error(result)
            else:
                st.success(f"결과: {result}")
