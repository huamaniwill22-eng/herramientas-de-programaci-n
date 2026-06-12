import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

class AppReservaBus:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reserva de Pasajes - BusExpress")
        self.root.geometry("750x600")
        self.root.configure(bg="#f0f2f5")
        
        # Estado de la aplicación
        self.precio_por_asiento = 45.0
        self.asientos_seleccionados = set()
        
        # Simulación de asientos ocupados (puedes cambiar estos números)
        self.asientos_ocupados = {3, 7, 8, 12, 19, 20, 24}
        
        self.crear_estilos()
        self.crear_widgets()

    def crear_estilos(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Configuración de colores principales
        self.style.configure("TLabel", background="#f0f2f5", foreground="#333333", font=("Segoe UI", 10))
        self.style.configure("Titulo.TLabel", font=("Segoe UI", 16, "bold"), foreground="#1a3a5f")
        self.style.configure("Subtitulo.TLabel", font=("Segoe UI", 12, "bold"), foreground="#1a3a5f")
        self.style.configure("TFrame", background="#f0f2f5")
        
        # Estilo de botones
        self.style.configure("TButton", font=("Segoe UI", 10, "bold"), borderwidth=1)
        self.style.configure("Reservar.TButton", background="#28a745", foreground="white")
        self.style.map("Reservar.TButton", background=[("active", "#218838")])

    def crear_widgets(self):
        # ------------------ ENCABEZADO ------------------
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill="x", padx=20, top=True, pady=15)
        
        titulo = ttk.Label(header_frame, text="🚌 RESERVA DE PASAJES DE AUTOBÚS", style="Titulo.TLabel")
        titulo.pack(side="left")

        # ------------------ PANEL DE DATOS (Izquierda) ------------------
        left_frame = ttk.Frame(self.root, padding=10)
        left_frame.pack(side="left", fill="y", padx=20, pady=10)
        
        ttk.Label(left_frame, text="Datos del Viaje", style="Subtitulo.TLabel").pack(anchor="w", pady=(0, 15))
        
        # Origen
        ttk.Label(left_frame, text="Origen:").pack(anchor="w")
        self.combo_origen = ttk.Combobox(left_frame, values=["Lima", "Cusco", "Arequipa", "Trujillo"], state="readonly", width=22)
        self.combo_origen.pack(fill="x", pady=(0, 10))
        self.combo_origen.current(0)
        
        # Destino
        ttk.Label(left_frame, text="Destino:").pack(anchor="w")
        self.combo_destino = ttk.Combobox(left_frame, values=["Cusco", "Lima", "Puno", "Tacna"], state="readonly", width=22)
        self.combo_destino.pack(fill="x", pady=(0, 10))
        self.combo_destino.current(0)
        
        # Fecha (Simulada con opciones de los próximos días)
        ttk.Label(left_frame, text="Fecha de Viaje:").pack(anchor="w")
        hoy = datetime.now()
        fechas_proximas = [(hoy + timedelta(days=i)).strftime("%d/%m/%Y") for i in range(1, 6)]
        self.combo_fecha = ttk.Combobox(left_frame, values=fechas_proximas, state="readonly", width=22)
        self.combo_fecha.pack(fill="x", pady=(0, 20))