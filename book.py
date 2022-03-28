class Order:
    compteur = 1
    def __init__(self, quantity, price):
        self.id = compteur
        self.q = quantity
        self.p = price
        compteur+=1


class Book:
    def __init__(self, name, list_order = []):
        self.n = name
        self.orders = list_order
    def insert_buy(self, quantity, price):
        self.list_order.append((Order(quantity,price), 1))
    def insert_sell(self, quantity, price):
        self.list_order.append((Order(quantity,price), -1))
    def affichage_book(self):
        for i in range(len(self.list_order)):
            orders_to_be_executed = []
            if list_order[i,1] == 1 :
                print("--- Insert BUY",str(list_order[i,0].q)+"@"+str(list_order[i,0].p),"id="+str(list_order[i,0].id),"on",str(self.n))
                print("Book on",str(self.n))
                orders_to_be_executed.append((1,list_order[i,0].q, list_order[i,0].p, list_order[i,0].id))

            elif list_order[i,1] == -1 :
                print("--- Insert SELL",str(list_order[i,0].q)+"@"+str(list_order[i,0].p),"id="+str(list_order[i,0].id),"on",str(self.n))
                print("Book on",str(self.n))
                orders_to_be_executed.append((-1,list_order[i,0].q, list_order[i,0].p, list_order[i,0].id))


            orders_to_be_executed = sorted(orders_to_be_executed, key=lambda x: x[2])
            for k in range(len(orders_to_be_executed)):
                if orders_to_be_executed[k,0] == 1 :
                    print("        BUY",str(orders_to_be_executed[k,1].q)+"@"+str(orders_to_be_executed[k,2].p),"id="+str(orders_to_be_executed[k,3].id))

                elif orders_to_be_executed[k,0] == -1 :
                    print("        SELL",str(orders_to_be_executed[k,1].q)+"@"+str(orders_to_be_executed[k,2].p),"id="+str(orders_to_be_executed[k,3].id))




    
