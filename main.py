from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from datetime import datetime
import requests

app = Flask(__name__)
Bootstrap(app)
date = datetime.today().strftime('%d %B %Y')
website_list = [
    {
        "img_url": "https://cdn.cookielaw.org/logos/c7d0d27d-e055-4572-8927-d3c994df5f60/3275d2bc-df67-4c87-81ed-bdfb982b90c2/a3df5d54-4eba-4aeb-9fb3-189c22118d8c/udemy-logo.png",
        "name": "Udemy Premium cookies 2023 Updated Daily",
        "info": "Udemy is an online learning platform that offers a wide range of courses taught by expert instructors."},
    {
        "img_url": "https://cdn.cookielaw.org/logos/dd6b162f-1a32-456a-9cfe-897231c7763c/4345ea78-053c-46d2-b11e-09adaef973dc/Netflix_Logo_PMS.png",
        "name": "Netflix Premium Cookies 2023 Updated Daily",
        "info": "Netflix is a prominent subscription-based streaming service for movies, TV shows, documentaries, and other forms of entertainment content."}

]

content = {
    'udemy': {'title': 'Udemy Premium Cookies Updated Today 2023', 'website': 'Udemy', 'link': 'udemy-cookies'}
}


@app.route('/')
def home():
    return render_template('home.html', list=website_list)


@app.route('/udemy')
def udemy():
    return render_template('base.html', title=content['udemy']['title'], website=content['udemy']['website'],
                           today=date, link=content['udemy']['link'])


@app.route('/udemy-cookies/<i>')
def get_cookies(i):
    with open(f'static/udemy{i}.txt', 'r') as udemycookies:
        cookies = udemycookies.read()
    return render_template('cookies.html', cookies=cookies)


@app.route('/update')
def update():
    try:
        with open('static/udemy1.txt', 'w') as udemy1:
            response = requests.get('https://flask-production-9d9d.up.railway.app/udemy1').text
            udemy1.write(response)
            print('Done')
    except:
        return 'Error in 1'
    try:
        with open('static/udemy2.txt', 'w') as udemy2:
            response2 = requests.get('https://flask-production-9d9d.up.railway.app/udemy2').text
            udemy2.write(response2)
            print('Done')
    except:
        return 'Error in 2'
    try:
        with open('static/udemy3.txt', 'w') as udemy3:
            response3 = requests.get('https://flask-production-9d9d.up.railway.app/udemy3').text
            udemy3.write(response3)
            print('Done')
    except:
        return 'Error in 3'

    return 'Done'


app.run(debug=True)
