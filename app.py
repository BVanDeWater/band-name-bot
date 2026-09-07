from flask import Flask, Blueprint, render_template, jsonify
import generator

# Initialize Blueprint
band_name_bot_bp = Blueprint(
    "band_name_bot",
    __name__,
    template_folder="templates"
)
bp = band_name_bot_bp  # Convenient shorthand alias

# Preload word list into memory
generator.get_word_list()

@band_name_bot_bp.route("/")
def index():
    data = generator.generate_tweet()
    return render_template("index.html", data=data)

@band_name_bot_bp.route("/api/generate")
def api_generate():
    data = generator.generate_tweet()
    return jsonify(data)

@band_name_bot_bp.route("/api/band")
def api_band():
    return jsonify({"band_name": generator.generate_name()})

@band_name_bot_bp.route("/api/album")
def api_album():
    return jsonify({"album_name": generator.generate_album()})

def create_app():
    """Application factory for running standalone."""
    app = Flask(__name__)
    app.register_blueprint(band_name_bot_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
