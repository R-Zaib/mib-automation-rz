from flask import Flask, render_template, request, abort, jsonify, redirect
import random
import string
import json

app = Flask(__name__)

json_file_path = "shortcodes.json"

def load_shortcodes():
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def save_shortcodes(data):
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=2)

# creating random shortcode for the URL
def generate_random_shortcode():
    max_length = 6
    characters = string.ascii_letters + "_" + string.digits
    shortcode = ''.join(random.sample(characters, max_length))
    # validate here against the already created shortcodes or shortcodes inside the json file
    return shortcode

# checking the shortcodes in use using load_shortcodes 
def in_use_shortcode(shortcode):
    existing_data = load_shortcodes()
    return shortcode in existing_data

# https://www.w3schools.com/python/ref_string_isalnum.asp
def is_valid_shortcode(shortcode):
    valid_characters = shortcode.isalnum() or "_"
    return len(shortcode)==6 and valid_characters

def retrieve_url(shortcode):
    existing_data = load_shortcodes()
    url = existing_data.get(shortcode, None)

    if url is None:
        abort(404, description="Shortcode not found")

    return redirect(url)


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
    if not url:
        abort(400, description = "Url not present") 
        
    if shortcode is None:
        shortcode = generate_random_shortcode()

    if not is_valid_shortcode(shortcode):
        abort(412, description = "The provided shortcode is invalid") 
    
    
    if in_use_shortcode(shortcode):
        abort(409, description = "Shortcode already in use")
    
    existing_data = load_shortcodes() 
    
    existing_data[shortcode] = request_data["url"]
    save_shortcodes(existing_data)
        
    return jsonify({"shortcode": shortcode}), 201

@app.route('/<shortcode>', methods=['GET'])
def redirect_url_from_shortcode(shortcode):
    existing_data = load_shortcodes()
    url = existing_data.get(shortcode, None)

    if url is None:
        abort(404, description="Shortcode not found")

    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
