import streamlit as st

# LISTENING COMPREHENSION - 17 POINTS TOTAL

# NOTE: Place your audio file in the same directory as this script
# Supported formats: .mp3, .wav, .ogg
AUDIO_FILE_PATH = "audio.mp3"  # Change this to your audio file name

LISTENING_QUESTIONS = [
    {
        "question": "What is the main topic of the audio?",
        "type": "multiple_choice",
        "options": [
            "How to become a doctor",
            "Career opportunities as a licensed technician",
            "How to fix computers at home",
            "Finding a job online"
        ],
        "correct": "Career opportunities as a licensed technician",
        "points": 2
    },
    {
        "question": "What is the name of the technical school mentioned in the audio?",
        "type": "multiple_choice",
        "options": [
            "ACME Technical School",
            "Tech Career Institute",
            "Licensed Technician Academy",
            "State Technical College"
        ],
        "correct": "ACME Technical School",
        "points": 2
    },
    {
        "question": "Which programs does ACME Technical School offer? (Select the correct combination)",
        "type": "multiple_choice",
        "options": [
            "Nursing, medicine, and pharmacy",
            "Air conditioning, refrigeration, electronics, automotive and computer technology",
            "Business, accounting, and finance",
            "Teaching, engineering, and architecture"
        ],
        "correct": "Air conditioning, refrigeration, electronics, automotive and computer technology",
        "points": 3
    },
    {
        "question": "When are classes held at ACME Technical School?",
        "type": "multiple_choice",
        "options": [
            "Only on weekdays",
            "Only on weekends",
            "Days, nights, and weekends",
            "Only at night"
        ],
        "correct": "Days, nights, and weekends",
        "points": 2
    },
    {
        "question": "Complete the sentence: 'Study _______ time or _______ time in our state-of-the-art labs.'",
        "type": "multiple_choice",
        "options": [
            "full / part",
            "all / some",
            "day / night",
            "long / short"
        ],
        "correct": "full / part",
        "points": 2
    },
    {
        "question": "What does the school offer to those who qualify?",
        "type": "multiple_choice",
        "options": [
            "Free housing",
            "Free transportation",
            "Financial aid",
            "Free computers"
        ],
        "correct": "Financial aid",
        "points": 2
    },
    {
        "question": "What free service comes with all programs?",
        "type": "multiple_choice",
        "options": [
            "Free textbooks",
            "Free meals",
            "Job placement services",
            "Free uniforms"
        ],
        "correct": "Job placement services",
        "points": 2
    },
    {
        "question": "According to the audio, who calls the school every day?",
        "type": "multiple_choice",
        "options": [
            "Students looking for classes",
            "Parents asking for information",
            "Employers looking for technicians",
            "Government officials"
        ],
        "correct": "Employers looking for technicians",
        "points": 2
    }
]

def show_listening():
    st.markdown("### LISTENING SECTION (17 points)")
    st.caption("Listen to the audio carefully and answer the comprehension questions.")
    
    # Initialize responses if not exist
    if 'listening_responses' not in st.session_state:
        st.session_state.listening_responses = {}
    
    st.markdown("---")
    
    # Audio player section
    st.markdown("#### 🔊 Audio")
    st.info("**Instructions:** Click the play button below to listen to the audio. You can listen as many times as you need.")
    
    try:
        # Try to load and display the audio file
        audio_file = open(AUDIO_FILE_PATH, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        audio_file.close()
    except FileNotFoundError:
        st.error(f"⚠️ Audio file '{AUDIO_FILE_PATH}' not found. Please contact your teacher.")
        st.info("**For Teachers:** Place your audio file in the same directory as this script and update the AUDIO_FILE_PATH variable at the top of listening.py")
        
        # Display transcript for testing purposes (remove this in production)
        with st.expander("📄 **Transcript (FOR TESTING ONLY - Remove before exam)**"):
            st.markdown("""
Have you ever thought about a career as a licensed technician? Things break every day. Licensed technicians are always needed to fix them. At ACME technical school, you'll learn the skills you need to become a licensed technician. We offer programs in air conditioning, refrigeration, electronics, and automotive and computer technology. Classes are held days, nights, and weekends. Study full time or part time in our state-of-the-art labs. We offer financial aid to those who qualify. And all programs come with free job placement services. Employers call us every day looking for you. So what are you waiting for? Apply online at acmefix.com. That's A-C-M-E-F-I-X dot com.
            """)
    
    st.markdown("---")
    
    # Display questions
    st.markdown("#### 📝 Listening Comprehension Questions")
    st.caption("Total: 8 multiple choice questions = 17 points")
    
    for idx, q in enumerate(LISTENING_QUESTIONS):
        st.markdown(f"**Question {idx + 1}** ({q['points']} points)")
        st.markdown(f"{q['question']}")
        
        answer = st.radio(
            "Select your answer:",
            options=q['options'],
            key=f"listening_q_{idx}",
            index=q['options'].index(st.session_state.listening_responses.get(idx))
                  if idx in st.session_state.listening_responses and st.session_state.listening_responses.get(idx) in q['options']
                  else 0
        )
        st.session_state.listening_responses[idx] = answer
        
        st.markdown("")  # Space between questions
    
    st.divider()
    
    # Calculate score
    correct_points = 0
    total_points = 0
    
    for idx, q in enumerate(LISTENING_QUESTIONS):
        total_points += q['points']
        if idx in st.session_state.listening_responses:
            user_answer = st.session_state.listening_responses[idx]
            if user_answer == q['correct']:
                correct_points += q['points']
    
    # Save score to session state
    st.session_state.listening_score = correct_points
    st.session_state.listening_total = total_points
    
    # Format answers for email
    listening_text = "LISTENING COMPREHENSION SECTION (17 POINTS)\n"
    listening_text += "="*60 + "\n\n"
    listening_text += "Topic: ACME Technical School - Career as a Licensed Technician\n"
    listening_text += f"Audio File: {AUDIO_FILE_PATH}\n\n"
    listening_text += "="*60 + "\n"
    listening_text += "STUDENT ANSWERS:\n"
    listening_text += "="*60 + "\n\n"
    
    for idx, q in enumerate(LISTENING_QUESTIONS):
        user_answer = st.session_state.listening_responses.get(idx, "No answer")
        is_correct = user_answer == q['correct']
        
        listening_text += f"Q{idx + 1}. ({q['points']} points) {q['question']}\n"
        listening_text += f"Student answer: {user_answer}\n"
        listening_text += f"Correct answer: {q['correct']} {'✓' if is_correct else '✗'}\n"
        listening_text += f"Points earned: {q['points'] if is_correct else 0}/{q['points']}\n\n"
    
    listening_text += "="*60 + "\n"
    listening_text += f"TOTAL SCORE: {correct_points}/{total_points} points\n"
    
    st.session_state.listening_answers = listening_text
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back to Instructions", use_container_width=True):
            st.session_state.current_section = 0
            st.rerun()
    with col3:
        if st.button("Next: Grammar →", use_container_width=True, type="primary"):
            st.session_state.current_section = 2
            st.rerun()