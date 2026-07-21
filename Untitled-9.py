import tkinter as tk
from tkinter import ttk


def calcular_pedido(stock_actual, stock_minimo):
    """Calcular la cantidad que debe solicitarse para un artículo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def cargar_datos():
    """Cargar la matriz de inventario con datos de ejemplo."""
    return [
        ["A001", "Teclado", 8, 15],
        ["A002", "Mouse", 25, 20],
        ["A003", "Monitor", 3, 10],
        ["A004", "Disco SSD", 12, 12],
        ["A005", "Memoria RAM", 6, 15],
        ["A006", "Cámara Web", 18, 12],
        ["A007", "Audífonos", 4, 10],
    ]


def auditar_inventario(tree, inventario, resumen_label):
    """Recorrer la matriz de inventario y actualizar la tabla con el estado de cada artículo."""
    for fila in tree.get_children():
        tree.delete(fila)

    total_articulos = len(inventario)
    articulos_con_pedido = 0
    total_unidades_pedir = 0

    for codigo, nombre, stock_actual, stock_minimo in inventario:
        cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)
        if cantidad_pedir > 0:
            estado = "🔴 Reabastecer"
            articulos_con_pedido += 1
            total_unidades_pedir += cantidad_pedir
        else:
            estado = "🟢 Stock suficiente"

        tree.insert(
            "",
            "end",
            values=(
                codigo,
                nombre,
                stock_actual,
                stock_minimo,
                cantidad_pedir,
                estado,
            ),
        )

    resumen = (
        f"Total de artículos: {total_articulos}   "
        f"Artículos con pedido: {articulos_con_pedido}   "
        f"Total de unidades a solicitar: {total_unidades_pedir}"
    )
    resumen_label.config(text=resumen)


def crear_interfaz():
    """Crear la ventana principal y todos los elementos de la interfaz gráfica."""
    root = tk.Tk()
    root.title("Sistema de Auditoría de Inventario")
    root.geometry("900x500")
    root.configure(bg="#eef2f7")
    root.resizable(False, False)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 900) // 2
    y = (screen_height - 500) // 2
    root.geometry(f"900x500+{x}+{y}")

    estilo = ttk.Style(root)
    estilo.theme_use("clam")
    estilo.configure(
        "TFrame",
        background="#eef2f7",
    )
    estilo.configure(
        "TLabel",
        background="#eef2f7",
        font=("Segoe UI", 11),
        foreground="#1f3864",
    )
    estilo.configure(
        "Header.TLabel",
        font=("Segoe UI", 20, "bold"),
        foreground="#0f2959",
        background="#eef2f7",
    )
    estilo.configure(
        "Accent.TButton",
        font=("Segoe UI", 11, "bold"),
        foreground="#ffffff",
        background="#2962ff",
        padding=10,
    )
    estilo.map(
        "Accent.TButton",
        background=[("active", "#1c4bcb"), ("!active", "#2962ff")],
    )
    estilo.configure(
        "Treeview",
        font=("Segoe UI", 10),
        background="#ffffff",
        fieldbackground="#f8f9fc",
        foreground="#1f3864",
    )
    estilo.configure(
        "Treeview.Heading",
        font=("Segoe UI", 10, "bold"),
        background="#dbe4f4",
        foreground="#0f2959",
    )

    encabezado_frame = ttk.Frame(root, padding=(20, 20, 20, 10))
    encabezado_frame.pack(fill="x")

    titulo = ttk.Label(
        encabezado_frame,
        text="Sistema de Auditoría de Inventario",
        style="Header.TLabel",
    )
    titulo.pack(side="left", anchor="w")

    inventario = cargar_datos()

    acciones_frame = ttk.Frame(encabezado_frame)
    acciones_frame.pack(side="right", anchor="e")

    resumen_label = ttk.Label(
        root,
        text="Presione 'Auditar Inventario' para generar el informe.",
        font=("Segoe UI", 11),
        foreground="#2f4f7f",
        background="#eef2f7",
    )
    resumen_label.pack(fill="x", padx=20, pady=(0, 10))

    boton_auditar = ttk.Button(
        acciones_frame,
        text="Auditar Inventario",
        style="Accent.TButton",
        command=lambda: auditar_inventario(tree, inventario, resumen_label),
    )
    boton_auditar.pack()

    contenedor = ttk.Frame(root, padding=20, style="TFrame")
    contenedor.pack(fill="both", expand=True)

    columnas = (
        "codigo",
        "articulo",
        "stock_actual",
        "stock_minimo",
        "cantidad_pedir",
        "estado",
    )
    tree = ttk.Treeview(
        contenedor,
        columns=columnas,
        show="headings",
        height=14,
    )

    tree.heading("codigo", text="Código")
    tree.column("codigo", width=100, anchor="center")
    tree.heading("articulo", text="Artículo")
    tree.column("articulo", width=220, anchor="w")
    tree.heading("stock_actual", text="Stock Actual")
    tree.column("stock_actual", width=110, anchor="center")
    tree.heading("stock_minimo", text="Stock Mínimo")
    tree.column("stock_minimo", width=110, anchor="center")
    tree.heading("cantidad_pedir", text="Cantidad a Pedir")
    tree.column("cantidad_pedir", width=130, anchor="center")
    tree.heading("estado", text="Estado")
    tree.column("estado", width=190, anchor="center")

    estilo.configure("Treeview", rowheight=28)
    estilo.map("Treeview", background=[("selected", "#c9d7ff")])

    scrollbar_vertical = ttk.Scrollbar(
        contenedor,
        orient="vertical",
        command=tree.yview,
    )
    scrollbar_horizontal = ttk.Scrollbar(
        contenedor,
        orient="horizontal",
        command=tree.xview,
    )
    tree.configure(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

    tree.grid(row=0, column=0, sticky="nsew")
    scrollbar_vertical.grid(row=0, column=1, sticky="ns")
    scrollbar_horizontal.grid(row=1, column=0, sticky="ew")

    contenedor.rowconfigure(0, weight=1)
    contenedor.columnconfigure(0, weight=1)

    return root


def main():
    """Inicializar y ejecutar la aplicación."""
    ventana = crear_interfaz()
    ventana.mainloop()


if __name__ == "__main__":
    main()
