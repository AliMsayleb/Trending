from country_fetcher import get_country
from flask import Flask, render_template, request
from twitter_fetcher import get_trending_hashtags
from utils import get_client_ip

app = Flask(__name__)


@app.route("/")
def home():
    ip_address = get_client_ip()
    country = request.args.get('country') if (request.args and request.args.get('country')) else get_country(ip_address)
    tags = get_trending_hashtags(country)

    return render_template('index.html', tags=tags)


@app.route("/about")
def about():

    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
