# Import necessary modules
# 'create_app' is a factory function from 'app' module that initializes and configures the Flask app
from app import create_app

# Initialize the Flask app
# This calls the 'create_app' function to create an instance of the Flask application
app = create_app()

# The main entry point of the application
# '__name__' is a special Python variable that is set to '__main__' when the script is executed directly
if __name__ == "__main__":
    # Run the Flask application with debugging enabled
    # 'app.run()' starts the Flask development server
    # 'debug=True' allows for automatic reloading on code changes and shows detailed error messages
    app.run(debug=True)
