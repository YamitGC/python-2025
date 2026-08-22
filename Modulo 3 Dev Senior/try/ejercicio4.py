"""import asyncio

async def tarea():
    
    try: 
        await asyncio.sleep(1)
    
        raise ValueError("Error en tarea asíncrona")
    
    except ValueError as e:
        print(f"Error capturado en async: {e}")
        
asyncio.run(tarea())"""

import psycopg2

try:
    conn = psycopg2.connect("dbname = empresa user = admin password = 123")
except psycopg2.OperationalError as e:
    print(f"Erroor de conexion contra la BD: {e}")