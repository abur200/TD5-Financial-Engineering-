compteur = 1
class Order:
    def __init__(self, quantity, price):
        global compteur
        self.id = compteur
        self.q = quantity
        self.p = price
        compteur+=1
        

class Book:
    def __init__(self, name, list_order = []):
        self.n = name
        self.list_order = list_order
    def insert_buy(self, quantity, price):
        self.list_order.append((Order(quantity,price), 1))
    def insert_sell(self, quantity, price):
        self.list_order.append((Order(quantity,price), -1))
    def affichage_book(self):
        orders_to_be_executed = []
        for i in range(len(self.list_order)):
            if self.list_order[i][1] == 1 :
                print("--- Insert BUY",str(self.list_order[i][0].q)+"@"+str(self.list_order[i][0].p),"id="+str(self.list_order[i][0].id),"on",str(self.n))
                for j in range(len(orders_to_be_executed)):
                    if self.list_order[i][0].p >= orders_to_be_executed[j][2] and self.list_order[i][0].q <= orders_to_be_executed[j][1] and orders_to_be_executed[j][0]==-1:
                        print("Execute",str(self.list_order[i][0].q), "at", str(self.list_order[i][0].p), "on", str(self.n))
                        orders_to_be_executed[j][1] -= self.list_order[i][0].q
                        self.list_order[i][0].q=0
                        if orders_to_be_executed[j][1] == 0:
                            orders_to_be_executed.remove(orders_to_be_executed[j])
                        break
                if self.list_order[i][0].q!=0:
                    orders_to_be_executed.append([1,self.list_order[i][0].q, self.list_order[i][0].p, self.list_order[i][0].id])
                print("Book on",str(self.n))
                    
                        
            elif self.list_order[i][1] == -1 :
                print("--- Insert SELL",str(self.list_order[i][0].q)+"@"+str(self.list_order[i][0].p),"id="+str(self.list_order[i][0].id),"on",str(self.n))
                for j in range(len(orders_to_be_executed)):
                    if self.list_order[i][0].p <= orders_to_be_executed[j][2] and self.list_order[i][0].q <= orders_to_be_executed[j][1] and orders_to_be_executed[j][0]==1:
                        print("Execute",str(self.list_order[i][0].q), "at", str(self.list_order[i][0].p), "on", str(self.n))
                        orders_to_be_executed[j][1] -= self.list_order[i][0].q
                        self.list_order[i][0].q=0
                        if orders_to_be_executed[j][1] == 0:
                            orders_to_be_executed.remove(orders_to_be_executed[j])
                        break
                if self.list_order[i][0].q!=0:
                    orders_to_be_executed.append([-1,self.list_order[i][0].q, self.list_order[i][0].p, self.list_order[i][0].id])
                print("Book on",str(self.n))
                    

            orders_to_be_executed = sorted(orders_to_be_executed, key=lambda x: x[2], reverse=True)
            for k in range(len(orders_to_be_executed)):
                if orders_to_be_executed[k][0] == 1 :
                    print("        BUY",str(orders_to_be_executed[k][1])+"@"+str(orders_to_be_executed[k][2]),"id="+str(orders_to_be_executed[k][3]))

                elif orders_to_be_executed[k][0] == -1 :
                    print("        SELL",str(orders_to_be_executed[k][1])+"@"+str(orders_to_be_executed[k][2]),"id="+str(orders_to_be_executed[k][3]))
                 
            print("------------------------")

    
