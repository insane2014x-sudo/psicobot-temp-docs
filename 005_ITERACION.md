# 🔄 ITERACIÓN 5 - Mejoras Avanzadas

**Fecha:** 20 Abril 2026  
**Estado:** 🟡 En progreso  
**Iteración anterior:** 4 ✅ COMPLETADA  
**Iteración actual:** 5 🟡 EN PROGRESO  
**Iteración siguiente:** 6 ⏳ PENDIENTE

## 🎯 OBJETIVOS ITERACIÓN 5

### **Basado en solicitud del usuario:**
1. **🔄 Edición/eliminación de registros** por expediente
2. **🔤 Autocompletado de nombre de juez** desde tabla separada
3. **🔍 Búsqueda avanzada** con múltiples criterios

### **Meta específica:**
- Sistema CRUD completo (Crear, Leer, Actualizar, Eliminar)
- Base de datos normalizada con tabla de jueces
- Interfaz de búsqueda con filtros combinados
- Mejora significativa en productividad del usuario

## 🗄️ ACTUALIZACIÓN BASE DE DATOS

### **Nueva tabla para jueces:**
```sql
CREATE TABLE IF NOT EXISTS jueces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_completo TEXT NOT NULL UNIQUE,
    especialidad TEXT,
    activo BOOLEAN DEFAULT 1,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Modificación tabla citas_piloto:**
```sql
-- Cambiar nombre_juez a juez_id (clave foránea)
ALTER TABLE citas_piloto ADD COLUMN juez_id INTEGER REFERENCES jueces(id);

-- Mantener nombre_juez como backup durante transición
-- O eliminar después de migración completa
```

### **Datos iniciales sugeridos:**
```sql
INSERT INTO jueces (nombre_completo, especialidad) VALUES
('JUAN PEREZ GARCIA', 'Penal'),
('MARIA LOPEZ MARTINEZ', 'Familia'),
('CARLOS GOMEZ RODRIGUEZ', 'Civil'),
('ANA DIAZ FERNANDEZ', 'Laboral'),
('LUIS RAMIREZ SANCHEZ', 'Penal');
```

## 🖥️ ACTUALIZACIÓN INTERFAZ

### **Nuevos elementos a agregar:**
1. **🔄 Botones "EDITAR" y "ELIMINAR"** en ventana de datos
2. **🔤 Campo de juez con autocompletado** (Combobox con búsqueda)
3. **🔍 Ventana de búsqueda avanzada** con múltiples filtros
4. **📋 Formulario de edición** (modal o ventana separada)

### **Organización propuesta:**
```
VENTANA DE DATOS (actualizada):
[LISTA DE REGISTROS]
[📄 GENERAR DOCUMENTO] [🔄 EDITAR] [🗑️ ELIMINAR] [CERRAR]

FORMULARIO PRINCIPAL (actualizado):
[Campo Juez:] → Combobox con autocompletado y botón "+" para agregar nuevo juez

BARRA DE BÚSQUEDA (actualizada):
[🔍 BÚSQUEDA AVANZADA] → Abre ventana con múltiples filtros
```

## 🔧 PLAN DE TRABAJO

### **Paso 1: Crear tabla de jueces y migrar datos (15 min)**
- Script para crear tabla `jueces`
- Migrar nombres únicos de `citas_piloto` a `jueces`
- Actualizar `citas_piloto` con `juez_id`

### **Paso 2: Implementar autocompletado de juez (15 min)**
- Cambiar Entry por Combobox con búsqueda
- Función para filtrar jueces mientras se escribe
- Botón para agregar nuevo juez si no existe

### **Paso 3: Agregar edición de registros (15 min)**
- Botón "EDITAR" en lista de datos
- Ventana modal con formulario pre-llenado
- Función para actualizar en base de datos

### **Paso 4: Agregar eliminación de registros (10 min)**
- Botón "ELIMINAR" con confirmación
- Eliminación suave (marcar como inactivo) o física
- Actualización de lista después de eliminar

### **Paso 5: Implementar búsqueda avanzada (15 min)**
- Ventana con múltiples campos de filtro
- Consulta SQL dinámica según filtros seleccionados
- Resultados en tabla similar a búsqueda simple

### **Paso 6: Probar y ajustar (5 min)**
- Probar flujo completo CRUD
- Verificar autocompletado y búsqueda avanzada
- Corregir errores menores

## 💻 CÓDIGO A DESARROLLAR

### **Nuevas funciones en `app.py`:**
1. **`crear_tabla_jueces()`** - Inicializa tabla de jueces
2. **`autocompletar_juez(event)`** - Filtra jueces mientras se escribe
3. **`editar_registro(registro_id)`** - Abre formulario de edición
4. **`eliminar_registro(registro_id)`** - Elimina con confirmación
5. **`busqueda_avanzada()`** - Abre ventana de filtros múltiples
6. **`aplicar_filtros()`** - Ejecuta búsqueda con criterios combinados

### **Nuevas ventanas/interfaces:**
1. **Ventana de edición** - Formulario modal para modificar registros
2. **Ventana de búsqueda avanzada** - Múltiples campos de filtro
3. **Diálogo de confirmación** - Para eliminación de registros

## 🧪 PRUEBAS A REALIZAR

### **Prueba 1: Autocompletado de juez**
- [ ] Combobox muestra lista de jueces
- [ ] Filtra mientras se escribe
- [ ] Permite seleccionar juez existente
- [ ] Botón para agregar nuevo juez funciona

### **Prueba 2: Edición de registros**
- [ ] Botón "EDITAR" abre formulario con datos
- [ ] Campos pre-llenados correctamente
- [ ] Guardar cambios actualiza base de datos
- [ ] Cambios se reflejan en lista inmediatamente

### **Prueba 3: Eliminación de registros**
- [ ] Botón "ELIMINAR" pide confirmación
- [ ] Eliminación exitosa (física o lógica)
- [ ] Registro desaparece de la lista
- [ ] Mensaje de confirmación apropiado

### **Prueba 4: Búsqueda avanzada**
- [ ] Ventana con múltiples campos de filtro
- [ ] Filtros combinados funcionan (AND)
- [ ] Resultados precisos según criterios
- [ ] Sin resultados muestra mensaje apropiado

### **Prueba 5: Integración completa**
- [ ] CRUD completo funciona sin errores
- [ ] Autocompletado integrado con edición
- [ ] Búsqueda avanzada incluye todos los campos
- [ ] Sistema estable después de múltiples operaciones

## 📈 CRITERIOS DE ÉXITO

### **Éxito mínimo:**
- ✅ Autocompletado de juez funcionando
- ✅ Edición básica de registros
- ✅ Eliminación con confirmación
- ✅ Búsqueda con 2-3 criterios combinados

### **Éxito completo:**
- ✅ Sistema CRUD completo y estable
- ✅ Autocompletado inteligente con agregar nuevo
- ✅ Búsqueda avanzada con todos los campos
- ✅ Interfaz intuitiva y responsive
- ✅ Manejo de errores robusto

## 👥 RESPONSABILIDADES

### **XeatBOSS:**
- Probar autocompletado con nombres reales de jueces
- Validar que la edición sea intuitiva y útil
- Sugerir criterios de búsqueda más relevantes
- Probar eliminación y confirmar que es segura

### **ClawXeatJr:**
- Implementar normalización de base de datos
- Guiar implementación de autocompletado
- Manejar transacciones y errores en CRUD
- Asegurar que búsqueda avanzada sea eficiente

## 🔄 CONSIDERACIONES TÉCNICAS

### **Estrategia de eliminación:**
**Opción A:** Eliminación física (DELETE) - Más simple pero sin recuperación
**Opción B:** Eliminación lógica (campo `activo=0`) - Permite recuperación
**Opción C:** Histórico de cambios (tabla `citas_historico`) - Completo pero complejo

**Recomendación:** Opción B (eliminación lógica) para primer implementación.

### **Autocompletado vs Combobox simple:**
- **Combobox con lista completa:** Simple pero puede ser larga
- **Autocompletado con filtro:** Más usable para muchas opciones
- **Combobox + búsqueda:** Mejor de ambos mundos

**Recomendación:** Combobox con autocompletado mientras se escribe.

### **Búsqueda avanzada:**
- **Filtros AND:** Todos los criterios deben cumplirse
- **Filtros OR:** Cualquier criterio puede cumplirse
- **Filtros mixtos:** Combinación compleja

**Recomendación:** Filtros AND simples para primera versión.

## 🚨 RIESGOS IDENTIFICADOS

### **Riesgo 1: Migración de datos de jueces**
**Mitigación:** Script de migración con backup y verificación

### **Riesgo 2: Autocompletado lento con muchos jueces**
**Mitigación:** Limitar resultados mostrados, usar índice en base de datos

### **Riesgo 3: Eliminación accidental**
**Mitigación:** Confirmación obligatoria, posiblemente papelera de reciclaje

### **Riesgo 4: Búsqueda avanzada muy compleja**
**Mitigación:** Empezar con 3-4 criterios esenciales, expandir después

## 📊 MÉTRICAS DE PROGRESO

### **Al inicio de iteración:**
- Funcionalidades: 7 (Guardar, Ver, Buscar simple, Generar Doc, Importar, Exportar)
- Tablas en BD: 1 (citas_piloto)
- Operaciones CRUD: 2 (Create, Read)

### **Al final de iteración (objetivo):**
- Funcionalidades: +3 (Editar, Eliminar, Buscar avanzada)
- Tablas en BD: 2 (+jueces)
- Operaciones CRUD: 4 (Create, Read, Update, Delete)
- Valor agregado: Sistema profesional completo

## 🔗 ENLACES RELACIONADOS

### **Documentación anterior:**
- [[004_ITERACION]] - Iteración 4 completada
- [[resumen_iteracion4_completa]] - Resumen de importación/exportación
- [[resumen_final_dia_2026-04-20]] - Resumen del día

### **Recursos técnicos:**
- [Tkinter Combobox autocomplete](https://stackoverflow.com/questions/41656176/tkinter-autocomplete)
- [SQLite FOREIGN KEY constraints](https://www.sqlite.org/foreignkeys.html)
- [Python SQLite CRUD operations](https://www.sqlitetutorial.net/sqlite-python/)

## 🎮 PLAN DE EJECUCIÓN

### **Minuto 0-15:** Crear tabla jueces y migrar datos
### **Minuto 15-30:** Implementar autocompletado de juez
### **Minuto 30-45:** Agregar edición de registros
### **Minuto 45-55:** Agregar eliminación de registros
### **Minuto 55-70:** Implementar búsqueda avanzada
### **Minuto 70-75:** Probar, ajustar, documentar

---
**Documentación creada:** 20 Abril 2026, 21:30 UTC  
**Tiempo asignado:** 75 minutos  
**Estado:** 🟡 EN EJECUCIÓN  
**Siguiente actualización:** Al completar iteración

**🚀 ¡COMENZAMOS IMPLEMENTACIÓN DE MEJORAS AVANZADAS!**