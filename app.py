from flask import Flask, render_template, request
from country_fetcher import get_country_code, get_country_id, get_country_name
from twitter_fetcher import get_trending_tags
from utils import get_client_ip

app = Flask(__name__)


@app.route("/")
def home():
    ip_address = get_client_ip()
    country_code = request.args.get('country') if (request.args and request.args.get('country')) else get_country_code(ip_address)
    woeid = get_country_id(country_code)
    tags = get_trending_tags(woeid)

    return render_template('index.html', tags=tags, country=get_country_name(country_code))


@app.route("/about")
def about():

    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
