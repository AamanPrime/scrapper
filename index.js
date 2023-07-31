const express = require('express');
const app = express()
const path = require('path')

const website = [
    { "img_url": "https://cdn.cookielaw.org/logos/c7d0d27d-e055-4572-8927-d3c994df5f60/3275d2bc-df67-4c87-81ed-bdfb982b90c2/a3df5d54-4eba-4aeb-9fb3-189c22118d8c/udemy-logo.png", "name": "Udemy Premium cookies 2023 Updated Daily", "info": "Udemy is an online learning platform that offers a wide range of courses taught by expert instructors." },
    { "img_url": "https://cdn.cookielaw.org/logos/dd6b162f-1a32-456a-9cfe-897231c7763c/4345ea78-053c-46d2-b11e-09adaef973dc/Netflix_Logo_PMS.png", "name": "Netflix Premium Cookies 2023 Updated Daily", "info": "Netflix is a prominent subscription-based streaming service for movies, TV shows, documentaries, and other forms of entertainment content." }

]





app.use(express.static(path.join(__dirname, 'public')))
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'))


app.listen(5000, () => {
    console.log('Listening')


})

app.get('/', (req, res) => {

    res.render('home.ejs', {website : website})



})

app.get('/udemy', (req, res) => {

    res.render('base.ejs')
})




