from flask import Flask
from controllers.movie_controller import movie_bp
from infrastructure.database import db
#from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('infrastructure.config.Config')

# Inicializar CORS
#CORS(app)

# Inicializar la base de datos
db.init_app(app)

# Registrar blueprints
app.register_blueprint(movie_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
