from flask import Flask, jsonify, redirect, render_template, request, url_for

from model.post import Post
from model.user import User

users={} #key=name,value=id
posts={} #key=id, value={date,author,content}

# START OF FUNCTIONS BLOCK

def reverse_dict(dict_to_reverce):
  #   Create a new dictionary with the keys(unique) and values(unique) swapped
  return dict(zip(dict_to_reverce.values(),dict_to_reverce.keys()))

def create_user(user:User):
  #    Create a new user and add it to the users dictionary
  users[user.name]=user.id 
  return jsonify({'user':user.name,'status':'created'})

def rename_user(name,new_name):
  #     Rename a user
  users[new_name]=users[name]
  del users[name]
  return jsonify({'response':f'user id:{users[new_name]} updated. Old name: {name}, new name: {new_name}'})

def delete_user(username):
  # Delete user
  del users[username]
  return jsonify({'responce':f'User {username} deleted.'})

def create_post(post:Post):
  #  Create a new post and add it to the posts dictionary
  if post.author not in  users:
    user=User(post.author)
    msg=create_user(user)
    print(msg)

  posts[post.id]=post.to_dict()
  return jsonify({'response':'Post created'})

def update_post(post_id,new_content):
  #   Update a post
  posts[post_id]['content']=new_content
  return  jsonify({'response':'Post updated'})

def delete_post(post_id):
  #  Delete post
  del posts[post_id]
  return jsonify({'response':'Post deleted'})

# END  OF FUNCTIONS BLOCK

# FLASK

app = Flask(__name__)

@app.route('/')
def  index():
  #    Return a HTML  page
  return render_template('index.html',users=users,posts=posts)

# START OF USERS ROUTES

@app.route('/add_user', methods=['POST'])
def  add_user():
  data=request.get_json() #{user}
  username=data['user']
  if username in  users:
    return jsonify({'error':f'User name {username}  already exists!'})
  user=User(username)
  return create_user(user)

@app.route('/edit_user', methods=['PUT'])
def edit_user():
  data=request.get_json()  #{user,new_name}
  if data['new_user'] in  users:
    return jsonify({'error':f'User name {data["new_user"]}  already exists!'})
  return rename_user(data['user'],data['new_user'])

@app.route('/kill_user', methods=['DELETE'])
def  kill_user():
  data=request.get_json()  #{user}
  if data['user'] not in users:
    return jsonify({'error':f'User {data["user"]} does not exist!'})
  return delete_user(data['user'])

@app.route('/get_users')
def get_users():
  return jsonify(users)

# END OF USERS ROUTES

#  START OF POSTS ROUTES

@app.route('/add_post',methods=['POST'])
def  add_post():
  data=request.get_json() #{author,content}
  post=Post(data['author'],data['content'])
  return create_post(post)

@app.route('/edit_post',methods=['PUT'])
def edit_post():
  data=request.get_json()  #{post_id,new_content}
  if  data['post_id'] not in posts:
    return jsonify({'error':f'Post {data["post_id"]} does not exist!'})
  return update_post(data['post_id'],data['new_content'])

@app.route('/kill_post',methods=['DELETE'])
def   kill_post():
  data=request.get_json()  #{post_id}
  if data['post_id'] not in posts:
    return jsonify({'error':f'Post {data["post_id"]} does not exist!'})
  return delete_post(data['post_id'])

@app.route('/get_posts')
def get_posts():
  return jsonify(posts)

#  END OF POSTS ROUTES




if __name__ == "__main__":
    app.run(debug=True)