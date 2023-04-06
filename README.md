# Nikola-Charging-Task

Here are the steps to set up and run the API on an EC2 instance and connect to RDS MySQL:

- Launch an EC2 instance in your AWS account and make sure it has access to the internet and to your RDS MySQL instance.
- SSH into the EC2 instance and install Python 3 and pip.
- Install the required packages using pip: Flask and mysql-connector-python.
- Copy the Flask app

Note that we are using environment variables to store the database credentials instead of hardcoding them in the code.

Here are the steps to create the Lambda function:

- Create an IAM role that grants the Lambda function permission to access the RDS MySQL instance and the weather API.
- Create a new Lambda function in the AWS Management Console.
- Configure the Lambda function to use the IAM role you created in step 1.
- Add the lambdaHandler.py code to the Lambda function to retrieve the latest weather data for a set of cities and update the weather data in the RDS MySQL database.
- Set up a CloudWatch Events rule to trigger the Lambda function at the desired interval (e.g. every 30 minutes).
- Save and test the Lambda function to ensure that it is updating the weather data in the RDS MySQL database correctly.

Note that you will need to set the DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, and API_KEY environment variables for the Lambda function to work correctly. You can set these environment variables in the Lambda function's configuration in the AWS Management Console.
