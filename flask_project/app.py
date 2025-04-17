from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema, QueryType
from ariadne.explorer import ExplorerGraphiQL
from adapters.graphql.schema import type_defs
from adapters.graphql.resolver import mutation
from flask_cors import CORS


# Crear query vacía (obligatoria para el esquema)
query = QueryType()

# Crear el esquema completo
schema = make_executable_schema(type_defs, query, mutation)

# Crear app Flask
app = Flask(__name__)

#CORS(app)
CORS(app, resources={r"/graphql": {"origins": "http://localhost:5173"}})

# Ruta para la interfaz GraphiQL
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return ExplorerGraphiQL().html(None), 200

# Ruta POST para operaciones GraphQL
@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=True
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

