"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    print("Current checkpoint: ", km)    
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    
    brevet_dist_km = request.args.get('brevet_dist_km', 1000, type=float)             #getting the brevit distance from the html
    # print("Brevet distance: ", brevet_dist_km)                                        #printing it out to make sure its right              

    brevet_start_time = request.args.get('brevet_start_time', arrow.now(), type=str)  #getting the brevit start time from the html                   
    # print("Brevet start time: ", brevet_start_time)                                   #printing it out to make sure its right          
    
    brevet_start_time = arrow.get(brevet_start_time, 'YYYY-MM-DDTHH:mm')              #parsing the string into an arrow
    # print("Brevet start time: ", brevet_start_time)                                   #printing it out to make sure its right      
    
    # FIXME!
    # Right now, only the current time is passed as the start time
    # and control distance is fixed to 200
    # You should get these from the webpage!

    # calling the functions in acp_times using the data we received from the html
    open_time = acp_times.open_time(km, brevet_dist_km, brevet_start_time).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, brevet_dist_km, brevet_start_time).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    print("RESULT:", result)         #this is just to make sure the result is correct
    
    return flask.jsonify(result=result)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
