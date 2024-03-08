from flask import Flask, render_template, request
# import connexion

app = Flask(__name__)

# app = connexion.App(__name__, specification_dir="./")
# app.add_api("swagger.yml")
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url_received = request.form["url_to_shorten"]
        return url_received
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)