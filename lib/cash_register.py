#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount = 0 ):
    self._discount = discount
    self.total = 0
    self.items = []
    self.previous_transcations = []

  @property
  def discount(self):
      return self._discount
    
  @discount.setter
  def discount(self,value):
      if not isinstance(self.discount,int):
        print("Discount must be an interger!")
      if self.discount > 100 or self.discount < 0:
        print("Not valid discount")
      if self.discount == 0:
        print("There is no discount to apply.")
  
      self.discount = value

  def add_item(self,item , price, quantity=1):
     self.total += price * quantity
     for _ in range(quantity):
        self.items.append(item)
     self.previous_transactions = {"Item": item ,"Price": price ,"Quantity": quantity }
  
  def apply_discount(self):
    if self.discount == 0:
       print("There is no discount to apply.")
       return
    
    self.total -= int(self.total * (self.discount/100))
    self.items.pop()
    print(f"After the discount, the total comes to ${self.total}.")


  def void_last_transaction(self):
       self.total -= (
        self.previous_transactions["Price"]
        * self.previous_transactions["Quantity"]
    )


