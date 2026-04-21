"""
Base de datos simplificada para GD-XEAT Pro - VERSIÓN CON IMPORT FIXED
"""

import sys
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# ========== IMPORT CONFIG ==========
# Intentar importar config de diferentes maneras
try:
    # Opción 1: Desde src.core.config
    from src.core.config import config
    print("✅ Config importada desde src.core.config")
except ImportError:
    try:
        # Opción 2: Desde core.config (ejecutando desde src/)
        from core.config import config
        print("✅ Config importada desde core.config")
    except ImportError:
        try:
            # Opción 3: Importar directamente
            import sys
            sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
            from src.core.config import config
            print("✅ Config importada con path modificado")
        except ImportError:
            # Opción 4: Configuración manual
            print("⚠️  No se pudo importar config, usando valores por defecto")
            
            class ConfigManual:
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                DATA_DIR = os.path.join(BASE_DIR, "data")
                DATABASE_DIR = os.path.join(DATA_DIR, "database")
                DATABASE_FILE = os.path.join(DATABASE_DIR, "gdxeat.db")
                DATABASE_URL = f"sqlite:///{DATABASE_FILE}"
                
                def __init__(self):
                    # Crear directorios
                    os.makedirs(self.DATABASE_DIR, exist_ok=True)
            
            config = ConfigManual()

# ========== BASE DE DATOS ==========
Base = declarative_base()
engine = create_engine(config.DATABASE_URL, echo=True)  # echo=True para ver SQL
SessionLocal = sessionmaker(bind=engine)

# ========== MODELOS SIMPLES ==========

class Expediente(Base):
    """Expediente judicial (versión simple)"""
    __tablename__ = "expedientes"
    
    id = Column(Integer, primary_key=True)
    numero = Column(String(100), unique=True, nullable=False)
    materia = Column(String(200))
    delito = Column(String(200))
    fecha_apertura = Column(DateTime, default=datetime.now)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<Expediente {self.numero}>"


class Audiencia(Base):
    """Audiencia programada (versión simple)"""
    __tablename__ = "audiencias"
    
    id = Column(Integer, primary_key=True)
    expediente_id = Column(Integer, nullable=False)  # Simplificado: sin ForeignKey por ahora
    fecha_hora = Column(DateTime, nullable=False)
    sala = Column(String(100))
    estado = Column(String(50), default="programada")  # programada, realizada, cancelada
    observaciones = Column(String(500))
    fecha_creacion = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<Audiencia {self.fecha_hora} - {self.estado}>"


# ========== FUNCIONES ==========

def init_db():
    """Inicializar base de datos (crear tablas)"""
    print("🗄️ INICIALIZANDO BASE DE DATOS...")
    
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    
    print(f"✅ Base de datos creada: {config.DATABASE_FILE}")
    print("📋 Tablas creadas:")
    for table in Base.metadata.tables:
        print(f"  - {table}")
    
    return True


def get_session():
    """Obtener sesión de base de datos"""
    return SessionLocal()


def add_expediente_ejemplo():
    """Agregar expediente de ejemplo para pruebas"""
    session = get_session()
    
    try:
        # Verificar si ya hay datos
        count = session.query(Expediente).count()
        
        if count == 0:
            # Crear expediente de ejemplo
            expediente = Expediente(
                numero="2026-00123-PE",
                materia="Robo agravado",
                delito="Robo",
            )
            
            session.add(expediente)
            session.commit()
            
            print("✅ Expediente de ejemplo creado")
            print(f"   Número: {expediente.numero}")
            print(f"   Materia: {expediente.materia}")
        
        return count
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
        return 0
    
    finally:
        session.close()


if __name__ == "__main__":
    # Prueba de base de datos
    print("🧪 PROBANDO BASE DE DATOS")
    print("=" * 50)
    
    # Inicializar
    init_db()
    
    # Agregar ejemplo
    add_expediente_ejemplo()
    
    # Mostrar información
    session = get_session()
    expedientes = session.query(Expediente).all()
    
    print(f"\n📊 EXPEDIENTES EN BASE DE DATOS: {len(expedientes)}")
    for exp in expedientes:
        print(f"  - {exp.numero}: {exp.materia}")
    
    session.close()
    print("\n✅ Base de datos lista para usar")