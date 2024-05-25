# Django Chat Application

This project is a Django application integrated with Tailwind CSS for styling. It leverages Django Channels for real-time chat functionality.


## Installation

### Prerequisites

- Python 3.x
- Node.js and npm
- PostgreSQL (or another supported database)

### Clone the Repository

```bash
git clone https://github.com/wilderherrera/django-chat.git
cd django-chat
```
### Run a virtual enviroment
```bash
python3 -m venv venv
source venv/bin/activate 
```

### Install requirements
```bash
pip install -r requirements.txt
```
### Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Frontend Setup with Tailwind CSS

This project uses Tailwind CSS for frontend styling. Follow these steps to set it up:

1. **Install Node.js and npm**: If you haven't already, download and install [Node.js](https://nodejs.org/), which includes npm (Node Package Manager).

2. **Install Tailwind CSS**: Once Node.js is installed, open your terminal and run the following command to install Tailwind CSS globally:

    ```bash
    npm install -g tailwindcss
    ```
3. **Installing missing dependencies**: 
```bash
npm install --save-dev cross-env
npm install postcss-simple-vars
npm install @tailwindcss/forms
npm install @tailwindcss/typography
npm install @tailwindcss/aspect-ratio
npm install --save-dev rimraf
4. **Initialize Tailwind CSS**: Navigate to your project directory and run the following command to create a `tailwind.config.js` file and `tailwind.css` file in your project:

    ```bash
    npx tailwindcss init
    ```

    This command initializes Tailwind CSS and generates a default configuration file.

5. **Include Tailwind CSS in Your Django Project**: To use Tailwind CSS in your Django project, include the generated `tailwind.css` file in your project's static files. You can import this CSS file in your HTML templates or use it with a tool like Webpack for bundling.

6. **Use Tailwind CSS Classes**: Once Tailwind CSS is set up, you can start using its utility classes in your HTML templates. Refer to the [Tailwind CSS documentation](https://tailwindcss.com/docs) for a list of available classes and how to use them.

7. **Compile Tailwind CSS**: If you make changes to your Tailwind CSS configuration or want to build optimized CSS for production, you need to compile Tailwind CSS. Run the following command to compile your CSS file:

    ```bash
    npx tailwindcss build tailwind.css -o output.css
    ```

    Replace `tailwind.css` with the path to your Tailwind CSS file and `output.css` with the desired output file name.

That's it! You've now installed and set up Tailwind CSS with your Django project. Happy styling!
  ```

### Build taildwind css styles
 ```bash
    python manage.py tailwind build
 ```
### Run Application
 ```bash
    python manage.py runserver 0.0.0.0:8000
 ```

## Test deployed applications 
This application is running in a AWS EC2 instance, you can check it on:

http://54.225.132.16:8000/auth/v1/login/

## Throttle Explanation
The chat has a limitation rate of request upon the socket server, this configuration is in the setting.py, there you could find something like:

![image](https://github.com/wilderherrera/django-chat/assets/42052737/0b65c848-b202-4a3e-97ad-48d108606535)

In this configuration it could be set a limit per minute of request that the server allow, if this limit is reached when the cliente try to send a message, an error will be printed:

![image](https://github.com/wilderherrera/django-chat/assets/42052737/7c3cfec3-7850-4959-be9d-3880c0f5d017)

# How to use the app
## Test deployed applications 
When you start the application you have to login as a first step, you can use this credentials:

![image](https://github.com/wilderherrera/django-chat/assets/42052737/dfc51c9d-15c8-4908-8a31-c15044039cfd)


```bash
username: wilder
pass: 20532050a
 ```
or go to sign up option and create your user, take in account that the password must be longer than 8 characters and it must has numbers and letters.
![image](https://github.com/wilderherrera/django-chat/assets/42052737/c1f7de86-fbda-4650-a8e6-0b4159e8e5c3)


when the user is created the app will redirect you to home page.
here you will find a list of chat rooms created before and the option to create a new one.

![image](https://github.com/wilderherrera/django-chat/assets/42052737/5e62242f-1d59-4453-85ff-6c6f080cd1d7)

both creating or using an existing chat room after click on it you will be in the chat room and you could start chatting.

![image](https://github.com/wilderherrera/django-chat/assets/42052737/15399090-a87d-4603-8f91-b7c007906d88)

When you send a message all people in the chat room will receive it, for example in this image another user send a message over the chat room

### Wilder Chat

![image](https://github.com/wilderherrera/django-chat/assets/42052737/bc24c248-26dd-4068-980f-8c0d3201490a)

### Katherine chat (On mobile device, responsive design is enabled by tailwind css)


![image](https://github.com/wilderherrera/django-chat/assets/42052737/9d866b06-6fb8-48d2-9bc5-f4a64371f644)

This is depicted with a different background color. When the user refreshes the web page, all messages in the conversation will be retrieved and displayed in the view.

## Technical Explanation

The application was developed using Django Channels, which allows for asynchronous communication and the socket implementation required for this project. To support this functionality, an ASGI server was enabled and Redis was configured as a cache manager. All messages, along with the system to retrieve messages after a web page refresh, are managed using Redis to ensure quick and efficient data retrieval.

For user management, the built-in Django authentication system was utilized, providing robust and secure user authentication and authorization. The front-end of the application was developed using Django templates, ensuring seamless integration with Django's backend and facilitating dynamic content rendering.

A comprehensive logging system was created and formatted using the settings.py file, enabling effective monitoring and debugging of the application. All requests are logged by a custom middleware, capturing details of each API call and other critical events, which helps in maintaining the application's reliability and security.

As a challenge point, throttling was implemented on the socket server to establish a limit on requests, preventing abuse and ensuring fair usage.Automated testing were managed using GitHub Actions, with a django.yml configuration file located in the .github/workflows directory.

System testing was thoroughly conducted using Django's TestCase and Channels testing frameworks, ensuring the application's functionality and performance under various conditions.

Finally, the application was deployed on an AWS instance to provide internet access, ensuring scalability and accessibility for users.





