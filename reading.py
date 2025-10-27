import streamlit as st

# READING COMPREHENSION - 16 POINTS TOTAL
READING_TEXT = """
**From Small Town to Big Dreams: The Story of Emma Rivera**

Emma Rivera grew up in a small town in the countryside. When she was younger, she used to help her parents at their family bakery every morning before school. She has worked there since she was ten years old. Emma has always loved baking, but she never imagined it would become her career.

"I used to think I would become a teacher," Emma says with a smile. "But everything changed when I was fifteen."

That year, Emma's chocolate cake won first place at the regional fair. Since that moment, she has won more than twenty baking competitions. She hasn't stopped improving her skills, and she has never given up on her dream of opening her own bakery in the city.

Three years ago, Emma moved to the capital to study at the Culinary Institute. It wasn't easy at first. "I couldn't speak English very well when I arrived," she admits. "The classes were more difficult than I expected, and the city was noisier and more expensive than my hometown. But I wasn't able to give up. I had worked too hard to get there."

Emma has been living in the capital for three years now. She has learned so much during this time. "The education here is as good as everyone said it would be," she explains. "My teachers have been incredible, and my classmates have become like family."

Last month, Emma finally opened her own small bakery called "Sweet Dreams." The bakery isn't as big as the famous shops downtown, but it's already becoming popular. Customers say her pastries are better than anything they have ever tasted before.

"Have you ever felt that you're exactly where you're supposed to be?" Emma asks. "I feel that way every single day now. I have never been happier in my life."

Emma's advice to young people? "Don't be afraid to follow your dreams. They might seem impossible now, but if you work hard and never give up, anything is possible. I used to be scared of leaving my hometown, but now I can't imagine living anywhere else."
"""

READING_QUESTIONS = [
    {
        "question": "What did Emma use to do when she was younger?",
        "type": "multiple_choice",
        "options": [
            "She used to teach at a school",
            "She used to help her parents at their family bakery",
            "She used to work at the Culinary Institute",
            "She used to sell cakes at regional fairs"
        ],
        "correct": "She used to help her parents at their family bakery",
        "points": 3
    },
    {
        "question": "How long has Emma been working at the bakery, and what happened when she was fifteen?",
        "type": "multiple_choice",
        "options": [
            "She has worked there for three years; she moved to the capital",
            "She has worked there since she was ten; her cake won first place at a regional fair",
            "She has worked there since she was fifteen; she opened her own bakery",
            "She has worked there for twenty years; she became a teacher"
        ],
        "correct": "She has worked there since she was ten; her cake won first place at a regional fair",
        "points": 3
    },
    {
        "question": "According to the text, how was the city different from Emma's hometown?",
        "type": "multiple_choice",
        "options": [
            "The city was quieter and cheaper than her hometown",
            "The city was as noisy as her hometown but more expensive",
            "The city was noisier and more expensive than her hometown",
            "The city was smaller and less expensive than her hometown"
        ],
        "correct": "The city was noisier and more expensive than her hometown",
        "points": 3
    },
    {
        "question": "What does Emma say about the education at the Culinary Institute and her bakery?",
        "type": "multiple_choice",
        "options": [
            "The education is better than expected, and her bakery is as big as downtown shops",
            "The education is as good as everyone said, and her bakery isn't as big as downtown shops",
            "The education is worse than expected, but her bakery is bigger than downtown shops",
            "The education is not as good as expected, and her bakery is very small"
        ],
        "correct": "The education is as good as everyone said, and her bakery isn't as big as downtown shops",
        "points": 4
    },
    {
        "question": "What is Emma's current feeling and advice to young people?",
        "type": "multiple_choice",
        "options": [
            "She has never been happier; she advises young people to become teachers",
            "She is unhappy; she advises people to stay in their hometowns",
            "She has never been happier; she advises people to follow their dreams and never give up",
            "She is nervous; she advises people to be scared of big changes"
        ],
        "correct": "She has never been happier; she advises people to follow their dreams and never give up",
        "points": 3
    }
]

def show_reading():
    st.markdown("### READING SECTION (16 points)")
    st.caption("Read the text carefully and answer the comprehension questions.")
    
    # Initialize responses if not exist
    if 'reading_responses' not in st.session_state:
        st.session_state.reading_responses = {}
    
    # Display the reading text
    st.markdown("---")
    st.markdown("#### 📖 Reading Text")
    st.markdown(READING_TEXT)
    st.markdown("---")
    
    # Display questions
    st.markdown("#### 📝 Comprehension Questions")
    st.caption("Total: 5 multiple choice questions = 16 points")
    
    for idx, q in enumerate(READING_QUESTIONS):
        st.markdown(f"**Question {idx + 1}** ({q['points']} points)")
        st.markdown(f"{q['question']}")
        
        answer = st.radio(
            "Select your answer:",
            options=q['options'],
            key=f"reading_q_{idx}",
            index=q['options'].index(st.session_state.reading_responses.get(idx))
                  if idx in st.session_state.reading_responses and st.session_state.reading_responses.get(idx) in q['options']
                  else 0
        )
        st.session_state.reading_responses[idx] = answer
        
        st.markdown("")  # Space between questions
    
    st.divider()
    
    # Calculate score
    correct_points = 0
    total_points = 0
    
    for idx, q in enumerate(READING_QUESTIONS):
        total_points += q['points']
        if idx in st.session_state.reading_responses:
            user_answer = st.session_state.reading_responses[idx]
            if user_answer == q['correct']:
                correct_points += q['points']
    
    # Save score to session state
    st.session_state.reading_score = correct_points
    st.session_state.reading_total = total_points
    
    # Format answers for email
    reading_text = "READING COMPREHENSION SECTION (16 POINTS)\n"
    reading_text += "="*60 + "\n\n"
    reading_text += "READING TEXT:\n"
    reading_text += READING_TEXT.replace("**", "") + "\n\n"
    reading_text += "="*60 + "\n"
    reading_text += "STUDENT ANSWERS:\n"
    reading_text += "="*60 + "\n\n"
    
    for idx, q in enumerate(READING_QUESTIONS):
        user_answer = st.session_state.reading_responses.get(idx, "No answer")
        is_correct = user_answer == q['correct']
        
        reading_text += f"Q{idx + 1}. ({q['points']} points) {q['question']}\n"
        reading_text += f"Student answer: {user_answer}\n"
        reading_text += f"Correct answer: {q['correct']} {'✓' if is_correct else '✗'}\n"
        reading_text += f"Points earned: {q['points'] if is_correct else 0}/{q['points']}\n\n"
    
    reading_text += "="*60 + "\n"
    reading_text += f"TOTAL SCORE: {correct_points}/{total_points} points\n"
    
    st.session_state.reading_answers = reading_text
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back to Grammar", use_container_width=True):
            st.session_state.current_section = 2
            st.rerun()
    with col3:
        if st.button("Next: Writing →", use_container_width=True, type="primary"):
            st.session_state.current_section = 4
            st.rerun()