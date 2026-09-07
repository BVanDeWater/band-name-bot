# Band Name Bot 🎸

A randomized band name, album name, and promo tweet generator built with Python and Flask.

Available as a reusable **Flask Blueprint** or a standalone application.

## Quickstart

### 1. Installation

```bash
pip install -r requirements.txt
```

### 2. Integrating into an Existing Flask App

Import and register the blueprint into your parent Flask application:

```python
from flask import Flask
from app import band_name_bot_bp  # or 'from app import bp'

app = Flask(__name__)

# Register with an optional prefix
app.register_blueprint(band_name_bot_bp, url_prefix="/band-bot")
```

### 3. Running Standalone

To run the application locally by itself:

```bash
python app.py
```
Open your browser at `http://localhost:5000`.

### 4. Blueprint Routes & Endpoints

When mounted at a prefix (e.g. `/band-bot`):
- `GET /band-bot/` - Web user interface.
- `GET /band-bot/api/generate` - JSON endpoint returning band name, album name, and tweet.
- `GET /band-bot/api/band` - JSON endpoint returning a random band name.
- `GET /band-bot/api/album` - JSON endpoint returning a random album name.

### 5. CLI Script

To run the terminal loop:
```bash
python main.py
```
