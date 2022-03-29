#!/usr/bin/env python3

import pandas as pd
from book import Order 


order1 = Order(10, 10.0)
order2 = Order(120, 12.0)
order3 = Order(5, 10.0)
order4 = Order(2, 11.0)
order5 = Order(1, 10.0)
order6 = Order(10, 10.0)




df = pd.DataFrame({"Buy": [(order1.q,order1.p), (order3.q,order3.p), (order4.q,order4.p)] , "Sell": [(order2.q,order2.p), (order5.q,order5.p), (order6.q,order6.p)]})
print(df)
