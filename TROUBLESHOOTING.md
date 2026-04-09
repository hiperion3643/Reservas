# 🔧 Guía de Troubleshooting

## Problemas Comunes y Soluciones

### 1. "LaTeX no está instalado"
**Error**: `❌ LaTeX no está instalado correctamente`

**Soluciones**:

#### Windows
```bash
# Descargar MiKTeX desde: https://miktex.org/
# O instalar con Chocolatey:
choco install miktex
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install texlive-full
# O versión mínima:
sudo apt-get install texlive texlive-latex-extra texlive-lang-spanish
```

#### macOS
```bash
# Con Homebrew:
brew install basictex
# O descargar desde: https://www.tug.org/mactex/
```

**Verificar instalación**:
```bash
pdflatex --version
```

---

### 2. "No se encuentra Hoja_Membretada.pdf"
**Error**: `❌ No se encuentra el archivo Hoja_Membretada.pdf`

**Causa**: El archivo no está en la carpeta correcta

**Solución**:
1. Verifica que `Hoja_Membretada.pdf` esté en la carpeta raíz del proyecto
2. Estructura correcta:
```
Reservas/
├── app.py
├── memo_reservas.tex
├── Hoja_Membretada.pdf     ← AQUÍ
├── requirements.txt
└── README.md
```

---

### 3. "No se encuentra memo_reservas.tex"
**Error**: `❌ No se encuentra el archivo memo_reservas.tex`

**Causa**: Template no está en la carpeta correcta

**Solución**:
Verifica que el archivo esté en la raíz del proyecto:
```
Reservas/
├── app.py
├── memo_reservas.tex       ← AQUÍ
├── Hoja_Membretada.pdf
└── requirements.txt
```

---

### 4. Errores de La tabla se corta al imprimir (tamaño A4)
**Síntoma**: La tabla aparece cortada o mal formateada

**Causa**: Se estaba usando tamaño A4 en v1.0

**Solución**: 
✅ Ya está corregido en v2.0 con `letterpaper`

**Verificación**:
En `memo_reservas.tex` línea 14 debe decir:
```latex
paper=letterpaper,    ← Correcto
```

---

### 5. Módulo pandas no encontrado
**Error**: `ModuleNotFoundError: No module named 'pandas'`

**Solución**:
```bash
# Instalar dependencias
pip install -r requirements.txt

# O instalar pandas específicamente
pip install pandas
```

---

### 6. El PDF está vacío o se corta
**Síntoma**: PDF generado pero sin contenido o cortado

**Causa**: Márgenes mal configurados o LaTeX con errores

**Solución**:
1. Verifica los márgenes en `memo_reservas.tex`:
```latex
\geometry{
    paper=letterpaper,
    margin=1.5cm,
    top=3.8cm,
    bottom=2.5cm,
    left=2.5cm,
    right=2.5cm
}
```

2. Reduce el número de destinos (máximo 6-7 en una página)

3. Reduce el tamaño de fuente en la tabla:
```latex
{\tiny              ← Cambiar a \tiny en lugar de \small
\begin{tabular}...
}
```

---

### 7. La hoja membretada no aparece
**Síntoma**: PDF generado pero sin fondo de hoja membretada

**Causa**: 
- Archivo PDF corrupto
- Ruta incorrecta

**Solución**:
1. Verifica que `Hoja_Membretada.pdf` es válido:
```bash
file Hoja_Membretada.pdf    # Debe mostrar: PDF document
```

2. Regenera el PDF siguiendo estos pasos:
   - Accede a `memo_reservas.tex`
   - Verifica línea 23-27:
```latex
\AddToShipoutPictureBG{%
    \put(0,0){%
        \includegraphics[width=\paperwidth,height=\paperheight]{Hoja_Membretada.pdf}%
    }%
}
```

3. Si sigue sin funcionar, comenta temporalmente:
```latex
% \AddToShipoutPictureBG{%
%     \put(0,0){%
%         \includegraphics[width=\paperwidth,height=\paperheight]{Hoja_Membretada.pdf}%
%     }%
% }
```

---

### 8. Caracteres especiales se ven mal (ñ, á, é, etc.)
**Síntoma**: Caracteres españoles aparecen como símbolos raros

**Causa**: Encoding incorrecto

**Solución**:
Verifica que `memo_reservas.tex` tenga:
```latex
\usepackage[utf8]{inputenc}     ← Línea 2
\usepackage[spanish]{babel}     ← Línea 3
```

Y verifica que el archivo esté guardado en UTF-8:
```bash
file -i memo_reservas.tex       # Debe ser: UTF-8
```

---

### 9. Streamlit se cuelga al generar PDF
**Síntoma**: App se congela/ tarda mucho tiempo

**Causa**: LaTeX compilando o timeout

**Solución**:
1. Espera más tiempo (compilación LaTeX es lenta)
2. Reduce el número de destinos
3. Verifica que LaTeX esté bien instalado:
```bash
pdflatex --version
```

---

### 10. "Debe agregar al menos un destino"
**Error**: `❌ Debe agregar al menos un destino con nombre y ubicación`

**Causa**: Falta llenar los campos Lugar y Ubicación

**Solución**:
1. Asegúrate de llenar ambos campos en cada destino:
   - ✅ "Lugar" (nombre del lugar)
   - ✅ "Ubicación" (ubicación geográfica)
   - ⭕ "Motivo" (opcional)

2. No puedes dejar campos vacíos

---

## 📊 Límites Recomendados

| Elemento | Mínimo | Máximo | Óptimo |
|----------|--------|--------|--------|
| Destinos | 1 | 8 | 3-5 |
| Caracteres por ubicación | - | 30 | 15 |
| Caracteres por motivo | - | 40 | 20 |
| Personas viajando | 1 | 20 | 2-10 |

---

## ✅ Checklist de Configuración

- [ ] LaTeX instalado: `pdflatex --version` funciona
- [ ] Archivo `Hoja_Membretada.pdf` existe en carpeta raíz
- [ ] Archivo `memo_reservas.tex` existe en carpeta raíz
- [ ] Dependencias instaladas: `pip list | grep pandas`
- [ ] Carpeta de proyecto es correcta:
```bash
pwd                          # Debe mostrar: .../Reservas
ls *.pdf *.tex *.py          # Debe listar los archivos principales
```

---

## 🔍 Debugging

### Ver errores LaTeX completos
Edita `app.py` línea ~80 y cambia:

```python
# De esto:
for err in error_lines[:5]:  # Solo los primeros 5
    st.code(err)

# A esto:
for err in error_lines:      # Todos los errores
    st.code(err)
```

### Guardar archivo LaTeX generado
Para inspeccionar qué se generó:

```python
# Agregar después de generar_latex_con_datos():
with open('debug_generated.tex', 'w', encoding='utf-8') as f:
    f.write(latex_code)
```

Luego ver el archivo `debug_generated.tex`

---

## 📞 No encuentras la solución?

1. Verifica el archivo `debug_generated.tex` (si lo creaste)
2. Intenta compilar directamente con LaTeX:
```bash
pdflatex -interaction=nonstopmode memorandum.tex
```
3. Revisa los logs de compilación
4. Contacta a: officialia.partes@usalud.edu.mx

---

**Última actualización**: v2.0 (2026-04-09)

