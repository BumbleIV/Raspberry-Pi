from flask import Flask

import flaskr


if __name__ == '__main__':
    app = flaskr.create_app()
    app.run(debug=True, port=5000)

