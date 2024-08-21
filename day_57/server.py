from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
current_day = datetime.date.today()
@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = current_day.year
    return render_template("index.html", num=random_number, year=current_year)

@app.route(f'/guess/<name>')
def guess(name):
    
    
    genderize_url = f"https://api.genderize.io?name={name}"
    
    ageify_url = f"https://api.agify.io?name={name}"
    
    response = requests.get(genderize_url)
    age_response = requests.get(ageify_url)

    gender_data = response.json()
    age_data = age_response.json()
    age = age_data["age"]
    gender = gender_data["gender"]
    
    return render_template("reveal.html", person_age = age, person_gender = gender, person_name = name)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
