import streamlit as st
import time

st.set_page_config(page_title="Countdown Timer", page_icon="⏳")

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    .timer-display {
        font-size: 80px;
        font-weight: bold;
        text-align: center;
        color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        background: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'current_time' not in st.session_state:
    st.session_state.current_time = 0

st.title("⏳ Pro Countdown Timer")
st.write("Enter the duration and hit start!")

col1, col2 = st.columns(2)
with col1:
    mins_input = st.number_input("Minutes", min_value=0, value=0, step=1, disabled=st.session_state.timer_running)
with col2:
    secs_input = st.number_input("Seconds", min_value=0, max_value=59, value=0, step=1, disabled=st.session_state.timer_running)

if not st.session_state.timer_running:
    st.session_state.current_time = mins_input * 60 + secs_input

timer_placeholder = st.empty()

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("🚀 Start Countdown", disabled=st.session_state.timer_running):
        if st.session_state.current_time > 0:
            st.session_state.timer_running = True
            st.rerun()
        else:
            st.warning("Please enter a time greater than 0.")

with btn_col2:
    if st.button("🛑 Stop Timer", disabled=not st.session_state.timer_running):
        st.session_state.timer_running = False
        st.rerun()

if st.session_state.timer_running:
    while st.session_state.current_time >= 0 and st.session_state.timer_running:
        mins, secs = divmod(st.session_state.current_time, 60)
        timer_format = f"{mins:02d}:{secs:02d}"

        timer_placeholder.markdown(f'<div class="timer-display">{timer_format}</div>', unsafe_allow_html=True)

        time.sleep(1)
        st.session_state.current_time -= 1

        if st.session_state.current_time < 0:
            st.session_state.timer_running = False
            timer_placeholder.markdown('<div class="timer-display">00:00</div>', unsafe_allow_html=True)
            st.balloons()
            st.success("⏰ Time's Up!")
            st.rerun()
else:
    mins, secs = divmod(st.session_state.current_time, 60)
    timer_format = f"{mins:02d}:{secs:02d}"
    timer_placeholder.markdown(f'<div class="timer-display">{timer_format}</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("Developed with ❤️ by Fatimah Noman")
