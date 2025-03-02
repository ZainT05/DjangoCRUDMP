How to Setup this Project:

Precaution: Python, Pip, and XAMPP/MariaDB(MySQL) is needed to run this project

Step 1: Clone/Download the Project to get the files

Step 2: Open your MySQL or XAMPP to access PhpMyAdmin

Step 3: Import the Database you got from the GitHub Repository called: "student_db.sql" inside the PhpMyAdmin in the SQL Import Section

Step 4: Create a folder called "Django" and then go inside the folder then paste the folder inside that you got from the GitHub Repository called: "student_management"

Step 5: Run a Command Prompt/Terminal inside the folder and then setup a Python Virtual Environment called "venv" by typing: "python -m venv venv" or "py -m venv venv" now you are inside the Python's virtual environment

Step 6: Run the venv or Python's Virtual Environment by typing "venv\Scripts\activate" and then install MySQL so Django and MariaDB can work by typing: "pip install mysqlclient"

Step 7: Navigate to the "student_management" folder by typing "cd student_management"

Step 8: Type "python manage.py runserver" to run the Django Server

Step 9: Visit Django's default url link which is: 127.0.0.1:8000

Step 10: Explore the site and its features especially the CRUD(Create, Read, Update, Delete) Functions
