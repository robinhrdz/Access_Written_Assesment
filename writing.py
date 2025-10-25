import streamlit as st

def show_writing():
    st.markdown("### WRITING SECTION")
    st.caption("Write your essay or response (minimum 150 words).")
    
    writing = st.text_area(
        "Your composition:",
        value=st.session_state.writing_answers,
        height=300,
        placeholder="Write your essay here..."
    )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.writing_answers = writing
            st.session_state.current_section = 3
            st.rerun()
    with col3:
        if st.button("Review & Submit →", use_container_width=True, type="primary"):
            st.session_state.writing_answers = writing
            st.session_state.current_section = 5
            st.rerun()