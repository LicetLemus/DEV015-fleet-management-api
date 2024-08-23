# Point of entry for the application

from src import create_app

app = create_app()

if __name__ == '__main__':
    app.run() # run the application