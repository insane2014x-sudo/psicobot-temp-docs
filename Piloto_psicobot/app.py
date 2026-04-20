import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os


class AplicacionPiloto:

    def __init__(self):
        # 1. Crear una ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Aplicacion Piloto v1.0")
        self.ventana.geometry("800x800")
        # SI NO QUEREMOS QUE NO EXPANDA LA PANTALLA
        # self.ventana.resizable(width=False, height=False)

        #2. Configurar color de fondo
        self.ventana.config(bg="#f0f0f0")

        #3. Inicializar a la base de datos
        self.inicializar_base_datos()

        #4.Crear interfaz
        self.crear_interfaz()

    def inicializar_base_datos(self):
        """Crea la base de datos SQLite si no existe"""
        try:
            self.conexion = sqlite3.connect("piloto.db")
            self.cursor = self.conexion.cursor()

            #Crear tabla si no existe
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS citas_piloto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expediente TEXT NOT NULL,
            iniciales_persona TEXT NOT NULL,
            fecha DATE NOT NULL,
            nombre_juez TEXT NOT NULL,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            self.conexion.commit()
            print("Base de datos creado exitosamente")
        except Exception as e:
            print(f"❌ Error en base de datos: {e}")

    def crear_interfaz(self):

        #TITULO
        titulo = tk.Label(
            self.ventana,
            text="📋 SISTEMA PSICOBOT - PILOTO",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#444444",
        )
        titulo.pack(pady=10)

        #SUBTITULO
        subtitulo = tk.Label(
            self.ventana,
            text="Ingrese los datos de la cita psicológica:",
            font = ("Arial", 10),
            bg="#f0f0f0",
            fg="#666666"
        )
        subtitulo.pack(pady=10)

        # MARCO PARA LOS CAMPOS
        marco_campos = tk.Frame(self.ventana, bg="#f0f0f0")
        marco_campos.pack(pady=10, fill="both", expand=True)


        # SEPARADOR
        separador = ttk.Separator(marco_campos, orient="horizontal")
        separador.grid(row=8, column=0, columnspan=2, pady=20, sticky="ew")

        # BÚSQUEDA POR EXPEDIENTE
        marco_busqueda = tk.Frame(marco_campos, bg="#f0f0f0")
        marco_busqueda.grid(row=9, column=0, columnspan=2, pady=10)

        tk.Label(
            marco_busqueda,
            text="🔍 Buscar por expediente:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        ).pack(side="left", padx=(0, 10))

        self.campo_busqueda = tk.Entry(
            marco_busqueda,
            width=20,
            font=("Arial", 10)
        )
        self.campo_busqueda.pack(side="left", padx=(0, 10))

        boton_buscar = tk.Button(
            marco_busqueda,
            text="BUSCAR",
            font=("Arial", 9, "bold"),
            bg="#FF9800",  # Naranja
            fg="white",
            command=self.buscar_expediente
        )
        boton_buscar.pack(side="left")
        print("✅ Sistema de búsqueda agregado")

        # ================= SECCIÓN 1: DATOS BÁSICOS =================
        seccion1 = tk.LabelFrame(
            marco_campos,
            text=" 📋 DATOS BÁSICOS",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0",
            fg="#2E7D32",  # Verde oscuro
            relief="ridge",
            borderwidth=2
        )
        seccion1.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # 1. CAMPO EXPEDIENTE
        etiqueta_expediente = tk.Label(
            seccion1,
            text="📄 Expediente:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_expediente.grid(row=0, column=0, padx=15, pady=8, sticky="w")

        self.campo_expediente = tk.Entry(
            seccion1,
            width=35,
            font=("Arial", 10)
        )
        self.campo_expediente.grid(row=0, column=1, padx=15, pady=8)

        # 2. CAMPO INICIALES PERSONA
        etiqueta_iniciales = tk.Label(
            seccion1,
            text="👤 Iniciales persona:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_iniciales.grid(row=1, column=0, padx=15, pady=8, sticky="w")

        self.campo_iniciales = tk.Entry(
            seccion1,
            width=35,
            font=("Arial", 10)
        )
        self.campo_iniciales.grid(row=1, column=1, padx=15, pady=8)

        # 3. CAMPO FECHA
        etiqueta_fecha = tk.Label(
            seccion1,
            text="📅 Fecha (DD/MM/AAAA):",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_fecha.grid(row=2, column=0, padx=15, pady=8, sticky="w")

        self.campo_fecha = tk.Entry(
            seccion1,
            width=35,
            font=("Arial", 10)
        )
        self.campo_fecha.grid(row=2, column=1, padx=15, pady=8)

        # 4. CAMPO NOMBRE JUEZ
        etiqueta_juez = tk.Label(
            seccion1,
            text="⚖️ Nombre de juez:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_juez.grid(row=3, column=0, padx=15, pady=8, sticky="w")

        self.campo_juez = tk.Entry(
            seccion1,
            width=35,
            font=("Arial", 10)
        )
        self.campo_juez.grid(row=3, column=1, padx=15, pady=8)

        # ================= SECCIÓN 2: DATOS DE PERSONA =================
        seccion2 = tk.LabelFrame(
            marco_campos,
            text=" 👤 DATOS DE PERSONA",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0",
            fg="#1565C0",  # Azul
            relief="ridge",
            borderwidth=2
        )
        seccion2.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # 5. CAMPO TIPO DE PERSONA (DROPDOWN)
        etiqueta_tipo = tk.Label(
            seccion2,
            text="👥 Tipo de persona:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_tipo.grid(row=0, column=0, padx=15, pady=8, sticky="w")
        self.campo_tipo = ttk.Combobox(
            seccion2,
            values=["Agraviado", "Denunciado", "Testigo", "Otro"],
            width=32,
            font=("Arial", 10),
            state="readonly"
        )
        self.campo_tipo.grid(row=0, column=1, padx=15, pady=8)
        self.campo_tipo.current(0)

        # 6. CAMPO EDAD
        etiqueta_edad = tk.Label(
            seccion2,
            text="🔢 Edad:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_edad.grid(row=1, column=0, padx=15, pady=8, sticky="w")

        self.campo_edad = tk.Entry(
            seccion2,
            width=35,
            font=("Arial", 10)
        )
        self.campo_edad.grid(row=1, column=1, padx=15, pady=8)

        # ================= SECCIÓN 3: DATOS LEGALES =================
        seccion3 = tk.LabelFrame(
            marco_campos,
            text=" ⚖️ DATOS LEGALES",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0",
            fg="#6A1B9A",  # Púrpura
            relief="ridge",
            borderwidth=2
        )
        seccion3.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        # 7. CAMPO TIPO DE DELITO
        etiqueta_delito = tk.Label(
            seccion3,
            text="🔨 Tipo de delito:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_delito.grid(row=0, column=0, padx=15, pady=8, sticky="w")

        self.campo_delito = tk.Entry(
            seccion3,
            width=35,
            font=("Arial", 10)
        )
        self.campo_delito.grid(row=0, column=1, padx=15, pady=8)

        # 8. CAMPO LUGAR
        etiqueta_lugar = tk.Label(
            seccion3,
            text="📍 Lugar:",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        etiqueta_lugar.grid(row=1, column=0, padx=15, pady=8, sticky="w")

        self.campo_lugar = tk.Entry(
            seccion3,
            width=35,
            font=("Arial", 10)
        )
        self.campo_lugar.grid(row=1, column=1, padx=15, pady=8)

        print("✅ Interfaz organizada en 3 secciones")


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
        boton_guardar.grid(row=6, column=0, columnspan=2, pady=30)

        # BOTÓN VER DATOS
        boton_ver = tk.Button(
            marco_campos,
            text="👁️ VER DATOS GUARDADOS",
            font=("Arial", 10),
            bg="#2196F3",  # Azul
            fg="white",
            padx=15,
            pady=5,
            command=self.mostrar_datos_guardados
        )
        boton_ver.grid(row=7, column=0, columnspan=2, pady=10)

        self.etiqueta_mensaje = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.etiqueta_mensaje.pack(pady=10)

    def guardar_datos(self):
        """Obtiene datos de los campos y guarda en base de datos"""
        print("🔄 Intentando guardar datos...")

        # 1. Obtener datos de los campos (AGREGAR NUEVOS)
        expediente = self.campo_expediente.get().strip()
        iniciales = self.campo_iniciales.get().strip()
        fecha = self.campo_fecha.get().strip()
        juez = self.campo_juez.get().strip()
        tipo_persona = self.campo_tipo.get().strip()
        edad_texto = self.campo_edad.get().strip()
        tipo_delito = self.campo_delito.get().strip()
        lugar = self.campo_lugar.get().strip()

        # 2. Validar que todos los campos tengan datos (AGREGAR NUEVOS)
        campos_requeridos = [expediente, iniciales, fecha, juez, tipo_persona]
        if any(not campo for campo in campos_requeridos):
            self.mostrar_mensaje("❌ Por favor, complete todos los campos requeridos", "red")
            return

        # 3. Validar formato de fecha (simple)
        if not self.validar_fecha(fecha):
            self.mostrar_mensaje("❌ Formato de fecha inválido. Use DD/MM/AAAA", "red")
            return

        # 4. Validar edad (si se ingresó)
        edad = None
        if edad_texto:
            try:
                edad = int(edad_texto)
                if edad < 0 or edad > 120:
                    self.mostrar_mensaje("❌ Edad debe estar entre 0 y 120", "red")
                    return
            except ValueError:
                self.mostrar_mensaje("❌ Edad debe ser un número", "red")
                return

        try:
            # 5. Insertar en base de datos (ACTUALIZADO CON NUEVOS CAMPOS)
            self.cursor.execute("""
                        INSERT INTO citas_piloto 
                        (expediente, iniciales_persona, fecha, nombre_juez, 
                         tipo_persona, edad, tipo_delito, lugar)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """, (expediente, iniciales, fecha, juez,
                          tipo_persona, edad, tipo_delito, lugar))
            self.conexion.commit()

            # 6. Mostrar mensaje de éxito
            self.mostrar_mensaje(f"✅ Datos guardados: {expediente} - {tipo_persona}", "green")

            # 7. Limpiar campos para nueva entrada
            self.limpiar_campos()

            print(f"✅ Datos guardados en base de datos: {expediente} ({tipo_persona})")

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
        def limpiar_campos(self):
            """Limpia todos los campos de entrada"""
            self.campo_expediente.delete(0, tk.END)
            self.campo_iniciales.delete(0, tk.END)
            self.campo_fecha.delete(0, tk.END)
            self.campo_juez.delete(0, tk.END)
            self.campo_edad.delete(0, tk.END)
            self.campo_delito.delete(0, tk.END)  # NUEVO
            self.campo_lugar.delete(0, tk.END)  # NUEVO
            self.campo_tipo.current(0)

        # Poner foco en primer campo
        self.campo_expediente.focus_set()

    def mostrar_datos_guardados(self):
        """Muestra una ventana con todos los datos guardados"""
        try:
            # Obtener todos los registros
            self.cursor.execute("SELECT * FROM citas_piloto ORDER BY fecha_creacion DESC")
            registros = self.cursor.fetchall()

            if not registros:
                messagebox.showinfo("Datos Guardados", "No hay datos guardados aún.")
                return

            # Crear ventana nueva
            ventana_datos = tk.Toplevel(self.ventana)
            ventana_datos.title("📊 Datos Guardados - Psicobot Piloto")
            ventana_datos.geometry("1200x400")  # Más ancho para nuevos campos
            ventana_datos.configure(bg="#f0f0f0")

            # Título
            tk.Label(
                ventana_datos,
                text=f"📋 TOTAL REGISTROS: {len(registros)}",
                font=("Arial", 14, "bold"),
                bg="#f0f0f0",
                fg="#333333"
            ).pack(pady=10)

            # Marco para tabla
            marco_tabla = tk.Frame(ventana_datos, bg="white")
            marco_tabla.pack(pady=10, padx=10, fill="both", expand=True)

            # ENCABEZADOS ACTUALIZADOS (10 columnas)
            encabezados = ["ID", "Expediente", "Iniciales", "Fecha", "Juez", "Creado", "Persona", "Edad", "Delito",
                           "Lugar"]
            anchos = [5, 15, 10, 12, 20, 12, 8, 15, 15, 20]  # Anchos personalizados

            for i, (encabezado, ancho) in enumerate(zip(encabezados, anchos)):
                tk.Label(
                    marco_tabla,
                    text=encabezado,
                    font=("Arial", 9, "bold"),
                    bg="#4CAF50",
                    fg="white",
                    width=ancho,
                    relief="ridge"
                ).grid(row=0, column=i, padx=1, pady=1, sticky="nsew")

            # DATOS (manejar posibles valores None en nuevos campos)
            for fila_idx, registro in enumerate(registros, start=1):
                for col_idx, valor in enumerate(registro):
                    color_fondo = "#E8F5E9" if fila_idx % 2 == 0 else "#FFFFFF"

                    # Formatear valor (manejar None)
                    texto = str(valor) if valor is not None else ""

                    # Acortar texto largo para mejor visualización
                    if col_idx in [4, 7, 8]:  # Juez, Delito, Lugar
                        if len(texto) > 15:
                            texto = texto[:12] + "..."

                    tk.Label(
                        marco_tabla,
                        text=texto,
                        font=("Arial", 8),
                        bg=color_fondo,
                        fg="#333333",
                        width=anchos[col_idx],
                        relief="ridge",
                        anchor="w"
                    ).grid(row=fila_idx, column=col_idx, padx=1, pady=1, sticky="nsew")

            # Botón cerrar
            tk.Button(
                ventana_datos,
                text="CERRAR",
                font=("Arial", 10, "bold"),
                bg="#f44336",
                fg="white",
                command=ventana_datos.destroy
            ).pack(pady=10)

            print(f"✅ Mostrando {len(registros)} registros con {len(encabezados)} columnas")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los datos:\n{str(e)}")
            print(f"❌ Error mostrando datos: {e}")

    def buscar_expediente(self):
        """Busca registros por número de expediente"""
        texto_busqueda = self.campo_busqueda.get().strip()

        if not texto_busqueda:
            self.mostrar_mensaje("❌ Ingrese un expediente para buscar", "red")
            return

        try:
            # Buscar expedientes que contengan el texto
            self.cursor.execute("""
                                SELECT *
                                FROM citas_piloto
                                WHERE expediente LIKE ?
                                ORDER BY fecha_creacion DESC
                                """, (f"%{texto_busqueda}%",))

            resultados = self.cursor.fetchall()

            if not resultados:
                messagebox.showinfo("Búsqueda", f"No se encontraron expedientes con: '{texto_busqueda}'")
                return

            # Mostrar resultados en ventana similar
            ventana_resultados = tk.Toplevel(self.ventana)
            ventana_resultados.title(f"🔍 Resultados búsqueda: '{texto_busqueda}'")
            ventana_resultados.geometry("900x300")
            ventana_resultados.configure(bg="#f0f0f0")

            # Título
            tk.Label(
                ventana_resultados,
                text=f"🔍 RESULTADOS: {len(resultados)} registros encontrados",
                font=("Arial", 12, "bold"),
                bg="#f0f0f0",
                fg="#333333"
            ).pack(pady=10)

            # Marco para tabla
            marco_tabla = tk.Frame(ventana_resultados, bg="white")
            marco_tabla.pack(pady=10, padx=10, fill="both", expand=True)

            # Encabezados (solo campos principales)
            encabezados = ["Expediente", "Iniciales", "Fecha", "Juez", "Tipo", "Edad"]

            for i, encabezado in enumerate(encabezados):
                tk.Label(
                    marco_tabla,
                    text=encabezado,
                    font=("Arial", 9, "bold"),
                    bg="#FF9800",  # Naranja para resultados
                    fg="white",
                    width=15,
                    relief="ridge"
                ).grid(row=0, column=i, padx=1, pady=1, sticky="nsew")

            # Datos
            for fila_idx, registro in enumerate(resultados, start=1):
                # Tomar solo campos relevantes: expediente, iniciales, fecha, juez, tipo_persona, edad
                datos_relevantes = [registro[1], registro[2], registro[3], registro[4],
                                    registro[6] if registro[6] else "",
                                    registro[7] if registro[7] else ""]

                for col_idx, valor in enumerate(datos_relevantes):
                    color_fondo = "#FFF3E0" if fila_idx % 2 == 0 else "#FFFFFF"
                    tk.Label(
                        marco_tabla,
                        text=str(valor),
                        font=("Arial", 9),
                        bg=color_fondo,
                        fg="#333333",
                        width=15,
                        relief="ridge",
                        anchor="w"
                    ).grid(row=fila_idx, column=col_idx, padx=1, pady=1, sticky="nsew")

                    print(f"✅ Búsqueda completada: {len(resultados)} resultados para '{texto_busqueda}'")

        except Exception as e:
            messagebox.showerror("Error", f"Error en búsqueda:\n{str(e)}")
            print(f"❌ Error en búsqueda: {e}")

    def ejecutar(self):
        # Este metodo es necesario para iniciar el bucle de la interfaz
        self.ventana.mainloop()

if __name__ == "__main__":
    print("🚀 INICIANDO APLICACIÓN PSICOBOT PILOTO")
    print("=" * 40)
    app = AplicacionPiloto()
    app.ejecutar()