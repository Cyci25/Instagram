# InstagramClone

 This is a clone of the website for the popular photo app,Instagram.This application was created on 15th December 2018

# Author
Cynthia Muriithi

## Link to Deployed Site on Heroku


## Setup and installation

- Clone the Repo uding the following command:

- Activate virtual environment using python3.6 as default handler by running 
    `python3.6 -m venv virtual` then enter the virtual environment using `source virtual/bin/activate`
- Download the latest version of pip in the virtual environment: `$ curl https://bootstrap.pypa.io/get-pip.py | python`

- Install all application dependancies 
`pip install -r requirements.txt`

- Create the Database
    -On the terminal,run `psql`
    - Create a database by typing 
      `CREATE DATABASE instagram;` for example.

- Create a .env file and add the following:

    - SECRET_KEY = `<Secret_key>`
    - DB_NAME = `instagram`
    - DB_USER = `<Username>`
    - DB_PASSWORD = `your db password`
    - DEBUG = `True`

- Run Initial Migration
    `python3.6 manage.py makemigrations <name of the app>`
    `python3.6 manage.py migrate`

- Run the app
    `python3.6 manage.py runserver`
    `Open terminal on localhost:8000`

## User Stories
The application user is able to:
- Create an account and confirm through email verification.
- Sign in to the application to start using.
- Upload pictures to the application and edit their profile.
- See their profile with all their uploaded pictures.
- Follow other users and see their pictures on the timeline.
- Like a picture and leave a comment on it.
 
## Admin
The application admin is able to:
- Regulate images uploaded deleting them from the admin dashboard.
- Close a users account.

## Technologies Used
- Python 3.6.6(Django Framework)
- HTML5
- CSS3
- Bootstrap4
- Bootstrap3
- Postgresql
- Heroku(Deployment)
- Visual Studio Code text editor

## Known Bugs
No known bugs so far.Contact me if you come across any.

## Support and Contact Details
For any comments,suggestions,feedback or inquiries about my application,Contact me via email:c2muriithi@gmail.com


## License
*MIT License*
Copyright <2018> <Cynthia Muriithi>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2018 **Cynthia Muriithi**
