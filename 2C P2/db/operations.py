import psycopg2 as psq 

DB_NAME = "Librería"
DB_USER = "postgres"
DB_PASSWORD = "12345"   
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psq.connect(
            dbname = DB_NAME,
            user = DB_USER,
            password = DB_PASSWORD,
            host = DB_HOST,
            port = DB_PORT,
)
cursor =conn.cursor()

"Creal clienye recibe un diccionario con name, email, password, adress y phone y devielve una tupla, donde el primer parametro es el estado y el segundo ekl mensaaje"
def crear_usuario(data:dict): 
    if not data["name"] or not data ["email"] or not data["password"]:
       return (False, "nombre,  correo y contraseña son obligatorios ")
    
    try :
        cursor.execute("INSERT INTO usuarios (Nombre, correo, password, direccion, telefono) VALUES (%s,%s,%s,%s,%s)" , (data["name"], data["email"], data["password"], data["address"], data["phone"]))
        conn.commit()
        return (True, "El usuario se registro con exito")
    except Exception as e:
       print(e)
    return (False, "Ocurruo un error al guardar el usuario")


def update_client(client_id, updated_data):
    #Validacion pendiente
    cursor.execute("UPDATE clientes SET nombre=%s, telefono=%s, direcciones=%s, password=%s where id=%s",  (updated_data["name"], updated_data["phone"], updated_data["address"], updated_data["password"], client_id)) 
    conn.commit()

def delete_client(client_id):
    cursor.execute("DELETE FROM clientes WHERE id=%s", (client_id)) 
    conn.commit()

def get_all_clients():
    cursor.execute("SELECT * FROM clientes ORDER BY id")
    clientes = cursor.fetchall()
    print  (clientes)
    return clientes

def get_one_client(client_id):
   cursor.execute ("SELECT * FROM clientes where id=%s", (client_id))
   cliente = cursor.fetchone()
   if not cliente:
      return None 
   return cliente