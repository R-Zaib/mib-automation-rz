from flask import Flask, render_template, request, abort, jsonify
from url_shortener_logic
# import connexion

app = Flask(__name__)

# app = connexion.App(__name__, specification_dir="./")
# app.add_api("swagger.yml")

# root route for front-end
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        long_url = request.form["url_to_shorten"]
        return long_url
    else:
        return render_template("home.html")

@app.route("/shorten", methods=["POST"])
def shorten_url():
    request_data = request.get_json()

    url = request_data.get("url")
    shortcode = request_data.get("shortcode")
    
    #checking whether url is present
    if url not in request_data:
        abort(400, description = "Url not present")
        
    if shortcode in request_data:
        if not is_valid_shortcode(shortcode):
            abort(412, description = "The provided shortcode is invalid") 
        
        if in_use_shortcode(shortcode):
            abort(409, description = "Shortcode already in use")
        

    return jsonify({"shortcode": "placeholder"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)