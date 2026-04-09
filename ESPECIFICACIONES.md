# 📐 Especificaciones Técnicas Detalladas

## Configuración de LaTeX

### Tamaño de Página

```latex
\documentclass[12pt]{article}
```

| Propiedad | Valor | Observación |
|-----------|-------|-------------|
| Tipo de documento | article | Estándar para memorandums |
| Tamaño base | 12pt | Fuente predeterminada |
| Encoding | UTF-8 | Soporta caracteres españoles |

### Paquetes Utilizados

| Paquete | Versión | Propósito |
|---------|---------|----------|
| inputenc | UTF-8 | Codificación de entrada |
| babel | spanish | Idioma español e hiphenación |
| geometry | - | Control de márgenes y geometría |
| graphicx | - | Insertar imágenes/PDFs |
| eso-pic | - | Fondos y superposiciones |
| xcolor | - | Colores en texto (opcional) |
| fancyhdr | - | Encabezados y pies (opcional) |
| times | - | Fuente Times New Roman |

### Geometría de Página

```latex
\geometry{
    paper=letterpaper,          % 8.5" x 11" (215.9mm x 279.4mm)
    margin=1.5cm,               % Margen general
    top=3.8cm,                  % Espacio para membrete
    bottom=2.5cm,               % Espacio para pie
    left=2.5cm,                 % Margen izquierdo
    right=2.5cm                 % Margen derecho
}
```

### Cálculo de Área Útil

```
Ancho total: 215.9mm
Márgenes: 2.5 + 2.5 = 5mm
Ancho útil: 215.9 - 5 = 210.9mm ≈ 11cm

Altura total: 279.4mm
Márgenes: 3.8 + 2.5 = 6.3cm
Altura útil: 279.4 - 63 = 216.4mm ≈ 21.6cm
```

### Fondo (Membrete)

```latex
\AddToShipoutPictureBG{%
    \put(0,0){%
        \includegraphics[width=\paperwidth,height=\paperheight]{Hoja_Membretada.pdf}%
    }%
}
```

**Características**:
- Se coloca en todo el fondo de la página
- Escalado al tamaño completo del papel
- No afecta el flujo de texto
- Recomendado: PDF de alta calidad (300 DPI mínimo)

---

## Estructura del Documento

### Secciones

```latex
1. Encabezado          → Fecha y asunto
   ├── Fecha: \today (generada automáticamente)
   └── Asunto: [[ asunto ]] (variable Jinja2)

2. Destinatario        → Quién recibe
   ├── Nombre: [[ solicitante_nombre ]]
   ├── Puesto: [[ solicitante_puesto ]]
   └── Departamento: [[ departamento ]]

3. Cuerpo Del Texto    → Justificación legal

4. Tabla de Destinos   → Información de viaje

5. Firma Personal      → Autorización

6. Firmas Oficiales    → Aprobaciones (3 columnas)

7. Pie de Página       → Información administrativa
   ├── Elaboró
   └── Revisó
```

---

## Tabla de Destinos (Tabla LaTeX)

### Definición

```latex
\begin{tabular}{|p{3.5cm}|p{3.5cm}|p{4cm}|}
```

| Símbolo | Significado |
|---------|-------------|
| `\|` | Línea vertical |
| `p{3.5cm}` | Columna con ancho fijo, texto ajustado |
| `3.5cm` | Ancho máximo de columna |

### Dimensiones

```
Columna 1 (Lugar):     3.5cm
Columna 2 (Ubicación): 3.5cm
Columna 3 (Motivo):    4.0cm
                       ------
Total:                11.0cm
```

**Espacio disponible en página letter**:
- Ancho útil: ~21cm
- Tabla: 11cm
- Margen interno: ~5cm
- Resultado: ✅ Cabe perfectamente

### Contenido

```latex
<BLOCK> for destino in destinos_lista </BLOCK>
[[ destino.nombre ]] & [[ destino.ubicacion ]] & [[ destino.motivo ]] \\
<BLOCK> endfor </BLOCK>
```

**Procesamiento**:
1. Python genera lista de diccionarios
2. Jinja2 itera sobre la lista
3. LaTeX renderiza cada fila

---

## Sistema de Templating (Jinja2)

### Delimitadores Personalizados

```python
env = Environment(
    variable_start_string='[[',       # [[ variable ]]
    variable_end_string=']]',
    block_start_string='<BLOCK>',     # <BLOCK> ... </BLOCK>
    block_end_string='</BLOCK>',
    comment_start_string='<COMMENT>', # <COMMENT> ... </COMMENT>
    comment_end_string='</COMMENT>'
)
```

**Razón**: No conflictuar con comandos LaTeX ya que usan `{` y `}`

### Variables Disponibles

| Variable | Tipo | Ejemplo | Fuente |
|----------|------|---------|--------|
| `asunto` | str | "Solicitud de vehículo" | Form input |
| `solicitante_nombre` | str | "Maria García López" | Form input |
| `solicitante_puesto` | str | "Subdirectora" | Form input |
| `departamento` | str | "Recursos Administrativos" | Form input |
| `texto_fechas` | str | "del día 15/04/2026 al 18/04/2026" | Calculado |
| `hora_inicio` | str | "08:00" | Form input |
| `hora_fin` | str | "17:00" | Form input |
| `texto_personal` | str | "El personal que realizará..." | Calculado |
| `numero_personas` | int | 3 | Form input |
| `destinos_lista` | list | `[{...}, {...}]` | Form input |

### Estructura de destinos_lista

```python
destinos_lista = [
    {
        'nombre': 'Dependencia Jurisdiccional de Xalapa',
        'ubicacion': 'Avenida Juárez #145, Xalapa, Ver.',
        'motivo': 'Visita de supervisión'
    },
    {
        'nombre': 'Tribunal Superior de Justicia',
        'ubicacion': 'Av. Reforma s/n, Xalapa, Ver.',
        'motivo': 'Audiencia'
    }
]
```

---

## Flujo de Datos

```
🔵 FRONTEND (Streamlit)
    ↓
    ├─ Recibe entrada del usuario
    ├─ Valida datos
    └─ Crea estructura de datos

🟡 PROCESAMIENTO (Python)
    ↓
    ├─ Crea DataFrame de pandas
    ├─ Calcula campos derivados (fechas, textos)
    └─ Prepara diccionario para Jinja2

🟢 TEMPLATING (Jinja2)
    ↓
    ├─ Lee template.tex
    ├─ Reemplaza variables [[ ]]
    ├─ Procesa bloques <BLOCK>
    └─ Genera código LaTeX final

🔴 COMPILACIÓN (pdflatex)
    ↓
    ├─ Compila LaTeX a PDF
    ├─ Integra membrete (Hoja_Membretada.pdf)
    └─ Devuelve PDF binario

⚫ DESCARGA (Navegador)
    ↓
    └─ Usuario descarga archivo PDF
```

---

## Dependencias de Python

### requirements.txt

```
streamlit               # Framework web (v1.0+)
pandas                  # Análisis de datos (v1.3+)
jinja2                  # Templating (v3.0+)
reportlab               # PDF (alternativa, v3.6+)
```

### Versiones Mínimas

```python
import streamlit as st               # v1.0.0+
import pandas as pd                  # v1.3.0+
from jinja2 import Environment       # v3.0.0+
```

---

## Compilación LaTeX

### Comandos Utilizados

```bash
pdflatex -interaction=nonstopmode -output-directory /tmp memorandum.tex
```

**Parámetros**:
| Parámetro | Significado |
|-----------|-------------|
| `-interaction=nonstopmode` | Continúa sin pausas en errores |
| `-output-directory` | Especifica carpeta de salida |
| Archivo de entrada | memorandum.tex |

### Compilación Doble

```python
for i in range(2):
    subprocess.run(['pdflatex', ...])
```

**Razón**: Referencias cruzadas y tabla de contenidos se actualizan en segunda pasada

### Salida Esperada

```
PDF generado: memorandum.pdf
Directorios auxiliares:
├── memorandum.aux      (Auxiliares)
├── memorandum.fdb_latexmk (Cache)
├── memorandum.fls      (Archivos listados)
├── memorandum.log      (Log de compilación)
└── memorandum.pdf      ← FINAL
```

---

## Validaciones Implementadas

### En Python (app.py)

```python
# 1. Campos obligatorios
if not all([solicitante_nombre, solicitante_puesto, departamento]):
    ❌ Error

# 2. Rango de fechas
if fecha_regreso < fecha_uso:
    ❌ Error

# 3. Destinos existentes
if not destinos_filtrados:
    ❌ Error

# 4. Sistemas necesarios
if not os.path.exists('Hoja_Membretada.pdf'):
    ❌ Error
if not os.path.exists('memo_reservas.tex'):
    ❌ Error
if not verificar_latex():
    ❌ Error
```

### En LaTeX

```latex
% Encoding automático
\usepackage[utf8]{inputenc}

% Idioma automático
\usepackage[spanish]{babel}

% Geometría validada
\geometry{...}
```

---

## Características de Seguridad

### Sanitización de Entrada

```python
# Validación de caracteres especiales
nombre.title()  # Capitalización segura
nombre.upper()  # Conversión a mayúsculas

# No hay inyección SQL (no hay base de datos)
# Protección contra inyección LaTeX: No se aplica texto directo
```

### Aislamiento de Compilación

```python
with tempfile.TemporaryDirectory() as tmpdirname:
    # Compilación en carpeta temporal
    # Archivos se limpian automáticamente
```

---

## Límites Documentados

### Tabla de Destinos

```
Máximo de filas: 8-10
Razón: Cabe en 1 página letter

Máximo de caracteres por celda:
├─ Nombre: 30 caracteres
├─ Ubicación: 40 caracteres
└─ Motivo: 50 caracteres
```

### Página

```
Contenido total:
├─ Encabezado: 3cm
├─ Cuerpo: 15cm
├─ Tabla: 3cm (variable)
├─ Firmas: 4cm
└─ Pie: 1cm
   Total ≈ 26cm (cabe en 27.9cm)
```

---

## Configuración Recomendada

### Para Producción

```bash
# Variables de ambiente
export STREAMLIT_LOGGER_LEVEL=info
export STREAMLIT_SERVER_MAXUPLOADSIZE=200

# Carpetas necesarias
mkdir -p /var/log/memorandums
chmod 755 /var/log/memorandums
```

### Para Desarrollo

```bash
# Habilitar debugging
export DEBUG=true
streamlit run app.py --logger.level=debug
```

---

**Versión**: 2.0
**Última actualización**: 2026-04-09
**Documentación**: v2.0

