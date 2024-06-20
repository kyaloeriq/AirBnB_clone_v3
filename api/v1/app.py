from flask import Flask
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.route('/api/v1/status', methods=['GET'])
def status():
    return {"status": "OK"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
