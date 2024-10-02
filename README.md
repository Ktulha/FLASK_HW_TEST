# FLASK_HW_TEST

Here is the complete list of app routes:

GET Routes:


'/' - Returns an HTML page using the index.html template, and passes the users and posts dictionaries as variables to the template.
'/get_users' - Returns a JSON response containing the users dictionary.
'/get_posts' - Returns a JSON response containing the posts dictionary.

POST Routes:


'/add_user' - Creates a new user and adds it to the users dictionary. #{user}

'/add_post' - Creates a new post and adds it to the posts dictionary. If user does not exists, then it will be created. #{author,content}

PUT Routes:

'/edit_user' - Renames a user in the users dictionary. #{user,new_name}

'/edit_post' - Updates the content of a post in the posts dictionary. #{post_id,new_content}

DELETE Routes:

'/kill_user' - Deletes a user from the users dictionary. #{user}

'/kill_post' - Deletes a post from the posts dictionary. #{post_id}
