import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import streamlit as st
import re

def sanitize_sheet_name(name):
    """
    Limpia el nombre para que sea válido en Google Sheets
    - Máximo 100 caracteres
    - No puede contener: [ ] * ? : \ /
    """
    # Reemplazar caracteres no permitidos
    name = re.sub(r'[\[\]*?:\\/]', '_', name)
    # Limitar a 100 caracteres
    name = name[:100]
    return name

def enviar_a_sheets(nombre, email, clase, listening, grammar, reading, writing, switches, grammar_score=None, grammar_total=None, listening_score=None, listening_total=None, reading_score=None, reading_total=None):
    """
    Envía los resultados del assessment a Google Sheets
    Crea una nueva pestaña para cada estudiante
    """
    try:
        # Configurar credenciales
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        
        # Obtener credenciales desde secrets
        creds = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"], 
            scopes=scope
        )
        
        # Autorizar cliente
        client = gspread.authorize(creds)
        
        # Abrir la hoja de cálculo
        spreadsheet_name = st.secrets["sheets"]["spreadsheet_name"]
        spreadsheet = client.open(spreadsheet_name)
        
        # Crear nombre de pestaña: "Nombre - Fecha"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        sheet_name = sanitize_sheet_name(f"{nombre} - {timestamp}")
        
        # Intentar crear una nueva pestaña con MÁS FILAS
        try:
            worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=500, cols=10)
        except gspread.exceptions.APIError as e:
            # Si ya existe, agregar un número
            sheet_name = sanitize_sheet_name(f"{nombre} - {timestamp} (2)")
            worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=500, cols=10)
        
        # Formatear scores
        listening_score_text = ""
        grammar_score_text = ""
        reading_score_text = ""
        
        if listening_score is not None and listening_total is not None:
            percentage = (listening_score/listening_total*100) if listening_total > 0 else 0
            listening_score_text = f"AUTO-GRADED SCORE: {listening_score}/{listening_total} ({percentage:.1f}%)"
        
        if grammar_score is not None and grammar_total is not None:
            percentage = (grammar_score/grammar_total*100) if grammar_total > 0 else 0
            grammar_score_text = f"AUTO-GRADED SCORE: {grammar_score}/{grammar_total} ({percentage:.1f}%)"
        
        if reading_score is not None and reading_total is not None:
            percentage = (reading_score/reading_total*100) if reading_total > 0 else 0
            reading_score_text = f"AUTO-GRADED SCORE: {reading_score}/{reading_total} ({percentage:.1f}%)"
        
        # Crear el contenido de la pestaña con formato
        data = [
            ["WRITTEN ASSESSMENT SUBMISSION"],
            [""],
            ["Student Information"],
            ["Name:", nombre],
            ["Email:", email],
            ["Class:", clase],
            ["Submission Time:", datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
            [""],
            ["="*80],
            ["LISTENING SECTION - 17 points"],
            ["="*80],
            [""]
        ]
        
        # Agregar listening respuestas línea por línea
        if listening:
            for line in listening.split('\n'):
                data.append([line])
        
        data.extend([
            [""],
            [listening_score_text],
            [""],
            ["="*80],
            ["GRAMMAR SECTION - 52 points"],
            ["="*80],
            [""]
        ])
        
        # Agregar grammar respuestas línea por línea
        if grammar:
            for line in grammar.split('\n'):
                data.append([line])
        
        data.extend([
            [""],
            [grammar_score_text],
            [""],
            ["="*80],
            ["READING SECTION - 16 points"],
            ["="*80],
            [""]
        ])
        
        # Agregar reading respuestas línea por línea
        if reading:
            for line in reading.split('\n'):
                data.append([line])
        
        data.extend([
            [""],
            [reading_score_text],
            [""],
            ["="*80],
            ["WRITING SECTION - 15 points (Manual Grading Required)"],
            ["="*80],
            [""]
        ])
        
        # Agregar writing respuestas línea por línea
        if writing:
            for line in writing.split('\n'):
                data.append([line])
        
        data.extend([
            [""],
            ["="*80],
            ["SECURITY METRICS"],
            ["="*80],
            ["Tab switches:", switches],
            ["Status:", "HIGH ACTIVITY - Review recommended" if switches > 5 else "Normal activity"]
        ])
        
        # Escribir los datos
        worksheet.update('A1', data, value_input_option='RAW')
        
        # Formatear solo el encabezado principal
        worksheet.format('A1', {
            'textFormat': {'bold': True, 'fontSize': 14}
        })
        worksheet.format('A3', {
            'textFormat': {'bold': True},
            'backgroundColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}
        })
        
        # Ajustar ancho de columna A usando el método correcto
        try:
            worksheet.columns_auto_resize(0, 0)  # Auto-resize columna A (índice 0)
        except:
            pass  # Si falla, no pasa nada
        
        print(f"\n{'='*50}")
        print(f"✅ Sheet created: {sheet_name}")
        print(f"✅ Total rows written: {len(data)}")
        print(f"{'='*50}\n")
        
        return True
        
    except gspread.exceptions.SpreadsheetNotFound:
        raise Exception(f"No se encontró la hoja '{spreadsheet_name}'. Verifica que existe y está compartida con el service account.")
    
    except gspread.exceptions.APIError as e:
        raise Exception(f"Error de API de Google Sheets: {str(e)}")
    
    except KeyError as e:
        raise Exception(f"Falta configuración en secrets.toml: {str(e)}")
    
    except Exception as e:
        raise Exception(f"Error al guardar en Google Sheets: {str(e)}")


def test_connection():
    """
    Función de prueba para verificar la conexión
    """
    try:
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        
        creds = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"], 
            scopes=scope
        )
        
        client = gspread.authorize(creds)
        spreadsheet_name = st.secrets["sheets"]["spreadsheet_name"]
        spreadsheet = client.open(spreadsheet_name)
        
        return True, f"✅ Conexión exitosa con '{spreadsheet_name}'"
        
    except Exception as e:
        return False, f"❌ Error: {str(e)}"