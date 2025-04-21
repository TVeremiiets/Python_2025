
import decimal
from pywebio.input import slider, FLOAT, NUMBER
from pywebio.output import put_html, put_success


# HEADER
put_html("<h1>Welcome to our shop</h1>")

#imput section
cheese_weight = slider ("Cheese", type=FLOAT, min_value=1, max_value=5,value=0.15, required=True)

