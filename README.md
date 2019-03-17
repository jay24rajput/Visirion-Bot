# Visirion-Bot

## Proposed Solution
This app is used for automated merge, rebase, squashing, fast forwarding of pull requests on version control systems, like Github. <br>
It acts as a chatbot to make it easy for new developers to manage large codebases, by enabling them to use basic commands on the Github comments section.

## Workflow
- Fork the original repository of the organisation or user.<br>
- Checkout to some branch. <br>
- Push to your branch. <br>
- Compare and send pull request.<br>
- Once the maintainer reviews the pull request he will trigger the bot as: <br>
**```@visirion```**```rebase``` <br>
- Wait for visirion to perform rebase, once done all the changes will be in sync with master.

## How to Set up (Only for maintainers)
- Clone and download the repository: <br>
```git clone https://github.com/jay24rajput/Vision-Bot.git``` <br>
- Install dependencies: <br>
```pip3 install -r requirements.txt --user``` <br>
- Run the server: <br>
```python3 manage.py runserver``` <br> 
- Publish the localhost as: <br>
``` ngrok http -host-header=rewrite localhost:8000``` <br>
- Create webhooks for your repository: <br>
[Webhooks for github](https://developer.github.com/webhooks/creating/)
- Enter the **http** address from the ngrok: <br>
eg: ```http://6712e41e.ngrok.io``` <br>
- Generate and Enter the secret key <br>
```
$ python manage.py shell
   from django.utils.crypto import get_random_string
   get_random_string(50)
```
- Update webhook and deliver the request and check the response.

## Perfoming Rebase
When not doing a fast forward merge, your git history looks like this: <br>
![bad-history](data/bad-history.png)
<br>

Chaos. This makes it pretty difficult to figure out what code is where and when and how it got there.
When you rebase and only do fast forward merges, you get a git history that looks like this:<br>
![clean-history](data/clean-history.png) <br>
A nice, clean, straight line. This makes it sooooo much nicer! <br>

### This is how the Visirion Bot performs Rebasing

![Rebase%20Message](data/Rebase%20Messge.png) <br>
