skywatch provider scraper
===================

This scraper was built to retrieve a list of data set provider from  [skywatch website](https://www.skywatch.co/datasets)

> SkyWatch is on a mission to make satellite data accessible to the
> world. Every day, trillions of pixels are captured by satellites
> orbiting our planet. With new applications for this data being
> discovered every week, the demand for this imagery is increasing
> across many industries.

Live execution available at AWS Lambda API:
https://jwqnrdh5v1.execute-api.us-east-1.amazonaws.com/dev/skywatchDataSet

Using a request tool like Postman, execute link above with a POST request.

Should return a json:

    {
	    "datasets": {
	        "Name1": "Provider1",
   	        "Name2": "Provider2",
    },
	    "total": 2
	}

