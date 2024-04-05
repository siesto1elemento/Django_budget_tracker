# demo_video.mp4…
https://github.com/siesto1elemento/Django_budget_tracker/assets/89785142/2c3aa132-cc69-4249-b120-512a4a7a9e52


[Track your Expense according to your Lifestyle.pptx](https://github.com/siesto1elemento/Django_budget_tracker/files/14891203/Track.your.Expense.according.to.your.Lifestyle.pptx)



# Django_budget_tracker
A budget tracker app made in django, tailored for tracking lifestyle expenses

# How to Run a Django Project




This guide will walk you through the steps to run a Django project on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.6 or later)
- Pip (Python package manager)
- Virtualenv (optional but recommended)

## Step 1: Clone the Repository

Clone the Django project repository from GitHub:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the URL of your Django project repository.

## Step 2: Create a Virtual Environment (Optional)

Navigate to the project directory and create a virtual environment:

```bash
cd <project-directory>
python -m venv env
```

Activate the virtual environment:

- **Windows:**
  ```bash
  .\env\Scripts\activate
  ```


## Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Step 4: Perform Database Migrations

Run database migrations to create database tables:

```bash
python manage.py migrate
```

## Step 5: Create a Superuser (Optional)

If your project uses Django's built-in admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account.

## Step 6: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

By default, the server will run on `http://127.0.0.1:8000/`.

## Step 7: Access the Application

Open your web browser and navigate to the URL provided by the development server (`http://127.0.0.1:8000/`).



