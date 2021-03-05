from flask import Flask, render_template, jsonify
from app import views

app=Flask(__name__)


app.run(debug=True)
