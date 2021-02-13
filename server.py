from flask import Flask, render_template
from random import randint
import datetime
import requests
import json

gender_api_endpoint = "https://api.genderize.io/?name="
age_api_endpoint = "https://api.agify.io/?name="

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.datetime.today().year
    return render_template('/index.html', num=year)


@app.route('/info/<name>')
def get_info(name):
    age = age_api_endpoint + name
    age_response = requests.get(age)
    age_data = json.loads(age_response.text)
    age = age_data['age']

    gender = gender_api_endpoint + name
    gender_response = requests.get(gender)
    gender_data = json.loads(gender_response.text)
    gender = gender_data['gender']

    name = str(name).title()
    return render_template('/info.html', name=name, age=age, gender=gender)

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    blogs = requests.get(blog_url)
    blogs = json.loads(blogs.text)

    return render_template("/blogs.html",blogs=blogs)

if __name__ == '__main__':
    app.run(debug=True)
