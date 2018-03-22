from flask import Flask, json
import os

app = Flask(__name__)

@app.route("/")
def default():
    html = """
<html>
  <head>
    <title>Environment Variables</title>
    <style>
      body {
        font-family:sans-serif;
        font-size:smaller;
      }
    </style>
  </head>
  <body>
    <ol>
"""

    sorted_keys = sorted(os.environ.keys())
    for key in sorted_keys:
        html += "      <li>{}={}</li>\n".format(key, os.getenv(key))

    html += """
    </ol>
  </body>
</html>
"""
    return html

@app.route("/api")
def api():
    # cleanse unsafe hash values
    data = {}
    for key in os.environ.keys():
        safe_key = "{}".format(key)
        safe_val = "{}".format(os.environ[key])
        data[safe_key] = safe_val

    resp = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
