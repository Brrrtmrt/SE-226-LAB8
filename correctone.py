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
        return "Book"+"uid:"+self.uid+"title:"+self.title+"year:"+self.year+"author"+self.author+"pages:"+str(self.pages)+"\n"

class Article(ArchiveItem):
    journal=""
    doi=""
    def __init_(self,uid,title,year,journal,doi):
        ArchiveItem.__init_(uid,title,year)
        self.journal=journal
        self.doi=doi
    
    def __str__(self):
        return "Article"+"uid:"+self.uid+"title:"+self.title+"year:"+self.year+"journal:"+self.journal+"doi:"+self.doi+"\n"

class Podcast(ArchiveItem):
    host=0
    duration=0
    
    def __init_(self,uid,title,year,host,duration):
        ArchiveItem.__init_(uid,title,year)
        self.host=host
        self.duration=duration
    
    def __str__(self):
        return "Podcast"+"uid:"+self.uid+"title:"+self.title+"year:"+self.year+"host:"+str(self.host)+"duration:"+str(self.duration)+"\n"
        

def save_to_file(items,filename):
    
    
    f=open(filename,"w")
    for x in items:
        f.write(str(x))
                
   
        
def load_from_file(filename):
    items = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(":")
            if len(parts) < 2:
                continue
            item_type = parts[0]
            data = line[len(item_type) + 1:].strip()
            fields = data.split(" ")
            
            if item_type == "Book":
                uid, title, year, author, pages = fields
                items.append(Book(uid, title, int(year), author, int(pages)))
            elif item_type == "Article":
                uid, title, year, journal, doi = fields
                items.append(Article(uid, title, int(year), journal, doi))
            elif item_type == "Podcast":
                uid, title, year, host, duration = fields
                items.append(Podcast(uid, title, int(year), host, int(duration)))
            else:
                uid, title, year = fields
                items.append(ArchiveItem(uid, title, int(year)))
    return items
