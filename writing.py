import streamlit as st

# WRITING SECTION - 10 POINTS TOTAL

def show_writing():
    st.markdown("### WRITING SECTION (17 points)")
    st.caption("Write a clear and organized composition.")
    
    # Initialize if not exists
    if 'writing_answers' not in st.session_state:
        st.session_state.writing_answers = ""
    
    st.markdown("---")
    
    # Writing prompt
    st.markdown("## ✍️ Writing Task")
    st.markdown("### **Write about: How does Airport Security work and why is it important?**")
    
    st.markdown("")
    st.markdown("**Aspects to consider:**")
    st.markdown("""
1. **Grammar (5 points)**: Use correct verb tenses, sentence structure, and punctuation
2. **Structure (3 points)**: Clear organization with steps and explanation
3. **Vocabulary (3 points)**: Use appropriate and varied vocabulary related to airport security
4. **Content (3 points)**: Explain the process clearly and why it's important
5. **Length (3 point)**: Write at least 80 words
    """)
    
    st.markdown("---")
    
    # Writing instructions
    st.info("""
**📝 Instructions:**
- Explain how airport security works step by step
- Explain why airport security is important
- Use time-order words (First, Then, Next, After that, Finally)
- Use grammar you have learned (present simple, comparatives, used to, etc.)
- Write at least **80 words**
- Organize your ideas clearly
    """)
    
    st.markdown("")
    
    # Writing area
    writing = st.text_area(
        "**Your composition:**",
        value=st.session_state.writing_answers,
        height=400,
        key="writing_composition",
        placeholder="Write your composition here...\n\nSuggested structure:\n\nIntroduction: What is airport security?\n\nBody: How does it work? (explain the steps)\n\nConclusion: Why is it important?"
    )
    st.session_state.writing_answers = writing
    
    # Word counter
    word_count = len(writing.split()) if writing else 0
    if word_count < 80:
        st.info(f"💡 Current word count: {word_count}/80 words (Recommended minimum: 80 words for full credit)")
    else:
        st.success(f"✅ Word count: {word_count} words")
    
    st.markdown("")
    
    
    # Prepare formatted output for email
    writing_output = "WRITING SECTION (15 POINTS)\n"
    writing_output += "="*60 + "\n\n"
    writing_output += "TASK: Write about how Airport Security works and why it is important\n\n"
    writing_output += "="*60 + "\n"
    writing_output += "STUDENT COMPOSITION:\n"
    writing_output += "-"*60 + "\n\n"
    writing_output += st.session_state.writing_answers + "\n\n"
    writing_output += "="*60 + "\n"
    writing_output += f"Word Count: {word_count} words\n"
    writing_output += f"Recommended Minimum: 80 words\n"
    writing_output += f"Length Point: {'1 point (80+ words)' if word_count >= 80 else '0 points (less than 80 words)'}\n\n"
    writing_output += "="*60 + "\n"
    writing_output += "GRADING RUBRIC (17 points total):\n"
    writing_output += "-"*60 + "\n"
    writing_output += "1. Grammar (5 pts): _____ / 5\n"
    writing_output += "   - Correct verb tenses, sentence structure, punctuation\n\n"
    writing_output += "2. Structure (3 pts): _____ / 3\n"
    writing_output += "   - Clear introduction, body, and conclusion\n\n"
    writing_output += "3. Vocabulary (3 pts): _____ / 3\n"
    writing_output += "   - Appropriate and varied vocabulary\n\n"
    writing_output += "4. Content (3 pts): _____ / 3\n"
    writing_output += "   - Clear explanation of process and importance\n\n"
    writing_output += f"5. Length (3 pt): {'_____ / 1' if word_count >= 80 else '0 / 1'}\n"
    writing_output += f"   - Minimum 80 words {'(MET)' if word_count >= 80 else '(NOT MET)'}\n\n"
    writing_output += "="*60 + "\n"
    writing_output += "TOTAL SCORE: _____ / 15 points\n\n"
    writing_output += "TEACHER COMMENTS:\n"
    writing_output += "-"*60 + "\n\n\n"
    writing_output += "** This section requires manual grading by the teacher **\n"
    
    st.session_state.writing_formatted = writing_output
    
    st.markdown("---")
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back to Reading", use_container_width=True):
            st.session_state.current_section = 3
            st.rerun()
    with col3:
        if st.button("Review & Submit →", use_container_width=True, type="primary"):
            st.session_state.current_section = 5
            st.rerun()