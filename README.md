# Dynamic-Question-Pop-up

## Overview

This project is a Django-based web application designed to update credit scores based on user responses to dynamically generated questions. The system includes an algorithm that calculates a credit score based on predefined factors and a pop-up interface that presents questions one by one for user input.

---

![image](https://raw.githubusercontent.com/abdrrahim2002/Dynamic-Question-Pop-up/refs/heads/main/images/1.png)

![image](https://raw.githubusercontent.com/abdrrahim2002/Dynamic-Question-Pop-up/refs/heads/main/images/2.png)

![image](https://raw.githubusercontent.com/abdrrahim2002/Dynamic-Question-Pop-up/refs/heads/main/images/3.png)

---

## Features

- Dynamic Question Pop-up: Displays questions one by one in a modal interface.

- Credit Scoring Algorithm: Computes a user's credit score based on their responses.

- Configurable Questions: Each question has 4 options to choose from, and you can add as many questions as needed.

## Technologies Used

- Django 4.2
- bootstrap
- crispy-bootstrap4
- django-crispy-forms
- django-formtools

## Installation

1. Clone the repository

```
git clone https://github.com/abdrrahim2002/Dynamic-Question-Pop-up.git
```

2. Create and activate a virtual environment

```
virtualenv env
source env/bin/activate
```

3. Enter to the project folder and install dependencies

```
cd Dynamic-Question-Pop-up
pip install -r requirements.txt 
```
> [!NOTE]
> No need to run migrations as they are already configured.

4. Create super user

```
python manage.py createsuperuser
```

5. Start the development server

```
python manage.py runserver
```

6. Access the application

Open `http://127.0.0.1:8000/` in your web browser.

7. Setup the questions

- Go to the admin dashboard at `http://127.0.0.1:8000/admin`.
- Navigate to **Questions** to configure your questions.

![image](https://raw.githubusercontent.com/abdrrahim2002/Dynamic-Question-Pop-up/refs/heads/main/images/4.png)

> [!NOTE]
> By default <br>
> Option 1 = 10 points <br>
> Option 2 = 7 points <br>
> Option 3 = 4 points <br>
> Option 4 = 0 points <br>
> You can change these values by modifying the numbers in the **get_score_by_select** and **calculate_result** functions in the **views.py** file located in the **Credit_Bereau_Score** folder.

![image](https://raw.githubusercontent.com/abdrrahim2002/Dynamic-Question-Pop-up/refs/heads/main/images/8.png)

8. Track user responses

- In the **User responses** section of the **admin dashboard**, you can track user responses.

![image](https://raw.githubusercontent.com/abdrrahim2002/Dynamic-Question-Pop-up/refs/heads/main/images/5.png)

![image](https://raw.githubusercontent.com/abdrrahim2002/Dynamic-Question-Pop-up/refs/heads/main/images/6.png)

- In the **User profiles** section of the **admin dashboard**, you can view the total score of each user.

![image](https://raw.githubusercontent.com/abdrrahim2002/Dynamic-Question-Pop-up/refs/heads/main/images/7.png)

---

# Acknowledgments

Thank you for checking out this project! Your feedback and contributions are greatly appreciated. Happy coding! 🚀
  
