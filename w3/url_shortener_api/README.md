# URL Shortener Service

This is a simple Flask application that provides URL shortening functionality similar to services like TinyURL and Bit.ly. 
It also allows users to retrieve statistics on the usage of shortcodes.

## Endpoints

- `POST /shorten`: Shortens a URL.
- `GET /<shortcode>`: Redirects to the original URL associated with the provided shortcode.
- `GET /<shortcode>/stats`: Retrieves statistics on the usage of the provided shortcode.

## Installation

1. Clone the repository:

- git clone git@github.com:R-Zaib/mib-automation-rz.git
- cd /mib-automation-rz/w3/url_shortener_api

2. Install the required dependencies:
- Flask: Web framework for Python.
- Python Standard Library: Required for various functionalities such as file I/O, random generation, and datetime manipulation.

3. Run the Flask application:
- python app.py

# Usage

1. To shorten a URL, send a POST request to /shorten with a JSON payload containing the URL:
POST /shorten
Content-Type: application/json
{"url": "https://example.com"}

2. To provide a custom shortcode, include it in the JSON payload:
POST /shorten
Content-Type: application/json
{"url": "https://example.com", "shortcode": "custom123"}

3. To retrieve the original URL associated with a shortcode, send a GET request to /<shortcode>:
GET /custom123

4. To retrieve statistics for a shortcode, send a GET request to /<shortcode>/stats:
GET /custom123/stats

# License

This project is licensed under the MIT License. It is an open project, for contributions and updates, you can contact me on Github.
