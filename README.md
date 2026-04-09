# 📄 Generador de Memorandums de Solicitud de Vehículos

Sistema automatizado para generar memorandums institucionales con tabla de destinos formateada, optimizado para impresión en **tamaño carta**.

## ✨ Mejoras v2.0

- ✅ **Formato Letter (Tamaño Carta)**: Página optimizada para impresoras estándar
- ✅ **DataFrame de Pandas**: Manejo robusto de datos de destinos
- ✅ **Tabla LaTeX adaptada**: Columnas con ancho fijo para mejor presentación
- ✅ **Márgenes calibrados**: Ajustados para el tamaño carta
- ✅ **Validación mejorada**: Previene errores antes de generar PDF

## 📋 Requisitos

- Python 3.8+
- LaTeX instalado:
  - **Windows**: MiKTeX
  - **Linux**: TeX Live
  - **Mac**: MacTeX
- Archivo `Hoja_Membretada.pdf` en el directorio raíz

## ⚙️ Instalación

```bash
pip install -r requirements.txt
```

## 🚀 Uso

```bash
streamlit run app.py
```

### Pasos para generar un memorandum

1. **Información del Solicitante**
   - Nombre completo
   - Puesto
   - Departamento
   - Asunto

2. **Fechas y Horarios**
   - Fecha de salida
   - Fecha de regreso
   - Hora de inicio
   - Hora de regreso

3. **Destinos** *(almacenados en DataFrame)*
   - Click en "➕ Agregar destino"
   - Ingrese: Lugar, Ubicación, Motivo
   - Los datos se procesan automáticamente

4. **Personal**
   - Total de personas que viajan

5. **Generar**
   - Click en "Generar Memorandum"
   - Descargue el PDF

## 📐 Especificaciones Técnicas

### Configuración de Página
```
Tipo:        Letter (Carta) - 8.5" × 11"
Márgenes:    2.5cm (laterales), 3.8cm (superior), 2.5cm (inferior)
```

### Tabla de Destinos
```
Columnas:    Lugar (3.5cm) | Ubicación (3.5cm) | Motivo (4cm)
Origen:      DataFrame de Pandas
Formato:     Tabla LaTeX con bordes
```

## 📦 Archivos Requeridos

```
├── app.py                    # Aplicación Streamlit
├── memo_reservas.tex         # Plantilla LaTeX (letra)
├── Hoja_Membretada.pdf       # Membrete institucional
├── requirements.txt          # Dependencias
└── README.md
```

## 📝 Notas Importantes

- Los campos con * son obligatorios
- Mínimo un destino con Lugar y Ubicación
- Fecha en español automático
- Folio generado por timestamp
- Tabla dinámica según número de destinos
- Validación de datos antes de compilar

## 📧 Contacto

- 📧 officialia.partes@usalud.edu.mx
- 📞 22 26 90 06 13
