# Write your code below: 
from contextlib import contextmanager

@contextmanager
def generic(card_type, sender, receiver):
  card_file = open(card_type, 'r')
  order = open(f"{sender}_generic.txt", 'w')

  try:
    order.write(f"Dear {receiver}, \n")
    order.write(card_file.read())
    order.write(f"\nSincerely, {sender} \n")
    yield order

  finally:
    card_file.close()
    order.close()

with generic("thankyou_card.txt","Mwenda","Amanda") as file:
  print("Card Generated!")

with open("Mwenda_generic.txt", "r") as first_order:
  print(first_order.read())

class personalized:
  def __init__(self, sender, receiver):
    self.file = open(f"{sender}_personalized.txt", 'w')
    self.sender = sender
    self.receiver = receiver

  def __enter__(self):
    self.file.write(f"Dear {self.receiver}, \n \n")
    return self.file

  def __exit__(self, exc_type, exc_value, Traceback):
    self.file.write(f"\n\nSincerely,\n{self.sender}")
    self.file.close()

with personalized("John", "Michael") as card:
  card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

with open("John_personalized.txt", "r") as second_order:
  print(second_order.read())