'''
    This program shows how the predefined data in _tejas_module.py is accessed in this file 
by importing the module containing the definitions

Here, the _tejas_module.py represents a user-defined module in Python

'''
import _tejas_module
print(f"\nHello Everyone !")
print(f"My full name is {_tejas_module.full_name}.")
print(f"Mobile Number : {_tejas_module.contact_num}")
print(f"Address: {_tejas_module.address}")
print(f"Email Id: {_tejas_module.mail_id}.")
print("\nThank You for visiting my profile")
