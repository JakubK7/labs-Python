class Book:
  def __init__(self, title, author, year):
      self.title = title
      self.author = author
      self.year = year
      self.is_available = True

  def borrow_book(self):
    if self.is_available:
      self.is_available = False
      return True
    return False
  
  def return_book(self):
    if not self.is_available:
      self.is_available = True
      return True
    return False
  
  def __str__(self):
    status = "Available" if self.is_available else "Checked Out"
    return f"'{self.title}' - {self.author} ({self.year}), {status}"
  