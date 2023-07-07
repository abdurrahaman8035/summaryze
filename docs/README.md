# Summaryze

Summaryze is a web application that provides an automated text summarization service to users. It uses the GPT-3 API to generate a summary of uploaded handouts in PDF, DOCX or TXT format.

## Getting Started

These instructions will help you set up a local development environment and get the app running on your machine.

### Prerequisites

- Python 3.7 or higher
- Django 3.2 or higher
- GPT-3 API key (for production use only)

### Installing

1. Clone the repo to your local machine using the following command:

```
git clone https://github.com/your-username/summaryze.git
```

2. Navigate to the project directory:

```
cd summaryze
```

3. Create a virtual environment and activate it:

```
python3 -m venv env
source env/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Run the development server:

```
python manage.py runserver
```

6. Open your browser and navigate to `http://localhost:8000` to access the app.

### Deployment

To deploy the app to a production environment, you will need to:

1. Set up a PostgreSQL database on a cloud platform like Heroku.
2. Configure your production settings in `settings.py`.
3. Set the `DJANGO_SECRET_KEY` and `GPT3_API_KEY` environment variables.
4. Deploy the app using a tool like Heroku CLI or Git.

## Built With

- Python 3 - The programming language used
- Django 3 - The web framework used
- Bootstrap 4 - The CSS framework used
- GPT-3 API - The text summarization API used

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the GPT-3 API
- Stack Overflow for providing helpful solutions to development problems