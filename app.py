from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
WEATHER_API = os.getenv("WEATHER_API")

@app.route("/", methods=['GET'])
def home():

    # getting weather
    weather = requests.get(f'http://api.weatherapi.com/v1/current.json?q=Karachi&key={WEATHER_API}').json()

    # getting top stories
    headlines = requests.get(f'https://newsapi.org/v2/everything?q=Pakistan&searchIn=title,description&language=en&sortBy=publishedAt&pageSize=6&apiKey={API_KEY}').json()
    
    # getting trending section
    trendinghome = requests.get(f'https://newsapi.org/v2/top-headlines?category=general&pageSize=3&apiKey={API_KEY}').json()

    # getting business section
    businesshome = requests.get(f'https://newsapi.org/v2/top-headlines?category=business&pageSize=3&apiKey={API_KEY}').json()

    # getting technology section
    technologyhome = requests.get(f'https://newsapi.org/v2/top-headlines?category=technology&pageSize=3&apiKey={API_KEY}').json()

    #getting sports section
    sportshome = requests.get(f'https://newsapi.org/v2/top-headlines?category=sports&pageSize=3&apiKey={API_KEY}').json()

    #Entertainment
    entertainmenthome = requests.get(f'https://newsapi.org/v2/top-headlines?category=entertainment&pageSize=3&apiKey={API_KEY}').json()

    return render_template("home.html", topheadlines=headlines, weather=weather, trendinghome=trendinghome, businesshome=businesshome, technologyhome=technologyhome, sportshome=sportshome, entertainmenthome=entertainmenthome)

    # return render_template("test.html")




@app.route("/pakistan", methods=['GET'])
def pakistan():

    pakistan=requests.get(f'https://newsapi.org/v2/everything?q=pakistan&pageSize=20&apiKey={API_KEY}').json()

    return render_template("pakistan.html", pakistan=pakistan)



@app.route("/sports", methods=['GET'])
def sports():

    sports=requests.get(f'https://newsapi.org/v2/top-headlines?category=sports&pageSize=20&apiKey={API_KEY}').json()

    return render_template("sports.html", sports=sports)



@app.route("/trending", methods=['GET'])
def trending():

    trending=requests.get(f'https://newsapi.org/v2/top-headlines?category=general&pageSize=20&apiKey={API_KEY}').json()

    return render_template("trending.html", trending=trending)
    


@app.route("/business", methods=['GET'])
def business():

    business=requests.get(f'https://newsapi.org/v2/top-headlines?category=business&pageSize=20&apiKey={API_KEY}').json()

    return render_template("business.html", business=business)


@app.route("/technology", methods=['GET'])
def technology():

    technology=requests.get(f'https://newsapi.org/v2/top-headlines?category=technology&pageSize=20&apiKey={API_KEY}').json()

    return render_template("technology.html", technology=technology)



@app.route("/entertainment", methods=['GET'])
def entertainment():

    entertainment=requests.get(f'https://newsapi.org/v2/top-headlines?category=entertainment&pageSize=20&apiKey={API_KEY}').json()

    return render_template("entertainment.html", entertainment=entertainment)







if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port, debug=True)