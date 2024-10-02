from static.config import user_iterator

class User:
  def __init__(self, name):
   global user_iterator
   user_iterator+=1
   self.id=user_iterator
   self.name=name
  
  def to_dict(self):
    return {'id': self.id}