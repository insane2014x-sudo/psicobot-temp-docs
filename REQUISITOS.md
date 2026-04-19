# ⚙️ REQUISITOS - Especificaciones Técnicas

## 🎯 Alcance del Sistema

Psicobot es un sistema de automatización de transcripción psicológica que procesa grabaciones de audio, genera transcripciones formateadas, gestiona datos de participantes y produce documentos listos para entrega, todo de manera 100% local.

## 📋 Requisitos Funcionales

### **RF01: Transcripción de Audio**
**ID:** `RF01`  
**Prioridad:** ALTA  
**Descripción:** El sistema debe transcribir automáticamente archivos de audio a texto.

**Criterios de Aceptación:**
- CA01: Soporta formatos MP3, WAV, M4A
- CA02: Identifica automáticamente idioma español
- CA03: Proporciona texto crudo con timestamps
- CA04: Maneja audio de 45-60 minutos de duración
- CA05: Tolerancia a ruido de fondo moderado

**Especificaciones Técnicas:**
- Herramienta: Whisper (OpenAI) local
- Modelo mínimo: `whisper-medium`
- Precisión objetivo: 90%+ en audio claro
- Tiempo procesamiento: 2-3x tiempo real

### **RF02: Corrección Contextual Psicológica**
**ID:** `RF02`  
**Prioridad:** ALTA  
**Descripción:** El sistema debe corregir y formatear transcripciones según contexto psicológico.

**Criterios de Aceptación:**
- CA01: Identifica automáticamente psicóloga vs paciente
- CA02: Aplica formato: psicóloga (¿?), paciente (.)
- CA03: Corrige términos psicológicos comunes
- CA04: Mantiene fidelidad al contenido original
- CA05: Proporciona confianza en correcciones

**Especificaciones Técnicas:**
- Herramienta: Ollama con qwen2.5-coder
- Prompt especializado en psicología
- Validación humana requerida para términos críticos
- Log de cambios realizados

### **RF03: Gestión de Participantes**
**ID:** `RF03`  
**Prioridad:** MEDIA  
**Descripción:** El sistema debe gestionar base de datos local de participantes.

**Criterios de Aceptación:**
- CA01: CRUD completo (Crear, Leer, Actualizar, Eliminar)
- CA02: Búsqueda por nombre, tipo, fecha
- CA03: Clasificación presencial/virtual
- CA04: Historial de sesiones por participante
- CA05: Exportación a CSV/Excel

**Especificaciones Técnicas:**
- Base de datos: SQLite local
- Esquema normalizado
- Backup automático diario
- Interfaz: CLI simple + posibles exports

### **RF04: Generación de Documentos**
**ID:** `RF04`  
**Prioridad:** ALTA  
**Descripción:** El sistema debe generar documentos Word a partir de plantillas.

**Criterios de Aceptación:**
- CA01: Rellena plantillas Word existentes
- CA02: Inserta transcripción formateada
- CA03: Incorpora datos de participantes
- CA04: Mantiene formato profesional
- CA05: Genera nombre de archivo consistente

**Especificaciones Técnicas:**
- Formato: .docx (Microsoft Word)
- Plantillas con marcadores `{{variable}}`
- Compatibilidad Word 2010+
- Preserva estilos y formatos originales

### **RF05: Sistema de Recordatorios**
**ID:** `RF05`  
**Prioridad:** BAJA  
**Descripción:** El sistema debe proporcionar recordatorios de sesiones programadas.

**Criterios de Aceptación:**
- CA01: Lee agenda desde Excel existente
- CA02: Envía recordatorios via Telegram
- CA03: Alertas: 24h, 1h, 15min antes
- CA04: Incluye información preparatoria
- CA05: Confirma recepción de alertas

**Especificaciones Técnicas:**
- Integración: API Telegram (bot)
- Formato Excel: columnas específicas
- Horarios configurables
- Log de envíos

### **RF06: Flujo de Trabajo Unificado**
**ID:** `RF06`  
**Prioridad:** MEDIA  
**Descripción:** El sistema debe orquestar el flujo completo desde audio a documento.

**Criterios de Aceptación:**
- CA01: Interfaz de línea de comandos intuitiva
- CA02: Progreso automático entre etapas
- CA03: Manejo de errores con recuperación
- CA04: Logs detallados de procesamiento
- CA05: Opción de pausa/reanudación

**Especificaciones Técnicas:**
- Script principal: `psicobot`
- Estados: preparación, transcripción, corrección, generación, revisión
- Timeouts configurables
- Sistema de reintentos

## 🛡️ Requisitos No Funcionales

### **RNF01: Rendimiento**
**ID:** `RNF01`  
**Categoría:** Rendimiento  
**Descripción:** El sistema debe procesar sesiones en tiempo razonable.

**Métricas:**
- Transcripción: 2-3x tiempo real (90-180min para 60min audio)
- Corrección: 5-10 minutos por sesión
- Generación documento: 1-2 minutos
- **Total objetivo:** < 3 horas por sesión (vs 6-8 manual)

**Límites:**
- Máximo tamaño audio: 2GB
- Máxima duración: 120 minutos
- Uso RAM: < 8GB durante transcripción
- Uso CPU: < 80% sostenido

### **RNF02: Confiabilidad**
**ID:** `RNF02`  
**Categoría:** Confiabilidad  
**Descripción:** El sistema debe ser estable y recuperable ante fallos.

**Métricas:**
- Disponibilidad: 99% durante horas laborales
- Tasa de fallos: < 5% de sesiones procesadas
- Tiempo medio entre fallos: > 100 horas
- Tiempo medio de recuperación: < 15 minutos

**Mecanismos:**
- Checkpoints entre etapas
- Logs detallados para debugging
- Sistema de reintentos automáticos
- Backup de datos en procesamiento

### **RNF03: Usabilidad**
**ID:** `RNF03`  
**Categoría:** Usabilidad  
**Descripción:** El sistema debe ser fácil de usar para usuario técnico.

**Métricas:**
- Tiempo aprendizaje: < 2 horas para flujo básico
- Comandos memorizables: < 10 principales
- Mensajes de error comprensibles
- Documentación accesible

**Características:**
- Interfaz CLI con colores y progreso
- Comandos con `--help` completo
- Ejemplos de uso incluidos
- Mensajes en español

### **RNF04: Mantenibilidad**
**ID:** `RNF04`  
**Categoría:** Mantenibilidad  
**Descripción:** El sistema debe ser fácil de mantener y extender.

**Métricas:**
- Cobertura de tests: > 70%
- Deuda técnica: < 5 días
- Documentación actualizada
- Código modular y documentado

**Características:**
- Estructura modular clara
- Configuración externa (YAML/JSON)
- Logs estructurados
- Sistema de plugins/extensions

### **RNF05: Seguridad**
**ID:** `RNF05`  
**Categoría:** Seguridad  
**Descripción:** El sistema debe proteger la privacidad de datos sensibles.

**Métricas:**
- Cero datos enviados a internet
- Permisos de archivos restrictivos
- Logs sanitizados (sin datos personales)
- Backups encriptados opcionales

**Mecanismos:**
- Procesamiento 100% local
- Base de datos local encriptable
- Archivos temporales borrados seguramente
- Sin registros de audio/texto crudo persistentes

### **RNF06: Compatibilidad**
**ID:** `RNF06`  
**Categoría:** Compatibilidad  
**Descripción:** El sistema debe funcionar en el entorno objetivo.

**Entorno Objetivo:**
- Sistema operativo: Windows 10/11 con WSL2
- WSL: Ubuntu 22.04 LTS
- Python: 3.10+
- RAM: 16GB mínimo recomendado
- Almacenamiento: 50GB libre mínimo

**Dependencias:**
- Whisper (OpenAI)
- Ollama + qwen2.5-coder
- FFmpeg
- Python libraries específicas

## 🔧 Requisitos Técnicos Detallados

### **Infraestructura de Software**

#### **Whisper Configuration:**
```yaml
whisper:
  model: "medium"  # small, medium, large, large-v2
  language: "es"
  task: "transcribe"
  temperature: 0.2
  best_of: 5
  beam_size: 5
  patience: 1.0
  length_penalty: 1.0
  suppress_tokens: "-1"
  initial_prompt: "Transcripción psicológica:"
  condition_on_previous_text: true
  fp16: true  # Si GPU disponible
```

#### **Ollama Configuration:**
```yaml
ollama:
  model: "qwen2.5-coder:latest"
  temperature: 0.3
  top_p: 0.9
  top_k: 40
  repeat_penalty: 1.1
  num_predict: 4096
  
prompts:
  psicologia: |
    Eres un asistente especializado en transcripciones psicológicas.
    Identifica si habla la PSICÓLOGA o el PACIENTE.
    Formato:
    - PSICÓLOGA: ¿pregunta con signos de interrogación?
    - PACIENTE: oración normal con punto.
    Corrige términos psicológicos específicos.
    Mantén fidelidad al contenido original.
```

#### **Base de Datos Schema:**
```sql
-- Tabla participantes
CREATE TABLE participantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('presencial', 'virtual')),
    contacto TEXT,
    notas TEXT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla sesiones
CREATE TABLE sesiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    participante_id INTEGER REFERENCES participantes(id),
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    duracion INTEGER,  -- en minutos
    tipo_sesion TEXT,
    archivo_audio TEXT,
    archivo_transcripcion TEXT,
    archivo_acta TEXT,
    estado TEXT CHECK(estado IN ('programada', 'realizada', 'transcrita', 'aprobada')),
    notas TEXT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### **Requisitos de Hardware**

#### **Mínimo:**
- CPU: 4 cores modernos (Intel i5/Ryzen 5 o superior)
- RAM: 8GB (16GB recomendado)
- Almacenamiento: 50GB SSD
- GPU: Opcional (acelera Whisper significativamente)

#### **Recomendado:**
- CPU: 8 cores
- RAM: 16GB+
- Almacenamiento: 100GB+ SSD
- GPU: NVIDIA con 4GB+ VRAM (para Whisper acelerado)

### **Requisitos de Red**
- **Local solamente:** No requiere conexión a internet para funcionamiento
- **Opcional:** Solo para:
  - Descarga inicial de modelos
  - Actualizaciones de software
  - Recordatorios Telegram

## 📊 Métricas de Calidad

### **Calidad de Transcripción:**
- **WER (Word Error Rate):** < 15% en audio claro
- **Identificación hablantes:** > 90% precisión
- **Formato psicológico:** > 95% correcto
- **Términos especializados:** > 85% correctos

### **Eficiencia del Sistema:**
- **Tiempo total procesamiento:** < 3 horas por sesión de 1h
- **Uso recursos:** < 80% RAM, < 90% CPU durante peaks
- **Tasa de éxito:** > 90% sesiones procesadas sin intervención
- **Tiempo revisión humana:** < 15 minutos por sesión

### **Satisfacción del Usuario:**
- **Encuesta post-implementación:**
  - Facilidad de uso: > 4/5
  - Confiabilidad: > 4/5
  - Ahorro de tiempo percibido: > 70%
  - Intención de uso continuo: > 4/5

## 🚨 Restricciones y Limitaciones

### **Limitaciones Conocidas:**
1. **Audio de baja calidad:** Reduce precisión significativamente
2. **Múltiples hablantes simultáneos:** Dificulta identificación
3. **Términos muy especializados:** Requiere corrección manual
4. **Acentos regionales fuertes:** Puede afectar transcripción
5. **Sesiones > 2 horas:** Requiere procesamiento por segmentos

### **Restricciones de Diseño:**
1. **Local solamente:** No hay versión cloud/nube
2. **Un usuario a la vez:** No diseñado para multi-usuario
3. **Windows + WSL:** Entorno principal soportado
4. **Español:** Idioma principal, otros requieren ajustes

## 🔄 Requisitos de Evolución

### **Fase 1 (Piloto):**
- RF01, RF02 básicos funcionando
- RNF01, RNF05 cumplidos
- Interfaz CLI básica

### **Fase 2 (Implementación):**
- RF01-04 completos
- RNF01-05 cumplidos
- Sistema semi-automático

### **Fase 3 (Completo):**
- RF01-06 completos
- RNF01-06 cumplidos
- Sistema totalmente automatizado

## 📝 Criterios de Aceptación Final

El sistema será considerado **exitoso** si cumple:

### **Obligatorios (must-have):**
1. ✅ Transcribe audio psicológico con > 85% precisión
2. ✅ Identifica psicóloga/paciente con > 90% precisión
3. ✅ Genera documentos Word usables sin corrección mayor
4. ✅ Mantiene todos los datos 100% locales
5. ✅ Reduce tiempo total en > 60%

### **Deseables (should-have):**
1. ⚡ Procesa sesión de 1h en < 2 horas
2. 📊 Gestión de participantes funcional
3. 🔔 Sistema de recordatorios básico
4. 🛡️ Backups automáticos

### **Opcionales (nice-to-have):**
1. 🎨 Interfaz gráfica básica
2. 📈 Reportes estadísticos
3. 🔄 Sincronización multi-dispositivo
4. 🎯 Reconocimiento de emociones básico

## 🧪 Criterios de Prueba

### **Pruebas de Unidad:**
- Cobertura de código: > 70%
- Pruebas por requisito funcional
- Validación de formatos y esquemas

### **Pruebas de Integración:**
- Flujo completo de extremo a extremo
- Compatibilidad entre componentes
- Manejo de errores y recuperación

### **Pruebas de Usuario:**
- Sesiones reales (con consentimiento y anonimización)
- Feedback cualitativo y cuantitativo
- Medición de tiempo real vs estimado

### **Pruebas de Seguridad:**
- Verificación de no-fuga de datos
- Validación de permisos de archivos
- Pruebas de recuperación ante fallos

---
**Versión requisitos:** 1.0.0  
**Basado en:** Conversaciones con XeatBoss, 19 Abril 2026  
**Estado:** Aprobado para Fase 1 (Piloto)  
**Responsable:** ClawXeatJr