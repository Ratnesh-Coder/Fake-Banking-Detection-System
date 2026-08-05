from flask import Flask
from routes.nonce_routes import nonce_bp
from routes.verify_routes import verify_bp
from routes.h2_routes import h2_bp
from routes.key_routes import key_bp

app = Flask(__name__)

app.register_blueprint(nonce_bp)
app.register_blueprint(verify_bp)
app.register_blueprint(h2_bp)
app.register_blueprint(key_bp)

@app.route("/")
def home():
    return "Server Running"

if __name__ == "__main__":
    app.run(debug=True)