from model.modelo import CafeteriaModel
from view.vista import CafeteriaView
from tkinter import messagebox
from datetime import datetime

class CafeteriaController:
    def __init__(self):
        self.model = CafeteriaModel()
        self.view = CafeteriaView(self)
        self.actualizar_todo()

    def guardar(self, tipo):
        monto = self.view.entry_monto.get()
        try:
            val = float(monto)
            self.model.ejecutar_query("INSERT INTO movimientos (tipo, monto) VALUES (%s, %s)", (tipo, val))
            self.actualizar_todo()
            self.view.entry_monto.delete(0, 'end')
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido")

    def eliminar(self):
        selected = self.view.tabla.selection()
        if not selected: return
        id_mov = self.view.tabla.item(selected)['values'][0]
        if messagebox.askyesno("Eliminar", "¿Seguro que quieres borrar este registro?"):
            self.model.ejecutar_query("DELETE FROM movimientos WHERE id=%s", (id_mov,))
            self.actualizar_todo()

    def modificar(self):
        selected = self.view.tabla.selection()
        if not selected: return
        id_mov = self.view.tabla.item(selected)['values'][0]
        nuevo_monto = self.view.entry_monto.get()
        try:
            val = float(nuevo_monto)
            self.model.ejecutar_query("UPDATE movimientos SET monto=%s WHERE id=%s", (val, id_mov))
            self.actualizar_todo()
        except ValueError:
            messagebox.showinfo("Info", "Escribe el nuevo monto en el cuadro de texto")

    def actualizar_todo(self):
        # 1. Traemos los últimos 30 movimientos (sin importar el día)
        movs = self.model.obtener_ultimos_movimientos(30)
        
        # Limpiamos la tabla visual
        self.view.tabla.delete(*self.view.tabla.get_children())
        
        # Variables para sumar lo que hay en el tablero actual
        total_ganancias = 0
        total_gastos = 0
        
        for r in movs:
            # Insertamos en la tabla
            self.view.tabla.insert("", "end", values=(r['id'], r['tipo'], f"${r['monto']:.2f}", r['fecha']))
            
            # Sumamos TODO lo que se ve en la tabla para el saldo del tablero
            if r['tipo'] == 'Ganancia':
                total_ganancias += float(r['monto'])
            else:
                total_gastos += float(r['monto'])
        
        # Actualizamos el recuadro azul con el saldo de los movimientos visibles
        saldo_tablero = total_ganancias - total_gastos
        self.view.lbl_dia.configure(text=f"Saldo en Tablero: ${saldo_tablero:,.2f}")

        # 2. El recuadro de la derecha sigue mostrando el acumulado de la semana escolar
        ini, fin = self.model.obtener_rango_semanal()
        s = self.model.ejecutar_query(
            "SELECT tipo, SUM(monto) as total FROM movimientos WHERE DATE(fecha) BETWEEN %s AND %s GROUP BY tipo", 
            (ini, fin)
        )
        
        res_s = {i['tipo']: float(i['total']) for i in s}
        gan_s = res_s.get('Ganancia', 0)
        gas_s = res_s.get('Gasto', 0)
        
        self.view.lbl_sem.configure(text=f"Semana (Lun-Vie)\nNeto: ${gan_s - gas_s:,.2f}")


    def limpiar_todo(self):
        # Preguntamos para evitar accidentes
        confirmacion = messagebox.askyesno(
            "⚠️ ¡ADVERTENCIA!", 
            "¿Estás seguro de que quieres borrar TODO el historial de la base de datos?\nEsta acción no se puede deshacer."
        )
        
        if confirmacion:
            try:
                # Llamamos al modelo para vaciar la tabla
                self.model.limpiar_historial_completo()
                # Refrescamos la pantalla (ahora todo saldrá en $0.00)
                self.actualizar_todo()
                messagebox.showinfo("Éxito", "El historial ha sido vaciado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo limpiar la base de datos: {e}")

                
if __name__ == "__main__":
    app = CafeteriaController()
    app.view.mainloop()