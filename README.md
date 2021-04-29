# Covid19 India Data API

An API that scrapes [covid19india.org](https://www.covid19india.org/) for data and provides it in JSON format.

## Endpoints

This API has a single endpoint [/statecoviddata](https://covid19indiaorgapi.herokuapp.com/statecoviddata).
This endpoint provides all the Covid data of all the Indian states in the following form :-

[
    {
        "state_name": "Maharashtra",
        "confirmed": 4539553,
        "active": 670301,
        "recovered": 3799266,
        "deceased": 67985,
        "tested": 27000000,
        "vaccine_doses": 15000000
    },
]

## Author 
- [anshul3pathi](https://github.com/anshul3pathi)