# crear_excel_ejemplo.py
import pandas as pd
import os

print("📊 CREANDO EXCEL DE EJEMPLO PARA IMPORTACIÓN")
print("=" * 50)

# Datos de ejemplo (similares a tu trabajo psicológico)
datos = [
    {
        'EXPEDIENTE': '2026-00123-PE',
        'INICIALES': 'A.B.C.',
        'FECHA': '15/04/2026',
        'JUEZ': 'JUEZ MARIA PEREZ GARCIA',
        'TIPO_PERSONA': 'Agraviado',
        'EDAD': 35,
        'TIPO_DELITO': 'Robo agravado',
        'LUGAR': 'La Merced, Chanchamayo'
    },
    {
        'EXPEDIENTE': '2026-00124-PE',
        'INICIALES': 'X.Y.Z.',
        'FECHA': '16/04/2026',
        'JUEZ': 'JUEZ CARLOS GOMEZ LOPEZ',
        'TIPO_PERSONA': 'Denunciado',
        'EDAD': 42,
        'TIPO_DELITO': 'Lesiones leves',
        'LUGAR': 'San Ramón, Junín'
    },
    {
        'EXPEDIENTE': '2026-00125-PE',
        'INICIALES': 'M.N.O.',
        'FECHA': '17/04/2026',
        'JUEZ': 'JUEZ ANA LOPEZ MARTINEZ',
        'TIPO_PERSONA': 'Testigo',
        'EDAD': 28,
        'TIPO_DELITO': 'Amenazas',
        'LUGAR': 'Pichanaki, Junín'
    },
    {
        'EXPEDIENTE': '2026-00126-PE',
        'INICIALES': 'P.Q.R.',
        'FECHA': '18/04/2026',
        'JUEZ': 'JUEZ LUIS MARTINEZ RODRIGUEZ',
        'TIPO_PERSONA': 'Agraviado',
        'EDAD': 51,
        'TIPO_DELITO': 'Hurto simple',
        'LUGAR': 'Perené, Junín'
    },
    {
        'EXPEDIENTE': '2026-00127-PE',
        'INICIALES': 'S.T.U.',
        'FECHA': '19/04/2026',
        'JUEZ': 'JUEZ ROSA DIAZ FERNANDEZ',
        'TIPO_PERSONA': 'Denunciado',
        'EDAD': 33,
        'TIPO_DELITO': 'Estafa',
        'LUGAR': 'Chanchamayo, Junín'
    }
]

# Crear DataFrame
df = pd.DataFrame(datos)

# Guardar como Excel
nombre_archivo = 'ejemplo_importacion.xlsx'
df.to_excel(nombre_archivo, index=False, sheet_name='DATOS')

print(f"✅ Excel creado: {nombre_archivo}")
print(f"📊 Estructura: {len(df)} filas, {len(df.columns)} columnas")
print("\n📋 COLUMNAS DISPONIBLES:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i:2d}. {col}")

print("\n📄 CONTENIDO DEL EXCEL:")
print("=" * 80)
print(df.to_string(index=False))

print("\n🎯 INSTRUCCIONES:")
print("1. Este archivo está listo para importar")
print("2. Ejecuta: python importar_excel.py")
print("3. Se importarán 5 registros de ejemplo")
print("4. Luego puedes probar en tu aplicación")

# Verificar que se creó
if os.path.exists(nombre_archivo):
    size_kb = os.path.getsize(nombre_archivo) / 1024
    print(f"\n📁 Archivo creado: {size_kb:.1f} KB")
    print("✅ Listo para usar!")
else:
    print("❌ Error: No se pudo crear el archivo")