1. # hackathon-2
2. project of the second hackathon
3. E-commerce Store Setup
4. Backend Setup (Django & Django Rest Framework)
5. Install Django and Django Rest Framework:
    - Use pip to install Django and DRF.
6. Start a new Django project:
    - Create a new Django project.
    - Navigate into the project directory.
7. Create a core app:
    - Inside your project directory, create a new app called "core".
8. Add rest_framework and core to INSTALLED_APPS in settings.py:
    - Open settings.py and add 'rest_framework' and 'core' to the INSTALLED_APPS list.
9. Create models for User, Product, Cart, and Order:
    - Define the models for User, Product, Cart, and Order in core/models.py.
10. Create serializers for the models:
     - Create serializers for User, Product, Cart, CartItem, Order, and OrderItem in core/serializers.py.
11. Create viewsets for the models:
     - Create viewsets for User, Product, Cart, CartItem, Order, and OrderItem in core/views.py.
12. Set up URLs for the API endpoints:
     - Register the viewsets with a router in core/urls.py.
     - Include the core.urls in the main urls.py of your project.
13. Run database migrations:
     - Apply the database migrations.
14. Create a superuser:
     - Create a superuser to access the admin interface.
15. Run the development server:
     - Start the development server.
16. Frontend Setup (JavaScript, HTML, CSS)
17. Create the HTML file:
     - Create an index.html file with the basic structure for your frontend, including a header and a main section to display products.
18. Create the CSS file:
     - Create a styles.css file with basic styles for the HTML elements.
19. Create the JavaScript file:
     - Create a script.js file and use the Fetch API to retrieve the product data from the backend and display it in the HTML.
20. Running the Project
     - Ensure the backend server is running:
        - Make sure the Django development server is running.
     - Open index.html in a browser:
        - Open the index.html file in your web browser to view the frontend.
