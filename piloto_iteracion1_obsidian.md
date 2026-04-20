# 🧪 PILOTO - Iteración 1

**Fecha:** 20 Abril 2026  
**Estado:** 🟡 En progreso  
**Objetivo:** Sistema mínimo funcional con interfaz gráfica

## 🎯 OBJETIVOS ITERACIÓN 1

### **Meta principal:**
Crear aplicación Windows simple que permita ingresar datos de citas psicológicas y guardarlos en base de datos local.

### **Componentes a desarrollar:**
1. 🖥️ **Interfaz gráfica** (Tkinter) con 4 campos
2. 🗄️ **Base de datos** (SQLite) con 1 tabla
3. 🔗 **Conexión** interfaz → base de datos
4. ✅ **Verificación** de funcionamiento

## 📋 CAMPOS DEL FORMULARIO

### **4 campos a implementar:**
1. **📄 Expediente** (Texto, ej: "2026-00123-PE")
2. **👤 Iniciales persona** (Texto, ej: "M.P.R.")
3. **📅 Fecha** (Fecha, formato: DD/MM/AAAA)
4. **⚖️ Nombre de juez** (Texto, ej: "DR. JUAN PÉREZ")

## 🗄️ ESTRUCTURA BASE DE DATOS

### **Tabla: `citas_piloto`**
```sql
CREATE TABLE citas_piloto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expediente TEXT NOT NULL,
    iniciales_persona TEXT NOT NULL,
    fecha DATE NOT NULL,
    nombre_juez TEXT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔧 TECNOLOGÍAS UTILIZADAS

### **Stack mínimo:**
- **Python 3.10+** - Lenguaje principal
- **Tkinter** - Interfaz gráfica (viene con Python)
- **SQLite3** - Base de datos (viene con Python)
- **datetime** - Manejo de fechas (viene con Python)

### **Sin dependencias externas:**
- No necesita `pip install`
- Todo incluido en Python estándar
- Portable y fácil de distribuir

## 🚀 PLAN DE TRABAJO

### **Paso 1: Crear interfaz Tkinter**
- Ventana principal (500x400 px)
- 4 etiquetas + 4 campos de entrada
- Botón "Guardar"
- Etiqueta para mensajes

### **Paso 2: Crear base de datos**
- Archivo `piloto.db`
- Tabla `citas_piloto`
- Función de inicialización

### **Paso 3: Conectar componentes**
- Función `guardar_datos()`
- Validación básica de entrada
- Inserción en SQLite
- Mensaje de confirmación

### **Paso 4: Probar y verificar**
- Ejecutar aplicación
- Ingresar datos de prueba
- Verificar que se guardan
- Ver datos en base de datos

## 📁 ESTRUCTURA DE ARCHIVOS

```
piloto_iteracion1/
├── app.py                    # Aplicación principal
├── database.py              # Funciones base de datos
├── piloto.db               # Base de datos SQLite
└── README.md               # Instrucciones
```

## 💻 CÓDIGO BASE

### **app.py (esqueleto):**
```python
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class AplicacionPiloto:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Psicobot - Piloto")
        self.ventana.geometry("500x400")
        
        self.crear_interfaz()
        self.inicializar_db()
    
    def crear_interfaz(self):
        # Campos: expediente, iniciales, fecha, juez
        # Botón guardar
        pass
    
    def inicializar_db(self):
        # Crear/conectar a piloto.db
        pass
    
    def guardar_datos(self):
        # Obtener datos de campos
        # Validar
        # Insertar en SQLite
        # Mostrar mensaje
        pass
    
    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = AplicacionPiloto()
    app.ejecutar()
```

## 🧪 PRUEBAS A REALIZAR

### **Prueba 1: Interfaz visible**
- [ ] La ventana se abre
- [ ] Los 4 campos son visibles
- [ ] El botón "Guardar" es clickeable

### **Prueba 2: Base de datos**
- [ ] Archivo `piloto.db` se crea
- [ ] Tabla `citas_piloto` existe
- [ ] Puede insertar registros

### **Prueba 3: Flujo completo**
- [ ] Ingresar datos en campos
- [ ] Click "Guardar"
- [ ] Mensaje "✅ Datos guardados"
- [ ] Verificar en base de datos

## 📈 CRITERIOS DE ÉXITO

### **Éxito mínimo:**
- Aplicación se ejecuta sin errores
- Datos se guardan en SQLite
- Mensaje de confirmación funciona

### **Éxito completo:**
- Interfaz intuitiva y clara
- Validación de datos básica
- Posibilidad de ver datos guardados
- Código documentado y claro

## 👥 RESPONSABILIDADES

### **XeatBoss:**
- Probar cada componente
- Dar feedback de usabilidad
- Sugerir mejoras
- Documentar problemas

### **ClawXeatJr:**
- Desarrollar código paso a paso
- Explicar cada parte
- Corregir errores
- Guiar pruebas

## 🔄 SIGUIENTES ITERACIONES

### **Iteración 2 (si esta funciona):**
- Agregar más campos
- Listar datos guardados
- Buscar/editar registros

### **Iteración 3:**
- Generar documento Word automático
- Plantilla básica
- Campos dinámicos

### **Iteración 4:**
- Importar desde Excel
- Exportar a Excel
- Reportes simples

## 📝 NOTAS Y OBSERVACIONES

### **Decisiones de diseño:**
- Usar Tkinter (viene con Python, no necesita instalación)
- SQLite (base de datos local, sin servidor)
- Todo en un solo archivo inicialmente (simple)

### **Consideraciones:**
- La aplicación será 100% local
- No requiere conexión a internet
- Los datos quedan en la PC del usuario
- Fácil de distribuir (ejecutable .exe posible)

---
**Documentación creada:** 20 Abril 2026, 01:13 UTC  
**Para usar:** Copiar a Obsidian y seguir como guía  
**Siguiente paso:** Crear código de la interfaz