from static.config import mesage_iterator
from datetime import datetime
class Post:
  def __init__(self, author,content):
    global mesage_iterator
    mesage_iterator+=1
    self.id=mesage_iterator
    self.date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.author=author
    self.content=content
  def to_dict(self):
    return {'date':self.date,'author':self.author,'content':self.content}