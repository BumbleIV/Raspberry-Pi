from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import flaskr


if __name__ == '__main__':
    app = flaskr.create_app()
    app.run(debug=True, port=5000)

