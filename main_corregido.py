"""
Interfaz principal FLET para GD-XEAT Pro - VERSIÓN CORREGIDA
"""

import flet as ft
from datetime import datetime
import sys
import os

# Agregar src al path para imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.config import config
from core.database import init_db, get_session


class GDXeatApp:
    """Aplicación principal GD-XEAT Pro"""
    
    def __init__(self):
        self.page = None
        self.session = None
        self.current_tab = 0
        
        # Inicializar base de datos
        self._init_database()
    
    def _init_database(self):
        """Inicializar base de datos"""
        try:
            init_db()
            self.session = get_session()
            print("✅ Base de datos conectada")
            return True
        except Exception as e:
            print(f"❌ Error conectando a base de datos: {e}")
            return False
    
    def build(self, page: ft.Page):
        """Construir interfaz principal"""
        self.page = page
        
        # Configurar página
        page.title = f"{config.APP_NAME} v{config.APP_VERSION}"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window_width = config.UI_WIDTH
        page.window_height = config.UI_HEIGHT
        page.window_min_width = 800
        page.window_min_height = 600
        page.padding = 20
        
        # Barra de navegación superior
        app_bar = ft.AppBar(
            title=ft.Text(config.APP_NAME, size=24, weight=ft.FontWeight.BOLD),
            center_title=False,
            bgcolor=ft.colors.BLUE_700,
            color=ft.colors.WHITE,
            actions=[
                ft.IconButton(ft.icons.NOTIFICATIONS_OUTLINED, on_click=self._show_notifications),
                ft.IconButton(ft.icons.SETTINGS_OUTLINED, on_click=self._show_settings),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Acerca de", on_click=self._show_about),
                        ft.PopupMenuItem(),  # Separador
                        ft.PopupMenuItem(text="Salir", on_click=self._exit_app),
                    ]
                )
            ]
        )
        
        # Contenido principal con pestañas
        self.tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="📅 Calendario",
                    icon=ft.icons.CALENDAR_TODAY_OUTLINED,
                    content=self._build_calendario_tab(),
                ),
                ft.Tab(
                    text="📁 Expedientes",
                    icon=ft.icons.FOLDER_OPEN_OUTLINED,
                    content=self._build_expedientes_tab(),
                ),
                ft.Tab(
                    text="📝 Documentos",
                    icon=ft.icons.DESCRIPTION_OUTLINED,
                    content=self._build_documentos_tab(),
                ),
                ft.Tab(
                    text="📬 Oficios",
                    icon=ft.icons.MAIL_OUTLINED,
                    content=self._build_oficios_tab(),
                ),
                ft.Tab(
                    text="📊 Dashboard",
                    icon=ft.icons.DASHBOARD_OUTLINED,
                    content=self._build_dashboard_tab(),
                ),
            ],
            expand=True,
        )
        
        # Barra de estado inferior
        status_bar = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("✅ Sistema listo", size=12),
                    ft.VerticalDivider(),
                    ft.Text(f"Usuario: XeatBOSS", size=12),
                    ft.VerticalDivider(),
                    ft.Text(f"Base de datos: Conectada", size=12),
                    ft.VerticalDivider(),
                    ft.Text(f"{datetime.now().strftime('%d/%m/%Y %H:%M')}", size=12),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=10,
            bgcolor=ft.colors.GREY_100,
            border_radius=ft.border_radius.all(5),
        )
        
        # Layout principal
        page.add(app_bar)
        page.add(self.tabs)
        page.add(status_bar)
        
        # Actualizar cada minuto
        page.on_interval = 60000  # 60 segundos
        page.update()
    
    def _build_calendario_tab(self):
        """Construir pestaña de calendario"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("📅 Calendario de Audiencias", size=20, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Text("En construcción...", size=16),
                    ft.Text("Próximamente: Visualización de audiencias programadas por día/semana/mes"),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=20,
            alignment=ft.alignment.center,
        )
    
    def _build_expedientes_tab(self):
        """Construir pestaña de expedientes"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("📁 Gestión de Expedientes", size=20, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    
                    # Barra de búsqueda
                    ft.Row(
                        controls=[
                            ft.TextField(
                                label="Buscar expediente",
                                hint_text="Número, materia, delito...",
                                width=400,
                                prefix_icon=ft.icons.SEARCH_OUTLINED,
                            ),
                            ft.ElevatedButton(
                                "Buscar",
                                icon=ft.icons.SEARCH_OUTLINED,
                                on_click=self._buscar_expediente,
                            ),
                            ft.ElevatedButton(
                                "Nuevo Expediente",
                                icon=ft.icons.ADD_OUTLINED,
                                bgcolor=ft.colors.GREEN,
                                color=ft.colors.WHITE,
                                on_click=self._nuevo_expediente,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    
                    # Lista de expedientes
                    ft.Container(
                        content=ft.Text("Lista de expedientes aparecerá aquí..."),
                        padding=20,
                        border=ft.border.all(1, ft.colors.GREY_300),
                        border_radius=ft.border_radius.all(5),
                        expand=True,
                    ),
                ],
                spacing=20,
                expand=True,
            ),
            padding=20,
            expand=True,
        )
    
    def _build_documentos_tab(self):
        """Construir pestaña de documentos"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("📝 Gestión de Documentos", size=20, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Text("En construcción...", size=16),
                    ft.Text("Próximamente: Generación de actas, oficios, cadenas de custodia"),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=20,
            alignment=ft.alignment.center,
        )
    
    def _build_oficios_tab(self):
        """Construir pestaña de oficios"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("📬 Gestión de Oficios", size=20, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    ft.Text("En construcción...", size=16),
                    ft.Text("Próximamente: Oficios entrantes/salientes, seguimiento, plantillas"),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=20,
            alignment=ft.alignment.center,
        )
    
    def _build_dashboard_tab(self):
        """Construir pestaña de dashboard"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("📊 Dashboard del Sistema", size=20, weight=ft.FontWeight.BOLD),
                    ft.Divider(),
                    
                    # Métricas rápidas
                    ft.Row(
                        controls=[
                            self._build_metric_card("📅 Audiencias Hoy", "0", ft.colors.BLUE),
                            self._build_metric_card("📁 Expedientes Activos", "0", ft.colors.GREEN),
                            self._build_metric_card("📝 Documentos Pendientes", "0", ft.colors.ORANGE),
                            self._build_metric_card("📬 Oficios Sin Responder", "0", ft.colors.RED),
                        ],
                        spacing=20,
                    ),
                    
                    # Gráficos/estadísticas
                    ft.Container(
                        content=ft.Text("Estadísticas y gráficos aparecerán aquí..."),
                        padding=20,
                        border=ft.border.all(1, ft.colors.GREY_300),
                        border_radius=ft.border_radius.all(5),
                        expand=True,
                    ),
                ],
                spacing=20,
                expand=True,
            ),
            padding=20,
            expand=True,
        )
    
    def _build_metric_card(self, title: str, value: str, color: str):
        """Construir tarjeta de métrica"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(title, size=14, color=ft.colors.GREY_700),
                    ft.Text(value, size=32, weight=ft.FontWeight.BOLD, color=color),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.GREY_300),
            border_radius=ft.border_radius.all(10),
            width=200,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.colors.GREY_300,
            ),
        )
    
    # Métodos de eventos
    def _show_notifications(self, e):
        """Mostrar notificaciones"""
        self.page.show_snack_bar(
            ft.SnackBar(ft.Text("No hay notificaciones nuevas"))
        )
    
    def _show_settings(self, e):
        """Mostrar configuración"""
        self.page.show_snack_bar(
            ft.SnackBar(ft.Text("Configuración - En construcción"))
        )
    
    def _show_about(self, e):
        """Mostrar información acerca de"""
        about_dialog = ft.AlertDialog(
            title=ft.Text(f"{config.APP_NAME}"),
            content=ft.Column(
                controls=[
                    ft.Text(f"Versión: {config.APP_VERSION}"),
                    ft.Text(f"Descripción: {config.APP_DESCRIPTION}"),
                    ft.Text("Desarrollado por: ClawXeatJr (soporte técnico)"),
                    ft.Text("Usuario: XeatBOSS"),
                    ft.Text(f"Fecha: {datetime.now().strftime('%d/%m/%Y')}"),
                ],
                tight=True,
                spacing=10,
            ),
            actions=[
                ft.TextButton("Cerrar", on_click=lambda e: self.page.close(about_dialog)),
            ],
        )
        self.page.open(about_dialog)
    
    def _exit_app(self, e):
        """Salir de la aplicación"""
        if self.session:
            self.session.close()
        self.page.window_close()
    
    def _buscar_expediente(self, e):
        """Buscar expediente"""
        self.page.show_snack_bar(
            ft.SnackBar(ft.Text("Búsqueda de expedientes - En construcción"))
        )
    
    def _nuevo_expediente(self, e):
        """Crear nuevo expediente"""
        self.page.show_snack_bar(
            ft.SnackBar(ft.Text("Crear nuevo expediente - En construcción"))
        )


def main(page: ft.Page):
    """Función principal de la aplicación"""
    app = GDXeatApp()
    app.build(page)


if __name__ == "__main__":
    print(f"🚀 INICIANDO {config.APP_NAME} v{config.APP_VERSION}")
    print("=" * 50)
    
    # Inicializar directorios
    config.inicializar_directorios()
    
    # Ejecutar aplicación FLET
    ft.app(
        target=main,
        view=ft.AppView.FLET_APP,
        assets_dir="assets",
    )