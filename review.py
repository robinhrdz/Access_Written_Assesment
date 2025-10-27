import streamlit as st
from sheets_sender import enviar_a_sheets
from tab_tracker import reset_tab_counter, get_tab_count

def calculate_grammar_score():
    """
    Recalcula el score de grammar basado en las respuestas almacenadas
    Calcula el total dinámicamente sumando todos los puntos
    """
    from grammar import GRAMMAR_QUESTIONS
    
    correct_points = 0
    # Calcular total sumando todos los puntos de las preguntas
    total_possible_points = sum(q['points'] for q in GRAMMAR_QUESTIONS)
    
    if 'grammar_responses' not in st.session_state:
        return 0, total_possible_points
    
    for idx, q in enumerate(GRAMMAR_QUESTIONS):
        if idx in st.session_state.grammar_responses:
            user_answer = st.session_state.grammar_responses[idx]
            
            # Multiple choice
            if q['type'] == 'multiple_choice':
                if user_answer == q['correct']:
                    correct_points += q['points']
            
            # Fill in the blank
            elif q['type'] == 'fill_blank':
                if user_answer.strip().lower() in [ans.lower() for ans in q['accepts']]:
                    correct_points += q['points']
            
            # Write sentence
            elif q['type'] == 'write_sentence':
                if user_answer.strip().lower() in [ans.lower() for ans in q['accepts']]:
                    correct_points += q['points']
    
    return correct_points, total_possible_points

def calculate_reading_score():
    """
    Recalcula el score de reading basado en las respuestas almacenadas
    SIEMPRE retorna 16 como total posible
    """
    from reading import READING_QUESTIONS
    
    correct_points = 0
    total_possible_points = 16  # HARDCODED: Total de puntos posibles
    
    if 'reading_responses' not in st.session_state:
        return 0, total_possible_points
    
    for idx, q in enumerate(READING_QUESTIONS):
        if idx in st.session_state.reading_responses:
            user_answer = st.session_state.reading_responses[idx]
            if user_answer == q['correct']:
                correct_points += q['points']
    
    return correct_points, total_possible_points

def calculate_listening_score():
    """
    Recalcula el score de listening basado en las respuestas almacenadas
    SIEMPRE retorna 17 como total posible
    """
    from listening import LISTENING_QUESTIONS
    
    correct_points = 0
    total_possible_points = 17  # HARDCODED: Total de puntos posibles
    
    if 'listening_responses' not in st.session_state:
        return 0, total_possible_points
    
    for idx, q in enumerate(LISTENING_QUESTIONS):
        if idx in st.session_state.listening_responses:
            user_answer = st.session_state.listening_responses[idx]
            if user_answer == q['correct']:
                correct_points += q['points']
    
    return correct_points, total_possible_points

def show_review():
    st.markdown("### 📋 Review Your Answers")
    st.caption("Please review all your answers before submitting.")
    
    st.divider()
    
    # ============================================
    # STUDENT INFORMATION
    # ============================================
    st.markdown("### 👤 Student Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**Name:** {st.session_state.student_name}")
    with col2:
        st.info(f"**Email:** {st.session_state.student_email}")
    with col3:
        st.info(f"**Class:** {st.session_state.student_class}")
    
    st.divider()
    
    # ============================================
    # LISTENING SECTION REVIEW
    # ============================================
    st.markdown("### 🔊 Listening Section (17 points)")
    with st.expander("View Listening Answers", expanded=False):
        if 'listening_responses' in st.session_state:
            from listening import LISTENING_QUESTIONS
            
            for idx, q in enumerate(LISTENING_QUESTIONS):
                st.markdown(f"**Question {idx + 1}** ({q['points']} pts)")
                st.markdown(f"{q['question']}")
                user_answer = st.session_state.listening_responses.get(idx, "❌ No answer provided")
                st.success(f"Your answer: {user_answer}")
                st.markdown("")
        else:
            st.warning("⚠️ No listening answers found. Please complete the Listening section.")
    
    st.divider()
    
    # ============================================
    # GRAMMAR SECTION REVIEW
    # ============================================
    st.markdown("### 📝 Grammar Section (52 points)")
    with st.expander("View Grammar Answers", expanded=False):
        if 'grammar_responses' in st.session_state:
            from grammar import GRAMMAR_QUESTIONS
            
            current_section = None
            
            for idx, q in enumerate(GRAMMAR_QUESTIONS):
                # Show section header when section changes
                if q.get("section") != current_section:
                    current_section = q.get("section")
                    st.markdown(f"#### {current_section}")
                    st.markdown("---")
                
                st.markdown(f"**Question {idx + 1}** ({q['points']} pts)")
                st.markdown(f"{q['question']}")
                
                user_answer = st.session_state.grammar_responses.get(idx, "❌ No answer provided")
                
                # Display answer based on question type
                if q['type'] == 'multiple_choice':
                    st.success(f"Your answer: {user_answer}")
                elif q['type'] == 'fill_blank':
                    st.success(f"Your answer: {user_answer}")
                elif q['type'] == 'write_sentence':
                    st.text_area(
                        "Your answer:",
                        value=user_answer,
                        height=80,
                        disabled=True,
                        key=f"review_grammar_{idx}"
                    )
                    word_count = len(user_answer.split()) if user_answer else 0
                    if 'min_words' in q and word_count > 0:
                        st.caption(f"📊 Word count: {word_count} words")
                
                st.markdown("")
        else:
            st.warning("⚠️ No grammar answers found. Please complete the Grammar section.")
    
    st.divider()
    
    # ============================================
    # READING SECTION REVIEW
    # ============================================
    st.markdown("### 📖 Reading Section (16 points)")
    with st.expander("View Reading Answers", expanded=False):
        if 'reading_responses' in st.session_state:
            from reading import READING_QUESTIONS, READING_TEXT
            
            # Show reading text
            st.markdown("#### Reading Text")
            with st.container():
                st.markdown(READING_TEXT)
            
            st.markdown("---")
            st.markdown("#### Your Answers")
            
            for idx, q in enumerate(READING_QUESTIONS):
                st.markdown(f"**Question {idx + 1}** ({q['points']} pts)")
                st.markdown(f"{q['question']}")
                user_answer = st.session_state.reading_responses.get(idx, "❌ No answer provided")
                st.success(f"Your answer: {user_answer}")
                st.markdown("")
        else:
            st.warning("⚠️ No reading answers found. Please complete the Reading section.")
    
    st.divider()
    
    # ============================================
    # WRITING SECTION REVIEW
    # ============================================
    st.markdown("### ✍️ Writing Section (15 points)")
    with st.expander("View Writing Composition", expanded=False):
        if st.session_state.writing_answers:
            st.markdown("**Task:** Write about how Airport Security works and why it is important")
            st.markdown("---")
            st.markdown("**Your Composition:**")
            st.text_area(
                "Writing",
                value=st.session_state.writing_answers,
                height=300,
                disabled=True,
                key="review_writing_display"
            )
            
            # Word count
            word_count = len(st.session_state.writing_answers.split()) if st.session_state.writing_answers else 0
            if word_count >= 80:
                st.success(f"✅ Word count: {word_count} words (Requirement met: 80+ words)")
            else:
                st.warning(f"⚠️ Word count: {word_count} words (Requirement: 80+ words)")
        else:
            st.warning("⚠️ No writing composition found. Please complete the Writing section.")
    
    st.divider()
    
    # ============================================
    # COMPLETION CHECK
    # ============================================
    st.markdown("### ✅ Submission Checklist")
    
    all_complete = True
    checklist = []
    
    # Check each section
    listening_complete = 'listening_responses' in st.session_state and len(st.session_state.listening_responses) > 0
    grammar_complete = 'grammar_responses' in st.session_state and len(st.session_state.grammar_responses) > 0
    reading_complete = 'reading_responses' in st.session_state and len(st.session_state.reading_responses) > 0
    writing_complete = st.session_state.writing_answers and len(st.session_state.writing_answers.strip()) > 0
    
    col1, col2 = st.columns(2)
    
    with col1:
        if listening_complete:
            st.success("✅ Listening Section Complete")
        else:
            st.error("❌ Listening Section Incomplete")
            all_complete = False
        
        if grammar_complete:
            st.success("✅ Grammar Section Complete")
        else:
            st.error("❌ Grammar Section Incomplete")
            all_complete = False
    
    with col2:
        if reading_complete:
            st.success("✅ Reading Section Complete")
        else:
            st.error("❌ Reading Section Incomplete")
            all_complete = False
        
        if writing_complete:
            st.success("✅ Writing Section Complete")
        else:
            st.error("❌ Writing Section Incomplete")
            all_complete = False
    
    st.divider()
    
    # ============================================
    # FINAL CONFIRMATION & SUBMISSION
    # ============================================
    if all_complete:
        st.success("🎉 All sections completed! You're ready to submit.")
        acepto = st.checkbox("✅ I confirm this is my own work and I have reviewed all my answers", value=False)
    else:
        st.error("⚠️ Please complete ALL sections before submitting.")
        acepto = False
    
    st.markdown("")
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back to Edit", use_container_width=True):
            st.session_state.current_section = 4
            st.rerun()
    
    with col3:
        submit_button = st.button(
            "🚀 Submit Assessment", 
            use_container_width=True, 
            type="primary", 
            disabled=not (acepto and all_complete)
        )
        
        if submit_button:
            if not all_complete:
                st.error("❌ Please complete ALL sections before submitting.")
            else:
                # ============================================
                # RECALCULAR TODOS LOS SCORES ANTES DE ENVIAR
                # ============================================
                grammar_score, grammar_total = calculate_grammar_score()
                reading_score, reading_total = calculate_reading_score()
                listening_score, listening_total = calculate_listening_score()
                
                # Guardar en session state
                st.session_state.grammar_score = grammar_score
                st.session_state.grammar_total = grammar_total
                st.session_state.reading_score = reading_score
                st.session_state.reading_total = reading_total
                st.session_state.listening_score = listening_score
                st.session_state.listening_total = listening_total
                
                switches = get_tab_count()
                
                # Print score to console
                print(f"\n{'='*50}")
                print(f"ASSESSMENT SUBMITTED")
                print(f"{'='*50}")
                print(f"Student: {st.session_state.student_name}")
                print(f"Email: {st.session_state.student_email}")
                print(f"Class: {st.session_state.student_class}")
                print(f"Listening Score: {listening_score}/{listening_total} ({listening_score/listening_total*100:.1f}%)")
                print(f"Grammar Score: {grammar_score}/{grammar_total} ({grammar_score/grammar_total*100:.1f}%)")
                print(f"Reading Score: {reading_score}/{reading_total} ({reading_score/reading_total*100:.1f}%)")
                print(f"Tab Switches: {switches}")
                print(f"{'='*50}\n")
                
                try:
                    with st.spinner("📤 Submitting your assessment..."):
                        # Send to Google Sheets with ALL scores
                        enviar_a_sheets(
                            st.session_state.student_name,
                            st.session_state.student_email,
                            st.session_state.student_class,
                            st.session_state.listening_answers,
                            st.session_state.grammar_answers,
                            st.session_state.reading_answers,
                            st.session_state.writing_answers,
                            switches,
                            grammar_score=grammar_score,
                            grammar_total=grammar_total,
                            listening_score=listening_score,
                            listening_total=listening_total,
                            reading_score=reading_score,
                            reading_total=reading_total
                        )
                    
                    # Success message
                    st.success("✅ Assessment submitted successfully to Google Sheets!")
                    st.balloons()
                    
                    # Display scores
                    st.markdown("### 📊 Your Scores")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        listening_pct = (listening_score/listening_total*100) if listening_total > 0 else 0
                        st.metric("🔊 Listening", f"{listening_score}/{listening_total}", f"{listening_pct:.1f}%")
                    
                    with col2:
                        grammar_pct = (grammar_score/grammar_total*100) if grammar_total > 0 else 0
                        st.metric("📝 Grammar", f"{grammar_score}/{grammar_total}", f"{grammar_pct:.1f}%")
                    
                    with col3:
                        reading_pct = (reading_score/reading_total*100) if reading_total > 0 else 0
                        st.metric("📖 Reading", f"{reading_score}/{reading_total}", f"{reading_pct:.1f}%")
                    
                    with col4:
                        st.metric("✍️ Writing", "Pending", "Manual grading")
                    
                    # Tab switch warning
                    if switches > 5:
                        st.warning(f"⚠️ Note: {switches} tab switches were detected during the assessment.")
                    else:
                        st.info(f"✅ Assessment completed with {switches} tab switch(es).")
                    
                    st.markdown("---")
                    st.info("💡 Your teacher will review your writing section and provide your final score.")
                    
                    reset_tab_counter()
                    
                    st.markdown("")
                    if st.button("🔄 Start New Assessment", use_container_width=True):
                        for key in list(st.session_state.keys()):
                            del st.session_state[key]
                        st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Submission error: {e}")
                    print(f"ERROR: {e}")
                    
                    # Show error details for debugging
                    with st.expander("🔍 Error Details (for debugging)"):
                        st.code(str(e))
                        import traceback
                        st.code(traceback.format_exc())