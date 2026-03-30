# Generador de Memorandums para Solicitud de Vehículos

Esta aplicación permite generar memorandums para solicitar vehículos institucionales en formato PDF.

## Requisitos

- Python 3.8 o superior
- Las siguientes dependencias de Python:
  - streamlit
  - reportlab

## Instalación

1. Clone o descargue este repositorio
2. Instale las dependencias necesarias:

```bash
pip install streamlit reportlab
```

## Cómo ejecutar la aplicación

Para ejecutar la aplicación, utilice el siguiente comando:

```bash
streamlit run app.py
```

**Importante:** No ejecute la aplicación directamente con `python app.py`, ya que esto generará advertencias y no funcionará correctamente.

## Uso

1. Complete todos los campos del formulario
2. Agregue tantos destinos como necesite usando el botón "+"
3. Especifique la ubicación exacta de cada destino
4. Haga clic en "Generar Memorandum"
5. Descargue el PDF generado
6. Presente el documento en la secretaría administrativa

## Notas importantes

- Los campos con * son obligatorios
- Puede agregar múltiples destinos con sus ubicaciones específicas
- El folio se genera automáticamente con fecha y hora
- El memorandum se genera en formato PDF listo para imprimir

## Contacto

Para dudas o soporte:
- 📧 oficialia.partes@usalud.edu.mx
- 📞 22 26 90 06 13
