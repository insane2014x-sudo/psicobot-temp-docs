import sqlite3
import os

def actualizar_base_datos():
    """Agrega nuevas columnas a la tabla existente"""

    print("🔄 ACTUALIZANDO BASE DE DATOS...")
    print("=" * 40)

    # Verificar si existe la base de datos
    if not os.path.exists("piloto.db"):
        print("❌ No se encuentra piloto.db")
        print("   Ejecuta primero la aplicación para crearla.")
        return
    try:
        conexion = sqlite3.connect("piloto.db")
        cursor = conexion.cursor()
        # Verificar estructura actual
        cursor.execute("PRAGMA table_info(citas_piloto)")
        columnas_actuales = [col[1] for col in cursor.fetchall()]
        print(f"📊 Columnas actuales: {columnas_actuales}")

        # Agregar nuevas columnas si no existen
        nuevas_columnas = [
            ("tipo_persona", "TEXT"),
            ("edad", "INTEGER"),
            ("tipo_delito", "TEXT"),
            ("lugar", "TEXT")
        ]

        for columna, tipo in nuevas_columnas:
            if columna not in columnas_actuales:
                print(f"➕ Agregando columna: {columna} ({tipo})")
                cursor.execute(f"ALTER TABLE citas_piloto ADD COLUMN {columna} {tipo}")

        # Verificar estructura final
        cursor.execute("PRAGMA table_info(citas_piloto)")
        columnas_finales = [col[1] for col in cursor.fetchall()]

        print(f"\n✅ Base de datos actualizada")
        print(f"📊 Columnas finales: {columnas_finales}")
        print(f"📈 Total columnas: {len(columnas_finales)}")

        # Contar registros existentes
        cursor.execute("SELECT COUNT(*) FROM citas_piloto")
        total_registros = cursor.fetchone()[0]
        print(f"📋 Registros existentes: {total_registros}")

        conexion.commit()
        conexion.close()

        print("\n🎯 Base de datos lista para nuevos campos")

    except Exception as e:
        print(f"❌ Error actualizando base de datos: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    actualizar_base_datos()