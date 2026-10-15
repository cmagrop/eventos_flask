from datetime import datetime, date
from flask import flash
from config.mysqlconnection import connectMySQL

DB = 'db_eventos' #varible global
class Event:
    def __init__(self,data):
        self.id = data.get('id')
        self.event_name = data.get('event_name')
        self.location = data.get('location')
        self.event_date = data.get('event_date')
        self.details = data.get('details')
        self.user_id = data.get('user_id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
    @classmethod
    def obtener_todos_eventos_con_organizadores(cls):
        query="""
        select e.*,u.first_name as name,u.last_name as last_name
        from events e
        join users u  on e.user_id= u.id
        order by e.event_date asc
        """
        results = connectMySQL(DB).query_db(query)
        events=[]
        if results: #si existen resultados
            for row in results: #row: fila
                events.append(cls(row))#cls(row)<->Event(row)
        return events        
    @classmethod
    def ObtenerIdsVinculadosEventoUsuario(cls,data):
        query = """
        select event_id
        from users_events
        where user_id=%(user_id)s 
        """
        results = connectMySQL(DB).query_db(query,data)
        ids_agrupados=[]
        if results:
            for row in results:
                ids_agrupados.append(row['event_id'])
            return ids_agrupados       
        
    @classmethod
    def guardar(cls,data):
        query="""
        insert into events(event_name,location,event_date,details,user_id)
        values(%(event_name)s,%(location)s,%(event_date)s,%(details)s,%(user_id)s)
        """
        event_id= connectMySQL(DB).query_db(query,data)
        #llamando método para unir anfitrion con evento
        cls.unirAnfitrionEvento({'user_id':data['user_id'],'event_id':event_id})
        return event_id

    @classmethod
    def unirAnfitrionEvento(cls,data):
        query="""insert into users_events
        (user_id,event_id)
        values(%(user_id)s,%(event_id)s);
        """
        return connectMySQL(DB).query_db(query,data)

   #obtener informacion en base al id del evento
   # actualizar evento
   # eliminar evento     


    


    
            
