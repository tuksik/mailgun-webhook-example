# example webapp to test mailgun webhook

This app build using flask microframework. Incoming mail will be stored on file inbox.txt

before running the example, install flask:
> pip install flask
run webapp
> python main.py
watch for incoming mail 
> tail -f inbox.txt
