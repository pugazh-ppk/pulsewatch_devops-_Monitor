from flask import Flask, render_template, request
from monitor import check_website

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    url = ""
    error = None

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if not url:
            error = "Please enter a website URL."
        else:
            result = check_website(url)
            if not result.get("ok"):
                error = result.get("error")

    return render_template("index.html", result=result, url=url, error=error)

@app.get("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
