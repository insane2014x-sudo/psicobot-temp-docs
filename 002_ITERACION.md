# 🔄 ITERACIÓN 2 - Sistema Psicobot

**Fecha:** 20 Abril 2026  
**Estado:** 🟡 En progreso  
**Iteración anterior:** 1 ✅ COMPLETADA  
**Iteración actual:** 2 🟡 EN PROGRESO  
**Iteración siguiente:** 3 ⏳ PENDIENTE

## 🎯 OBJETIVOS ITERACIÓN 2

### **Basado en plan original:**
1. **📝 Agregar más campos** al formulario (de 4 a 8-10 campos)
2. **📋 Listar datos guardados** con mejor visualización
3. **🔍 Buscar/editar registros** funcionalidad básica

### **Meta específica para hoy (30 minutos):**
- Agregar 2-3 campos más al formulario
- Mejorar la visualización de datos
- Implementar búsqueda simple por expediente

## 📋 CAMPOS ACTUALES (Iteración 1)

### **4 campos existentes:**
1. 📄 **Expediente** (texto)
2. 👤 **Iniciales persona** (texto)
3. 📅 **Fecha** (DD/MM/AAAA)
4. ⚖️ **Nombre de juez** (texto)

## 🆕 CAMPOS A AGREGAR (Iteración 2)

### **Propuesta de nuevos campos:**
5. **👥 Tipo de persona** (dropdown: Agraviado/Denunciado/Testigo)
6. **🔢 Edad** (número)
7. **⚖️ Tipo de delito** (texto)
8. **📍 Lugar** (texto)

### **Justificación:**
- **Tipo de persona** → Clasificación esencial para documentos
- **Edad** → Datos demográficos básicos
- **Tipo de delito** → Información legal relevante
- **Lugar** → Contexto geográfico

## 🗄️ ACTUALIZACIÓN BASE DE DATOS

### **Nueva estructura de tabla:**
```sql
CREATE TABLE citas_piloto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expediente TEXT NOT NULL,
    iniciales_persona TEXT NOT NULL,
    fecha TEXT NOT NULL,
    nombre_juez TEXT NOT NULL,
    tipo_persona TEXT,           -- NUEVO
    edad INTEGER,                -- NUEVO
    tipo_delito TEXT,            -- NUEVO
    lugar TEXT,                  -- NUEVO
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🖥️ ACTUALIZACIÓN INTERFAZ

### **Nuevos elementos a agregar:**
1. **Dropdown** para "Tipo de persona"
2. **Campo numérico** para "Edad"
3. **Campo texto** para "Tipo de delito"
4. **Campo texto** para "Lugar"
5. **Barra de búsqueda** por expediente
6. **Botón "BUSCAR"**
7. **Botón "EDITAR"** en lista de datos

## 🔧 PLAN DE TRABAJO (30 MINUTOS)

### **Paso 1: Actualizar base de datos (5 min)**
- Modificar tabla existente o crear nueva versión
- Mantener compatibilidad con datos existentes

### **Paso 2: Agregar campos a interfaz (10 min)**
- Añadir 4 nuevos campos al formulario
- Implementar dropdown para tipo de persona

### **Paso 3: Implementar búsqueda (10 min)**
- Campo de búsqueda por expediente
- Función que filtra la lista de datos
- Resultados en tiempo real

### **Paso 4: Probar y ajustar (5 min)**
- Verificar que todo funciona
- Corregir errores menores
- Documentar cambios

## 💻 CÓDIGO A MODIFICAR

### **Archivos afectados:**
1. **`app.py`** - Interfaz principal
   - Función `crear_interfaz()` → Agregar nuevos campos
   - Función `guardar_datos()` → Manejar nuevos campos
   - Nueva función `buscar_expediente()`

2. **Base de datos** - `piloto.db`
   - Actualizar estructura de tabla
   - Migrar datos existentes (si es necesario)

## 🧪 PRUEBAS A REALIZAR

### **Prueba 1: Campos nuevos funcionan**
- [ ] Los 4 nuevos campos son visibles
- [ ] Dropdown muestra opciones correctas
- [ ] Validación de edad (solo números)

### **Prueba 2: Guardado con nuevos campos**
- [ ] Datos completos se guardan en SQLite
- [ ] Campos vacíos se manejan correctamente
- [ ] Visualización muestra nuevos campos

### **Prueba 3: Búsqueda funciona**
- [ ] Campo de búsqueda es funcional
- [ ] Filtra correctamente por expediente
- [ ] Muestra mensaje si no encuentra

### **Prueba 4: Compatibilidad hacia atrás**
- [ ] Datos antiguos siguen funcionando
- [ ] Aplicación no se rompe con datos viejos
- [ ] Migración suave (si es necesaria)

## 📈 CRITERIOS DE ÉXITO

### **Éxito mínimo (lograr hoy):**
- ✅ 2 nuevos campos agregados y funcionando
- ✅ Búsqueda por expediente implementada
- ✅ Aplicación sigue funcionando sin errores

### **Éxito completo (si hay tiempo):**
- ✅ Todos los 4 nuevos campos funcionando
- ✅ Dropdown con opciones predefinidas
- ✅ Validación mejorada de datos
- ✅ Interfaz mejor organizada

## 👥 RESPONSABILIDADES

### **XeatBOSS:**
- Probar cada nuevo campo
- Sugerir mejoras en interfaz
- Validar que los datos sean útiles para su trabajo
- Documentar problemas encontrados

### **ClawXeatJr:**
- Guiar implementación paso a paso
- Explicar modificaciones en base de datos
- Ayudar con validaciones y manejo de errores
- Asegurar compatibilidad con versión anterior

## 🔄 CONSIDERACIONES TÉCNICAS

### **Manejo de migración de datos:**
**Opción A:** Crear nueva tabla y copiar datos
**Opción B:** Modificar tabla existente con ALTER TABLE
**Opción C:** Mantener dos versiones durante transición

**Recomendación:** Opción B (ALTER TABLE) es más simple para pocos datos.

### **Validación de nuevos campos:**
- **Edad:** Solo números, rango 0-120
- **Tipo de persona:** Solo opciones permitidas
- **Lugar:** Texto con longitud máxima
- **Tipo de delito:** Texto libre pero con límite

## 📝 NOTAS DE DISEÑO

### **Organización de interfaz:**
```
SECCIÓN 1: Datos básicos
- Expediente, Iniciales, Fecha, Juez

SECCIÓN 2: Datos de persona  
- Tipo de persona (dropdown), Edad

SECCIÓN 3: Datos legales
- Tipo de delito, Lugar
```

### **Mejoras visuales:**
- Separadores entre secciones
- Colores diferentes por sección
- Tooltips explicativos para campos nuevos
- Iconos representativos para cada campo

## 🚨 RIESGOS IDENTIFICADOS

### **Riesgo 1: Ruptura de datos existentes**
**Mitigación:** Hacer backup de `piloto.db` antes de cambios

### **Riesgo 2: Interfaz muy cargada**
**Mitigación:** Agrupar campos lógicamente, usar pestañas si es necesario

### **Riesgo 3: Tiempo insuficiente**
**Mitigación:** Priorizar 2 campos esenciales primero

## 📊 MÉTRICAS DE PROGRESO

### **Al inicio de iteración:**
- Campos: 4
- Funcionalidades: Guardar, Ver datos
- Líneas código: ~835
- Tiempo estimado: 30 minutos

### **Al final de iteración (objetivo):**
- Campos: 6-8
- Funcionalidades: + Búsqueda
- Líneas código: ~950
- Valor agregado: +40%

## 🔗 ENLACES RELACIONADOS

### **Documentación anterior:**
- [[001_ITERACION]] - Iteración 1 completada
- [[resumen_piloto_exitoso]] - Resumen del día
- [[piloto_iteracion1_obsidian]] - Plan original iteración 1

### **Recursos técnicos:**
- [SQLite ALTER TABLE](https://www.sqlite.org/lang_altertable.html)
- [Tkinter Dropdown (Combobox)](https://docs.python.org/3/library/tkinter.ttk.html#combobox)
- [Python input validation](https://docs.python.org/3/library/re.html)

## 🎮 PLAN DE EJECUCIÓN

### **Minuto 0-5:** Actualizar base de datos
### **Minuto 5-15:** Agregar campos a interfaz
### **Minuto 15-25:** Implementar búsqueda
### **Minuto 25-30:** Probar y documentar

## 💡 SUGERENCIAS PARA PRÓXIMAS ITERACIONES

### **Iteración 3 (Generador documentos):**
- Usar plantilla Word real
- Integrar docxtpl para campos dinámicos
- Botón "Generar Acta" en lista de datos

### **Iteración 4 (Importar/Exportar):**
- Leer desde Excel existente
- Exportar datos a Excel
- Reporte estadístico simple

---
**Documentación creada:** 20 Abril 2026, 03:20 UTC  
**Tiempo asignado:** 30 minutos  
**Estado:** 🟡 EN EJECUCIÓN  
**Siguiente actualización:** Al completar iteración

**🚀 ¡COMENZAMOS IMPLEMENTACIÓN!**