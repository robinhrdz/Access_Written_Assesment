import streamlit as st

def show_listening():
    st.markdown("### LISTENING SECTION")
    st.caption("Listen to the audio and answer the questions below.")
    
    listening = st.text_area(
        "Your answers:",
        value=st.session_state.listening_answers,
        height=300,
        placeholder="1. Answer to question 1...\n2. Answer to question 2...\n3. Answer to question 3..."
    )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.listening_answers = listening
            st.session_state.current_section = 0
            st.rerun()
    with col3:
        if st.button("Next: Grammar →", use_container_width=True, type="primary"):
            st.session_state.listening_answers = listening
            st.session_state.current_section = 2
            st.rerun()