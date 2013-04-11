from flask import (
    Flask,
    render_template,
    session,
    redirect,
    request,
    url_for
)

import urllib
import requests
import json
from oauth import sign_url

app = Flask(__name__)

YELP_SEARCH_URL = 'http://api.yelp.com/v2/search'


@app.route('/')
def index():
    # url args:
    # http://localhost:5000/?data1=5&data2=7
    # print request.args['data1']
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    search_term = request.form['term']
    location = request.form['location']

    # will print search term in terminal
    # print "search: %s" % search_term


    # term and location are keys for the yelp api
    # they just happen to be the same as what we had
    # in the html file
    data = {
    'term': search_term,
    'location': location
    }

    query_string = urllib.urlencode(data) # encode this data

    # put the search terms in the url
    api_url = YELP_SEARCH_URL + "?" + query_string

    # authenticate the url with the yelp api
    signed_url = sign_url(api_url)

    # get the desired results from yelp
    # requests is a library
    # returns in the JSON format
    response = requests.get(signed_url)

    # get the fields from the json document:
    json_response = json.loads(response.text)

    return render_template('results.html',
                            search_term=search_term,
                            location=location,
                            businesses=json_response['businesses']) 
                            # the businesses array in the json document

if __name__ == '__main__':
    app.run(debug=True)
