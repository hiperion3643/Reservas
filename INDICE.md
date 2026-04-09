# 📚 Índice de Documentación

## 🎯 ¿Qué documento debo leer?

### 👤 Soy usuario final (quiero generar memorandums)

**Nivel Principiante**:
1. [INICIO_RAPIDO.md](INICIO_RAPIDO.md) ← **Comienza aquí** ⭐
   - Instalación en 5 minutos
   - Tu primer memorandum en 2 minutos
   - Verificación de funcionamiento

2. [IMPRESION.md](IMPRESION.md)
   - Cómo imprimir correctamente
   - Tamaño carta (Letter)
   - Solución de problemas de impresión

**Nivel Intermedio**:
3. [README.md](README.md)
   - Características completas
   - Uso detallado
   - Personalización básica

4. [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
   - Errores comunes
   - Soluciones paso a paso
   - Debugging

---

### 👨‍💼 Soy administrador / Soporte IT

**Instalación y Configuración**:
1. [INICIO_RAPIDO.md](INICIO_RAPIDO.md) - Instalación básica
2. [README.md](README.md) - Requisitos completos
3. [ESPECIFICACIONES.md](ESPECIFICACIONES.md) - Detalles técnicos

**Problemas y Mantenimiento**:
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Arreglar errores
- [CAMBIOS_v2.0.md](CAMBIOS_v2.0.md) - Historial de cambios

**Configuración Avanzada**:
- [ESPECIFICACIONES.md](ESPECIFICACIONES.md) - LaTeX, Python, Jinja2

---

### 👨‍💻 Soy desarrollador / Quiero modificar el código

**Entender la arquitectura**:
1. [CAMBIOS_v2.0.md](CAMBIOS_v2.0.md) - Cómo se estructura
2. [ESPECIFICACIONES.md](ESPECIFICACIONES.md) - Detalles técnicos
3. [README.md](README.md) - Funcionalidades

**Código fuente**:
- `app.py` - Aplicación Streamlit
- `memo_reservas.tex` - Template LaTeX
- `requirements.txt` - Dependencias

**Para personalizar**:
- Ver sección "🔧 Personalización" en [README.md](README.md)

---

## 📖 Resumen de Documentos

| Documento | Audiencia | Tiempo de lectura | Propósito |
|-----------|-----------|-------------------|----------|
| [INICIO_RAPIDO.md](INICIO_RAPIDO.md) | Todos | 5 min | Empezar rápido |
| [README.md](README.md) | Usuarios/Admin | 10 min | Visión general |
| [IMPRESION.md](IMPRESION.md) | Usuarios | 10 min | Imprimir correctamente |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Admin/Soporte | 15 min | Resolver problemas |
| [CAMBIOS_v2.0.md](CAMBIOS_v2.0.md) | Dev/Admin | 10 min | Qué cambió |
| [ESPECIFICACIONES.md](ESPECIFICACIONES.md) | Dev/Admin | 20 min | Detalles técnicos |
| [INDICE.md](INDICE.md) | Todos | 2 min | Este archivo |

---

## 🚀 Flujos de Uso por Rol

### Flujo 1: Primer Usuario (Primera vez)

```
1. Lee: INICIO_RAPIDO.md (5 min)
   ↓
2. Instala: pip install -r requirements.txt
   ↓
3. Ejecuta: streamlit run app.py
   ↓
4. Genera: Tu primer memorandum
   ↓
5. Lee: IMPRESION.md (imprime correctamente)
   ↓
6. ✅ Listo!
```

### Flujo 2: Usuario con Problemas

```
1. Busca el error en: TROUBLESHOOTING.md
   ↓
2. Sigue los pasos de solución
   ↓
3. Si sigue fallando:
   - Lee ESPECIFICACIONES.md (detalles técnicos)
   - Contacta: officialia.partes@usalud.edu.mx
```

### Flujo 3: Administrador Nuevo

```
1. Lee: README.md (visión general)
   ↓
2. Sigue: Instrucciones en INICIO_RAPIDO.md
   ↓
3. Estudia: ESPECIFICACIONES.md (para soporte)
   ↓
4. Guarda: TROUBLESHOOTING.md (para referencia)
   ↓
5. ✅ Listo para soportar usuarios
```

### Flujo 4: Desarrollador que Modifica

```
1. Lee: CAMBIOS_v2.0.md (qué hay)
   ↓
2. Estudia: ESPECIFICACIONES.md (cómo funciona)
   ↓
3. Examina: Código fuente
   ↓
4. Modifica según necesidad
   ↓
5. Tests: Sigue pasos en INICIO_RAPIDO.md
   ↓
6. Documenta: Actualiza CAMBIOS_v2.0.md
```

---

## 🔍 Buscar por Tema

### "No funciona LaTeX"
→ [TROUBLESHOOTING.md](TROUBLESHOOTING.md) Sección 1

### "La tabla se corta al imprimir"
→ [IMPRESION.md](IMPRESION.md) Sección "El documento se corta"

### "¿Cómo cambio los márgenes?"
→ [README.md](README.md) Sección "Personalización"
→ [ESPECIFICACIONES.md](ESPECIFICACIONES.md) Sección "Geometría"

### "¿Cuál es el tamaño máximo de destinos?"
→ [ESPECIFICACIONES.md](ESPECIFICACIONES.md) Sección "Límites"

### "Quiero saber qué cambió en v2.0"
→ [CAMBIOS_v2.0.md](CAMBIOS_v2.0.md) completo

### "¿Cómo imprimo correctamente?"
→ [IMPRESION.md](IMPRESION.md) completo

### "Necesito instalar todo de cero"
→ [INICIO_RAPIDO.md](INICIO_RAPIDO.md) Sección 1

### "¿Qué es pandas? ¿Por qué se usa?"
→ [CAMBIOS_v2.0.md](CAMBIOS_v2.0.md) Sección 3
→ [ESPECIFICACIONES.md](ESPECIFICACIONES.md) Sección "Flujo de datos"

---

## 📋 Checklist de Archivos

Verifica que tengas estos archivos en tu carpeta:

```
Reservas/
├── 📖 README.md                    ✅ Visión general
├── 📖 INICIO_RAPIDO.md             ✅ Primeros pasos
├── 📖 IMPRESION.md                 ✅ Guía de impresión
├── 📖 TROUBLESHOOTING.md           ✅ Solución de problemas
├── 📖 CAMBIOS_v2.0.md              ✅ Qué es nuevo
├── 📖 ESPECIFICACIONES.md          ✅ Detalles técnicos
├── 📖 INDICE.md                    ✅ Este archivo
├── 💻 app.py                       ✅ Código principal
├── 📄 memo_reservas.tex            ✅ Template LaTeX
├── 🎨 Hoja_Membretada.pdf          ✅ Membrete (solicitar si falta)
├── 📝 requirements.txt              ✅ Dependencias
├── 📊 __pycache__/                 ⚫ Auto-generada
└── 📁 Otros archivos auxiliares    ⬜ Generados al compilar
```

---

## 🆘 Necesito ayuda urgente

### Opción 1: Buscar en la documentación
```
1. Abre TROUBLESHOOTING.md
2. Busca tu error o problema
3. Sigue los pasos indicados
```

### Opción 2: Revisar especificaciones
```
1. Si entiendes de Python/LaTeX
2. Lee ESPECIFICACIONES.md sección relevante
3. Identifica la causa
```

### Opción 3: Contactar soporte
```
📧 Email: officialia.partes@usalud.edu.mx
📎 Adjunta:
   - Captura de pantalla del error
   - Los pasos que seguiste
   - Sistema operativo
   - Versión de Python (python --version)
```

---

## 🎓 Recursos Externos

### Para Entender LaTeX
- [LaTeX Project](https://www.latex-project.org/)
- [Overleaf Tutorials](https://www.overleaf.com/learn)

### Para Entender Streamlit
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)

### Para Entender Pandas
- [Pandas Documentation](https://pandas.pydata.org/)
- [Pandas Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)

### Para Instalar LaTeX
- **Windows**: [MiKTeX](https://miktex.org/)
- **Mac**: [MacTeX](https://www.tug.org/mactex/)
- **Linux**: TeX Live (apt, yum, pacman)

---

## 📅 Historial de Versiones

| Versión | Fecha | Cambios Principales |
|---------|-------|---------------------|
| 1.0 | 2026-03-XX | Versión inicial |
| 2.0 | 2026-04-09 | **Tamaño Letter, Pandas, Tabla mejorada** |
| 2.1 | Próxima | Mejoras planeadas |

---

## 🎯 Próximos Pasos Recomendados

### Si es tu primera vez
1. ✅ Lee [INICIO_RAPIDO.md](INICIO_RAPIDO.md)
2. ✅ Instala según instrucciones
3. ✅ Genera un memorandum de prueba
4. ✅ Lee [IMPRESION.md](IMPRESION.md) antes de imprimir

### Si tienes experiencia
1. ✅ Lee [CAMBIOS_v2.0.md](CAMBIOS_v2.0.md) - Qué cambió
2. ✅ Review [ESPECIFICACIONES.md](ESPECIFICACIONES.md) - Cómo funciona
3. ✅ Customiza según necesidad
4. ✅ Documenta tus cambios

### Para administrador/soporte
1. ✅ Completa todos los pasos anteriores
2. ✅ Memoriza [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
3. ✅ Crea un documento interno de soluciones
4. ✅ Entrena a usuarios en [IMPRESION.md](IMPRESION.md)

---

**Versión de Documentación**: 2.0
**Actualizado**: 2026-04-09
**Sitio de soporte**: officialia.partes@usalud.edu.mx

