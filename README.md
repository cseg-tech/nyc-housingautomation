# NYC Housing Complaint Alert System
A notification system that alerts NYC tenants, tenant organizers, and other users who sign up for the service whenever a housing complaint is filed in their building.

## Project Details
Please find this project's scope document and other details <a href="https://github.com/cseg-tech/nyc-housingautomation/blob/master/docs/ProjectScope.md">here</a>

## Requirements
This project requires both Python, and NodeJS to run. The backend has been built in Flask, which is dependant on Python3.6, while the frontend is built in ReactJS, and requires either npm or yarn to install the required packages.

## Setup:
 - Navigate to project directory on terminal, ensure that dependancies are installed
 - Setup a virtual environment using virtualenv venv. Download virtualenv <a href="https://www.andreagrandi.it/2018/12/19/installing-python-and-virtualenv-on-osx/">here</a>
 - Install the required packages from requirements.txt into your venv
 - Ensure that your MongoDB instance is active
 - Naviate to app/static, and run ```npm install``` to install the required dependancies for the ReactJS frontend.
 - From the root, run ```./refreshReact.sh``` to generate a fresh build of the ReactJS frontend.
 - This project requires a .env file at its root to run. Please contact the authors for access to the same, or compile your own based on the guidelines below.
 - ```python run.py```

## Unit Tests:
 - To run unit tests on the backend, run ```python -m unittest tests.py``` from your root directory.
 
## Environment Variable Guidelines
 This project depends on a number of environment variables to run succesfully. The same have been listed and described below.
 - NYC_311_TOKEN: Token to query NYC Open Data's 311 database. Ref <a href="https://opendata.cityofnewyork.us/">here</a>
 - GEOCLI_ID: A valid ID for the NYC <a href="https://maps.nyc.gov/geoclient/v1/doc">GeoClient API</a>
 - GEOCLI_KEY: A private key for the same ID to the NYC <a href="https://maps.nyc.gov/geoclient/v1/doc">GeoClient API</a>
 - MONGO_UNAME: A username for a MongoDB Atlas Cloud Instance with the appropriate database permissions
 - MONGO_PASS: A password for the afformentioned MongoDB user instance
 - SENDGRID_KEY: An API key to access SendGrid's email sending service. Ref <a href="https://sendgrid.com/">here</a>

## License
![GitHub](https://img.shields.io/github/license/cseg-tech/nyc-housingautomation.svg)

Released under a GNU General Public License (v3.0). For the full text of the license see `LICENSE`.

## Contact
Built by a team of developers at [CSEG Tech](http://www.columbiaseg.org).

Email: columbiaseg@gmail.com
