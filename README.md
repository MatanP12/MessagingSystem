# MessagingSystem
A simple messaging system API implemented using Python and Django framework

# Getting started
1. Clone the [MessagingSystem](https://github.com/MatanP12/MessagingSystem) repository
2. Open any terminal and navigate to the project directory.
3. Run `run` command.
4. Run `python manage.py runserver` command.
5. make HTTP calls to `http://localhost:8000` 

# API
* POST `/login` with username and pssword in the body will login to the 
>  username: "MotiLuchim",
>  password: "moti1234"
* GET `/messages` will recieve all the messages to the loggen in user.
* POST `/messages` with message 
> subject: "First message"      
> message: "This is my first message!!"   
> receiver: "KerenLaser"
 * GET `/messages/new` will get only the new messages for the logged in user.
 * PUT `/messages/<int:message_id>` will recieve the message with the given id and mark it as readed.
 * DELETE `/messages/<int:message_id>` will delete the message with the given id

**There is a postman collection for another examples**