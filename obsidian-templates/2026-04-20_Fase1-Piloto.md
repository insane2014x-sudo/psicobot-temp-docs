# 📋 2026-04-20 - Fase 1: Prueba Piloto

**Fecha:** 20 Abril 2026  
**Proyecto:** Psicobot  
**Fase:** 1 - Prueba Piloto  
**Estado:** 🟡 En progreso

## 🎯 Objetivo del Día
Completar instalación de herramientas necesarias y ejecutar primera prueba de concepto de transcripción psicológica automatizada.

## 📊 Checklist Instalación

### **Sección 1: Verificación Sistema Base**
- [ ] WSL2 con Ubuntu funcionando
- [ ] Memoria RAM suficiente (16GB+ disponible)
- [ ] Espacio disco (50GB+ libre en WSL)
- [ ] Acceso a archivos Windows (`/mnt/c/Users/`)

### **Sección 2: Herramientas Base (WSL)**
- [ ] Python 3.10+ instalado (`python3 --version`)
- [ ] pip3 funcionando (`pip3 --version`)
- [ ] Git instalado (`git --version`)
- [ ] FFmpeg instalado (`ffmpeg -version`)
- [ ] SQLite3 instalado (`sqlite3 --version`)

### **Sección 3: IA Local**
- [ ] Ollama funcionando (`ollama --version`)
- [ ] Modelo qwen2.5-coder disponible (`ollama list`)
- [ ] Whisper instalado (`whisper --help` o `pip3 show openai-whisper`)

### **Sección 4: Office & Formatos**
- [ ] Microsoft Word disponible (para plantillas .docx)
- [ ] Permisos de escritura en `/mnt/c/Users/[Usuario]/`
- [ ] Audio de prueba disponible (formato .mp3 o .wav)

## 🕐 Estimación de Tiempo
| Tarea | Tiempo estimado | Tiempo real | Diferencia |
|-------|----------------|-------------|------------|
| Verificación sistema | 15 min | | |
| Instalación herramientas | 45 min | | |
| Configuración IA | 30 min | | |
| Prueba concepto | 60 min | | |
| **Total** | **2h 30min** | | |

## 📝 Notas & Observaciones

### **Comandos de verificación:**
```bash
# En WSL, ejecutar para verificar:
echo "=== VERIFICACIÓN SISTEMA ==="
uname -a
python3 --version
pip3 --version
git --version
ffmpeg -version 2>/dev/null || echo "FFmpeg NO instalado"
sqlite3 --version 2>/dev/null || echo "SQLite3 NO instalado"
ollama list
echo "=== FIN VERIFICACIÓN ==="
```

### **Comandos de instalación (si falta algo):**
```bash
# Instalar dependencias faltantes:
sudo apt update
sudo apt install -y python3-pip git ffmpeg sqlite3

# Instalar Whisper:
pip3 install openai-whisper

# Verificar Whisper:
python3 -c "import whisper; print('✅ Whisper instalado')"
```

## 🔗 Enlaces Relacionados
- [[Psicobot-Home]] - Página principal
- [[PLAN]] - Plan de 6 semanas (Fase 1: Semanas 1-2)
- [[FLUJO_TRABAJO]] - Diagrama de flujo objetivo
- [[REQUISITOS]] - Especificaciones técnicas

## 👥 Responsabilidades

### **XeatBoss:**
- [ ] Ejecutar comandos de verificación
- [ ] Instalar dependencias faltantes
- [ ] Probar acceso a archivos Windows
- [ ] Preparar audio de prueba (sin datos reales)
- [ ] Documentar problemas encontrados

### **ClawXeatJr:**
- [ ] Guiar paso a paso instalación
- [ ] Proporcionar soluciones a problemas
- [ ] Crear script demo de transcripción
- [ ] Verificar funcionamiento conjunto

## 🎮 Próximos Pasos (si todo funciona)
1. Ejecutar script demo transcripción
2. Procesar audio de prueba
3. Verificar formato psicológico automático
4. Documentar resultados y tiempo ahorrado

## 🚨 Puntos Críticos
1. **FFmpeg es ESSENCIAL** para procesamiento audio
2. **Whisper requiere Python 3.10+**
3. **Ollama debe estar corriendo** (`ollama serve`)
4. **Audio prueba debe ser** .mp3 o .wav, claro, sin ruido excesivo

## 📈 Métricas del Día
- **Herramientas instaladas:** 0/10
- **Tiempo total instalación:** 0h 0min
- **Problemas resueltos:** 0
- **Prueba concepto exitosa:** No

---
**Checklist creado:** 19 Abril 2026  
**Para actualizar:** Marcar checkboxes conforme se completen  
**Siguiente paso:** Completar instalación y ejecutar [[Script-Demo-Transcripcion]]