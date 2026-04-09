# 🚀 Inicio Rápido - Primeros Pasos

## ⚡ Instalación Rápida (5 minutos)

### 1️⃣ Requisitos Previos

Verifica que tengas:
```bash
python --version        # Python 3.8+
pdflatex --version      # LaTeX instalado
```

Si falta LaTeX:
- **Windows**: [Descargar MiKTeX](https://miktex.org/)
- **Linux**: `sudo apt-get install texlive-full`
- **Mac**: `brew install basictex`

### 2️⃣ Instalar Dependencias

```bash
# En tu carpeta del proyecto
cd ~/Proyectos/Reservas

# Instalar paquetes Python
pip install -r requirements.txt
```

**Debería instalar**:
- streamlit
- pandas
- jinja2
- reportlab

### 3️⃣ Verificar Archivos

Asegúrate de tener **en la carpeta raíz**:
```bash
ls -la

Memorandum_App/
├── app.py                    ✅ Aplicación
├── memo_reservas.tex         ✅ Template LaTeX
├── Hoja_Membretada.pdf       ✅ Membrete (IMPORTANTE!)
├── requirements.txt          ✅ Dependencias
└── README.md
```

Si falta `Hoja_Membretada.pdf`, solicítalo a:
📧 officialia.partes@usalud.edu.mx

### 4️⃣ Iniciar la App

```bash
streamlit run app.py
```

Se abrirá en navegador:
```
http://localhost:8501
```

---

## 📝 Primer Memorandum (2 minutos)

### Paso 1: Información Solicitante

```
Nombre completo: Maria García López
Puesto: Subdirectora de Admisión
Departamento: Recursos Administrativos
Asunto: Solicitud de vehículo institucional
```

### Paso 2: Fechas y Horarios

```
Fecha de salida: 2026-04-15
Fecha de regreso: 2026-04-15
Hora de inicio: 08:00
Hora de regreso: 17:00
```

### Paso 3: Agregar Destinos

Haz clic en **➕ Agregar destino** (mínimo 1 requerido)

**Ejemplo de destino**:
```
Lugar: Dependencia Jurisdiccional de Xalapa
Ubicación: Avenida Juárez #145, Xalapa, Ver.
Motivo: Visita de supervisión administrativa
```

Puedes agregar más destinos con el botón **➕**

### Paso 4: Personal

```
Total de personas: 3
```

Incluye al solicitante + acompañantes

### Paso 5: Generar

Haz clic en **📄 Generar Memorandum** (botón grande azul)

Espera a que aparezca: ✅ Memorandum generado exitosamente

### Paso 6: Descargar

Haz clic en el botón **📥 Descargar Memorandum PDF**

---

## ✅ Verificación de Funcionamiento

Después de génerar el PDF:

1. **Abre el PDF descargado**
   - [ ] Membrete visible
   - [ ] Datos correctos
   - [ ] Tabla con destinos

2. **Imprime con configuración correcta**
   - [ ] Tamaño: Carta (Letter)
   - [ ] Escala: 100%
   - [ ] "Imprimir fondos": Sí
   - Ver [IMPRESION.md](IMPRESION.md) para más detalles

3. **Entrégalo en Secretaría Administrativa**

---

## 📚 Documentación Completa

| Documento | Contenido |
|-----------|----------|
| [README.md](README.md) | Información general y características |
| [CAMBIOS_v2.0.md](CAMBIOS_v2.0.md) | Qué se mejoró en esta versión |
| [IMPRESION.md](IMPRESION.md) | Guía detallada de impresión |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Solución de problemas |

---

## 🎯 Casos de Uso Comunes

### Caso 1: Viaje de un día
```
Fecha de salida: 2026-04-15
Fecha de regreso: 2026-04-15  ← Misma fecha
Destinos: 2-3 lugares
Personas: Solo el solicitante
```

### Caso 2: Viaje de varios días
```
Fecha de salida: 2026-04-15
Fecha de regreso: 2026-04-18  ← Diferente
Destinos: Múltiples
Personas: 1 solicitante + acompañantes
```

### Caso 3: Comisión oficial
```
Destinos: 5-6 lugares
Motivo: "Comisión oficial"
Personas: Equipo completo (5-10)
Horario: Jornada laboral (08:00 - 17:00)
```

---

## 🔄 Flujo General

```
┌─────────────────────────┐
│ 1. Llenar formulario    │ ← Aquí estás
└──────────┬──────────────┘
           │
┌──────────▼──────────────┐
│ 2. Verificar datos      │
└──────────┬──────────────┘
           │
┌──────────▼──────────────┐
│ 3. Generar PDF          │ ← Click botón azul
└──────────┬──────────────┘
           │
┌──────────▼──────────────┐
│ 4. Descargar PDF        │ ← Click descarga
└──────────┬──────────────┘
           │
┌──────────▼──────────────┐
│ 5. Imprimir (Carta)     │ ← Ver IMPRESION.md
└──────────┬──────────────┘
           │
┌──────────▼──────────────┐
│ 6. Entregar ✅          │
└─────────────────────────┘
```

---

## ⚠️ Límites y Recomendaciones

| Aspecto | Mínimo | Máximo | Óptimo |
|---------|--------|--------|--------|
| Destinos | 1 | 8 | 3-5 |
| Personas | 1 | 20 | 2-10 |
| Carácteres por ubicación | - | 50 | 20 |
| Caracteres por motivo | - | 100 | 40 |

**Razón**: Ajuste a tamaño carta (8.5" × 11")

---

## 🆘 Si algo falla

1. **LaTeX no funciona**
   - Ver [TROUBLESHOOTING.md](TROUBLESHOOTING.md) → Sección 1

2. **Falta Hoja_Membretada.pdf**
   - Ver [TROUBLESHOOTING.md](TROUBLESHOOTING.md) → Sección 2

3. **PDF se corta al imprimir**
   - Ver [IMPRESION.md](IMPRESION.md) → "El documento se corta"

4. **Otros problemas**
   - Ver [TROUBLESHOOTING.md](TROUBLESHOOTING.md) completo

---

## 💡 Tips Útiles

### Guardar como Plantilla
Si usas datos recurrentes:
1. Anota los valores en un documento
2. Reutiliza para solicitudes similares

### Múltiples Memorandums
Genera varios en la misma sesión:
1. Completa formulario
2. Genera PDF
3. **Sin recargar**, cambia datos
4. Genera otro PDF

### Editar el Membrete
Si necesitas cambiar `Hoja_Membretada.pdf`:
1. Crea nueva versión en tu herramienta de PDF
2. Reemplaza el archivo
3. Vuelve a generar

---

## 🎓 Próximos Pasos

Después de tu primer memorandum:

1. ✅ Familiarízate con el formulario
2. ✅ Prueba con 2-3 destinos
3. ✅ Prueba la impresión (ver [IMPRESION.md](IMPRESION.md))
4. ✅ Pregunta dudas a: officialia.partes@usalud.edu.mx

---

## 📞 Contacto y Soporte

**Para problemas técnicos**:
- 📧 officialia.partes@usalud.edu.mx
- 📎 Adjunta captura de pantalla del error

**Para cambios en el membrete**:
- 📧 officialia.partes@usalud.edu.mx
- Proporciona la nueva hoja membretada en PDF

**Para mejoras o solicitudes**:
- 📧 officialia.partes@usalud.edu.mx

---

**Bienvenido al Sistema de Memorandums v2.0** 🎉

¡Listo para generar tu primer documento!

