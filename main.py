from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
import requests
from wtforms import SubmitField, TextAreaField
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FDFGDgfhgfh'
Bootstrap(app)
date = datetime.today().strftime('%d %B %Y')
website_list = [
    {
        "img_url": "https://cdn.cookielaw.org/logos/c7d0d27d-e055-4572-8927-d3c994df5f60/3275d2bc-df67-4c87-81ed-bdfb982b90c2/a3df5d54-4eba-4aeb-9fb3-189c22118d8c/udemy-logo.png",
        "name": "Udemy Premium Cookies 2023 Updated Daily",
        "info": "Udemy is an online learning platform that offers a wide range of courses taught by expert instructors.",
        "link": 'udemy'},
    {
        "img_url": "https://cdn.cookielaw.org/logos/dd6b162f-1a32-456a-9cfe-897231c7763c/4345ea78-053c-46d2-b11e-09adaef973dc/Netflix_Logo_PMS.png",
        "name": "Netflix Premium Cookies 2023 Updated Daily",
        "info": "Netflix is a prominent subscription-based streaming service for movies, TV shows, documentaries, and other forms of entertainment content.",
        'link': 'netflix'}

]

content = {
    'udemy': {'title': 'Udemy Premium Cookies Updated Today 2023', 'website': 'Udemy', 'link': 'udemy-cookies'},
    'netflix': {'title': 'Netflix Premium Cookies Updated Today 2023', 'website': 'Netflix', 'link': 'netflix-cookies'}
}


class CUpd(FlaskForm):
    text = TextAreaField('Enter Cookies')
    submit = SubmitField('Upload')


@app.route('/')
def home():
    return render_template('home.html', list=website_list)


@app.route('/udemy')
def udemy():
    return render_template('base.html', title=content['udemy']['title'], website=content['udemy']['website'],
                           today=date, link=content['udemy']['link'], img=website_list[0]['img_url'],
                           info=website_list[0]['info'])


@app.route('/netflix')
def netflix():
    return render_template('base.html', title=content['netflix']['title'], website=content['netflix']['website'],
                           today=date, link=content['netflix']['link'], img=website_list[1]['img_url'],
                           info=website_list[1]['info'])


@app.route('/udemy-cookies/<i>')
def get_cookies(i):
    with open(f'static/udemy{i}.txt', 'r') as udemycookies:
        cookies = udemycookies.read()
    return render_template('cookies.html', cookies=cookies)


@app.route('/netflix-cookies/<i>')
def get_ncookies(i):
    with open(f'static/netflix{i}.txt', 'r') as netflixcookies:
        cookies = netflixcookies.read()
    return render_template('cookies.html', cookies=cookies)


@app.route('/update')
def update():
    try:
        with open('static/udemy1.txt', 'w') as udemy1:
            response = requests.get('https://flask-production-9d9d.up.railway.app/udemy1').text
            udemy1.write(response)
    except:
        return 'Error in 1'
    try:
        with open('static/udemy2.txt', 'w') as udemy2:
            response2 = requests.get('https://flask-production-9d9d.up.railway.app/udemy2').text
            udemy2.write(response2)
    except:
        return 'Error in 2'
    try:
        with open('static/udemy3.txt', 'w') as udemy3:
            response3 = requests.get('https://flask-production-9d9d.up.railway.app/udemy3').text
            udemy3.write(response3)
    except:
        return 'Error in 3'
    try:
        with open('static/netflix1.txt', 'w') as netflix1:
            netflix1.write(requests.get('https://flask-production-9d9d.up.railway.app/netflix/1').text)
    except:
        return 'Error in 4'
    try:
        with open('static/netflix2.txt', 'w') as netflix1:
            netflix1.write(requests.get('https://flask-production-9d9d.up.railway.app/netflix/2').text)
    except:
        return 'Error in 5'
    try:
        with open('static/netflix3.txt', 'w') as netflix1:
            netflix1.write(requests.get('https://flask-production-9d9d.up.railway.app/netflix/3').text)
    except:
        return 'Error in 6'

    return 'Done'


@app.route('/c/<f>', methods=['POST', 'GET'])
def cupdate(f):
    form = CUpd()
    if form.validate_on_submit():
        c = form.text.data
        with open(f'static/{f}.txt', 'w') as file:
            file.write(c)
        return render_template('cupdate.html', form=form, updated = True)
    return render_template('cupdate.html', form=form, updated = False)


if __name__ == '__main__':
    app.run(debug=True)
