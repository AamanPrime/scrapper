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
        "img_url": "https://cdn.cookielaw.org/logos/dd6b162f-1a32-456a-9cfe-897231c7763c/4345ea78-053c-46d2-b11e-09adaef973dc/Netflix_Logo_PMS.png",
        "name": "Netflix Premium Cookies 2023 Updated Daily",
        "info": "Netflix is a prominent subscription-based streaming service for movies, TV shows, documentaries, and other forms of entertainment content.",
        'link': 'netflix'},
    {
        'img_url':'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Grammarly_logo.svg/1200px-Grammarly_logo.svg.png',
        'name': 'Grammarly Premium Cookies 2023 Updated Daily',
        'info':'It reviews spelling, grammar, punctuation, clarity, engagement, and delivery mistakes in English texts, detects plagiarism, and suggests replacements for the identified errors.',
        'link': 'grammarly'
    },
    {
        'img_url':'https://images.ctfassets.net/00atxywtfxvd/2MlqAOzmHjSPtssv6HlNox/1cb35b40775835a5f574ebc5509907a1/coursera-wordmark-blue.svg',
        'name': 'Coursera Premium Cookies 2023 Updated Daily',
        'info': 'Coursera is an online learning platform that partners with universities and organizations to offer courses, certificates, and degrees online.',
        'link': 'coursera'
    },
{
        "img_url": "https://cdn.cookielaw.org/logos/c7d0d27d-e055-4572-8927-d3c994df5f60/3275d2bc-df67-4c87-81ed-bdfb982b90c2/a3df5d54-4eba-4aeb-9fb3-189c22118d8c/udemy-logo.png",
        "name": "Udemy Premium Cookies 2023 Updated Daily",
        "info": "Udemy is an online learning platform that offers a wide range of courses taught by expert instructors.",
        "link": 'udemy'},
    {
        'img_url':'https://www.svgrepo.com/show/353573/codecademy.svg',
        'name': 'Codecademy Premium Cookies 2023 Updated Daily',
        'info': 'Offers free coding classes in 12 different programming languages including Python, Java, Go, JavaScript, Ruby, SQL, C++, C#, and Swift, as well as markup languages HTML and CSS.',
        'link': 'codecademy'
    },
    {
        'img_url': 'https://logowik.com/content/uploads/images/educative9956.jpg',
        'name': 'Educative Premium Cookies 2023 Updated Daily',
        'info': 'Educative provides interactive and adaptive courses for software developers with pre-configured developer environments in the cloud.',
        'link': 'educative'
    }


]

content = {
    'netflix': {'title': 'Netflix Premium Cookies Updated Today 2023', 'website': 'Netflix', 'link': 'netflix/cookies', 'two' : False, 'three' : False},
    'grammarly': {'title': website_list[1]['name'], 'website': 'Grammarly', 'link': 'grammarly/cookies', 'two' : False, 'three' : False},
    'coursera': {'title': website_list[2]['name'], 'website': 'Coursera', 'link': 'coursera/cookies', 'two' : False, 'three' : False},
    'udemy': {'title': 'Udemy Premium Cookies Updated Today 2023', 'website': 'Udemy', 'link': 'udemy/cookies', 'two' : True, 'three' : False},
    'codecademy': {'title': website_list[4]['name'], 'website': 'Codecademy', 'link': 'codecademy/cookies', 'two' : False, 'three' : False},
    'educative': {'title': website_list[5]['name'], 'website': 'Educative', 'link': 'educative/cookies', 'two' : False, 'three' : False}
}


class CUpd(FlaskForm):
    text = TextAreaField('Enter Cookies')
    submit = SubmitField('Upload')


@app.route('/')
def home():
    return render_template('home.html', list=website_list)


@app.route('/<website>')
def web(website):
    i = list(content.keys()).index(website)
    return render_template('base.html', title=content[website]['title'], website=content[website]['website'],
                           today=date, link=content[website]['link'], img=website_list[i]['img_url'],
                           info=website_list[i]['info'], two = content[website]['two'], three = content[website]['three'])


# @app.route('/netflix')
# def netflix():
#     return render_template('base.html', title=content['netflix']['title'], website=content['netflix']['website'],
#                            today=date, link=content['netflix']['link'], img=website_list[1]['img_url'],
#                            info=website_list[1]['info'])


@app.route('/<website>/cookies/<i>')
def get_cookies(website,i):
    with open(f'static/{website}{i}.txt', 'r') as data:
        cookies = data.read()
    return render_template('cookies.html', cookies=cookies)


# @app.route('/netflix-cookies/<i>')
# def get_ncookies(i):
#     with open(f'static/netflix{i}.txt', 'r') as netflixcookies:
#         cookies = netflixcookies.read()
#     return render_template('cookies.html', cookies=cookies)


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
        with open('static/grammarly.txt', 'w') as grammarly:
            grammarly.write(requests.get('https://flask-production-9d9d.up.railway.app/grammarly').text)
    except:
        return 'Error in Grammarly'
    try:
        with open('static/coursera.txt', 'w') as coursera:
            coursera.write(requests.get('https://flask-production-9d9d.up.railway.app/coursera').text)
    except:
        return 'Error in Coursera'
    try:
        with open('static/codecademy.txt', 'w') as codecademy:
            codecademy.write(requests.get('https://flask-production-9d9d.up.railway.app/codecademy').text)
    except:
        return 'Error in Codecademy'
    try:
        with open('static/educative.txt', 'w') as codecademy:
            codecademy.write(requests.get('https://flask-production-9d9d.up.railway.app/educative').text)
    except:
        return 'Error in Educative'

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
