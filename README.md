# NYC Housing Complaint Alert System
A notification system that alerts NYC tenants, tenant organizers, and other users who sign up for the service whenever a housing complaint is filed in their building.

## Technical Information:
### Setup:
 - Navigate to project directory on terminal, ensure that dependancies are installed
 - Setup a virtual environment using virtualenv venv. Download virtualenv <a href="https://www.andreagrandi.it/2018/12/19/installing-python-and-virtualenv-on-osx/">here</a>
 - Install the required packages from requirements.txt into your venv
  - Ensure that your MongoDB instance is active
 - ```python run.py```

## Unit Tests:
 - To run unit tests, run ```python -m unittest tests.py``` from your root directory.

## Overview
### Use Cases
- **Tenants** can use the tool to coordinate with other tenants, gather supporting evidence for housing court proceedings, or generally be informed of the complaints being filed in their building.
- **Tenant Organizers** can use the tool to monitor all the issues being reported in the buildings and complexes they work with.
- **Family and friends of vulnerable tenants** can use the tool to be informed of any issues being reported in the building their elderly relatives are living in (e.g. mold, lack of heating).

### Goals
- **Reduce lead times** between tenants experiencing issues and tenant organizers or relatives being informed of those issues.
- **Help tenant associations and community groups** monitor housing conditions.
- **Facilitate tenant organizing** by keeping tenants informed about the housing issues in their buildings.

## Built With

## Features
This project is under active development.

### Current Features
- Create an account to manage alert preferences
- Select building(s) to receive alerts for
- Select complaint categories to receive alerts for (e.g. heat/hot water)
- Select alert frequency

### Future Development
Additional alert categories:
- **Evictions.** Support for eviction-related updates.
- **Permit Issuance.** Support for development approval-related updates.

Additional account functionality:
- **Status update.** Updates on when complaints are marked as closed and whether a violation was issued.
- **View recent complaint activity.** Create a basic summary of the complaint and violation histories for the selected building(s) and categories.
- **Facilitate the filing of 311 complaints.** Prompt users about filing 311 complaints for the issues they are monitoring. Display complaint history in the selected building(s) for categories not selected (e.g. “Others in your building have reported X, Y, Z issues, as well. Are you experiencing these issues?”).
- **NYCHA residents.** Identify NYCHA addresses and refer user to MyNYCHA.
- **Right to Counsel.** Identify potential RTC eligibility by zip code and refer user to info about RTC.
- **Link to other resources.** E.g. JustFix.nyc, Heat Seek, Legal Aid Society, etc.

Additional alert mediums:
- **SMS alerts**

Additional languages:
- **Spanish**

## License
![GitHub](https://img.shields.io/github/license/cseg-tech/nyc-housingautomation.svg)

Released under a GNU General Public License (v3.0). For the full text of the license see `LICENSE`.

## Contact
Built by a team of developers at [CSEG Tech](http://www.columbiaseg.org).

Email: columbiaseg@gmail.com
