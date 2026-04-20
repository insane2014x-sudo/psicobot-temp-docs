# autocompletado_juez_mejorado.py
# Función inteligente de autocompletado para nombres de jueces - Versión B (Inteligente)

import sqlite3
from tkinter import messagebox

class AutocompletadoJuez:
    """Clase para manejar autocompletado inteligente de jueces"""
    
    def __init__(self, db_path="piloto.db"):
        self.db_path = db_path
        self._timer = None
        self.conexion = None
        self.cursor = None
        
    def conectar_db(self):
        """Conectar a la base de datos"""
        try:
            self.conexion = sqlite3.connect(self.db_path)
            self.cursor = self.conexion.cursor()
            return True
        except Exception as e:
            print(f"❌ Error conectando a DB: {e}")
            return False
    
    def desconectar_db(self):
        """Desconectar de la base de datos"""
        if self.conexion:
            self.conexion.close()
    
    def autocompletar_juez(self, event):
        """
        Función principal de autocompletado - Versión inteligente con debouncing
        
        Características:
        1. Debouncing (evita múltiples llamadas rápidas)
        2. Búsqueda en cualquier parte del nombre
        3. Prioriza resultados que comienzan con el texto
        4. Límite de resultados para mejor rendimiento
        5. Manejo de teclas de navegación
        
        Uso:
        combobox_juez.bind('<KeyRelease>', autocompletador.autocompletar_juez)
        """
        
        # Obtener widget y texto actual
        widget = event.widget
        texto = widget.get().strip().upper()
        
        # Ignorar teclas de navegación y especiales
        teclas_ignorar = {'Up', 'Down', 'Return', 'Escape', 'Tab', 'Shift_L', 'Shift_R', 
                         'Control_L', 'Control_R', 'Alt_L', 'Alt_R', 'Caps_Lock'}
        
        if event.keysym in teclas_ignorar:
            return
        
        # DEBUG (opcional)
        # print(f"🔍 Tecla: {event.keysym}, Texto: '{texto}'")
        
        # Cancelar timer anterior si existe (debouncing)
        if self._timer:
            widget.after_cancel(self._timer)
        
        # Programar autocompletado después de 150ms
        self._timer = widget.after(150, self._ejecutar_autocompletado, widget, texto, event.keysym)
        
        return "break"  # Detener propagación del evento
    
    def _ejecutar_autocompletado(self, widget, texto, tecla):
        """Ejecuta el autocompletado después del delay de debouncing"""
        
        # Conectar a DB si no está conectado
        if not self.conexion:
            if not self.conectar_db():
                return
        
        # Si texto vacío o muy corto, mostrar todos
        if not texto or len(texto) < 2:
            self._mostrar_todos_jueces(widget)
            return
        
        # Si es tecla de borrar, no mostrar lista
        if tecla in ('BackSpace', 'Delete'):
            return
        
        try:
            # ESTRATEGIA 1: Buscar jueces que COMIENCEN con el texto (prioridad alta)
            self.cursor.execute("""
                SELECT nombre_completo FROM jueces 
                WHERE activo = 1 AND nombre_completo LIKE ? 
                ORDER BY 
                    CASE 
                        WHEN nombre_completo LIKE ? THEN 1  -- Exact match al inicio
                        ELSE 2
                    END,
                    nombre_completo
                LIMIT 8
            """, (f'{texto}%', f'{texto}'))
            
            resultados = [row[0] for row in self.cursor.fetchall()]
            
            # ESTRATEGIA 2: Si pocos resultados, buscar en cualquier parte del nombre
            if len(resultados) < 5 and len(texto) > 2:
                self.cursor.execute("""
                    SELECT nombre_completo FROM jueces 
                    WHERE activo = 1 AND nombre_completo LIKE ? 
                    AND nombre_completo NOT LIKE ?
                    ORDER BY nombre_completo
                    LIMIT 5
                """, (f'%{texto}%', f'{texto}%'))
                
                resultados_adicionales = [row[0] for row in self.cursor.fetchall()]
                resultados.extend(resultados_adicionales)
            
            # ESTRATEGIA 3: Búsqueda por palabras individuales (para nombres compuestos)
            if len(resultados) < 3 and ' ' in texto:
                palabras = texto.split()
                for palabra in palabras:
                    if len(palabra) > 2:
                        self.cursor.execute("""
                            SELECT nombre_completo FROM jueces 
                            WHERE activo = 1 AND nombre_completo LIKE ? 
                            AND nombre_completo NOT IN ({})
                            ORDER BY nombre_completo
                            LIMIT 3
                        """.format(','.join(['?']*len(resultados))), 
                        (f'%{palabra}%', *resultados))
                        
                        mas_resultados = [row[0] for row in self.cursor.fetchall()]
                        for juez in mas_resultados:
                            if juez not in resultados:
                                resultados.append(juez)
            
            # Actualizar valores del Combobox
            widget['values'] = resultados
            
            # Mostrar lista desplegable si hay resultados
            if resultados:
                # Pequeño delay adicional para mejor UX
                widget.after(50, lambda: self._mostrar_lista(widget))
            
            # DEBUG (opcional)
            # print(f"🔍 Encontrados {len(resultados)} jueces para '{texto}'")
            
        except Exception as e:
            print(f"❌ Error en autocompletado: {e}")
    
    def _mostrar_todos_jueces(self, widget):
        """Muestra todos los jueces activos"""
        try:
            self.cursor.execute("""
                SELECT nombre_completo FROM jueces 
                WHERE activo = 1 
                ORDER BY nombre_completo
                LIMIT 20
            """)
            
            todos_jueces = [row[0] for row in self.cursor.fetchall()]
            widget['values'] = todos_jueces
            
        except Exception as e:
            print(f"❌ Error mostrando todos los jueces: {e}")
    
    def _mostrar_lista(self, widget):
        """Muestra la lista desplegable del Combobox"""
        try:
            widget.event_generate('<Down>')
        except:
            pass
    
    def actualizar_lista_jueces(self, widget):
        """Actualiza la lista completa de jueces en el widget"""
        self._mostrar_todos_jueces(widget)
    
    def agregar_nuevo_juez(self, nombre_juez, especialidad=None, ventana_padre=None):
        """Agrega un nuevo juez a la base de datos"""
        if not nombre_juez:
            if ventana_padre:
                messagebox.showwarning("Campo vacío", "Ingrese un nombre de juez para agregar.", parent=ventana_padre)
            return False
        
        try:
            self.cursor.execute("""
                INSERT OR IGNORE INTO jueces (nombre_completo, especialidad) 
                VALUES (?, ?)
            """, (nombre_juez.upper(), especialidad))
            
            self.conexion.commit()
            
            if ventana_padre:
                messagebox.showinfo("✅ Juez agregado", 
                                  f"Juez '{nombre_juez}' agregado exitosamente.", 
                                  parent=ventana_padre)
            
            print(f"✅ Nuevo juez agregado: {nombre_juez} ({especialidad})")
            return True
            
        except Exception as e:
            if ventana_padre:
                messagebox.showerror("Error", 
                                   f"No se pudo agregar el juez:\n{str(e)}", 
                                   parent=ventana_padre)
            print(f"❌ Error agregando juez: {e}")
            return False
    
    def obtener_jueces(self, limite=50):
        """Obtiene lista de todos los jueces activos"""
        try:
            self.cursor.execute("""
                SELECT nombre_completo, especialidad 
                FROM jueces 
                WHERE activo = 1 
                ORDER BY nombre_completo
                LIMIT ?
            """, (limite,))
            
            return self.cursor.fetchall()
        except Exception as e:
            print(f"❌ Error obteniendo jueces: {e}")
            return []

# Función de conveniencia para uso rápido
def crear_autocompletador(db_path="piloto.db"):
    """Crea y configura un autocompletador listo para usar"""
    return AutocompletadoJuez(db_path)

# Ejemplo de uso
if __name__ == "__main__":
    print("🧪 TESTEO DE AUTOCOMPLETADO DE JUEZ")
    print("=" * 50)
    
    # Crear autocompletador
    autocompletador = crear_autocompletador()
    
    if autocompletador.conectar_db():
        # Obtener y mostrar jueces
        jueces = autocompletador.obtener_jueces(10)
        print(f"✅ Conectado a base de datos")
        print(f"📋 Jueces disponibles ({len(jueces)}):")
        for nombre, especialidad in jueces:
            print(f"   👨‍⚖️ {nombre} ({especialidad})")
        
        autocompletador.desconectar_db()
    else:
        print("❌ No se pudo conectar a la base de datos")
    
    print("\n🎯 Instrucciones de uso:")
    print("1. Importar: from autocompletado_juez_mejorado import crear_autocompletador")
    print("2. Crear instancia: autocompletador = crear_autocompletador('piloto.db')")
    print("3. Conectar: autocompletador.conectar_db()")
    print("4. Enlazar evento: combobox.bind('<KeyRelease>', autocompletador.autocompletar_juez)")
    print("5. Para agregar juez: autocompletador.agregar_nuevo_juez('NOMBRE', 'ESPECIALIDAD')")