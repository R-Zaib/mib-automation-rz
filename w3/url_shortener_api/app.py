from flask import Flask, render_template, request, abort, jsonify
# from url_shortener_logic import generate_random_shortcode, is_valid_shortcode, in_use_shortcode
import random
import string
import json

app = Flask(__name__)


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
    return shortcode

# checking the shortcodes in use using dummy data for now, will update later 
# to take in parameter from the request_data variable
def in_use_shortcode(shortcode):
    shortcode_in_use = ["9pqIug", "voyExA", "dSFugI", "nb0C9h", "P7c_Ez", "abc123"]
    return shortcode in shortcode_in_use

# https://www.w3schools.com/python/ref_string_isalnum.asp
def is_valid_shortcode(shortcode):
    valid_characters = shortcode.isalnum() or "_"
    return len(shortcode)==6 and valid_characters and not in_use_shortcode(shortcode)



# root route for front-end
# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         long_url = request.form["url_to_shorten"]
#         return long_url
#     else:
#         return render_template("home.html")

@app.route("/shorten", methods=["POST"])
def shorten_url():
    request_data = request.get_json()

    get_url = request_data.get("url")
    get_shortcode = request_data.get("shortcode")
    
    #checking whether url is present
    if not get_url:
        abort(400, description = "Url not present") 
        
    if get_shortcode is None:
        get_shortcode = generate_random_shortcode()

    elif get_shortcode in request_data:
        if not is_valid_shortcode(get_shortcode):
            abort(412, description = "The provided shortcode is invalid") 
        
        if in_use_shortcode(get_shortcode):
            abort(409, description = "Shortcode already in use")
        

    return jsonify({"shortcode": get_shortcode}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)

