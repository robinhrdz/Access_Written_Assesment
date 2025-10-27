import streamlit as st

# GRAMMAR QUESTIONS - 52 POINTS TOTAL
GRAMMAR_QUESTIONS = [
    # ============================================
    # SECTION 1: Past Participles (5 points)
    # ============================================
    {
        "section": "Present Perfect: Past Participles (5 pts)",
        "type": "fill_blank",
        "question": "Write the past participle of: Drive",
        "correct": "driven",
        "accepts": ["driven", "Driven"],
        "points": 0.5
    },
    {
        "section": "Present Perfect: Past Participles (5 pts)",
        "type": "fill_blank",
        "question": "Write the past participle of: Sell",
        "correct": "sold",
        "accepts": ["sold", "Sold"],
        "points": 0.5
    },
    {
        "section": "Present Perfect: Past Participles (5 pts)",
        "type": "fill_blank",
        "question": "Write the past participle of: Drink",
        "correct": "drunk",
        "accepts": ["drunk", "Drunk"],
        "points": 0.5
    },
    {
        "section": "Present Perfect: Past Participles (5 pts)",
        "type": "fill_blank",
        "question": "Write the past participle of: Run",
        "correct": "run",
        "accepts": ["run", "Run"],
        "points": 0.5
    },
    {
        "section": "Present Perfect: Past Participles (5 pts)",
        "type": "fill_blank",
        "question": "Write the past participle of: Have",
        "correct": "had",
        "accepts": ["had", "Had"],
        "points": 0.5
    },
    {
        "section": "Present Perfect: Past Participles (5 pts)",
        "type": "fill_blank",
        "question": "Write the past participle of: Be",
        "correct": "been",
        "accepts": ["been", "Been"],
        "points": 0.5
    },
    {
        "section": "Present Perfect: Past Participles (5 pts)",
        "type": "fill_blank",
        "question": "Write the past participle of: Speak",
        "correct": "spoken",
        "accepts": ["spoken", "Spoken"],
        "points": 0.5
    },
    {
        "section": "Present Perfect: Past Participles (5 pts)",
        "type": "fill_blank",
        "question": "Write the past participle of: Solve",
        "correct": "solved",
        "accepts": ["solved", "Solved"],
        "points": 0.5
    },
    {
        "section": "Present Perfect: Past Participles (5 pts)",
        "type": "fill_blank",
        "question": "Write the past participle of: Choose",
        "correct": "chosen",
        "accepts": ["chosen", "Chosen"],
        "points": 0.5
    },
    {
        "section": "Present Perfect: Past Participles (5 pts)",
        "type": "fill_blank",
        "question": "Write the past participle of: Take",
        "correct": "taken",
        "accepts": ["taken", "Taken"],
        "points": 0.5
    },
    
    # ============================================
    # SECTION 2: Questions with EVER (7 points)
    # ============================================
    {
        "section": "Present Perfect using Ever and Never (7pts)",
        "type": "write_sentence",
        "question": "Create a question in present perfect with 'ever': You / visit Spain",
        "correct": "Have you ever visited Spain?",
        "accepts": [
            "Have you ever visited Spain?",
            "Have you ever visited Spain",
            "have you ever visited Spain?",
            "have you ever visited Spain",
            "have you ever visited spain?",
            "have you ever visited spain"
        ],
        "points": 1
    },
    {
        "section": "Present Perfect using Ever and Never (7pts)",
        "type": "write_sentence",
        "question": "Create a question in present perfect with 'ever': He / see a shooting star",
        "correct": "Has he ever seen a shooting star?",
        "accepts": [
            "Has he ever seen a shooting star?",
            "Has he ever seen a shooting star",
            "has he ever seen a shooting star?",
            "has he ever seen a shooting star"
        ],
        "points": 1
    },
    {
        "section": "Present Perfect using Ever and Never (7pts)",
        "type": "write_sentence",
        "question": "Create a question in present perfect with 'ever': You / break a bone",
        "correct": "Have you ever broken a bone?",
        "accepts": [
            "Have you ever broken a bone?",
            "Have you ever broken a bone",
            "have you ever broken a bone?",
            "have you ever broken a bone"
        ],
        "points": 1
    },
    {
        "section": "Present Perfect using Ever and Never (7pts)",
        "type": "write_sentence",
        "question": "Create a question in present perfect with 'ever': We / speak to a celebrity",
        "correct": "Have we ever spoken to a celebrity?",
        "accepts": [
            "Have we ever spoken to a celebrity?",
            "Have we ever spoken to a celebrity",
            "have we ever spoken to a celebrity?",
            "have we ever spoken to a celebrity"
        ],
        "points": 1
    },
    {
        "section": "Present Perfect using Ever and Never (7pts)",
        "type": "write_sentence",
        "question": "Create a sentence in present perfect with 'never': I / drive a truck",
        "correct": "I have never driven a truck.",
        "accepts": [
            "I have never driven a truck.",
            "I have never driven a truck",
            "i have never driven a truck.",
            "i have never driven a truck"
        ],
        "points": 1
    },
    {
        "section": "Present Perfect using Ever and Never (7pts)",
        "type": "write_sentence",
        "question": "Create a sentence in present perfect with 'never': She / eat sushi",
        "correct": "She has never eaten sushi.",
        "accepts": [
            "She has never eaten sushi.",
            "She has never eaten sushi",
            "she has never eaten sushi.",
            "she has never eaten sushi"
        ],
        "points": 1
    },
    {
        "section": "Present Perfect using Ever and Never (7pts)",
        "type": "write_sentence",
        "question": "Create a sentence in present perfect with 'never': They / see a ghost",
        "correct": "They have never seen a ghost.", 
        "accepts": [
            "They have never seen a ghost.",
            "They have never seen a ghost",
            "they have never seen a ghost.",
            "they have never seen a ghost"
        ],
        "points": 1
    },
    
    # ============================================
    # SECTION 3: FOR and SINCE (6 points)
    # ============================================
    {
        "section": "Present Perfect: FOR and SINCE (6pts)",
        "type": "multiple_choice",
        "question": "What do we use to talk about length of time?",
        "options": ["For", "Since"],
        "correct": "For",
        "points": 1
    },
    {
        "section": "Present Perfect: FOR and SINCE (6pts)",
        "type": "multiple_choice",
        "question": "What do we use to talk about a specific point in time?",
        "options": ["For", "Since"],
        "correct": "Since",
        "points": 1
    },
    {
        "section": "Present Perfect: FOR and SINCE (6pts)",
        "type": "fill_blank",
        "question": "Edgar _____ (own) his own business ______ 2015. (Write: the COMPLETE sentence",
        "correct": "Edgar has owned his own business since 2015",
        "accepts": [
            "Edgar has owned his own business since 2015",
            "Edgar has owned his own business since 2015.",
            "edgar has owned his own business since 2015",
            "edgar has owned his own business since 2015."
        ],
        "points": 1
    },
    {
        "section": "Present Perfect: FOR and SINCE (6pts)",
        "type": "fill_blank",
        "question": "She ________ (not/take) a vacation since 2015. (Write the complete negative form)",
        "correct": "She has not taken a vacation since 2015",
        "accepts": [
            "She has not taken a vacation since 2015",
            "She has not taken a vacation since 2015.",
            "She hasn't taken a vacation since 2015",
            "She hasn't taken a vacation since 2015.",
            "she has not taken a vacation since 2015",
            "she has not taken a vacation since 2015.",
            "she hasn't taken a vacation since 2015",
            "she hasn't taken a vacation since 2015."
        ],
        "points": 1
    },
    {
        "section": "Present Perfect: FOR and SINCE (6pts)",
        "type": "fill_blank",
        "question": "You ___ (be) a manager ____ two years, right? (Write: verb / for or since)",
        "correct": "You have been a manager for two years, right?",
        "accepts": [
            "You have been a manager for two years, right?",
            "You have been a manager for two years, right",
            "you have been a manager for two years, right?",
            "you have been a manager for two years, right"
        ],
        "points": 1
    },
    {
        "section": "Present Perfect: FOR and SINCE (6pts)",
        "type": "fill_blank",
        "question": "We _____ (be) out of town _____ three weeks. (Write: verb / for or since)",
        "correct": "have been / for",
        "accepts": [
            "have been / for",
            "have been for",
            "have been/for",
            "We have been out of town for three weeks",
            "We have been out of town for three weeks.",
            "we have been out of town for three weeks",
            "we have been out of town for three weeks."
        ],
        "points": 1
    },
    
    # ============================================
    # SECTION 4: USED TO (5 points)
    # ============================================
    {
        "section": "Select the best option: USED TO (5pts)",
        "type": "multiple_choice",
        "question": "Which sentence is correct?",
        "options": [
            "I use to go to the gym every day when I was younger.",
            "I used to go to the gym every day when I was younger.", 
            "I am used to go to the gym every day when I was younger."
        ],
        "correct": "I used to go to the gym every day when I was younger.",
        "points": 1
    },
    {
        "section": "Select the best option: USED TO (5pts)",
        "type": "multiple_choice",
        "question": "Which sentence is correct?",
        "options": [
            "My friends use to play soccer on weekends.",
            "My friends are used to play soccer on weekends.",
            "My friends used to play soccer on weekends."
        ],
        "correct": "My friends used to play soccer on weekends.",
        "points": 1
    },
    {
        "section": "Select the best option: USED TO (5pts)",
        "type": "multiple_choice",
        "question": "Select the best option to complete the sentence: \n\n 'She _____ (not / used to) like coffee, but now she drinks it every morning.'",
        "options": [
            "doesn't used to",
            "didn't use to",
            "didn't used to"
        ],
        "correct": "didn't use to",
        "points": 1   
    }, 
    {
        "section": "Select the best option: USED TO (5pts)",
        "type": "multiple_choice",
        "question": "Select the best option to complete the sentence: \n\n 'They _____ (live) in the city, but now they live in the countryside.'",
        "options": [
            "use to live",
            "used to live",
            "are used to live"
        ],
        "correct": "used to live",
        "points": 1   
    }, 
    {
        "section": "Select the best option: USED TO (5pts)",
        "type": "multiple_choice",
        "question": "True or False, We use 'used to' to contrast past habits with present situations?",
        "options": [
            "True",
            "False"
        ],
        "correct": "True",
        "points": 1   
    }, 

    # ============================================
    # SECTION 5: Can / Could for possibility and ability, be able to for ability (4 points)
    # ============================================
    {
        "section": "Select the best option: Can/Could/be able to (4pts)",
        "type": "multiple_choice",
        "question": "Select the best option to complete the sentence: \n\n 'My flight was delayed, so I couldn't / was able to go to my mom's birthday party last weekend.'",
        "options": [
            "couldn't",
            "was able to", 
        ],
        "correct": "couldn't",
        "points": 1   
    }, 
    {
        "section": "Select the best option: Can/Could/be able to (4pts)",
        "type": "multiple_choice",
        "question": "Select the best option to complete the sentence: \n\n 'I can't / couldn't hear the annoucement because of the noise.'",
        "options": [
            "can't",
            "couldn't",
        ],
        "correct": "couldn't",
        "points": 1   
    }, 
    {
        "section": "Select the best option: Can/Could/be able to (4pts)",
        "type": "multiple_choice",
        "question": "Select the best option to complete the sentence: \n\n 'Our flight will be able / won't be able to take off for another ten minutes. '",
        "options": [
            "will be able",
            "won't be able", 
        ],
        "correct": "won't be able",
        "points": 1   
    }, 
    {
        "section": "Select the best option: Can/Could/be able to (4pts)",
        "type": "multiple_choice",
        "question": "Select the best option to complete the sentence: \n\n 'They weren't able / wasn't able to finish the project on time because of the delays.'",
        "options": [
            "weren't able",
            "wasn't able",  
        ],
        "correct": "weren't able",
        "points": 1   
    }, 

    # ============================================
    # SECTION 6: Possessive Adjectives and Possessive Pronouns (5 points)
    # ============================================
    {
        "section": "Possessive Adjectives and Possessive Pronouns (5pts)",
        "type": "fill_blank",
        "question": "That is my chair. It isn't _______. (Write the complete sentence)",
        "correct": "That is my chair. It isn't yours.",
        "accepts": [
            "That is my chair. It isn't yours.",
            "That is my chair. It isn't yours",
            "that is my chair. it isn't yours.",
            "that is my chair. it isn't yours",
            "That is my chair, it isn't yours.",
            "That is my chair, it isn't yours"
        ],
        "points": 1
    },
    {
        "section": "Possessive Adjectives and Possessive Pronouns (5pts)",
        "type": "fill_blank",
        "question": "We love _______ new teacher; she's very kind. (Write the complete sentence)",
        "correct": "We love our new teacher; she's very kind.",
        "accepts": [
            "We love our new teacher; she's very kind.",
            "We love our new teacher; she's very kind",
            "we love our new teacher; she's very kind.",
            "we love our new teacher; she's very kind",
            "We love our new teacher, she's very kind.",
            "We love our new teacher, she's very kind"
        ],
        "points": 1
    },
    {
        "section": "Possessive Adjectives and Possessive Pronouns (5pts)",
        "type": "fill_blank",
        "question": "Those shoes are _______. I bought them yesterday. (Write the complete sentence)",
        "correct": "Those shoes are mine. I bought them yesterday.",
        "accepts": [
            "Those shoes are mine. I bought them yesterday.",
            "Those shoes are mine. I bought them yesterday",
            "those shoes are mine. i bought them yesterday.",
            "those shoes are mine. i bought them yesterday",
            "Those shoes are mine, I bought them yesterday.",
            "Those shoes are mine, I bought them yesterday"
        ],
        "points": 1
    },
    {
        "section": "Possessive Adjectives and Possessive Pronouns (5pts)",
        "type": "fill_blank",
        "question": "This is _______ umbrella, not his. (Write the complete sentence) SHE",
        "correct": "This is her umbrella, not his.",
        "accepts": [
            "This is her umbrella, not his.",
            "This is her umbrella, not his",
            "this is her umbrella, not his.",
            "this is her umbrella, not his",
            "This is her umbrella not his.",
            "This is her umbrella not his"
        ],
        "points": 1
    },
    {
        "section": "Possessive Adjectives and Possessive Pronouns (5pts)",
        "type": "fill_blank",
        "question": "These are _______ keys. We found them in your bag. (Write the complete sentence) THEY",
        "correct": "These are their keys. We found them in your bag.",
        "accepts": [
            "These are their keys. We found them in your bag.",
            "These are their keys. We found them in your bag",
            "these are their keys. we found them in your bag.",
            "these are their keys. we found them in your bag",
            "These are their keys, we found them in your bag.",
            "These are their keys, we found them in your bag"
        ],
        "points": 1
    },

    # ============================================
    # SECTION 7: Additions with too and either (3 points)
    # ============================================
    {
        "section": "Additions with too and either (3pts)",
        "type": "fill_blank",
        "question": "Re-write the sentence using too or either: \n\n 'John is busy and I am busy ___.'",
        "correct": "John is busy and I am, too.",
        "accepts": [
            "John is busy and I am, too.",
            "John is busy and I am, too",
            "john is busy and i am, too.",
            "john is busy and i am, too",
            "John is busy and I am too.",
            "John is busy and I am too",
            # Accept the literal completion with "busy, too"
            "John is busy and I am busy, too.",
            "John is busy and I am busy, too",
            "john is busy and i am busy, too.",
            "john is busy and i am busy, too"
        ],
        "points": 1
    },
    {
        "section": "Additions with too and either (3pts)",
        "type": "fill_blank",
        "question": "Re-write the sentence using too or either: \n\n 'Maria is not at home and she is not at home ____.'",
        "correct": "Maria is not at home and she is not, either.",
        "accepts": [
            "Maria is not at home and she is not, either.",
            "Maria is not at home and she is not, either",
            "maria is not at home and she is not, either.",
            "maria is not at home and she is not, either",
            "Maria is not at home and she is not either.",
            "Maria is not at home and she is not either",
            # Accept the literal completion
            "Maria is not at home and she is not at home, either.",
            "Maria is not at home and she is not at home, either",
            "maria is not at home and she is not at home, either.",
            "maria is not at home and she is not at home, either"
        ],
        "points": 1
    },
    {
        "section": "Additions with too and either (3pts)",
        "type": "fill_blank",
        "question": "Re-write the sentence using too or either: \n\n 'They don't like pizza and we don't like pizza ____.'",
        "correct": "They don't like pizza and we don't, either.",
        "accepts": [
            "They don't like pizza and we don't, either.",
            "They don't like pizza and we don't, either",
            "they don't like pizza and we don't, either.",
            "they don't like pizza and we don't, either",
            "They don't like pizza and we don't either.",
            "They don't like pizza and we don't either",
            # Accept the literal completion
            "They don't like pizza and we don't like pizza, either.",
            "They don't like pizza and we don't like pizza, either",
            "they don't like pizza and we don't like pizza, either.",
            "they don't like pizza and we don't like pizza, either"
        ],
        "points": 1
    },

    # ============================================
    # SECTION 8: Comparing Adjectives (5 points)
    # ============================================
    {
        "section": "Comparing Adjectives (5 points)",
        "type": "fill_blank",
        "question": "What is the comparative form of 'Heavy'?",
        "correct": "Heavier",
        "accepts": ["Heavier", "heavier"],
        "points": 1
    }, 
    {
        "section": "Comparing Adjectives (5 points)",
        "type": "fill_blank",
        "question": "What is the comparative form of 'convenient'?",
        "correct": "more convenient", 
        "accepts": ["more convenient", "More convenient", "More Convenient"],
        "points": 1
    }, 
    {
        "section": "Comparing Adjectives (5 points)",
        "type": "fill_blank",
        "question": "What is the comparative form of 'Good'?",
        "correct": "Better",
        "accepts": ["Better", "better"],
        "points": 1
    }, 
    {
        "section": "Comparing Adjectives (5 points)",
        "type": "fill_blank",
        "question": "What is the comparative form of 'Beautiful'?",
        "correct": "More beautiful",
        "accepts": ["More beautiful", "more beautiful", "More Beautiful"],
        "points": 1
    }, 
    {
        "section": "Comparing Adjectives (5 points)",
        "type": "fill_blank",
        "question": "What is the comparative form of 'Fast'?",
        "correct": "Faster",
        "accepts": ["Faster", "faster"],
        "points": 1
    },
    
    # ============================================
    # SECTION 9: Comparing with as ... as (4 points)
    # ============================================
    {
        "section": "Comparing with as ... as - Write COMPLETE sentences (4 points)",
        "type": "write_sentence",
        "question": "Complete the sentence using as ... as: \n\n 'This car is / that car (fast)'",
        "correct": "This car is as fast as that car.",
        "accepts": [
            "This car is as fast as that car.",
            "This car is as fast as that car",
            "this car is as fast as that car.",
            "this car is as fast as that car"
        ],
        "points": 1
    }, 
    {
        "section": "Comparing with as ... as - Write COMPLETE sentences (4 points)",
        "type": "write_sentence",
        "question": "Complete the sentence using as ... as: \n\n 'Customer service at hello.com / at world.com (not good)'",
        "correct": "Customer service at hello.com is not as good as at world.com.",
        "accepts": [
            "Customer service at hello.com is not as good as at world.com.",
            "Customer service at hello.com is not as good as at world.com",
            "customer service at hello.com is not as good as at world.com.",
            "customer service at hello.com is not as good as at world.com",
            # Also accept "it is at" variation
            "Customer service at hello.com is not as good as it is at world.com.",
            "Customer service at hello.com is not as good as it is at world.com",
            "customer service at hello.com is not as good as it is at world.com.",
            "customer service at hello.com is not as good as it is at world.com"
        ],
        "points": 1
    }, 
    {
        "section": "Comparing with as ... as - Write COMPLETE sentences (4 points)",
        "type": "write_sentence",
        "question": "Complete the sentence using as ... as: \n\n 'Shopping on aro.com / it is on acb.com (easy)'",
        "correct": "Shopping on aro.com is as easy as it is on acb.com.",
        "accepts": [
            "Shopping on aro.com is as easy as it is on acb.com.",
            "Shopping on aro.com is as easy as it is on acb.com",
            "shopping on aro.com is as easy as it is on acb.com.",
            "shopping on aro.com is as easy as it is on acb.com",
            # Accept without "it is"
            "Shopping on aro.com is as easy as on acb.com.",
            "Shopping on aro.com is as easy as on acb.com",
            "shopping on aro.com is as easy as on acb.com.",
            "shopping on aro.com is as easy as on acb.com",
            # Accept "acb.com" without "on"
            "Shopping on aro.com is as easy as acb.com.",
            "Shopping on aro.com is as easy as acb.com",
            "shopping on aro.com is as easy as acb.com.",
            "shopping on aro.com is as easy as acb.com"
        ],
        "points": 1
    }, 
    {
        "section": "Comparing with as ... as - Write COMPLETE sentences (4 points)",
        "type": "write_sentence",
        "question": "Complete the sentence using as ... as: \n\n 'Prices at La Torre / they are at Maxi (not high)'",
        "correct": "Prices at La Torre are not as high as they are at Maxi.",
        "accepts": [
            "Prices at La Torre are not as high as they are at Maxi.",
            "Prices at La Torre are not as high as they are at Maxi",
            "prices at La Torre are not as high as they are at Maxi.",
            "prices at La Torre are not as high as they are at Maxi",
            "prices at la Torre are not as high as they are at Maxi.",
            "prices at la Torre are not as high as they are at Maxi",
            "Prices at la Torre are not as high as they are at Maxi.",
            "Prices at la Torre are not as high as they are at Maxi",
            "prices at la torre are not as high as they are at maxi.",
            "prices at la torre are not as high as they are at maxi",
            # Accept without "they are"
            "Prices at La Torre are not as high as at Maxi.",
            "Prices at La Torre are not as high as at Maxi",
            "prices at la torre are not as high as at maxi.",
            "prices at la torre are not as high as at maxi"
        ],
        "points": 1
    }
]

def calculate_grammar_score_internal():
    """
    Calcula el score de grammar interno
    """
    correct_points = 0
    total_graded_points = 0
    
    for idx, q in enumerate(GRAMMAR_QUESTIONS):
        if idx in st.session_state.grammar_responses:
            user_answer = st.session_state.grammar_responses[idx]
            
            # Multiple choice
            if q['type'] == 'multiple_choice':
                total_graded_points += q['points']
                if user_answer == q['correct']:
                    correct_points += q['points']
            
            # Fill in the blank
            elif q['type'] == 'fill_blank':
                total_graded_points += q['points']
                if user_answer.lower() in [ans.lower() for ans in q['accepts']]:
                    correct_points += q['points']
            
            # Write sentence
            elif q['type'] == 'write_sentence':
                total_graded_points += q['points']
                if user_answer.lower() in [ans.lower() for ans in q['accepts']]:
                    correct_points += q['points']
    
    return correct_points, total_graded_points

def show_grammar():
    st.markdown("### GRAMMAR SECTION (52 points)")
    st.caption("Answer all questions carefully. Total: 52 points")
    
    # Inicializar respuestas si no existen
    if 'grammar_responses' not in st.session_state:
        st.session_state.grammar_responses = {}
    
    current_section = None
    
    # Mostrar cada pregunta según su tipo
    for idx, q in enumerate(GRAMMAR_QUESTIONS):
        # Mostrar encabezado de sección si es nueva
        if q.get("section") != current_section:
            current_section = q.get("section")
            st.markdown(f"### 📝 {current_section}")
            st.divider()
        
        st.markdown(f"**Question {idx + 1}** ({q['points']} pts): {q['question']}")
        
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
        
        st.markdown("")  # Espacio entre preguntas
    
    st.divider()
    
    # Calcular puntaje usando la función interna
    correct_points, total_graded_points = calculate_grammar_score_internal()
    
    # Guardar puntaje en session state INMEDIATAMENTE
    st.session_state.grammar_score = correct_points
    st.session_state.grammar_total = total_graded_points
    
    # Formatear respuestas para el email
    grammar_text = ""
    current_section_text = None
    
    for idx, q in enumerate(GRAMMAR_QUESTIONS):
        # Agregar encabezado de sección
        if q.get("section") != current_section_text:
            current_section_text = q.get("section")
            grammar_text += f"\n{'='*60}\n{current_section_text}\n{'='*60}\n"
        
        user_answer = st.session_state.grammar_responses.get(idx, "No answer")
        grammar_text += f"\nQ{idx + 1}. ({q['points']} pts) {q['question']}\n"
        grammar_text += f"Student answer: {user_answer}\n"
        
        # Agregar corrección para todas las preguntas
        if q['type'] == 'multiple_choice':
            is_correct = user_answer == q['correct']
            grammar_text += f"Correct answer: {q['correct']} {'✓' if is_correct else '✗'}\n"
            grammar_text += f"Points earned: {q['points'] if is_correct else 0}/{q['points']}\n"
        elif q['type'] == 'fill_blank':
            is_correct = user_answer.lower() in [ans.lower() for ans in q['accepts']]
            grammar_text += f"Correct answer: {q['correct']} {'✓' if is_correct else '✗'}\n"
            grammar_text += f"Points earned: {q['points'] if is_correct else 0}/{q['points']}\n"
        elif q['type'] == 'write_sentence':
            is_correct = user_answer.lower() in [ans.lower() for ans in q['accepts']]
            word_count = len(user_answer.split()) if user_answer else 0
            grammar_text += f"Correct answer: {q['correct']} {'✓' if is_correct else '✗'}\n"
            grammar_text += f"Word count: {word_count}\n"
            grammar_text += f"Points earned: {q['points'] if is_correct else 0}/{q['points']}\n"
    
    grammar_text += f"\n{'='*60}\n"
    grammar_text += f"AUTO-GRADED SCORE: {correct_points}/{total_graded_points} points\n"
    grammar_text += f"TOTAL POSSIBLE POINTS: 52\n"
    grammar_text += f"PERCENTAGE: {(correct_points/total_graded_points*100) if total_graded_points > 0 else 0:.1f}%\n"
    
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