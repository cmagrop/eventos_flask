from flask import Flask
#Importar Events Controllers
from controllers.events_controller import init_event_routes
#Pendiente la importacion de User Controllers
from controllers.users_controller import init_user_routes

app = Flask(__name__,template_folder="views")
app.secret_key="clave_secreta"

#Inicializar controladores
init_user_routes(app)
init_event_routes(app) 

if __name__ == '__main__':
    app.run(debug=True)