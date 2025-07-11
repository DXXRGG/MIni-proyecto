from db.db import conn

sql_chema = """
CREATE TABLE IF NOT EXISTS 
Usuarios (
   id SERIAL PRIMARY KEY, 
   Nombre VARCHAR(100) NOT NULL,
   Correo VARCHAR(100) NOT NULL,
   Password VARCHAR(100) NOT NULL,
   direccion TEXT NOT NULL,
   telefono VARCHAR(100),
   fecha_regisstro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

def inicia_db():
    try:
        cursor = conn.cursor()
        cursor.execute(sql_chema)
        conn.commit()
        print("Tablas creadas con exito")
    except Exception as e:
        print(e)
