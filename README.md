LLM Article Generator
======================

A small Flask app that generates articles from a title using LangChain + Groq LLM.

Contents
- `main.py` — Flask app (routes `/` and `/generate`).
- `templates/index.html` — frontend UI.
- `static/css/style.css` — page styling.
- `.env` — your GROQ API key (not committed).

Quick local run
----------------
1. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

2. Create a `.env` in the project root with your GROQ key:

```
GROQ_API_KEY=your_real_groq_key_here
```

3. Run the app:

```powershell
python main.py
```

Open `http://127.0.0.1:5000`.

Prepare for GitHub
-------------------
1. Initialize git (if not already):

```powershell
git init
git add .
git commit -m "Initial commit: LLM Article Generator"
```

2. Create a repository on GitHub and push:

```powershell
git remote add origin https://github.com/<your-username>/<repo>.git
git branch -M main
git push -u origin main
```

Deploy options (short guides)
----------------------------
I. Heroku (simple)
1. Install the Heroku CLI and log in.
2. Create app and push:

```powershell
heroku login
heroku create your-app-name
git push heroku main
heroku config:set GROQ_API_KEY=your_real_groq_key_here
heroku ps:scale web=1
heroku open
```
Heroku reads `Procfile` and uses `gunicorn` to run the app.

II. Render (recommended for Python)
1. Create an account at render.com.
2. Click "New Web Service" -> Connect GitHub repo -> Select repo.
3. Build command: `pip install -r requirements.txt`
   Start command: `gunicorn main:app --bind 0.0.0.0:$PORT`
4. Add environment variable `GROQ_API_KEY` in Render's dashboard.
Render will automatically build and deploy on push.

III. Railway / Fly.io / Railway
- Similar: connect repo or deploy via Docker. Use the `Dockerfile` included if you prefer container-based deploy.

IV. Docker (any host)
1. Build image:

```powershell
docker build -t llm-article-generator:latest .
```

2. Run container:

```powershell
docker run -e GROQ_API_KEY=your_real_groq_key_here -p 5000:5000 llm-article-generator:latest
```

V. GitHub Actions -> Deploy
- Add a deployment pipeline that builds the image and pushes to Docker Hub or deploys to your cloud provider.

Security notes
--------------
- Never commit your `.env` to a public repo. The repo already has `.gitignore` including `.env` and `.venv`.
- If your key was exposed, rotate it immediately.

Extras
------
- Add monitoring, healthchecks, and a production WSGI server (we use `gunicorn` already).
- For higher concurrency, add worker processes or background jobs for long LLM requests.

If you want, I can:
- Add a one-click Deploy to Render button and a small `render.yaml`.
- Create a GitHub Actions workflow to build a Docker image and publish it to Docker Hub.
- Help you push this repo to GitHub (I can create the commands you should run locally).
