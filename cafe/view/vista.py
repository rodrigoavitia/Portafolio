import customtkinter as ctk
from tkinter import ttk, messagebox

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class CafeteriaView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Sistema Cafetería - Panel de Control")
        self.geometry("1000x700")

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- BARRA LATERAL ---
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="☕ GESTIÓN", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=30)
        
        self.entry_monto = ctk.CTkEntry(self.sidebar, placeholder_text="Monto $", height=45, font=("Arial", 16))
        self.entry_monto.pack(pady=10, padx=20, fill="x")

        self.btn_ganancia = ctk.CTkButton(self.sidebar, text="＋ GANANCIA", fg_color="#28a745", height=50, 
                                         font=("Arial", 14, "bold"), command=lambda: self.controller.guardar("Ganancia"))
        self.btn_ganancia.pack(pady=10, padx=20, fill="x")

        self.btn_gasto = ctk.CTkButton(self.sidebar, text="－ GASTO", fg_color="#dc3545", height=50, 
                                       font=("Arial", 14, "bold"), command=lambda: self.controller.guardar("Gasto"))
        self.btn_gasto.pack(pady=10, padx=20, fill="x")

        ctk.CTkButton(self.sidebar, text="SALIR", fg_color="#444", command=self.quit).pack(side="bottom", pady=20)

        # --- PANEL PRINCIPAL ---
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)

        # Resúmenes Grandes
        self.frame_top = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.frame_top.pack(fill="x")

        self.card_dia = ctk.CTkFrame(self.frame_top, fg_color="#1f538d")
        self.card_dia.pack(side="left", expand=True, fill="both", padx=5)
        self.lbl_dia = ctk.CTkLabel(self.card_dia, text="Hoy: $0.00", font=ctk.CTkFont(size=28, weight="bold"))
        self.lbl_dia.pack(pady=25)

        self.card_sem = ctk.CTkFrame(self.frame_top)
        self.card_sem.pack(side="left", expand=True, fill="both", padx=5)
        self.lbl_sem = ctk.CTkLabel(self.card_sem, text="Semana: $0.00", font=ctk.CTkFont(size=18))
        self.lbl_sem.pack(pady=25)

        # --- TABLA DE MOVIMIENTOS ---
        ctk.CTkLabel(self.main_frame, text="Movimientos Recientes", font=("Arial", 16, "bold")).pack(pady=(20, 5), anchor="w")
        
        # Estilo de la tabla
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", 
                        rowheight=45, font=("Arial", 14)) # Filas altas y letra grande
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"), background="#3b3b3b", foreground="white")
        style.map("Treeview", background=[('selected', '#1f538d')])

        self.tabla = ttk.Treeview(self.main_frame, columns=("ID", "Tipo", "Monto", "Fecha"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Tipo", text="TIPO")
        self.tabla.heading("Monto", text="MONTO")
        self.tabla.heading("Fecha", text="HORA")
        
        self.tabla.column("ID", width=80, anchor="center")
        self.tabla.column("Tipo", width=150, anchor="center")
        self.tabla.column("Monto", width=150, anchor="center")
        self.tabla.column("Fecha", width=200, anchor="center")
        self.tabla.pack(fill="both", expand=True)

        # Botones de Acción abajo
        self.actions = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.actions.pack(fill="x", pady=15)
        ctk.CTkButton(self.actions, text="✏️ Editar Monto", width=150, command=self.controller.modificar).pack(side="left", padx=5)
        ctk.CTkButton(self.actions, text="🗑️ Eliminar", width=150, fg_color="#a11", command=self.controller.eliminar).pack(side="left", padx=5)

        self.btn_limpiar = ctk.CTkButton(
            self.actions, 
            text="⚠️ Limpiar Todo", 
            fg_color="#555", 
            hover_color="#333",
            command=self.controller.limpiar_todo
        )
        self.btn_limpiar.pack(side="right", padx=5)