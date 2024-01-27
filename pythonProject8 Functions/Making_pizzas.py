import pizza

pizza.make_pizza(16, 'pepperoni')

from pizza import make_pizza as mp

mp(12, 'cheese')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
#module_name.function_name()

#from module_name import function_name as fn

import pizza as p
p.make_pizza(16, 'pepperoni')