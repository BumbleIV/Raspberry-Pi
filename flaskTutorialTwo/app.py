from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "hello bi"

if name == '__main__':
    app.run(debug=True)


