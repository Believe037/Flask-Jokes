from flask import Flask, redirect, url_for, render_template
import pyjokes

app = Flask(__name__)

@app.route('/')
def home():
  random_joke = pyjokes.get_joke()
  
  return render_template('index.html', joke=random_joke)

@app.route('/generate_joke')
def generate_joke():
  random_joke = pyjokes.get_joke()
  return random_joke



if __name__ == "__main__":
  app.run(debug=True)