# Band Name Bot 🎸

A randomized band name, album name, and promo tweet generator built with Python and Flask.

## Quickstart

### 1. Installation

Using `pip`:
```bash
pip install -r requirements.txt
```

Or using Conda:
```bash
conda env update -f environment.yml
```

### 2. Run the Web App

```bash
python app.py
```
Open your browser at `http://localhost:5000`.

### 3. API Endpoints

- `GET /api/generate` - Returns a JSON object containing a band name, album title, and tweet.
- `GET /api/band` - Returns a JSON object with a random band name.
- `GET /api/album` - Returns a JSON object with a random album name.

### 4. Run CLI Script

```bash
python main.py
```
