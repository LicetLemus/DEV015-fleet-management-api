# Point of entry for the application

from app import create_app

app = create_app()

if __name__ == '__main__':
    """
    Runs the Flask application in debug mode.

    This script is executed when the module is run as the main program. It initializes the Flask application using the 
    `create_app` function and starts the development server with debugging enabled.
    
    The application will be accessible on the default Flask port (5000) and will provide detailed debugging 
    information for development purposes.
    """
    
    app.run(debug=True) # run the application