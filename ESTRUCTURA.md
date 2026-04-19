# 📁 ESTRUCTURA - Organización de Archivos del Proyecto

## 🎯 Visión de la Estructura

Una organización clara y consistente de archivos es fundamental para mantener el proyecto mantenible, escalable y fácil de usar. Esta estructura sigue principios de **modularidad**, **separación de preocupaciones** y **facilidad de navegación**.

## 🌳 Estructura Completa del Proyecto

```
psicobot/                              # Directorio raíz del proyecto
├── 📄 README.md                       # Documentación principal
├── 📄 PLAN.md                         # Plan de implementación
├── 📄 FLUJO_TRABAJO.md                # Diagramas y procesos
├── 📄 ESTRUCTURA.md                   # Este documento
├── 📄 REQUISITOS.md                   # Especificaciones técnicas
├── 📄 SEGURIDAD.md                    # Protocolos de privacidad
├── 📄 CHANGELOG.md                    # Historial de cambios
│
├── 📁 bin/                            # Scripts ejecutables principales
│   ├── 📄 psicobot                    # Script principal (orquestador)
│   ├── 📄 transcripcion.sh            # Transcripción completa
│   ├── 📄 gestion_participantes.sh    # Gestión de base de datos
│   └── 📄 generar_acta.sh             # Generación de documentos
│
├── 📁 src/                            # Código fuente y módulos
│   ├── 📁 transcripcion/              # Módulo de transcripción
│   │   ├── 📄 whisper_wrapper.py      # Interfaz con Whisper
│   │   ├── 📄 correccion_psicologica.py # Corrección con Ollama
│   │   ├── 📄 formateador_dialogo.py  # Formateo psicológico
│   │   └── 📄 __init__.py
│   │
│   ├── 📁 database/                   # Módulo de base de datos
│   │   ├── 📄 modelos.py              # Modelos de datos
│   │   ├── 📄 crud.py                 # Operaciones CRUD
│   │   ├── 📄 consultas.py            # Consultas específicas
│   │   └── 📄 __init__.py
│   │
│   ├── 📁 documentos/                 # Módulo de documentos
│   │   ├── 📄 plantilla_manager.py    # Gestión de plantillas
│   │   ├── 📄 generador_word.py       # Generación Word
│   │   └── 📄 __init__.py
│   │
│   ├── 📁 agenda/                     # Módulo de agenda
│   │   ├── 📄 sincronizador_excel.py  # Lectura Excel
│   │   ├── 📄 recordatorios.py        # Sistema de alertas
│   │   └── 📄 __init__.py
│   │
│   └── 📁 utils/                      # Utilidades generales
│       ├── 📄 logger.py               # Sistema de logging
│       ├── 📄 config_loader.py        # Carga de configuración
│       ├── 📄 validadores.py          # Validación de datos
│       └── 📄 __init__.py
│
├── 📁 config/                         # Configuración del sistema
│   ├── 📄 settings.yaml               # Configuración principal
│   ├── 📄 prompts.yaml                # Prompts para Ollama
│   ├── 📄 plantillas.yaml             # Definición plantillas
│   └── 📄 database_schema.yaml        # Esquema de base de datos
│
├── 📁 plantillas/                     # Plantillas de documentos
│   ├── 📄 acta_psicologia.docx        # Plantilla Word principal
│   ├── 📄 formato_transcripcion.txt   # Formato estándar
│   ├── 📄 encabezado_juzgado.docx     # Encabezados institucionales
│   └── 📁 personalizadas/             # Plantillas personalizadas
│
├── 📁 scripts/                        # Scripts de utilidad
│   ├── 📄 setup_whisper.sh            # Instalación Whisper
│   ├── 📄 setup_ollama.sh             # Configuración Ollama
│   ├── 📄 backup_database.sh          # Backup de base de datos
│   ├── 📄 limpiar_temporales.sh       # Limpieza archivos temp
│   └── 📄 health_check.sh             # Verificación sistema
│
├── 📁 docs/                           # Documentación detallada
│   ├── 📄 instalacion.md              # Guía de instalación
│   ├── 📄 uso_basico.md               # Guía de uso básico
│   ├── 📄 troubleshooting.md          # Solución de problemas
│   ├── 📄 desarrollo.md               # Guía para desarrolladores
│   └── 📁 api/                        # Documentación API interna
│
├── 📁 tests/                          # Pruebas del sistema
│   ├── 📁 unit/                       # Pruebas unitarias
│   ├── 📁 integration/                # Pruebas de integración
│   ├── 📁 fixtures/                   # Datos de prueba
│   └── 📄 run_tests.sh                # Ejecutor de pruebas
│
├── 📁 data/                           # Datos del sistema (USUARIO)
│   ├── 📁 audios/                     # Grabaciones de audio
│   │   ├── 📁 2026-04/                # Organizado por mes
│   │   │   ├── 📁 19/                 # Organizado por día
│   │   │   │   ├── 🎵 sesion_1.mp3
│   │   │   │   └── 🎵 sesion_2.mp3
│   │   │   └── 📁 20/
│   │   └── 📁 2026-05/
│   │
│   ├── 📁 transcripciones/            # Transcripciones procesadas
│   │   ├── 📁 brutas/                 # Texto sin procesar
│   │   ├── 📁 corregidas/             # Texto corregido
│   │   └── 📁 formateadas/            # Texto formateado final
│   │
│   ├── 📁 actas/                      # Documentos generados
│   │   ├── 📁 preliminares/           # Borradores
│   │   ├── 📁 aprobadas/              # Aprobadas para entrega
│   │   └── 📁 archivadas/             # Histórico
│   │
│   ├── 📁 database/                   # Base de datos local
│   │   ├── 🗃️ participantes.db       # Base de datos SQLite
│   │   ├── 🗃️ sesiones.db           # Registro de sesiones
│   │   └── 🗃️ configuracion.db      # Configuración del sistema
│   │
│   └── 📁 backups/                    # Copias de seguridad
│       ├── 📁 automaticos/            # Backups automáticos
│       └── 📁 manuales/               # Backups manuales
│
├── 📁 logs/                           # Registros del sistema
│   ├── 📄 aplicacion.log              # Log principal
│   ├── 📄 transcripcion.log           # Log de transcripciones
│   ├── 📄 errores.log                 # Log de errores
│   └── 📁 historico/                  # Logs históricos
│
└── 📁 .git/                           # Control de versiones (opcional)
    ├── 📄 .gitignore                  # Archivos a ignorar
    └── 📄 README_GIT.md               # Guía de uso Git
```

## 📋 Descripción Detallada de Directorios

### **📁 bin/ - Scripts Ejecutables**
Scripts principales que el usuario ejecuta directamente. Diseñados para ser intuitivos y con mensajes de ayuda.

**Ejemplo de uso:**
```bash
# Script principal
./bin/psicobot --help

# Transcripción específica
./bin/transcripcion.sh /ruta/audio.mp3 --psicologa "Dra. María"

# Gestión de participantes
./bin/gestion_participantes.sh agregar "Juan Pérez" virtual
```

### **📁 src/ - Código Fuente**
Código modular organizado por funcionalidad. Cada módulo es independiente y reusable.

**Estructura modular:**
- `transcripcion/`: Todo relacionado con procesamiento de audio/texto
- `database/`: Operaciones con base de datos
- `documentos/`: Generación y manejo de documentos
- `agenda/`: Gestión de calendario y recordatorios
- `utils/`: Utilidades compartidas

### **📁 config/ - Configuración**
Archivos de configuración en YAML/JSON para facilitar ajustes sin modificar código.

**settings.yaml ejemplo:**
```yaml
transcripcion:
  modelo_whisper: "medium"
  idioma: "es"
  temperatura: 0.2

correccion:
  modelo_ollama: "qwen2.5-coder"
  prompt_psicologia: "prompts/psicologia.txt"

database:
  ruta: "data/database/participantes.db"
  backup_automatico: true

documentos:
  plantilla_principal: "plantillas/acta_psicologia.docx"
  ruta_salida: "data/actas/"
```

### **📁 plantillas/ - Plantillas**
Plantillas reutilizables para documentos. Separadas del código para fácil personalización.

**Contenido típico:**
- Plantillas Word (.docx) con marcadores `{{variable}}`
- Formatos de texto estándar
- Encabezados y pies de página institucionales

### **📁 scripts/ - Scripts de Utilidad**
Scripts para mantenimiento, instalación y administración del sistema.

**Scripts importantes:**
- `setup_*.sh`: Instalación de dependencias
- `backup_*.sh`: Copias de seguridad
- `health_check.sh`: Diagnóstico del sistema

### **📁 docs/ - Documentación**
Documentación detallada para usuarios y desarrolladores.

**Para usuarios:**
- Guías paso a paso
- Ejemplos de uso
- Solución de problemas comunes

**Para desarrolladores:**
- Documentación de API interna
- Guías de contribución
- Estándares de código

### **📁 data/ - Datos del Usuario** ⚠️ **IMPORTANTE**
**Este directorio contiene TODOS los datos del usuario.** Está excluido de control de versiones por privacidad.

**Organización temporal:**
- `audios/2026-04/19/`: Un directorio por día
- Facilita búsqueda y backup
- Mantiene privacidad organizada

### **📁 logs/ - Registros**
Sistema de logging estructurado para diagnóstico y auditoría.

**Niveles de log:**
- INFO: Operaciones normales
- WARNING: Situaciones inusuales
- ERROR: Errores recuperables
- CRITICAL: Errores graves

## 🔄 Flujo de Datos entre Directorios

```
data/audios/2026-04-19/sesion.mp3
    ↓ (procesado por)
src/transcripcion/whisper_wrapper.py
    ↓ (genera)
data/transcripciones/brutas/2026-04-19_sesion.txt
    ↓ (procesado por)
src/transcripcion/correccion_psicologica.py
    ↓ (genera)
data/transcripciones/corregidas/2026-04-19_sesion.txt
    ↓ (usado por)
src/documentos/generador_word.py
    ↓ (con plantilla)
plantillas/acta_psicologia.docx
    ↓ (genera)
data/actas/aprobadas/2026-04-19_sesion.docx
```

## 🛡️ Consideraciones de Seguridad por Directorio

### **Directorios Críticos (máxima protección):**
- `data/`: Contiene información sensible
- `config/`: Contiene configuraciones del sistema
- `database/`: Base de datos con información personal

### **Protecciones implementadas:**
1. **Permisos de archivos:** Solo usuario dueño puede leer/escribir
2. **Exclusión de versionado:** `data/` no se sube a Git
3. **Encriptación opcional:** Para backups sensibles
4. **Logs sanitizados:** Sin información personal en logs

## 📊 Estructura para Escalabilidad

### **Para múltiples psicólogas:**
```
data/
├── 📁 dra_maria/
│   ├── 📁 audios/
│   ├── 📁 transcripciones/
│   └── 📁 actas/
│
├── 📁 dr_carlos/
│   ├── 📁 audios/
│   ├── 📁 transcripciones/
│   └── 📁 actas/
│
└── 📁 compartido/
    ├── 🗃️ participantes_comun.db
    └── 📁 plantillas_comunes/
```

### **Para múltiples juzgados/instituciones:**
```
plantillas/
├── 📁 juzgado_familia/
│   ├── 📄 acta_familia.docx
│   └── 📄 encabezado_familia.docx
│
├── 📁 clinica_psicologia/
│   ├── 📄 acta_clinica.docx
│   └── 📄 encabezado_clinica.docx
│
└── 📁 consulta_privada/
    ├── 📄 acta_privada.docx
    └── 📄 encabezado_privada.docx
```

## 🧹 Convenciones de Nombrado

### **Archivos de audio:**
```
YYYY-MM-DD_HH-MM_psicologa_paciente_tipo.ext
Ejemplo: 2026-04-19_10-00_dra_maria_ana_lopez_virtual.mp3
```

### **Archivos de transcripción:**
```
YYYY-MM-DD_psicologa_paciente_etapa.txt
Ejemplo: 2026-04-19_dra_maria_ana_lopez_corregida.txt
```

### **Archivos de actas:**
```
YYYY-MM-DD_psicologa_paciente_estado.docx
Ejemplo: 2026-04-19_dra_maria_ana_lopez_aprobada.docx
```

## 🔧 Estructura para Desarrollo

### **Entorno de desarrollo:**
```
psicobot_dev/
├── 📁 src/                          # Código fuente (enlace simbólico)
├── 📁 tests/                        # Pruebas
├── 📁 data_test/                    # Datos de prueba
│   ├── 📁 audios_muestra/           # Audios de ejemplo
│   └── 📁 transcripciones_muestra/  # Transcripciones de ejemplo
├── 📄 requirements.txt              # Dependencias Python
└── 📄 Makefile                      # Automatización tareas
```

### **Scripts de desarrollo:**
```bash
# Instalar dependencias
make install

# Ejecutar pruebas
make test

# Ejecutar con datos de prueba
make run_test

# Generar documentación
make docs
```

## 📈 Evolución de la Estructura

### **Versión 1.0 (Piloto):**
- Estructura básica funcional
- Mínimo de directorios necesarios
- Enfoque en simplicidad

### **Versión 2.0 (Producción):**
- Estructura modular completa
- Sistema de plugins/extensions
- Soporte multi-usuario

### **Versión 3.0 (Escalado):**
- Estructura para nube/local híbrida
- Replicación de datos
- Alta disponibilidad

## ✅ Checklist de Implementación

### **Para comenzar el proyecto:**
- [ ] Crear directorio raíz `psicobot/`
- [ ] Crear subdirectorios básicos (`bin/`, `src/`, `config/`)
- [ ] Configurar permisos adecuados
- [ ] Establecer `.gitignore` apropiado
- [ ] Documentar estructura en `ESTRUCTURA.md`

### **Para cada nueva funcionalidad:**
- [ ] Determinar módulo apropiado en `src/`
- [ ] Crear tests correspondientes en `tests/`
- [ ] Actualizar documentación en `docs/`
- [ ] Actualizar `CHANGELOG.md`

---
**Estructura versión:** 1.0.0 (Piloto)  
**Última revisión:** 19 de Abril, 2026  
**Próxima revisión:** Al finalizar Fase 1  
**Responsable:** ClawXeatJr