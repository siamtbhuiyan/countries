# COUNTRIES

#### Video Demo: https://youtu.be/j1rgV6FgZRE

#### Description: This is a website that shows information about countries. It was built with Flask, HTML, CSS, Bootstrap, Jinja and a bit of Javascript.

#### The code structure is a flask app structure where there is an app.py, a requirements.txt, a calls.py, templates folder where all the html files are stored and a static folder where the css file(s) are stored.

#### app.py: This is form where the app is running. There are routes configured for each path in the app. The 1st is the ("/") route. all the countries are called by a "all" function that is defined in the call.py file. This file returns certain information about every country. The countries are then passed to the index.html that is rendered. The next route that is configured is the ("/search") route. This gets all the countries and searches through them and puts the matched countries in a list that is then sent with the index.html file that is rendered to the screen. Next is the ("/filter") route. This also gets all the countries filters them by regions and renders to the index.html template. The last route is the ("/country") where it calls the get_country function that is defined in the calls.py file which returns details about a country. It is then stored in a variable and passed to the country.html template and rendered to the screen if no country is found it renders a no_countries.html template. There is also an error handling route that handles all the non existing routes and renders a 404 not found page as the 404.html template

#### calls.py: There are 2 function defined in this file. the 1st is all(). Where it makes a request to the https://restcountries.com/ api. Which returns all the details about all the countries. Out of all the information a few fields are selected and stored in a list as a list of countries. Which is then returned. The other fuction is get_country. This takes a country name as a perameter and uses that to make a request to the api which returns full details about that speciific country. A number of fields are selected from that and returned as a list.

#### requirements.txt: The requrements are mentioned here.

#### templates/layout.html: The basic layout of html and bootstrap cdn and google fonts cdn are in here. navbar and container are placed with jinja blocks in between. The there is a script tag that has the logic to submiting the filter request to the route.

#### templates/index.html: extends the layout.html. adds a search form that makes a get request to the /search route. It also adds a filter form that makes a get request to /filter route. It then adds a card with flag, name, population, region and capital for every country passed using jinja for loop it also adds a form that makes a get request to the /country route.

#### templates/country.html: extends the layout.html. It shows the flag in the middle. Some information about the country and then it shows the bordering country. Each with a form that submits to the /country route.

#### templates/no_countries.html: this extends layout adds search and filter and renders a simple h1.

#### templates/404.html: this simply adds an h1 and an h4.

#### static/styles.css: the design is a combination of bootstrap and custom design. All the custom design is in this file.
