# Trinita Roy — portfolio

Static site (no build step). Pages: `index.html`, `blog.html`, `post.html`, `notes.html`.

- **Preview locally:** `python3 -m http.server` then open http://localhost:8000
- **Add a note:** `python3 tools/add_note.py notes/file.pdf "Title" --tag "Topic"`
- **Deploy:** push to `main`. The workflow in `.github/workflows/pages.yml` publishes it.
  One-time setup: repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
