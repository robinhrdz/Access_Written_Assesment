import streamlit as st

CLASSES = ["Dream Chasers", "Everwood"]

def show_student_info():
    st.markdown("### Student Information")
    st.markdown("Please enter your details before starting the assessment.")
    
    nombre = st.text_input("Name *", value=st.session_state.student_name)
    email = st.text_input("Email Address *", value=st.session_state.student_email)
    clase = st.selectbox("Class *", options=CLASSES, index=CLASSES.index(st.session_state.student_class))
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col3:
        if st.button("Next: Listening Section", use_container_width=True, type="primary"):
            if nombre and email:
                st.session_state.student_name = nombre
                st.session_state.student_email = email
                st.session_state.student_class = clase
                st.session_state.current_section = 1
                st.rerun()
            else:
                st.error("Please fill in all required fields.")