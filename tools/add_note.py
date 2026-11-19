#!/usr/bin/env python3
"""Register a note in notes/notes.js.

  python3 tools/add_note.py notes/attention.pdf "Attention, by hand" --tag "Deep learning" --desc "Q, K, V worked through"
  python3 tools/add_note.py notes/page.jpg "Backprop" --date 2026-11-19

For PDFs it also tries to make a preview thumbnail (needs `pdftoppm`; skipped if missing).
"""
import argparse, json, re, shutil, subprocess, sys
from datetime import date
from pathlib import Path

root = Path(__file__).resolve().parent.parent
manifest = root / "notes" / "notes.js"

ap = argparse.ArgumentParser()
ap.add_argument("file", help="path to the file (inside notes/, or it will be copied there)")
ap.add_argument("title")
ap.add_argument("--tag", default="")
ap.add_argument("--desc", default="")
ap.add_argument("--date", default=date.today().isoformat())
a = ap.parse_args()

src = Path(a.file).resolve()
if not src.exists():
    sys.exit(f"File not found: {src}")
dest = root / "notes" / src.name
if src != dest:
    shutil.copy2(src, dest)

entry = {"title": a.title, "date": a.date, "tag": a.tag, "file": f"notes/{dest.name}"}
if a.desc:
    entry["desc"] = a.desc

if dest.suffix.lower() == ".pdf" and shutil.which("pdftoppm"):
    base = root / "notes" / f"{dest.stem}-thumb"
    subprocess.run(["pdftoppm", "-jpeg", "-r", "70", "-f", "1", "-l", "1", "-singlefile", str(dest), str(base)], check=False)
    if base.with_suffix(".jpg").exists():
        entry["thumb"] = f"notes/{dest.stem}-thumb.jpg"

text = manifest.read_text()
m = re.search(r"window\.NOTES\s*=\s*(\[.*\]);", text, re.S)
notes = json.loads(m.group(1))
notes = [n for n in notes if n["file"] != entry["file"]] + [entry]
new = "window.NOTES = " + json.dumps(notes, indent=2, ensure_ascii=False) + ";\n"
manifest.write_text(text[: m.start()] + new)
print(f"Added “{a.title}” → {entry['file']} ({len(notes)} notes total)")
