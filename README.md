# Recipes_Reviews
Simple website to manage/review receipes

Recipe Management and Review with Django
This is a repository for a web application built with Django that allows users to manage recipes and write reviews for them. It provides a convenient way to store and organize recipes, as well as share your thoughts and feedback on each recipe.

Features
User authentication: Users can create an account, log in.
Recipe management: Admin can create, edit, and delete recipes and ingredients.
Recipe review: Users can write reviews for recipes .
User dashboard: Users have a personalized dashboard to view recipes and reviews.
Admin panel: Admin  have access to an admin panel to manage recipes,and ingredients

Installation

1-Clone the repository:git clone https://https://github.com/hatim9681/Recipes_Reviews.git


2-Create and activate a virtual environment (optional but recommended):
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate  # For Windows

3-Install the dependencies:
pip install -r requirements.txt

4-Set up the database:
python manage.py makemigrations
python manage.py migrate

5-Create a superuser account
python manage.py createsuperuser

6-Start the development server:
python manage.py runserver

Open your web browser and visit http://localhost:8000 to access the application.


7-Usage
Once the application is running, you can register a new account or log in with your existing account. After logging in, you'll have access to the various features mentioned above, such as creating recipes, writing reviews, and register
