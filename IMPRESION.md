# 🖨️ Guía de Impresión

## Impresión Correcta del Memorandum

### ✨ Configuración Óptima

#### Tamaño de Página
- **Tipo**: Letter (Carta) - 8.5" × 11"
- **Orientación**: Vertical (Portrait)
- **Márgenes**: 2.5cm (laterales), 3.8cm (superior), 2.5cm (inferior)

#### En Adobe Reader / Navegador

1. **Abre el PDF descargado**

2. **Menú → Imprimir** (Ctrl+P o Cmd+P)

3. **Configuración Importante**:
   ```
   ✅ Tamaño de página: Carta (Letter)
   ✅ Orientación: Vertical
   ✅ Escala: 100% (SIN ajustar a página)
   ✅ Márgenes: Ninguno (0mm)
   ❌ NO marques "Ajustar a página"
   ❌ NO marques "Reducir a ancho de página"
   ```

4. **Opciones Avanzadas** (según lector):
   ```
   ✅ Imprimir anotaciones: No
   ✅ Imprimir fondos: Sí
   ❌ Anti-alias: No necesario
   ```

5. **Haz clic en Imprimir**

---

## 🖥️ Por Sistema Operativo

### Windows 10/11

**Con Microsoft Edge**:
1. Abre el PDF
2. Ctrl + P
3. Impresora: Selecciona tu impresora
4. Más opciones/opciones avanzadas:
   - Orientación: Vertical
   - Tamaño: Carta
   - Escala: 100%
5. Imprimir

**Con Adobe Reader**:
1. Archivo → Imprimir (Ctrl+P)
2. Configurar impresora
3. En Ajustes de página:
   - Tamaño de página: Carta
   - Escalado: Ninguno
4. Imprimir

### macOS

**Con Preview**:
1. Abre el PDF
2. ⌘ + P (Imprimir)
3. En el diálogo:
   - Tamaño de papel: Carta
   - Escala: 100%
4. Imprimir

**Con Adobe Reader**:
1. Archivo → Imprimir
2. Configurar igual que Windows

### Linux

**Con Okular/Evince**:
```bash
# Desde terminal
lpr -o media=Letter -o orientation-requested=3 Memorandum_*.pdf

# O abre el PDF gráficamente
okular Memorandum_*.pdf
# Botón Imprimir → Configurar como Windows
```

**Desde Firefox/Chrome**:
1. Ctrl + P
2. Más configuración:
   - Tamaño: Carta
   - Escala: 100%
3. Imprimir

---

## 🔧 Solución de Problemas de Impresión

### ❌ El documento se corta

**Síntoma**: Parte del documento no aparece al imprimir

**Soluciones**:
1. ✅ Verifica que escala esté al **100%** (NO ajustar a página)
2. ✅ Papel sea tamaño **Carta**
3. ✅ Márgenes de impresora al **mínimo** (0-3mm)
4. ✅ Desactiva "Ajustar a página ancha"

### ❌ La tabla está incompleta

**Síntoma**: Columnas de la tabla cortadas

**Causa**: Impresora con márgenes mayores a 2.5cm

**Solución**:
1. Accede a las propiedades de impresora
2. Establece márgenes mínimos:
   ```
   Izquierdo: 0.5cm
   Derecho: 0.5cm
   Superior: 1cm
   Inferior: 1cm
   ```
3. Vuelve a intentar

### ❌ El membrete no se ve

**Síntoma**: El fondo de hoja membretada no aparece

**Causas potenciales**:
- Opción "Imprimir gráficos" o "Imprimir fondos" desactivada
- PDF corrupto

**Solución**:
1. En opciones de impresora, activa:
   - ✅ "Imprimir gráficos de fondo"
   - ✅ "Imprimir imágenes"
   - ✅ "Color"

2. Si no funciona:
   - Regenera el PDF
   - Comprueba que `Hoja_Membretada.pdf` sea válido

### ❌ Letra cortada o deformada

**Síntoma**: Caracteres españoles (ñ, á) salen raro

**Causa**: Incompatibilidad de fuentes

**Solución**:
1. Actualiza PDF reader (Adobe Reader, navegador)
2. Intenta imprimir a PDF:
   ```
   Archivo → Imprimir → Impresora: "Imprimir a PDF"
   ```
3. Luego imprime ese PDF generado

---

## 📋 Checklist Antes de Imprimir

- [ ] Documento abierto en programa correcto (PDF compatible)
- [ ] Papel: Tamaño **Carta** (8.5" × 11")
- [ ] Orientación: **Vertical** (Portrait)
- [ ] Escala: **100%** exacto (sin ajustar)
- [ ] Márgenes impresora: **mínimos** (0.5cm)
- [ ] "Imprimir fondos": ✅ Activado
- [ ] "Imprimir gráficos": ✅ Activado
- [ ] Color: ✅ Activado (si lo requiere)
- [ ] Vista previa: Verifica que vea completo

---

## 💾 Guardar Digitalizado

Si necesitas un PDF de buena calidad para email/archivo:

### Desde Windows/Mac/Linux
```bash
# Opción 1: Imprimir a PDF (mejor)
Archivo → Imprimir → Impresora: "Microsoft Print to PDF"

# Opción 2: Convertir con ImageMagick (requiere instalación)
convert -density 300x300 Memorandum_*.pdf Memorandum_300dpi.pdf
```

### Desde navegador
```javascript
// En la consola del navegador (F12)
// El PDF ya se descargó desde Streamlit
// Simplemente guárdalo como está
```

---

## 📸 Especificaciones Recomendadas

| Aspecto | Valor |
|--------|-------|
| Resolución | 96-150 DPI (pantalla) |
| Para archivo digital | 150-200 DPI |
| Para impresión | 300 DPI |
| Compresión | Sin comprimir (para preservar calidad) |
| Formato | PDF/A-1 (si requiere archivo) |

---

## 🎨 Personalización de Impresión

### Imprimir a Color vs Blanco y Negro

**Recomendación**: Color (mejor presentación institucional)

Si necesitas convertir a B&N:
```
Impresora → Opciones → Color: "Escala de grises"
```

### Imprimir Doble Cara
Si tienes memorandums largos:
```
Impresora → Cargas de papel: "Automático (doble cara)"
Orientación de encuadernación: Izquierda
```

### Imprimir Múltiples Copias

En lugar de imprimir manualmente varias veces:
```
Número de copias: [cantidad]
✅ Intercalar: Sí (para orden correcto)
```

---

## ✅ Verificación de Calidad

Después de imprimir, verifica:

1. **Contenido**:
   - [ ] Membrete visible y centrado
   - [ ] Todos los datos del solicitante legibles
   - [ ] Tabla completa con todas las filas
   - [ ] Firmas con líneas visibles

2. **Formato**:
   - [ ] Márgenes uniformes
   - [ ] Texto recto, no sesgado
   - [ ] Espaciado consistente

3. **Legibilidad**:
   - [ ] Caracteres españoles correctamente
   - [ ] Contraste suficiente
   - [ ] Números y fechas claros

---

## 🔗 Referencias

- **Tamaño Carta**: 8.5" × 11" = 215.9mm × 279.4mm
- **Estándar**: ANSI Letter (USA)
- **Alternativa**: A4 (210mm × 297mm) - NO USAR

---

**Última actualización**: v2.0 (2026-04-09)
**Soporte**: officialia.partes@usalud.edu.mx

