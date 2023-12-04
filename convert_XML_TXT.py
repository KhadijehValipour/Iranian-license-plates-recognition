import xml.sax
import xml.etree.ElementTree as ET
import os
import glob

final_list = []
class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.counter = 0
        self.CurrentData = ""
        self.name = ""
        self.list = []

   # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag



   # Call when an elements ends
    def endElement(self, tag):
        
        
        if(self.CurrentData == "name"):
            #print("name:", self.name)
            self.counter+=1
            self.list.append(self.name)
            if self.counter == 8 :
                print("self.list" ,self.list)

                if self.list[2] == "الف":
                    self.list[2] = "A"
                elif self.list[2] == "ب":
                    self.list[2] = "B"
                elif self.list[2] == "پ":
                    self.list[2] = "P"
                elif self.list[2] == "ت":
                    self.list[2] = "T"
                elif self.list[2] == "ث":
                    self.list[2] = "Y"
                elif self.list[2] == "ز":
                    self.list[2] = "Z"
                elif self.list[2] == "ش":
                    self.list[2] = "X"
                elif self.list[2] == "ع":
                    self.list[2] = "E"
                elif self.list[2] == "ف":
                    self.list[2] = "F"
                elif self.list[2] == "ک":
                    self.list[2] = "K"
                elif self.list[2] == "گ":
                    self.list[2] = "G"
                elif self.list[2] == "D":
                    self.list[2] = "D"
                elif self.list[2] == "S":
                    self.list[2] = "S"
                elif self.list[2] == "ج":
                    self.list[2] = "J"
                elif self.list[2] == "د":
                    self.list[2] = "W"
                elif self.list[2] == "س":
                    self.list[2] = "C"
                elif self.list[2] == "ص":
                    self.list[2] = "U"
                elif self.list[2] == "ط":
                    self.list[2] = "R"
                elif self.list[2] == "ق":
                    self.list[2] = "Q"
                elif self.list[2] == "ل":
                    self.list[2] = "L"
                elif self.list[2] == "م":
                    self.list[2] = "M"
                elif self.list[2] == "ن":
                    self.list[2] = "N"
                elif self.list[2] == "و":
                    self.list[2] = "V"
                elif self.list[2] == "‍":
                    self.list[2] = "H"
                elif self.list[2] == "ه‍":
                    self.list[2] = "H"
                elif self.list[2] == "ی":
                    self.list[2] = "I"
                elif self.list[2] == "ژ (معلولین و جانبازان)":
                    self.list[2] = "@"

                  
                my_list = [''.join(self.list[0 : 8])]
                print(my_list[0])
                final_list.append(my_list[0])
   # Call when a character is read
    def characters(self, content):
        if(self.CurrentData == "name"):
            self.name = content

count= 0
path = 'validation'
for filename in os.listdir(path):
    if filename.endswith('.xml'): 
        fullname = os.path.join(path, filename)
        tree = ET.parse(fullname)
        # create an XMLReader
        parser = xml.sax.make_parser()

        # turn off namepsaces
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        # override the default ContextHandler
        Handler = XMLHandler()
        parser.setContentHandler( Handler )
        parser.parse(fullname)
        count+=1
        #print(count)

print(final_list)
print(len(final_list))

file_names = []
file_names = glob.glob("validation/*.jpg")
for i in range(len(file_names)):
    file_names[i]=file_names[i].replace("\\" , "/")

print(len(file_names))



with open("gt_validation.txt", "w", encoding="utf-8") as f:
    for i in range(len(file_names)):
        f.write(file_names[i]+"	"+final_list[i]+"\n")








