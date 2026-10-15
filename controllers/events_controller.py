from flask import render_template,request,redirect,url_for,session
from models.event_model import Event

def init_event_routes(app):
    @app.route("/events")
    def dashboard():
        if 'user_id' not in session:
            return redirect(url_for('index'))
        # en caso que no entre al if
        user_id = session['user_id']#capturar la sesion
        events= Event.obtener_todos_eventos_con_organizadores()
        ids_vinculados_evento =Event.ObtenerIdsVinculadosEventoUsuario({'user_id':user_id})
        return render_template('dashboard.html',
                               events=events,
                               ids_vinculados_evento=ids_vinculados_evento
                               )
