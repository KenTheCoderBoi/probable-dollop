class Citizen():
    def __init__(self,name,author,price,publishing_year):
        self.name=name
        self.author=author
        self.price=price
        self.publishing_year=publishing_year
    def create(self):
        print("name:"+self.name)
        print("author:"+self.author)
        print("price:"+str(self.price))
        print("oublished: "+str(self.publishing_year))
c1=Citizen("sussus","am",2989213,1038)
c1.create()
c2=Citizen("EZ","on",9112002,3892)
c2.create()