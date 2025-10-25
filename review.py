import streamlit as st
from sheets_sender import enviar_a_sheets
from tab_tracker import reset_tab_counter, get_tab_count

def show_review():
    st.markdown("### Review Your Answers")
    st.caption("Please review all your answers before submitting.")
    
    # Student Info
    with st.expander("Student Information", expanded=True):
        st.write(f"**Name:** {st.session_state.student_name}")
        st.write(f"**Email:** {st.session_state.student_email}")
        st.write(f"**Class:** {st.session_state.student_class}")
    
    # Listening
    with st.expander("Listening Section", expanded=False):
        st.text_area("Listening Answers", value=st.session_state.listening_answers, height=150, disabled=True, key="review_listening")
    
    # Grammar - SIN mostrar puntaje
    with st.expander("Grammar Section", expanded=False):
        # Mostrar solo las respuestas seleccionadas, no si son correctas
        if 'grammar_responses' in st.session_state:
            from grammar import GRAMMAR_QUESTIONS
            for idx, q in enumerate(GRAMMAR_QUESTIONS):
                st.write(f"**Q{idx + 1}:** {q['question']}")
                st.write(f"Your answer: {st.session_state.grammar_responses.get(idx, 'No answer')}")
                st.divider()
    
    # Reading
    with st.expander("Reading Section", expanded=False):
        st.text_area("Reading Answers", value=st.session_state.reading_answers, height=150, disabled=True, key="review_reading")
    
    # Writing
    with st.expander("Writing Section", expanded=False):
        st.text_area("Writing Composition", value=st.session_state.writing_answers, height=200, disabled=True, key="review_writing")
    
    st.divider()
    
    acepto = st.checkbox("I confirm this is my own work and I have completed all sections")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back to Edit", use_container_width=True):
            st.session_state.current_section = 4
            st.rerun()
    
    with col3:
        if st.button("Submit Assessment", use_container_width=True, type="primary", disabled=not acepto):
            if not (st.session_state.student_name and st.session_state.student_email and 
                    st.session_state.listening_answers and st.session_state.grammar_answers and 
                    st.session_state.reading_answers and st.session_state.writing_answers):
                st.error("Please complete ALL sections before submitting.")
            else:
                switches = get_tab_count()
                
                # IMPRIMIR PUNTAJE EN CONSOLA
                if 'grammar_score' in st.session_state:
                    print(f"\n{'='*50}")
                    print(f"ASSESSMENT SUBMITTED")
                    print(f"{'='*50}")
                    print(f"Student: {st.session_state.student_name}")
                    print(f"Email: {st.session_state.student_email}")
                    print(f"Class: {st.session_state.student_class}")
                    print(f"Grammar Score: {st.session_state.grammar_score}/{st.session_state.grammar_total}")
                    print(f"Tab Switches: {switches}")
                    print(f"{'='*50}\n")
                
                try:
                    # ENVIAR A GOOGLE SHEETS
                    enviar_a_sheets(
                        st.session_state.student_name,
                        st.session_state.student_email,
                        st.session_state.student_class,
                        st.session_state.listening_answers,
                        st.session_state.grammar_answers,
                        st.session_state.reading_answers,
                        st.session_state.writing_answers,
                        switches
                    )
                    
                    # Mostrar puntaje después de enviar
                    st.success("✅ Assessment submitted successfully to Google Sheets!")
                    
                    if 'grammar_score' in st.session_state:
                        grammar_percentage = (st.session_state.grammar_score/st.session_state.grammar_total*100)
                        st.info(f"📊 Grammar Score: {st.session_state.grammar_score}/{st.session_state.grammar_total} ({grammar_percentage:.1f}%)")
                    
                    if switches > 5:
                        st.warning(f"⚠️ Note: {switches} tab switches were detected during the assessment.")
                    else:
                        st.info(f"✅ Assessment completed with {switches} tab switch(es).")
                    
                    reset_tab_counter()
                    st.balloons()
                    
                    if st.button("Start New Assessment"):
                        for key in list(st.session_state.keys()):
                            del st.session_state[key]
                        st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Submission error: {e}")
                    print(f"ERROR: {e}")
                    
                    # Mostrar detalles del error para debugging
                    with st.expander("Error Details (for debugging)"):
                        st.code(str(e))