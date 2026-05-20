import pymysql
from datetime import datetime, timedelta

class CafeteriaModel:
    def __init__(self):
        self.config = {"host": "localhost", "user": "root", "password": "", "db": "cafeteria_escolar"}

    def conectar(self):
        return pymysql.connect(**self.config)

    def ejecutar_query(self, query, params=None):
        conn = self.conectar()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, params)
        if query.upper().startswith("SELECT"):
            res = cursor.fetchall()
            conn.close()
            return res
        conn.commit()
        conn.close()

    def obtener_rango_semanal(self):
        hoy = datetime.now().date()
        lunes = hoy - timedelta(days=hoy.weekday())
        viernes = lunes + timedelta(days=4)
        return lunes, viernes

    def obtener_resurtidos_domingo(self):
        # Consulta específica para los gastos de domingos
        return self.ejecutar_query("SELECT SUM(monto) as total FROM movimientos WHERE tipo='Gasto' AND DAYOFWEEK(fecha)=1")
    

    def obtener_ultimos_movimientos(self, limite=30):
    # Trae los últimos movimientos sin importar la fecha
        query = "SELECT * FROM movimientos ORDER BY fecha DESC LIMIT %s"
        return self.ejecutar_query(query, (limite,))

    def limpiar_historial_completo(self):
    # Borra todos los datos de la tabla de la base de datos
        return self.ejecutar_query("TRUNCATE TABLE movimientos")
    
    def limpiar_historial_completo(self):
        # TRUNCATE es el comando SQL para vaciar una tabla por completo
        return self.ejecutar_query("TRUNCATE TABLE movimientos")