# hatchd-take-home-task

## Problem Statement and Assumptions

The problem at hand was to create a single API which could be used to not only query bookings made for a parking lot with 4 spaces but also be used to allow users to book parking spaces for a particular date.
Some of the constraints were
1. A single user would be allowed to only book one parking space for any given day.
2. Bookings would have to be made 24 hours in advance of the booking date.
3. Only 4 slots would be available for any parking space. After 4 slots were to be filled, No further booking would be allowed.


## Assumptions
Some of the assumptions I made are as follows.
1. All customers have one single car with a unique license number.
2. Booking date starts at 12am
3. License plate numbers and names are less than 500 characters in length
4. Names can be blank too.


## To setup application
1. First create a virtual environment using `Python -m venv 'somename'`
2. Activate the virtual enviroment
3. run `pip install -r requirements.txt` to install all packages needed
4. run `python manage.py migrate` to run all migrations
5. run `python manage.py runserver` to start the server at `http://localhost:8000/`

## To access Django admin panel (optional)
1. Run `python manage.py createsuperuser` to create a superuser and go to `http://localhost:8000/admin/` to access the admin panel

## To run API

1. Open Postman
2. paste in the following url `http://127.0.0.1:8000/parking/parkinglot/`
3. Run the API with different parameters for GET and POST respectively
4. POST will take a simple JSON object as a post object:` {
    "name":"taariq",
    "license_plate_number":"taariq52",
    "date":"2022-05-28"
}`

5. GET will have date as a query parameter like `http://127.0.0.1:8000/parking/parkinglot/?query_date=2022-05-28`


## To run tests
1. Run `python manage.py test` to run all test cases

