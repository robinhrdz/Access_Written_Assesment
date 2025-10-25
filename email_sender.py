import smtplib
from email.message import EmailMessage
from datetime import datetime
import streamlit as st

CLASSES = {
    "Dream Chasers": "robin@guatemayalliance.org",
    "Everwood": "citlaly@guatemayalliance.org"
}

def enviar_evaluacion(nombre, email, clase, listening, grammar, reading, writing, switches):
    EMAIL = st.secrets["email"]["sender"]
    APP_PASSWORD = st.secrets["email"]["password"]
    
    em = EmailMessage()
    em["From"] = EMAIL
    em["To"] = CLASSES[clase]
    em["Reply-To"] = email
    em["Subject"] = f"[Assessment] {clase} - {nombre} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    
    cuerpo = f"""
WRITTEN ASSESSMENT SUBMISSION
=============================

Student Information:
- Name: {nombre}
- Email: {email}
- Class: {clase}
- Submission Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

LISTENING SECTION
{'-' * 50}
{listening}

GRAMMAR SECTION
{'-' * 50}
{grammar}

READING SECTION
{'-' * 50}
{reading}

WRITING SECTION
{'-' * 50}
{writing}

SECURITY METRICS
{'-' * 50}
Tab switches detected: {switches}
Status: {'HIGH ACTIVITY' if switches > 5 else 'Normal'}
"""
    
    em.set_content(cuerpo)
    
    # HTML version
    em.add_alternative(f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f5f5f5; padding: 20px; }}
                .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
                h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
                h2 {{ color: #34495e; margin-top: 30px; background: #ecf0f1; padding: 10px; border-radius: 5px; }}
                .info-box {{ background: #e8f4f8; padding: 15px; border-radius: 5px; margin: 20px 0; border-left: 4px solid #3498db; }}
                .section {{ background: #fafafa; padding: 20px; margin: 15px 0; border-radius: 5px; border: 1px solid #ddd; }}
                .security {{ background: {'#fff3cd' if switches > 5 else '#d1ecf1'}; padding: 15px; border-radius: 5px; border-left: 4px solid {'#ffc107' if switches > 5 else '#17a2b8'}; margin-top: 20px; }}
                pre {{ white-space: pre-wrap; word-wrap: break-word; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>WRITTEN ASSESSMENT SUBMISSION</h1>
                
                <div class="info-box">
                    <strong>Student:</strong> {nombre}<br>
                    <strong>Email:</strong> {email}<br>
                    <strong>Class:</strong> {clase}<br>
                    <strong>Submitted:</strong> {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}
                </div>
                
                <h2>LISTENING SECTION</h2>
                <div class="section">
                    <pre>{listening}</pre>
                </div>
                
                <h2>GRAMMAR SECTION</h2>
                <div class="section">
                    <pre>{grammar}</pre>
                </div>
                
                <h2>READING SECTION</h2>
                <div class="section">
                    <pre>{reading}</pre>
                </div>
                
                <h2>WRITING SECTION</h2>
                <div class="section">
                    <pre>{writing}</pre>
                </div>
                
                <div class="security">
                    <strong>Security Metrics:</strong><br>
                    Tab switches: <strong>{switches}</strong>
                    {' (High activity - Review recommended)' if switches > 5 else ' (Normal activity)'}
                </div>
            </div>
        </body>
        </html>
    """, subtype="html")
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as smtp:
            smtp.set_debuglevel(0)
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL, APP_PASSWORD)
            smtp.send_message(em)
    except Exception as smtp_error:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as smtp:
            smtp.login(EMAIL, APP_PASSWORD)
            smtp.send_message(em)