import requests as req
from bs4 import BeautifulSoup
from pandas import DataFrame




class IPL:
    """IPL class has some cool methods that displays the realtime information of ipl 2024
    this is acheived by utillizing web scraping """

    #satic variables that shares the same data to all IPL instances

    #changing the user-agent to chrome browser
    headers = {
        "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    #getting the HTML document from this websites

    response_matches = req.get("https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches", headers=headers)
    points_table = req.get("https://www.news18.com/cricket/ipl/points-table/",headers=headers)


    # BeautifulSoup objects
    soup1 = BeautifulSoup(response_matches.text, "html.parser")
    soup2 = BeautifulSoup(points_table.text, "html.parser")


    def __init__(self):
        pass


    @staticmethod
    def Points_Table():
        """this is a static method that displays the real-time points table
        of ipl 2024 by utilizing pandas and bs4 frameworks
        And return pandas object """
        try:
            # title = str(IPL.soup2.title.string).split("|")[0]
            html = str(IPL.soup2.table)
            soup3 = BeautifulSoup(html,"html.parser")

            #getting headers from points table
            pandas_dictionary = {x: [] for x in [str(x).strip("</h3>").strip() for x in soup3.find_all("h3") if x != " "]}


            """this part of code extracts the data form a table and store it in a dictionary"""
            table_row_data = []
            for x in soup3.find_all("td"):
                if (x not in table_row_data):
                    table_row_data.append(x.text.strip())

            for i, x in enumerate(pandas_dictionary.items()):
                for j in range(0 + i, (len(table_row_data) ), 9):
                    pandas_dictionary[x[0]].append(table_row_data[j])

            return DataFrame(pandas_dictionary)
        except Exception as e:
            print(e)

    @staticmethod
    def Todays_Match():
        print(IPL)



def main():
    result = IPL.Points_Table()
    print(result)

if(__name__ == "__main__"):
    main()




