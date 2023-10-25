# Blogging Web Application (COMP-8157)

A Blogging website with user authentication functionality. The application has been built with the following stack:

- Front-end: HTML, JS, Bootstrap
- Back-end: Python (FastAPI)
- Database: MongoDB

The web application has the following functionalities:

- Register and authenticate users into application
- View, add and remove blogs
- View, add and remove comments to individual blogs

# Instructions to run the Application

1. Create a virtual environment: `python -m venv env` (You can substitute `env` with an environment name of your choice)
2. Activate the environment:
    1. Windows - `env\Scripts\activate`
    2. Mac/Linux - `source .\env\Scripts\activate`
       <br>_Note_: `env` is your environment name.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the backend server:
    - Run the `run-server.py` script to start the back-end server.
    - _Note_: You can also run the following command from the root directory to start the
      server: `uvicorn blogger.controller.controller:app --reload`
5. Run the web server:
    - Open a terminal of your choice and run the web server: `python -m http.server -d blogger/frontend 8080`
6. Open your browser and run the web application: http://localhost:8080
