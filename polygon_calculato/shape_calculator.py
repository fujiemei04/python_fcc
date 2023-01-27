class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width=%s, height=% s)" % (self.width, self.height) 
  
  def set_width(self,width):
    self.width = width
    
  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.height*self.width
  
  def get_perimeter(self):
    return 2 *self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    shape = ""
    if (self.width > 50 or self.height > 50):
      shape = "Too big for picture."
      return shape
    for i in range(self.height):
      for j in range(self.width):
        shape = shape+"*"
      shape=shape+"\n"
    return shape
  
  def get_amount_inside(self,shape):
    fits = 0
    h_fit = int(self.width/shape.width)
    v_fit = int(self.height/shape.height)
    if h_fit == 0 or v_fit == 0:
      return 0
    if self.width/shape.width-h_fit > 0:
      if (h_fit == v_fit):
        fits = h_fit
      else:
        fits = h_fit+v_fit
    elif self.height/shape.height-v_fit > 0:
      if (h_fit == v_fit):
        fits = h_fit
      else:
        fits = h_fit+v_fit
    else:
      fits = h_fit*v_fit
    return fits
        
      
    


class Square(Rectangle):
  def __init__(self,side):
    self.width = side
    self.height = side

  def __str__(self):
    return "Square(side=% s)" % (self.width) 
  
  def set_side(self,side):
    self.width = side
    self.height = side

  def set_width(self,width):
    self.width = width
    self.height = width
    
  def set_height(self,height):
    self.width = height
    self.height = height