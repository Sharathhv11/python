from bs4 import BeautifulSoup
from pandas import DataFrame

with open("table.html","r") as f:
    html = f.read()
soup = BeautifulSoup(html,"html.parser")

# header_data =
# del header_data[9:]

pandas_dictionary = {x : [] for x in [str(x).strip("</h3>").strip() for x in soup.find_all("h3") if x!=" "] }

# table_links =[str(x.text).strip() for x in  soup.find_all("a")]
# del table_links[10:]

# pandas_dictionary["TEAMS"]=table_links
# pandas_dictionary["POS"]=list(range(1,11))
# table_data = soup.find_all("td")
# print(pandas_dictionary)

table_row_data =[]
for x in soup.find_all("td"):
    if(x not in table_row_data ):
        table_row_data.append(x.text.strip())
for i,x in enumerate(pandas_dictionary.items()):
    for j in range(0+i,(len(table_row_data)//2),9):
        pandas_dictionary[x[0]].append(table_row_data[j])




# print(DataFrame(pandas_dictionary))


