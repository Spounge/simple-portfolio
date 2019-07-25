# Simple Portfolio

A simple portfolio and blog using the Django web framework.


# Installation

## Heroku

To deploy on heroku

1. Click this button

    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Spounge/simple-portfolio/tree/master)

2. Wait for the build to finish and click on **manage app**

3. Click on **more** and run a console with bash.

4. Create a super user by running the command `./mysite/manage.py createsuperuser`

5. You can now open the application and access the admin site to add Posts and Jobs


## Linux

### Dependencies

- Python3
- PostgreSQL

To run locally

1. Clone this repo and enter it

2. Create a virtual environnement by running `bash python3 -m venv env` and source it `source env/bin/activate`

3. Install dependencies `pip install -r requirements.txt`

4. Create a PostgreSQL database called `portfoliodb` and owned by `postgres` with the password `123` (You can eventually modify `my/portfolio/settings.py` to you convinience).

5. Create a super user by running the command `./mysite/manage.py createsuperuser`

6. You can now run `./mysite/manage.py runserver`, open the site at `127.0.0.1:8000` and access the admin site to add Posts and Jobs


# Screenshots

![jobs_screen](https://user-images.githubusercontent.com/30945808/61883758-53f37800-aefb-11e9-9433-094b533dcf08.png)

![blog_screen](https://user-images.githubusercontent.com/30945808/61883792-5e157680-aefb-11e9-8aa9-4a297c579b00.png)
