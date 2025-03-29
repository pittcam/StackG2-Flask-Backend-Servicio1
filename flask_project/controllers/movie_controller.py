from flask import Blueprint, request, jsonify


movie_bp = Blueprint('movies', __name__)
movie_service = ()

@movie_bp.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    movie = movie_service.add_movie(data['title'], data['genre'], data['tmdb_id'], data['user_id'])
    return jsonify({"message": f"Película {movie.title} agregada"}), 201
