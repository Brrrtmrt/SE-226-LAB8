class ArchiveItem:
    uid=""
    title=""
    year=0
    
    def __init__(self,uid,title,year):
        self.uid=uid
        self.title=title
        self.year=int(year)
    def __str__(self):
        return "uid:"+self.uid+"title:"+self.title+"year:"+str(self.year)+"\n"
    def __eq__(self,other):
        return self.uid==other.uid
    
    def is_recent(self,n):
        return self.year>=2025-n and self.year<=2025
    

class Book(ArchiveItem):
    author=""
    pages=0
    
    def __init_(self,uid,title,year,author,pages):
        ArchiveItem.__init_(uid,title,year)
        self.author=author
        self.pages=pages
        
    def __str__(self):
        return "uid:"+self.uid+"title:"+self.title+"year:"+self.year+"author"+self.author+"pages:"+str(self.pages)+"\n"

class Article(ArchiveItem):
    journal=""
    doi=""
    def __init_(self,uid,title,year,journal,doi):
        ArchiveItem.__init_(uid,title,year)
        self.journal=journal
        self.doi=doi
    
    def __str__(self):
        return "uid:"+self.uid+"title:"+self.title+"year:"+self.year+"journal:"+self.journal+"doi:"+self.doi+"\n"

class Podcast(ArchiveItem):
    host=0
    duration=0
    
    def __init_(self,uid,title,year,host,duration):
        ArchiveItem.__init_(uid,title,year)
        self.host=host
        self.duration=duration
    
    def __str__(self):
        return "uid:"+self.uid+"title:"+self.title+"year:"+self.year+"host:"+str(self.host)+"duration:"+str(self.duration)+"\n"
        

def save_to_file(items,filename):
    
    
    f=open(filename,"w")
    for x in items:
        f.write(str(x))
                
   
        

        


l=list()

for i in range(5):
    a=ArchiveItem("a","a",i)
    l.append(a)

print(l)
print(str(l[0]))
save_to_file(l,"test.txt")
    
