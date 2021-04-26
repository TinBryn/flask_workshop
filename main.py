from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Leo Fern!"


def main():
    app.run()


if __name__ == "__main__":
    main()
