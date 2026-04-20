# 🖨️ ITERACIÓN 3 - Generador de Documentos Word

**Fecha:** 20 Abril 2026  
**Estado:** ⏳ Pendiente  
**Iteración anterior:** 2 ✅ COMPLETADA  
**Iteración actual:** 3 ⏳ PENDIENTE  
**Iteración siguiente:** 4 ⏳ PENDIENTE

## 🎯 OBJETIVOS ITERACIÓN 3

### **Basado en plan original:**
1. **📄 Generar documento Word automático** con datos guardados
2. **🖨️ Botón "GENERAR DOCUMENTO"** en interfaz principal
3. **🔧 Integrar `docxtpl`** para plantillas dinámicas
4. **📁 Sistema de guardado** de documentos generados

### **Meta específica:**
- Crear plantilla básica de acta psicológica
- Botón que genere .docx con datos del registro seleccionado
- Guardar documentos en carpeta `documentos_generados/`
- Mostrar mensaje de confirmación con ruta al archivo

## 🛠️ TECNOLOGÍAS A UTILIZAR

### **Dependencias necesarias:**
- **`docxtpl`** - Ya instalado (usado en scripts anteriores)
- **`python-docx`** - Ya instalado (viene con docxtpl)
- **`Jinja2`** - Ya instalado (viene con docxtpl)

### **Verificar instalación:**
```bash
python -c "import docxtpl; print('✅ docxtpl instalado')"
```

## 📋 ESTRUCTURA DE PLANTILLA

### **Plantilla básica propuesta:**
```
ACTA DE ENTREVISTA PSICOLÓGICA

DATOS BÁSICOS:
Expediente: {{EXPEDIENTE}}
Fecha: {{FECHA}}
Juez: {{NOMBRE_JUEZ}}

DATOS DE PERSONA:
Iniciales: {{INICIALES_PERSONA}}
Tipo: {{TIPO_PERSONA}}
Edad: {{EDAD}}

DATOS LEGALES:
Tipo de delito: {{TIPO_DELITO}}
Lugar: {{LUGAR}}

DESARROLLO DE LA ENTREVISTA:
[Texto dinámico generado automáticamente]

FIRMAS Y FECHAS:
_________________________________
Psicólogo/a
_________________________________
Fecha: {{FECHA_GENERACION}}
```

### **Campos dinámicos a incluir:**
1. `{{EXPEDIENTE}}` - Número de expediente
2. `{{INICIALES_PERSONA}}` - Iniciales de la persona
3. `{{FECHA}}` - Fecha de la cita
4. `{{NOMBRE_JUEZ}}` - Nombre del juez
5. `{{TIPO_PERSONA}}` - Tipo (Agraviado/Denunciado/Testigo)
6. `{{EDAD}}` - Edad de la persona
7. `{{TIPO_DELITO}}` - Tipo de delito
8. `{{LUGAR}}` - Lugar de los hechos
9. `{{FECHA_GENERACION}}` - Fecha de generación del documento
10. `{{ID_REGISTRO}}` - ID en base de datos

## 🖥️ ACTUALIZACIÓN DE INTERFAZ

### **Mejoras a implementar:**
1. **🔍 Mover búsqueda arriba** - Acceso inmediato
2. **📄 Botón "GENERAR DOCUMENTO"** - En lista de datos
3. **📁 Selector de plantilla** - (Opcional para futuras iteraciones)
4. **📊 Vista previa rápida** - (Opcional para futuras iteraciones)

### **Nueva organización propuesta:**
```
VENTANA PRINCIPAL:
[🔍 BARRA DE BÚSQUEDA] ← ARRIBA, INMEDIATO

SECCIÓN 1: DATOS BÁSICOS
SECCIÓN 2: DATOS DE PERSONA  
SECCIÓN 3: DATOS LEGALES

[BOTÓN GUARDAR]
[BOTÓN VER DATOS]

VENTANA DE DATOS:
[LISTA DE REGISTROS]
[BOTÓN GENERAR DOCUMENTO] ← NUEVO
```

## 🗄️ ACTUALIZACIÓN BASE DE DATOS

### **Nueva tabla para documentos generados:**
```sql
CREATE TABLE IF NOT EXISTS documentos_generados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    registro_id INTEGER REFERENCES citas_piloto(id),
    nombre_archivo TEXT NOT NULL,
    ruta_archivo TEXT NOT NULL,
    plantilla_usada TEXT,
    fecha_generacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Ventajas:**
- Historial de documentos generados
- Relación con registros originales
- Posibilidad de re-generar o modificar
- Auditoría completa

## 🔧 PLAN DE TRABAJO

### **Paso 1: Reorganizar interfaz (10 min)**
- Mover barra de búsqueda arriba
- Ajustar layout para mejor flujo
- Verificar que todos los elementos sean visibles

### **Paso 2: Crear plantilla Word (10 min)**
- Diseñar plantilla básica .docx
- Definir campos dinámicos
- Guardar como `plantilla_acta_basica.docx`

### **Paso 3: Implementar generador (15 min)**
- Función `generar_documento(registro_id)`
- Integración con `docxtpl`
- Guardado en carpeta organizada
- Mensaje de confirmación

### **Paso 4: Agregar botón a interfaz (10 min)**
- Botón en ventana de datos
- Conexión con función generadora
- Manejo de errores y validaciones

### **Paso 5: Probar y ajustar (5 min)**
- Generar múltiples documentos
- Verificar formato y contenido
- Corregir problemas menores

## 💻 CÓDIGO A DESARROLLAR

### **Nuevas funciones en `app.py`:**
1. **`reorganizar_interfaz()`** - Mover búsqueda arriba
2. **`crear_plantilla_basica()`** - Generar plantilla .docx inicial
3. **`generar_documento_word(registro_id)`** - Función principal
4. **`mostrar_boton_generar()`** - En ventana de datos

### **Archivos nuevos:**
```
piloto_psicobot/
├── app.py                    # Actualizado con nuevas funciones
├── plantilla_acta_basica.docx # Plantilla para documentos
├── documentos_generados/     # Carpeta para output
│   └── Acta_2026-00123-PE_20260420_1420.docx
└── piloto.db                # Con nueva tabla documentos_generados
```

## 🧪 PRUEBAS A REALIZAR

### **Prueba 1: Reorganización de interfaz**
- [ ] Barra de búsqueda visible inmediatamente
- [ ] Todas las secciones siguen accesibles
- [ ] Flujo visual lógico e intuitivo

### **Prueba 2: Generación de documentos**
- [ ] Botón "GENERAR DOCUMENTO" funciona
- [ ] Crea archivo .docx en carpeta correcta
- [ ] Todos los campos se rellenan correctamente
- [ ] Formato del documento es profesional

### **Prueba 3: Manejo de errores**
- [ ] Sin registro seleccionado → Mensaje apropiado
- [ ] Error en plantilla → Mensaje claro
- [ ] Permisos de escritura → Manejo adecuado

### **Prueba 4: Integración completa**
- [ ] Documento generado se abre en Word
- [ ] Contenido coincide con datos en base de datos
- [ ] Historial se guarda en tabla documentos_generados

## 📈 CRITERIOS DE ÉXITO

### **Éxito mínimo:**
- ✅ Botón "GENERAR DOCUMENTO" visible y funcional
- ✅ Documento .docx generado con datos básicos
- ✅ Archivo guardado en carpeta organizada
- ✅ Mensaje de confirmación al usuario

### **Éxito completo:**
- ✅ Plantilla profesional y bien formateada
- ✅ Todos los 10 campos dinámicos funcionando
- ✅ Historial en base de datos
- ✅ Posibilidad de seleccionar diferentes plantillas
- ✅ Vista previa antes de generar

## 👥 RESPONSABILIDADES

### **XeatBOSS:**
- Diseñar contenido de plantilla (texto, formato)
- Probar documentos generados con Word real
- Validar que la información sea útil para su trabajo
- Sugerir mejoras en formato y contenido

### **ClawXeatJr:**
- Implementar integración con `docxtpl`
- Guiar reorganización de interfaz
- Manejar errores y casos límite
- Asegurar compatibilidad con Windows/Word

## 🔄 CONSIDERACIONES TÉCNICAS

### **Formato de documentos:**
- Compatible con Word 2007+ (.docx)
- Mantener formato profesional
- Incluir encabezados y pies de página (opcional)
- Usar estilos de Word para consistencia

### **Organización de archivos:**
```
documentos_generados/
├── 2026-04-20/
│   ├── Acta_EXP-001_142035.docx
│   └── Acta_EXP-002_142150.docx
├── 2026-04-21/
└── plantillas/
    ├── acta_basica.docx
    └── acta_completa.docx
```

### **Nombres de archivos:**
```
Acta_[EXPEDIENTE]_[FECHA]_[HORA].docx
Ejemplo: Acta_2026-00123-PE_20260420_142035.docx
```

## 🚨 RIESGOS IDENTIFICADOS

### **Riesgo 1: Incompatibilidad con Word**
**Mitigación:** Usar formato .docx estándar, probar en Word real

### **Riesgo 2: Plantilla muy compleja**
**Mitigación:** Comenzar con plantilla simple, iterar mejoras

### **Riesgo 3: Permisos de escritura**
**Mitigación:** Manejar excepciones, sugerir rutas alternativas

### **Riesgo 4: Tiempo insuficiente**
**Mitigación:** Priorizar funcionalidad básica, dejar mejoras para iteración 4

## 📊 MÉTRICAS DE PROGRESO

### **Al inicio de iteración:**
- Funcionalidades: Guardar, Ver, Buscar
- Campos: 8
- Documentos generados: 0
- Tiempo estimado: 45-60 minutos

### **Al final de iteración (objetivo):**
- Funcionalidades: + Generar documento
- Campos: 8 (mismos, pero exportados a Word)
- Documentos generados: N (según pruebas)
- Valor agregado: Automatización de proceso manual

## 🔗 ENLACES RELACIONADOS

### **Documentación anterior:**
- [[002_ITERACION]] - Iteración 2 completada
- [[resumen_final_dia_2026-04-20]] - Resumen del día anterior
- [[piloto_iteracion1_obsidian]] - Plan original

### **Recursos técnicos:**
- [docxtpl documentation](https://docxtpl.readthedocs.io/)
- [Jinja2 template syntax](https://jinja.palletsprojects.com/)
- [Python-docx documentation](https://python-docx.readthedocs.io/)

## 🎮 PLAN DE EJECUCIÓN

### **Minuto 0-10:** Reorganizar interfaz (mover búsqueda arriba)
### **Minuto 10-20:** Crear plantilla básica .docx
### **Minuto 20-35:** Implementar función generadora
### **Minuto 35-45:** Agregar botón y conectar
### **Minuto 45-60:** Probar, ajustar, documentar

