import streamlit as st
from tab_tracker import inject_tab_tracker
from student_info import show_student_info
from listening import show_listening
from grammar import show_grammar
from reading import show_reading
from writing import show_writing
from review import show_review

st.set_page_config(page_title="Written Assessment", page_icon="📝", layout="wide")

# Inicializar session state
if 'current_section' not in st.session_state:
    st.session_state.current_section = 0
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""
if 'student_email' not in st.session_state:
    st.session_state.student_email = ""
if 'student_class' not in st.session_state:
    st.session_state.student_class = "Dream Chasers"
if 'listening_answers' not in st.session_state:
    st.session_state.listening_answers = ""
if 'grammar_answers' not in st.session_state:
    st.session_state.grammar_answers = ""
if 'reading_answers' not in st.session_state:
    st.session_state.reading_answers = ""
if 'writing_answers' not in st.session_state:
    st.session_state.writing_answers = ""

# Inyectar rastreador de pestañas
inject_tab_tracker()

# Header
st.title("Written Assessment")
st.markdown("**Complete all sections carefully. Your responses will be reviewed.**")
st.divider()

# Secciones
sections = ["Student Info", "Listening", "Grammar", "Reading", "Writing", "Review & Submit"]

# Progress bar
progress = st.session_state.current_section / (len(sections) - 1)
st.progress(progress)
st.caption(f"Section {st.session_state.current_section + 1} of {len(sections)}: **{sections[st.session_state.current_section]}**")
st.divider()

# Mostrar la sección correspondiente
if st.session_state.current_section == 0:
    show_student_info()
elif st.session_state.current_section == 1:
    show_listening()
elif st.session_state.current_section == 2:
    show_grammar()
elif st.session_state.current_section == 3:
    show_reading()
elif st.session_state.current_section == 4:
    show_writing()
elif st.session_state.current_section == 5:
    show_review()

# Footer
st.divider()
st.caption("This assessment is monitored for academic integrity.")
st.caption("Please ensure you have enough time to complete all sections before starting.")