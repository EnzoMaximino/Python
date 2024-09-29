from flask import Flask
from controllers import restaurantes_controller


app = Flask(__name__)
app.register_blueprint(restaurantes_controller)

if __name__ == "__main__":
    app.run()
