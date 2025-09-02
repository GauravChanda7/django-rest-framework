# Django REST Framework Learning Project

This project was created to practice the fundamentals of the Django REST Framework (DRF). Below is a summary of the key concepts and features implemented in this project.

## What I Learned

This project covers the essential building blocks of creating APIs with Django REST Framework. Here's a breakdown of the key areas I explored:

### 1. Setting up the Environment

-   **Installation**: The `requirements.txt` file shows the necessary packages, including Django and djangorestframework.
-   **Project Structure**: I learned how to structure a DRF project with a `core` project folder and a `home` app.
-   **Settings Configuration**: In `core/settings.py`, I configured the `INSTALLED_APPS` to include `'rest_framework'` and `'rest_framework.authtoken'`. I also set up global DRF settings for authentication, permissions, and pagination.

### 2. Models and Serializers

-   **Models**: I created `Person` and `Color` models in `home/models.py`. These models define the data structure for the API.
-   **Serializers**: In `home/serializers.py`, I created several serializers:
    -   `PersonSerializer`: A `ModelSerializer` to convert `Person` model instances to and from JSON.
    -   `ColorSerializer`: Another `ModelSerializer` for the `Color` model.
    -   `RegisterUserSerializer` and `LoginUserSerializer`: Custom serializers to handle user registration and login.

### 3. Views and Endpoints

I created several views in `home/views.py` to handle the API logic:

-   **Function-Based Views**: I started with function-based views like `person_list` and `person` using the `@api_view` decorator to handle different HTTP methods (GET, POST, PUT, PATCH, DELETE).
-   **Class-Based Views**: I then moved on to class-based views with `APIView` in the `PersonClassAPI`, which allowed for better organization and code reuse.
-   **ViewSets**: I implemented a `PeopleViewSet` using `viewsets.ModelViewSet`, which automatically provides the standard set of CRUD operations.

### 4. URLs and Routing

-   **URL Configuration**: In `home/urls.py`, I defined the URL patterns for the different views.
-   **Routers**: For the `PeopleViewSet`, I used a `DefaultRouter` to automatically generate the URLs for the viewset.

### 5. Authentication and Permissions

-   **Token Authentication**: I implemented token-based authentication for user login. The `LoginAPIUser` view generates a token for a user upon successful login.
-   **Permissions**: I used the `IsAuthenticated` permission class to restrict access to certain endpoints to authenticated users only.

### 6. Pagination

-   **Custom Pagination**: I created a custom pagination class `CustomUserPagination` in `home/pagination.py` to control the number of items returned in a list view.

By building this project, I gained a solid understanding of how to create a RESTful API with Django REST Framework, from setting up the project to implementing advanced features like authentication and pagination.