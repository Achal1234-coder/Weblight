# How to run the Project

## Step 1:- make one directory in your system let xyz

```
cd xyz
```
and clone the repo in this directory

```
git clone https://github.com/Achal1234-coder/Weblight.git
```

## Step 2:- Activate the virtual env

### For Ubuntu Run this commands

```
virtualenv env

source env/bin/activate
```
### For Windows run this commands

```
virtualenv env

env/Scripts/activate
```

Make sure virtualenv library installed globally

## Step 3:- Install Dependencies of application by run this command

```
pip install -r requirements.txt
```

## Step 4:- Run Make Migrations Command

```
python manage.py makemigrations
```
## Step 5:- Run Migrate Command

```
python manage.py migrate
```
## Step 6:- Create Super User to see the changes in database

```
python manage.py createsuperuser
```

## Step 7:- To run the server run this command

```
python manage.py runserver
```

## Note 1 :- Before run the API's please make a account on Twilio and Razorpay because some secret keys used in this application so you have to replace it in settings.py file(For security reason you also used environment file)

## Note 2:- Please replace this variables in settings.py file with yours, You will find this variable on Your Twilio account

```
ACCOUNT_SID='Your Sid Key'
AUTH_TOKEN='Your Token'
COUNTRY_CODE='+91'
TWILIO_PHONE_NUMBER='Your twilio phone no'
```
## Note 3:- Please Replace this variables in settings.py file with yours, You will find this variable on your Razorpay account(generate key)

```
RAZORPAY_KEY_ID = 'Your razorpay key'
RAZORPAY_SECRET = 'Your razorpay secret'
```

## Note 4:- In this application there are 7 API's are following as:-

### 1) For Registration hit this API from Postman
```
http://127.0.0.1:8000/

Method:- POST
```
### You have to give Form Data Input as shown in example:

```
phone_number : User Phone Number

user_name : Your name
```

## Please make sure both phone_number and user name should be unique and given phone number should registered in twilio account for gettong OTP otherwise you will not getting OTP

## 2) For Login hit this API from postman

```
http://127.0.0.1:8000/login/

Method:- POST
```
### You have to give this input in Form Format

```
phone_number : User Phone Number
```
### Your output come in this Format

```
{
    "messgae": "OTP send successfully on your phone no",
    "status": "Success"
}
```

## 3) For Verification of OTP hit this API

```
http://127.0.0.1:8000/otp/

Method:- POST
```
### You have to give this input in the Form Format

```
phone_number : your phone number

otp : 4 digit(otp)
```

### Your output come in this format

```
{
    "message": "User Successfully Log In",
    "status": "Success",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5OTgzNjU3LCJpYXQiOjE3MDk5ODMwNTcsImp0aSI6ImFjZTgwNWJiZTIyYjQzNDhiMzg5NzZlNjhlZmVhODFlIiwidXNlcl9pZCI6MX0.S6AQpbeAurmjQX23X2gXjdbgQVT6b2f8OmEQ96NTtWs"
}
```
### Note:- You have to copy this token to access payments API's this token is valid for 10 min after 10 min you have to login again. To get this token you have to validate your phone no.

## 4) For logout hit this API

```
http://127.0.0.1:8000/logout/

Method:- GET
```

### You have to give this input in the JSON Format

```
{
    "phone_number": "your phone number"
}
```

## 5) For Donation hit this API

```
http://127.0.0.1:8000/payment/

Method:- POST
```

### You have to give this input in the Form Format and also you have to give token in Headers

```
phone_number  : your phone number

amount  : enter donation price
```

### Note:- Give this token in headers of postman request

```
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5OTgzNjU3LCJpYXQiOjE3MDk5ODMwNTcsImp0aSI6ImFjZTgwNWJiZTIyYjQzNDhiMzg5NzZlNjhlZmVhODFlIiwidXNlcl9pZCI6MX0.S6AQpbeAurmjQX23X2gXjdbgQVT6b2f8OmEQ96NTtWs

```

## 6) For Getting Payment history hit this API

```
http://127.0.0.1:8000/payment/history/

Method:- GET
```

### Input in JSON format

```
{
    "phone_number": "1234567890"
}
```

### Note:- Give this token in headers of postman request

```
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5OTgzNjU3LCJpYXQiOjE3MDk5ODMwNTcsImp0aSI6ImFjZTgwNWJiZTIyYjQzNDhiMzg5NzZlNjhlZmVhODFlIiwidXNlcl9pZCI6MX0.S6AQpbeAurmjQX23X2gXjdbgQVT6b2f8OmEQ96NTtWs
```

## 7) For Getting Data Visualization hit this API

```
http://127.0.0.1:8000/payment/data_visualization/

Method:- GET
```

### Input in JSON format

```
{
    "phone_number": "1234567890"
}
```

### Note:- Give this token in headers of postman request

```
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5OTgzNjU3LCJpYXQiOjE3MDk5ODMwNTcsImp0aSI6ImFjZTgwNWJiZTIyYjQzNDhiMzg5NzZlNjhlZmVhODFlIiwidXNlcl9pZCI6MX0.S6AQpbeAurmjQX23X2gXjdbgQVT6b2f8OmEQ96NTtWs
```
