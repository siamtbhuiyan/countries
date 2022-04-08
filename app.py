from flask import Flask, redirect, render_template, request

from calls import all, get_country

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

countries = all()

@app.route("/")
def index():
    return render_template("index.html", countries=countries)


@app.route("/search")
def search():
    filtered_countries = []
    q = request.args.get("q")
    if q:
        for country in countries:
            if q.lower() in country["name"].lower():
                filtered_countries.append(country)
    else:
        filtered_countries = []
    if filtered_countries == []:
        return render_template("no_countries.html")
    return render_template("index.html", countries=filtered_countries)


@app.route("/filter")
def filter():
    filtered_countries = []
    q = request.args.get("region")
    for country in countries:
        if q.lower() == country["region"].lower():
            filtered_countries.append(country)
        elif q.lower() == 'filter by region':
            return redirect("/")
    return render_template("index.html", countries=filtered_countries)


@app.route("/country")
def country():
    country = get_country(request.args.get("country"))
    return render_template("country.html", country=country)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
