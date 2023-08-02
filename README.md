
# Project Details
This project is an submission to assigment. This is an api repo for social networking project.

### Built with
* Python
* Django rest framework
* Postgresql
* Dockerized

# Getting Started

Please do the necessary steps
1. Make a directory
   ```sh
   mkdir accuknox
   cd accuknox
   ```
   Install 3.11 Python. Though it will support any python version. But good to have the faster one.
2. Clone the repo
   ```sh
   git clone https://github.com/dudu-krish/accuknox.git
   ```
3. Create a virtual environment
   ```sh
   virtualenv venv
   ```
   Activate the virtual environment
   ```sh
   source venv/bin/activate
   ```
4. Install all the packages from requirements file
   ```sh
   pip install -r requirements
   ```
5. I have used postgresql. So database *accu* should be created. Update the settings.py file with your database configuration.
6. Migrate the tables
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Run the server
   ```sh
   python manage.py runserver
   ```
8. Load the postman collection in postman app and hit the API's
9. Create a superadmin
    ```sh
    python manage.py createsuperuser
    ```

### Using Docker

1. Run the command
   ```sh
   docker build -t accu_api_server .
   ```
2. Run the command
   ```sh
   docker run -p 8000:8000 accu_api_server
   ```


