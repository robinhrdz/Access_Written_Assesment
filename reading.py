import streamlit as st

def show_reading():
    st.markdown("### READING SECTION")
    st.caption("Read the text and answer the comprehension questions.")
    
    reading = st.text_area(
        "Your answers:",
        value=st.session_state.reading_answers,
        height=300,
        placeholder="1. Answer to question 1...\n2. Answer to question 2...\n3. Answer to question 3..."
    )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.reading_answers = reading
            st.session_state.current_section = 2
            st.rerun()
    with col3:
        if st.button("Next: Writing →", use_container_width=True, type="primary"):
            st.session_state.reading_answers = reading
            st.session_state.current_section = 4
            st.rerun()