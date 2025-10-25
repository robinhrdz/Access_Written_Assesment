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

def enviar_a_sheets(nombre, email, clase, listening, grammar, reading, writing, switches):
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
        
        # Intentar crear una nueva pestaña
        try:
            worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=100, cols=10)
        except gspread.exceptions.APIError as e:
            # Si ya existe, agregar un número
            sheet_name = sanitize_sheet_name(f"{nombre} - {timestamp} (2)")
            worksheet = spreadsheet.add_worksheet(title=sheet_name, rows=100, cols=10)
        
        # Formatear grammar score
        grammar_score = ""
        if 'grammar_score' in st.session_state:
            score = st.session_state.grammar_score
            total = st.session_state.grammar_total
            percentage = (score/total*100) if total > 0 else 0
            grammar_score = f"{score}/{total} ({percentage:.1f}%)"
        
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
            ["LISTENING SECTION"],
            ["=" * 50],
            [listening],
            [""],
            ["GRAMMAR SECTION"],
            ["=" * 50],
            [grammar],
            [""],
            ["Grammar Score:", grammar_score],
            [""],
            ["READING SECTION"],
            ["=" * 50],
            [reading],
            [""],
            ["WRITING SECTION"],
            ["=" * 50],
            [writing],
            [""],
            ["SECURITY METRICS"],
            ["=" * 50],
            ["Tab switches:", switches],
            ["Status:", "HIGH ACTIVITY - Review recommended" if switches > 5 else "Normal activity"]
        ]
        
        # Escribir los datos
        worksheet.update('A1', data, value_input_option='RAW')
        
        # Formatear encabezados (negrita)
        worksheet.format('A1', {
            'textFormat': {'bold': True, 'fontSize': 14}
        })
        worksheet.format('A3', {
            'textFormat': {'bold': True},
            'backgroundColor': {'red': 0.9, 'green': 0.9, 'blue': 0.9}
        })
        worksheet.format('A9', {
            'textFormat': {'bold': True},
            'backgroundColor': {'red': 0.85, 'green': 0.95, 'blue': 1}
        })
        worksheet.format('A13', {
            'textFormat': {'bold': True},
            'backgroundColor': {'red': 0.85, 'green': 0.95, 'blue': 1}
        })
        worksheet.format('A19', {
            'textFormat': {'bold': True},
            'backgroundColor': {'red': 0.85, 'green': 0.95, 'blue': 1}
        })
        worksheet.format('A23', {
            'textFormat': {'bold': True},
            'backgroundColor': {'red': 0.85, 'green': 0.95, 'blue': 1}
        })
        worksheet.format('A27', {
            'textFormat': {'bold': True},
            'backgroundColor': {'red': 1, 'green': 0.95, 'blue': 0.8}
        })
        
        # Ajustar ancho de columnas
        worksheet.columns_auto_resize(0, 1)  # Auto-ajustar columna A
        
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