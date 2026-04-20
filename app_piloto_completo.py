# app.py - Psicobot Piloto - Iteración 1
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class AplicacionPiloto:
    def __init__(self):
        # 1. Crear ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Psicobot - Piloto v1.0")
        self.ventana.geometry("500x400")
        
        # 2. Configurar color de fondo
        self.ventana.configure(bg="#f0f0f0")
        
        # 3. Inicializar base de datos
        self.inicializar_base_datos()
        
        # 4. Crear interfaz
        self.crear_interfaz()
        
        print("✅ Ventana creada - Lista para mostrar")

    def inicializar_base_datos(self):
        """Crea la base de datos SQLite si no existe"""
        try:
            self.conexion = sqlite3.connect("piloto.db")
            self.cursor = self.conexion.cursor()
            
            # Crear tabla si no existe
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS citas_piloto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    expediente TEXT NOT NULL,
                    iniciales_persona TEXT NOT NULL,
                    fecha TEXT NOT NULL,
                    nombre_juez TEXT NOT NULL,
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            self.conexion.commit()
            print("✅ Base de datos 'piloto.db' creada/inicializada")
            
        except Exception as e:
            print(f"❌ Error en base de datos: {e}")

    def crear_interfaz(self):
        """Crea todos los elementos de la interfaz"""
        # Título
        titulo = tk.Label(
            self.ventana,
            text="📋 SISTEMA PSICOBOT - PILOTO",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        titulo.pack(pady=20)
        
        # Subtítulo
        subtitulo = tk.Label(
            self.ventana,
            text="Ingrese los datos de la cita psicológica",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666666"
        )
        subtitulo.pack(pady=5)
        
        # MARCO PARA LOS CAMPOS
        marco_campos = tk.Frame(self.ventana, bg="#f0f0f0")
        marco_campos.pack(pady=20)
        
        # 1. CAMPO EXPEDIENTE
        etiqueta_expediente = tk.Label(
            marco_campos,
            text="📄 Expediente:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_expediente.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.campo_expediente = tk.Entry(
            marco_campos,
            width=30,
            font=("Arial", 10)
        )
        self.campo_expediente.grid(row=0, column=1, padx=10, pady=10)
        
        # 2. CAMPO INICIALES PERSONA
        etiqueta_iniciales = tk.Label(
            marco_campos,
            text="👤 Iniciales persona:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_iniciales.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.campo_iniciales = tk.Entry(
            marco_campos,
            width=30,
            font=("Arial", 10)
        )
        self.campo_iniciales.grid(row=1, column=1, padx=10, pady=10)
        
        # 3. CAMPO FECHA
        etiqueta_fecha = tk.Label(
            marco_campos,
            text="📅 Fecha (DD/MM/AAAA):",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_fecha.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        self.campo_fecha = tk.Entry(
            marco_campos,
            width=30,
            font=("Arial", 10)
        )
        self.campo_fecha.grid(row=2, column=1, padx=10, pady=10)
        
        # 4. CAMPO NOMBRE JUEZ
        etiqueta_juez = tk.Label(
            marco_campos,
            text="⚖️ Nombre de juez:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_juez.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        self.campo_juez = tk.Entry(
            marco_campos,
            width=30,
            font=("Arial", 10)
        )
        self.campo_juez.grid(row=3, column=1, padx=10, pady=10)
        
        # BOTÓN GUARDAR
        boton_guardar = tk.Button(
            marco_campos,
            text="💾 GUARDAR DATOS",
            font=("Arial", 11, "bold"),
            bg="#4CAF50",  # Verde
            fg="white",
            padx=20,
            pady=10,
            command=self.guardar_datos
        )
        boton_guardar.grid(row=4, column=0, columnspan=2, pady=30)
        
        # ETIQUETA PARA MENSAJES
        self.etiqueta_mensaje = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.etiqueta_mensaje.pack(pady=10)
        
        print("✅ Interfaz completa creada")

    def guardar_datos(self):
        """Obtiene datos de los campos y guarda en base de datos"""
        print("🔄 Intentando guardar datos...")
        
        # 1. Obtener datos de los campos
        expediente = self.campo_expediente.get().strip()
        iniciales = self.campo_iniciales.get().strip()
        fecha = self.campo_fecha.get().strip()
        juez = self.campo_juez.get().strip()
        
        # 2. Validar que todos los campos tengan datos
        if not expediente or not iniciales or not fecha or not juez:
            self.mostrar_mensaje("❌ Por favor, complete todos los campos", "red")
            return
        
        # 3. Validar formato de fecha (simple)
        if not self.validar_fecha(fecha):
            self.mostrar_mensaje("❌ Formato de fecha inválido. Use DD/MM/AAAA", "red")
            return
        
        try:
            # 4. Insertar en base de datos
            self.cursor.execute("""
                INSERT INTO citas_piloto (expediente, iniciales_persona, fecha, nombre_juez)
                VALUES (?, ?, ?, ?)
            """, (expediente, iniciales, fecha, juez))
            
            self.conexion.commit()
            
            # 5. Mostrar mensaje de éxito
            self.mostrar_mensaje(f"✅ Datos guardados: {expediente} - {iniciales}", "green")
            
            # 6. Limpiar campos para nueva entrada
            self.limpiar_campos()
            
            print(f"✅ Datos guardados en base de datos: {expediente}")
            
        except Exception as e:
            self.mostrar_mensaje(f"❌ Error al guardar: {str(e)}", "red")
            print(f"❌ Error en base de datos: {e}")

    def mostrar_mensaje(self, texto, color):
        """Muestra un mensaje en la interfaz"""
        self.etiqueta_mensaje.config(text=texto, fg=color)
        
        # Si es éxito, limpiar mensaje después de 3 segundos
        if color == "green":
            self.ventana.after(3000, lambda: self.etiqueta_mensaje.config(text=""))

    def validar_fecha(self, fecha_str):
        """Valida formato simple de fecha DD/MM/AAAA"""
        try:
            partes = fecha_str.split("/")
            if len(partes) != 3:
                return False
            dia, mes, anio = map(int, partes)
            
            # Validaciones básicas
            if dia < 1 or dia > 31:
                return False
            if mes < 1 or mes > 12:
                return False
            if anio < 2000 or anio > 2100:
                return False
                
            return True
        except:
            return False

    def limpiar_campos(self):
        """Limpia todos los campos de entrada"""
        self.campo_expediente.delete(0, tk.END)
        self.campo_iniciales.delete(0, tk.END)
        self.campo_fecha.delete(0, tk.END)
        self.campo_juez.delete(0, tk.END)
        
        # Poner foco en primer campo
        self.campo_expediente.focus_set()

    def ejecutar(self):
        """Inicia la aplicación"""
        self.ventana.mainloop()

# Punto de entrada del programa
if __name__ == "__main__":
    print("🚀 INICIANDO APLICACIÓN PSICOBOT PILOTO")
    print("=" * 40)
    
    app = AplicacionPiloto()
    app.ejecutar()