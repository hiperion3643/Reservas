import streamlit as st
from datetime import datetime, date
import subprocess
import os
import tempfile
import base64
import shutil
from jinja2 import Environment

# Configuración de página
st.set_page_config(
    page_title="Generador de Memorandums",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Generador de Memorandums para Solicitud de Vehículos")
st.markdown("Complete el formulario para generar su memorandum con la plantilla institucional")

# Funciones auxiliares
def obtener_iniciales(nombre_completo):
    """Obtiene las primeras 4 iniciales del nombre"""
    palabras = nombre_completo.strip().upper().split()
    iniciales = ''.join([palabra[0] for palabra in palabras if palabra])
    return iniciales[:4]

def fecha_espanol(fecha):
    """Convierte fecha a formato español"""
    meses = {
        1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
        5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
        9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
    }
    return f"{fecha.day} de {meses[fecha.month]} de {fecha.year}"

def verificar_latex():
    """Verifica si LaTeX está instalado"""
    try:
        result = subprocess.run(['pdflatex', '--version'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return True
        return False
    except:
        return False

def generar_latex_con_datos(datos):
    """Lee la plantilla LaTeX y reemplaza las variables usando Jinja2"""
    
    # Leer plantilla LaTeX
    with open('memo_reservas.tex', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Crear Environment de Jinja2 con delimitadores que no conflicten con LaTeX
    env = Environment(variable_start_string='[[', variable_end_string=']]')
    template = env.from_string(template_content)
    
    # Renderizar con los datos
    latex_code = template.render(**datos)
    
    return latex_code

def compilar_pdf(latex_code, output_dir):
    """Compila el código LaTeX a PDF"""
    try:
        tex_path = os.path.join(output_dir, 'memorandum.tex')
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(latex_code)
        
        # Copiar la plantilla PDF al directorio temporal para que LaTeX la encuentre
        if os.path.exists('Hoja_Membretada.pdf'):
            shutil.copy2('Hoja_Membretada.pdf', os.path.join(output_dir, 'Hoja_Membretada.pdf'))
        else:
            st.error("❌ No se encuentra el archivo Hoja_Membretada.pdf")
            return None
        
        # Compilar LaTeX dos veces
        for i in range(2):
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', '-output-directory', output_dir, tex_path],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                # Buscar errores específicos
                error_lines = []
                for line in result.stdout.split('\n'):
                    if 'Error' in line or 'error' in line or '!' in line:
                        error_lines.append(line)
                
                if error_lines:
                    st.error("❌ Errores de compilación LaTeX:")
                    for err in error_lines[:5]:
                        st.code(err)
                return None
        
        pdf_path = os.path.join(output_dir, 'memorandum.pdf')
        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as f:
                return f.read()
        
        return None
        
    except subprocess.TimeoutExpired:
        st.error("❌ Tiempo de espera agotado en la compilación")
        return None
    except Exception as e:
        st.error(f"❌ Error al compilar: {str(e)}")
        return None

def get_download_link(pdf_bytes, filename):
    """Genera link de descarga para el PDF"""
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}">'
    href += '<button style="background-color: #4CAF50; color: white; padding: 12px 24px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; font-weight: bold;">'
    href += '📥 Descargar Memorandum PDF'
    href += '</button></a>'
    return href

# Sidebar
with st.sidebar:
    st.header("📋 Instrucciones")
    st.markdown("""
    1. Verifica que los archivos estén en la carpeta:
       - `Hoja_Membretada.pdf` (tu plantilla)
       - `memo_reservas.tex` (código LaTeX)
    2. Completa el formulario
    3. Agrega destinos con el botón "+"
    4. Genera y descarga el PDF
    """)
    
    st.divider()
    
    st.header("✅ Verificación de archivos")
    
    # Verificar LaTeX
    if verificar_latex():
        st.success("✅ LaTeX está instalado")
    else:
        st.error("❌ LaTeX no está instalado")
        st.info("Instala MiKTeX (Windows) o TeX Live (Linux/Mac)")
    
    # Verificar plantilla PDF
    if os.path.exists('Hoja_Membretada.pdf'):
        st.success("✅ Hoja_Membretada.pdf encontrada")
    else:
        st.error("❌ No se encuentra Hoja_Membretada.pdf")
    
    # Verificar plantilla LaTeX
    if os.path.exists('memo_reservas.tex'):
        st.success("✅ memo_reservas.tex encontrada")
    else:
        st.error("❌ No se encuentra memo_reservas.tex")

# Inicializar sesión para destinos
if 'destinos' not in st.session_state:
    st.session_state.destinos = [{'nombre': '', 'ubicacion': '', 'motivo': ''}]

# Formulario principal
with st.form("solicitud_form"):
    st.header("📋 Información del Solicitante")
    
    col1, col2 = st.columns(2)
    
    with col1:
        solicitante_nombre = st.text_input("Nombre completo del solicitante *")
        solicitante_puesto = st.text_input("Puesto del solicitante *")
        departamento = st.text_input("Departamento de adscripción *")
        
    with col2:
        asunto = st.text_input("Asunto *", value="Solicitud de vehículo institucional")
        fecha_uso = st.date_input("Fecha de salida *", min_value=date.today())
        fecha_regreso = st.date_input("Fecha de regreso *", min_value=date.today())
        
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            hora_inicio = st.time_input("Hora de salida *", value=datetime.strptime("08:00", "%H:%M").time())
        with col_h2:
            hora_fin = st.time_input("Hora de regreso *", value=datetime.strptime("17:00", "%H:%M").time())
    
    st.header("📍 Destinos")
    
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        if st.form_submit_button("➕ Agregar destino"):
            st.session_state.destinos.append({'nombre': '', 'ubicacion': '', 'motivo': ''})
            st.rerun()
    with col_btn2:
        if len(st.session_state.destinos) > 1:
            if st.form_submit_button("➖ Quitar último"):
                st.session_state.destinos.pop()
                st.rerun()
    
    destinos_data = []
    for i, destino in enumerate(st.session_state.destinos):
        with st.container():
            st.markdown(f"**Destino {i+1}**")
            col_d1, col_d2, col_d3 = st.columns([2, 2, 3])
            with col_d1:
                nombre = st.text_input("Lugar", value=destino['nombre'], key=f"nom_{i}")
            with col_d2:
                ubicacion = st.text_input("Ubicación", value=destino['ubicacion'], key=f"ubi_{i}")
            with col_d3:
                motivo = st.text_input("Motivo", value=destino['motivo'], key=f"mot_{i}")
            destinos_data.append({'nombre': nombre, 'ubicacion': ubicacion, 'motivo': motivo})
    
    motivo_general = st.text_area("Motivo general (opcional)")
    
    st.header("👥 Personal que viaja")
    numero_personas = st.number_input("Total de personas (incluyendo solicitante) *", min_value=1, value=2, step=1)
    
    submitted = st.form_submit_button("📄 Generar Memorandum", type="primary")
    
    if submitted:
        # Validaciones
        if not os.path.exists('Hoja_Membretada.pdf'):
            st.error("❌ No se encuentra el archivo Hoja_Membretada.pdf")
        elif not os.path.exists('memo_reservas.tex'):
            st.error("❌ No se encuentra el archivo memo_reservas.tex")
        elif not verificar_latex():
            st.error("❌ LaTeX no está instalado correctamente")
        elif not all([solicitante_nombre, solicitante_puesto, departamento]):
            st.error("❌ Complete todos los campos obligatorios (marcados con *)")
        elif fecha_regreso < fecha_uso:
            st.error("❌ La fecha de regreso no puede ser menor a la fecha de salida")
        else:
            # Preparar texto de destinos
            destinos_filtrados = [d for d in destinos_data if d['nombre'] and d['ubicacion']]
            
            if destinos_filtrados:
                destinos_texto = "El vehículo será utilizado para visitar los siguientes lugares:\n\n"
                for i, d in enumerate(destinos_filtrados, 1):
                    destinos_texto += f"{i}. {d['nombre']}\n"
                    destinos_texto += f"   Ubicación: {d['ubicacion']}\n"
                    if d.get('motivo'):
                        destinos_texto += f"   Motivo: {d['motivo']}\n"
                    destinos_texto += "\n"
            elif motivo_general:
                destinos_texto = f"El vehículo será utilizado para: {motivo_general}"
            else:
                destinos_texto = "No se especificaron destinos."
            
            # Texto de personal
            if numero_personas == 1:
                texto_personal = f"El personal que realizará el viaje estará a cargo del C. {solicitante_nombre}, {solicitante_puesto} del Departamento de {departamento}."
            else:
                texto_personal = f"El personal que realizará el viaje estará a cargo del C. {solicitante_nombre}, {solicitante_puesto} del Departamento de {departamento}, junto con {numero_personas - 1} personas adicionales."
            
            # Texto de fechas
            if fecha_uso == fecha_regreso:
                texto_fechas = f"el día {fecha_uso.strftime('%d/%m/%Y')}"
            else:
                texto_fechas = f"del día {fecha_uso.strftime('%d/%m/%Y')} al {fecha_regreso.strftime('%d/%m/%Y')}"
            
            # Generar folio
            folio = datetime.now().strftime("%Y%m%d%H%M%S")
            
            # Fecha actual formateada
            fecha_actual = fecha_espanol(datetime.now())
            
            # Preparar datos para Jinja2
            datos_template = {
                'folio': folio,
                'asunto': asunto,
                'fecha_actual': fecha_actual,
                'texto_fechas': texto_fechas,
                'hora_inicio': hora_inicio.strftime("%H:%M"),
                'hora_fin': hora_fin.strftime("%H:%M"),
                'destinos': destinos_texto,
                'texto_personal': texto_personal,
                'solicitante_nombre': solicitante_nombre.upper(),
                'solicitante_puesto': solicitante_puesto.upper(),
                'departamento': departamento.upper(),
                'elaboro': obtener_iniciales(solicitante_nombre),
                'fecha_uso': fecha_uso.strftime("%d/%m/%Y"),
                'fecha_regreso': fecha_regreso.strftime("%d/%m/%Y"),
                'numero_personas': numero_personas,
                'destinos_lista': destinos_filtrados  # Para posible uso avanzado
            }
            
            # Generar y compilar
            with st.spinner("Generando memorandum..."):
                latex_code = generar_latex_con_datos(datos_template)
                
                with tempfile.TemporaryDirectory() as tmpdirname:
                    pdf_bytes = compilar_pdf(latex_code, tmpdirname)
                    
                    if pdf_bytes:
                        st.success("✅ Memorandum generado exitosamente")
                        filename = f"Memorandum_{folio}.pdf"
                        st.markdown(get_download_link(pdf_bytes, filename), unsafe_allow_html=True)
                        
                        # Mostrar resumen
                        with st.expander("📋 Ver resumen del memorandum"):
                            st.write(f"**Folio:** {folio}")
                            st.write(f"**Solicitante:** {solicitante_nombre}")
                            st.write(f"**Período:** {texto_fechas}")
                            st.write(f"**Horario:** {hora_inicio.strftime('%H:%M')} - {hora_fin.strftime('%H:%M')}")
                            st.write(f"**Total personas:** {numero_personas}")
                            if destinos_filtrados:
                                st.write("**Destinos:**")
                                for d in destinos_filtrados:
                                    st.write(f"- {d['nombre']} ({d['ubicacion']})")
                    else:
                        st.error("❌ Error al generar el PDF. Revisa los mensajes de error arriba.")

st.markdown("---")
st.markdown("© 2025 - Sistema de Generación de Memorandums")