# sqlalchemy-challenge

There are two files, app-Andaya.py, and climate_starter-Andaya.ipynb

The Resources folder contains the sqlite database

# climate_starter-Andaya.ipynb NOTES

Below are some captured images of charts and a histogram once the code is run.
Make note, there are two charts, one corresponding to all data from each date plotted, and one of only the maximum precipitation for a given date.


![Screenshot 2023-03-01 at 9 20 46 AM](https://user-images.githubusercontent.com/115322974/222214737-171dfc88-3ab4-40f1-9a5f-400a34481e54.png)
![Screenshot 2023-03-01 at 9 20 56 AM](https://user-images.githubusercontent.com/115322974/222214910-72a0b9fa-aa6d-40ef-9de9-ce133fa9fb8e.png)
![Screenshot 2023-03-01 at 9 21 18 AM](https://user-images.githubusercontent.com/115322974/222215115-45f62509-6888-4a92-beef-2b01e358e5ed.png)


# app-Andaya.py NOTES

For the dynamic route portion of the code (i.e. looking for minimum, maximum, and average temps for specific date ranges), dates inputted should be in the format of year-month-day into the URL


For year, four numbers are needed, for month or day, two numbers are needed for each


Thus, for example, for the date of May 7, 2015, the input should be (2015-05-07) and not something like (2015-5-7).


Specifically, if looking for data with a start date of May 7, 2015, the URL is (http://127.0.0.1:5000/api/v1.0/2015-05-07)

And for looking for data with a start date of May 7, 2015 and an end date of July 8, 2016, the URL is (http://127.0.0.1:5000/api/v1.0/2015-05-07/2016-07-08)
