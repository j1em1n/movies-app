from flask import Flask
from flask import render_template

app = Flask(__name__) 

app.config["DEBUG"] = True

@app.route("/")
def render_landing_page():
     return render_template("landing-page.html")

'''
@app.route("/")
def render_landing_page():
     return render_template("landing-page.html", user_account = "Heicoders", account_type = "Premium")
'''


import requests

url = "https://imdb8.p.rapidapi.com/title/auto-complete"

querystring = {"q":"game of thr"}

headers = {
    'x-rapidapi-key': "8f4e5e28c8msh1f72ed78b1fd81ap14b114jsncd604d9d801f",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")