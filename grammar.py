import streamlit as st

# Definir las preguntas con diferentes tipos
GRAMMAR_QUESTIONS = [
    # TIPO 1: Multiple choice (radio buttons)
    {
        "type": "multiple_choice",
        "question": "What is the comparative adjective of 'Big'?",
        "options": ["Biggest", "Bigger", "More big", "More bigger"],
        "correct": "Bigger"
    },
    {
        "type": "multiple_choice",
        "question": "Which sentence is correct?",
        "options": [
            "She don't like coffee",
            "She doesn't likes coffee",
            "She doesn't like coffee",
            "She not like coffee"
        ],
        "correct": "She doesn't like coffee"
    },
    
    # TIPO 2: Complete the sentence (fill in the blank)
    {
        "type": "fill_blank",
        "question": "Complete the sentence: 'I have been waiting ___ two hours.'",
        "correct": "for",
        "accepts": ["for"]  # Respuestas aceptables
    },
    {
        "type": "fill_blank",
        "question": "Have you ever ___ to France? (use the verb 'be' in past participle)",
        "correct": "been",
        "accepts": ["been"]
    },
    {
        "type": "fill_blank",
        "question": "She ___ to the store yesterday. (use 'go' in past tense)",
        "correct": "went",
        "accepts": ["went"]
    },
    
    # TIPO 3: Write the complete sentence
    {
        "type": "write_sentence",
        "question": "Write a sentence using the present perfect tense with the verb 'eat'.",
        "instruction": "Example: I have eaten breakfast.",
        "min_words": 5
    },
    {
        "type": "write_sentence",
        "question": "Write a sentence in passive voice using the verb 'make'.",
        "instruction": "Example: The cake was made by my sister.",
        "min_words": 5
    }
]

def show_grammar():
    st.markdown("### GRAMMAR SECTION")
    st.caption("Answer all questions. There are multiple choice, fill-in-the-blank, and sentence writing questions.")
    
    # Inicializar respuestas si no existen
    if 'grammar_responses' not in st.session_state:
        st.session_state.grammar_responses = {}
    
    # Mostrar cada pregunta según su tipo
    for idx, q in enumerate(GRAMMAR_QUESTIONS):
        st.markdown(f"**Question {idx + 1}:** {q['question']}")
        
        # TIPO 1: Multiple Choice
        if q['type'] == 'multiple_choice':
            answer = st.radio(
                "Select your answer:",
                options=q['options'],
                key=f"grammar_q_{idx}",
                index=q['options'].index(st.session_state.grammar_responses.get(idx)) 
                      if idx in st.session_state.grammar_responses and st.session_state.grammar_responses.get(idx) in q['options']
                      else 0
            )
            st.session_state.grammar_responses[idx] = answer
        
        # TIPO 2: Fill in the Blank
        elif q['type'] == 'fill_blank':
            answer = st.text_input(
                "Your answer:",
                value=st.session_state.grammar_responses.get(idx, ""),
                key=f"grammar_q_{idx}",
                placeholder="Type your answer here..."
            )
            st.session_state.grammar_responses[idx] = answer.strip()
        
        # TIPO 3: Write Complete Sentence
        elif q['type'] == 'write_sentence':
            if 'instruction' in q:
                st.caption(q['instruction'])
            answer = st.text_area(
                "Write your sentence:",
                value=st.session_state.grammar_responses.get(idx, ""),
                key=f"grammar_q_{idx}",
                height=100,
                placeholder="Write your complete sentence here..."
            )
            st.session_state.grammar_responses[idx] = answer.strip()
            
            # Contador de palabras
            word_count = len(answer.split()) if answer else 0
            if 'min_words' in q:
                if word_count < q['min_words']:
                    st.caption(f"⚠️ Minimum {q['min_words']} words required. Current: {word_count} words")
                else:
                    st.caption(f"✓ {word_count} words")
        
        st.divider()
    
    # Calcular puntaje (solo para preguntas con respuesta correcta definida)
    correct_count = 0
    total_graded = 0
    
    for idx, q in enumerate(GRAMMAR_QUESTIONS):
        if idx in st.session_state.grammar_responses:
            user_answer = st.session_state.grammar_responses[idx]
            
            # Multiple choice
            if q['type'] == 'multiple_choice':
                total_graded += 1
                if user_answer == q['correct']:
                    correct_count += 1
            
            # Fill in the blank
            elif q['type'] == 'fill_blank':
                total_graded += 1
                # Verificar si la respuesta está en las aceptadas (case-insensitive)
                if user_answer.lower() in [ans.lower() for ans in q['accepts']]:
                    correct_count += 1
    
    # Guardar puntaje en session state
    st.session_state.grammar_score = correct_count
    st.session_state.grammar_total = total_graded
    
    # Formatear respuestas para el email
    grammar_text = ""
    for idx, q in enumerate(GRAMMAR_QUESTIONS):
        user_answer = st.session_state.grammar_responses.get(idx, "No answer")
        grammar_text += f"Q{idx + 1}. {q['question']}\n"
        grammar_text += f"Type: {q['type']}\n"
        grammar_text += f"Student answer: {user_answer}\n"
        
        # Agregar corrección solo para preguntas con respuesta correcta
        if q['type'] == 'multiple_choice':
            is_correct = user_answer == q['correct']
            grammar_text += f"Correct answer: {q['correct']} {'✓' if is_correct else '✗'}\n"
        elif q['type'] == 'fill_blank':
            is_correct = user_answer.lower() in [ans.lower() for ans in q['accepts']]
            grammar_text += f"Correct answer: {q['correct']} {'✓' if is_correct else '✗'}\n"
        elif q['type'] == 'write_sentence':
            word_count = len(user_answer.split()) if user_answer else 0
            grammar_text += f"Word count: {word_count}\n"
            grammar_text += "(Requires manual grading)\n"
        
        grammar_text += "\n"
    
    grammar_text += f"\nAuto-graded Score: {correct_count}/{total_graded}"
    if total_graded > 0:
        grammar_text += f" ({(correct_count/total_graded*100):.1f}%)"
    grammar_text += f"\nTotal Questions: {len(GRAMMAR_QUESTIONS)}"
    grammar_text += f"\nSentence Writing Questions: {len([q for q in GRAMMAR_QUESTIONS if q['type'] == 'write_sentence'])} (require manual grading)"
    
    st.session_state.grammar_answers = grammar_text
    
    # Botones de navegación
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.current_section = 1
            st.rerun()
    with col3:
        if st.button("Next: Reading →", use_container_width=True, type="primary"):
            st.session_state.current_section = 3
            st.rerun()