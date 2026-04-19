#!/usr/bin/env python3
"""
Generador simplificado para Windows - Psicobot
Versión que funciona en TU PC
"""

from docxtpl import DocxTemplate
import os
from datetime import datetime

def main():
    print("🖨️  GENERADOR DE DOCUMENTOS PSICOBOT - WINDOWS")
    print("=" * 50)
    
    # RUTAS EN TU WINDOWS - AJUSTA SEGÚN NECESITES
    # Opción A: Usar plantilla de prueba simple (recomendado primero)
    plantilla_path = "plantilla_prueba_simple.docx"
    
    # Opción B: Usar tu plantilla real (si la copiaste)
    # plantilla_path = "A.A.A.A---46e0dd0d-4e26-47a5-aa90-d6fbe89963d7.docx"
    
    # Directorio de salida
    output_dir = "documentos_generados"
    os.makedirs(output_dir, exist_ok=True)
    
    # Verificar que existe la plantilla
    if not os.path.exists(plantilla_path):
        print(f"❌ Error: No se encuentra la plantilla: {plantilla_path}")
        print("\n📁 Archivos en tu carpeta actual:")
        for archivo in os.listdir('.'):
            if archivo.endswith('.docx'):
                print(f"  • {archivo}")
        print("\n💡 Copia tu plantilla a esta carpeta o ajusta la ruta.")
        return
    
    print(f"📄 Plantilla encontrada: {plantilla_path}")
    
    # Contexto de ejemplo (datos ficticios)
    contexto = {
        'EXPEDIENTE': '2026-00123-PE',
        'FECHA': datetime.now().strftime('%d/%m/%Y'),
        'HORA_INICIO': '09:00:00',
        'HORA_TERMINO': '10:30:00',
        'NOMBRE_JUEZ': 'DR. JUAN PÉREZ GARCÍA',
        'NOMBRE_FISCAL_PENAL': 'FISCAL MARÍA LÓPEZ RUIZ',
        'NOMBRE_FISCAL_FAMILIA': 'FISCAL CARLOS MARTÍNEZ SOTO',
        'NOMBRE_PSICOLOGA': 'PSIC. ANA TORRES VARGAS',
        'NOMBRE_ABOGADO': 'ABG. ROBERTO DÍAZ MENDIETA',
        'NOMBRE_AGRAVIADO': 'MARÍA PÉREZ RAMÍREZ',
        'DNI_AGRAVIADO': '87654321',
        'EDAD_AGRAVIADO': '32',
        'SEXO_AGRAVIADO': 'FEMENINO',
        'NOMBRE_DENUNCIADO': 'MANUEL GUTIÉRREZ ROJAS',
        'TIPO_DELITO': 'VIOLENCIA FAMILIAR',
        'TIPO_PARTICIPACION': 'VÍCTIMA',
        'VINCULO': 'EX PAREJA',
        'TIPO_DEFENSA': 'DEFENSORÍA PÚBLICA',
    }
    
    # Nombre del archivo de salida
    output_path = os.path.join(output_dir, f"Acta_Entrevista_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx")
    
    try:
        print(f"🔧 Cargando plantilla y rellenando {len(contexto)} campos...")
        doc = DocxTemplate(plantilla_path)
        doc.render(contexto)
        
        print(f"💾 Guardando documento: {output_path}")
        doc.save(output_path)
        
        if os.path.exists(output_path):
            tamano = os.path.getsize(output_path)
            print(f"\n✅ ¡DOCUMENTO GENERADO EXITOSAMENTE!")
            print(f"📍 Ubicación: {output_path}")
            print(f"📏 Tamaño: {tamano:,} bytes ({tamano/1024:.1f} KB)")
            
            # Mostrar contenido breve
            print("\n📝 Vista previa (primeras líneas):")
            from docx import Document
            doc_leido = Document(output_path)
            for i, para in enumerate(doc_leido.paragraphs[:5], 1):
                if para.text.strip():
                    print(f"  {i}. {para.text[:80]}{'...' if len(para.text) > 80 else ''}")
            
            print(f"\n🎯 ¡SISTEMA PSICOBOT FUNCIONANDO EN TU WINDOWS!")
            print("🚀 Mañana continuamos con más funcionalidades.")
        else:
            print("❌ Error: Documento no se guardó correctamente")
            
    except Exception as e:
        print(f"❌ Error generando documento: {e}")
        import traceback
        traceback.print_exc()
        
        print("\n🔧 POSIBLES SOLUCIONES:")
        print("1. Verifica que la plantilla sea .docx válido")
        print("2. Asegúrate de tener permisos de escritura")
        print("3. Prueba con plantilla_prueba_simple.docx primero")

if __name__ == "__main__":
    main()