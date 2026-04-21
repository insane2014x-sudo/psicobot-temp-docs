"""
Interfaz FLET integrada con base de datos GD-XEAT Pro - VERSIÓN CORREGIDA
"""

import flet as ft
from datetime import datetime
import sys
import os

# Agregar src al path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.config import config
from core.database_simple import get_session, Expediente, Audiencia


class GDXeatApp:
    def __init__(self):
        self.page = None
        self.session = get_session()
    
    def build(self, page: ft.Page):
        self.page = page
        
        # Configuración
        page.title = f"{config.APP_NAME} v{config.APP_VERSION}"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window_width = config.UI_WIDTH
        page.window_height = config.UI_HEIGHT
        page.padding = 20
        
        # Barra superior
        app_bar = ft.AppBar(
            title=ft.Text(config.APP_NAME, size=24, weight=ft.FontWeight.BOLD),
            center_title=False,
            bgcolor=ft.colors.BLUE_700,
        )
        
        # Pestañas
        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(
                    text="📅 Calendario",
                    content=self._build_calendario_tab(),
                ),
                ft.Tab(
                    text="📁 Expedientes",
                    content=self._build_expedientes_tab(),
                ),
                ft.Tab(
                    text="📊 Dashboard",
                    content=self._build_dashboard_tab(),
                ),
            ],
            expand=True
        )
        
        page.add(app_bar)
        page.add(tabs)
        
        print("✅ GD-XEAT Pro - Sistema listo")
    
    def _build_calendario_tab(self):
        """Pestaña de calendario"""
        # Obtener audiencias de la base de datos
        audiencias = self.session.query(Audiencia).all()
        
        # Crear lista de audiencias
        audiencias_lista = ft.Column(spacing=10)
        
        if audiencias:
            for aud in audiencias:
                audiencias_lista.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text(f"📅 {aud.fecha_hora.strftime('%d/%m/%Y %H:%M')}", 
                                       size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"Sala: {aud.sala} | Estado: {aud.estado}"),
                                ft.Text(f"Observaciones: {aud.observaciones[:50]}..." if aud.observaciones else "Sin observaciones"),
                            ]),
                            padding=15
                        )
                    )
                )
        else:
            audiencias_lista.controls.append(
                ft.Text("No hay audiencias programadas", color=ft.colors.GREY)
            )
        
        return ft.Container(
            content=ft.Column([
                ft.Text("📅 Calendario de Audiencias", size=20, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.ElevatedButton(
                    "➕ Nueva Audiencia",
                    icon=ft.icons.ADD,
                    on_click=self._nueva_audiencia,
                ),
                ft.Container(
                    content=audiencias_lista,
                    padding=20,
                    border=ft.border.all(1, ft.colors.GREY_300),
                    border_radius=ft.border_radius.all(5),
                    expand=True,
                ),
            ], spacing=20),
            padding=20,
            expand=True
        )
    
    def _build_expedientes_tab(self):
        """Pestaña de expedientes"""
        # Obtener expedientes de la base de datos
        expedientes = self.session.query(Expediente).all()
        
        # Crear tabla de expedientes
        rows = []
        for exp in expedientes:
            rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(exp.numero)),
                    ft.DataCell(ft.Text(exp.materia)),
                    ft.DataCell(ft.Text(exp.delito)),
                    ft.DataCell(ft.Text("✅" if exp.activo else "❌")),
                ])
            )
        
        return ft.Container(
            content=ft.Column([
                ft.Text("📁 Gestión de Expedientes", size=20, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.Row([
                    ft.ElevatedButton(
                        "➕ Nuevo Expediente",
                        icon=ft.icons.ADD,
                        on_click=self._nuevo_expediente,
                    ),
                    ft.Text(f"Total: {len(expedientes)} expedientes", 
                           color=ft.colors.BLUE, size=14),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Número")),
                        ft.DataColumn(ft.Text("Materia")),
                        ft.DataColumn(ft.Text("Delito")),
                        ft.DataColumn(ft.Text("Activo")),
                    ],
                    rows=rows,
                ),
            ], spacing=20),
            padding=20,
            expand=True
        )
    
    def _build_dashboard_tab(self):
        """Pestaña de dashboard"""
        # Estadísticas desde base de datos
        total_expedientes = self.session.query(Expediente).count()
        expedientes_activos = self.session.query(Expediente).filter_by(activo=True).count()
        total_audiencias = self.session.query(Audiencia).count()
        
        return ft.Container(
            content=ft.Column([
                ft.Text("📊 Dashboard del Sistema", size=20, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                
                # Métricas
                ft.Row([
                    self._metric_card("📁 Expedientes", total_expedientes, ft.colors.BLUE),
                    self._metric_card("✅ Activos", expedientes_activos, ft.colors.GREEN),
                    self._metric_card("📅 Audiencias", total_audiencias, ft.colors.ORANGE),
                ], spacing=20),
                
                # Información del sistema
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("ℹ️ Información del Sistema", size=16),
                            ft.Divider(height=1),
                            ft.Text(f"Base de datos: {config.DATABASE_FILE.name}"),
                            ft.Text(f"Expedientes cargados: {total_expedientes}"),
                            ft.Text(f"Última actualización: {datetime.now().strftime('%d/%m/%Y %H:%M')}"),
                        ]),
                        padding=20
                    )
                ),
            ], spacing=20),
            padding=20,
            expand=True
        )
    
    def _metric_card(self, title, value, color):
        """Tarjeta de métrica"""
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=14),
                ft.Text(str(value), size=32, weight=ft.FontWeight.BOLD, color=color),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            width=180,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.GREY_300),
            border_radius=ft.border_radius.all(10),
        )
    
    # Métodos de eventos (por implementar)
    def _nueva_audiencia(self, e):
        self.page.show_snack_bar(ft.SnackBar(ft.Text("Nueva audiencia - En construcción")))
    
    def _nuevo_expediente(self, e):
        self.page.show_snack_bar(ft.SnackBar(ft.Text("Nuevo expediente - En construcción")))


def main(page: ft.Page):
    app = GDXeatApp()
    app.build(page)


if __name__ == "__main__":
    print(f"🚀 INICIANDO {config.APP_NAME} v{config.APP_VERSION}")
    print("=" * 50)
    
    # Verificar directorios (ya se crean automáticamente en constructor de Config)
    print(f"📁 Directorio base de datos: {config.DATABASE_DIR}")
    print(f"📄 Archivo base de datos: {config.DATABASE_FILE}")
    
    # Ejecutar aplicación
    ft.app(target=main, view=ft.AppView.FLET_APP)