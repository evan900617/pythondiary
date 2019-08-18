from flask import Flask, render_template
import glob
from datetime import datetime
import os
app = Flask("BowTie")

@app.route("/category/<c>")
def category(c):
  fs = glob.glob("articles/" + c + "/*.txt")
  fill = []
  for i, f in enumerate(fs):
    a = open(f)
    article = a.read()
    fp = f.split("/")[-1].replace(".txt", "")
    utc = datetime.utcfromtimestamp(os.path.getmtime(f))
    t = (i, fp, str(utc), article)
    fill.append(t)
  return render_template("category.html", cat = fill, title=c)

@app.route("/")
def home():
    temp = glob.glob("articles/*")
    fill = []
    for t in temp:
      length = len(glob.glob(t + "/*.txt"))
      catergory = t.replace("articles/", "")
      f = (catergory, length)
      fill.append(f)
    return render_template("index.html", cat=fill)

app.run(debug=True, host="0.0.0.0", port="3000")