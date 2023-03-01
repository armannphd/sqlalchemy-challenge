import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine=engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/date"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return prcp from last year"""
    # Query prcp for last 12 monthsall passengers
    all_prcp_data = [Measurement.date, Measurement.prcp]
    year_ago_date = dt.datetime(2016, 8, 22)
    results = session.query(*all_prcp_data).filter(Measurement.date > year_ago_date).order_by(Measurement.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list 
    all_measurement = []
    for date, prcp in results:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["prcp"] = prcp
        all_measurement.append(measurement_dict)

    return jsonify(all_measurement)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    stations = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(stations))

    return jsonify(all_stations)
   
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return tobs from last year"""
    # Query prcp for last 12 monthsall passengers
    tobs_data = [Measurement.date, Measurement.tobs]
    year_ago_date = dt.datetime(2016, 8, 22)
    temp_at_most_active_station = session.query(*tobs_data).\
        filter(Measurement.date > year_ago_date).\
        filter(Measurement.station == 'USC00519281').\
        order_by(Measurement.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list 
    all_measurement = []
    for date, tobs in temp_at_most_active_station:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["tobs"] = tobs
        all_measurement.append(measurement_dict)

    return jsonify(all_measurement)

   



@app.route("/api/v1.0/date")
def date():
    session = Session(engine)

    """Return a list of all countries"""
    # Query all passengers
    date = ('2016-08-23')
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    temps = session.query(*sel).\
        filter(Measurement.date >= date).all()
    

    session.close()

    # Convert list of tuples into normal list
    temp_data = list(np.ravel(temps))
    
    return jsonify(temp_data)

@app.route("/api/v1.0/<start>")
def dat(start):
    session = Session(engine)

    """Return a list of all countries"""
    # Query all passengers
    
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    temps = session.query(*sel).\
        filter(Measurement.date >= start).all()
    

    session.close()

    # Convert list of tuples into normal list
    temp_data = list(np.ravel(temps))
    
    return jsonify(temp_data)
    
if __name__ == '__main__':
    app.run(debug=True)
