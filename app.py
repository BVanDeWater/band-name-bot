from flask import Flask, render_template, jsonify
import generator

app = Flask(__name__)

# Preload the word list into memory on startup
generator.get_word_list()

@app.route("/")
def index():
    data = generator.generate_tweet()
    return render_template("index.html", data=data)

@app.route("/api/generate")
def api_generate():
    data = generator.generate_tweet()
    return jsonify(data)

@app.route("/api/band")
def api_band():
    return jsonify({"band_name": generator.generate_name()})

@app.route("/api/album")
def api_album():
    return jsonify({"album_name": generator.generate_album()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
