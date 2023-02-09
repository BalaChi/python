# python --module venv venv -- to create venv
# .\venv\Scripts\activate  -- activation
import pyjokes
x = pyjokes.get_joke('en','neutral')
print(x)