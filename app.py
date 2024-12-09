from flask import Flask
from flask_restful import Api
from uuid import uuid4
from constants import APP_VERSION, DEFAULT_PORT

# In-memory Data Store
data_store = {
    "users": {}
}

def create_app():
    app = Flask(__name__)
    api = Api(app)

    # Import resources from api.py
    from api import UserListResource, UserResource
    # Change the route for listing all users to "/users"
    api.add_resource(UserListResource, '/users', endpoint='userslist', resource_class_kwargs={'data_store': data_store})

    # Add a separate resource or modify the existing UserListResource to only POST on "/user"
    # One approach: Add a separate route for POST /user by using the same resource but relying on the method
    api.add_resource(UserListResource, '/user', endpoint='userpost', resource_class_kwargs={'data_store': data_store})
    api.add_resource(UserResource, '/user/<string:user_id>', endpoint='userresource', resource_class_kwargs={'data_store': data_store})

    # Register non-RESTful routes from routes.py
    from routes import register_routes
    register_routes(app, data_store)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=DEFAULT_PORT)
