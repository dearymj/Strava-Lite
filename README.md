# Strava Lite

## GitHub Repository
[https://github.com/yourusername/strava-lite](https://github.com/yourusername/strava-lite)

## Name & Stevens Email
- Mingjing Yuan. 
- myuan5@stevens.edu

## Project Title
"Strava Lite"

## Description
This is a basic Flask server that helps users track their running workouts. It allows:
- User registration with a generated UUID
- Retrieval of user information
- Removal of users
- Listing all users
- Adding workouts to a user
- Listing workouts for a user

(Extra Credit)
- Following other users
- Viewing followed users’ workouts

## Bugs / Issues and Solutions
- **Issue**: Missing required fields caused 500 errors initially because of KeyErrors.  
  **Solution**: Added checks for required fields and return 400 if missing.
  
- **Issue**: Using `user_id` strings incorrectly as keys.  
  **Solution**: Ensured consistent use of UUID strings as keys in the `data_store`.

- **Issue**: Not returning 404 when user doesn't exist.  
  **Solution**: Checked `user_id` existence in `data_store` before accessing user data, returning 404 if not found.
