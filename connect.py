import requests
import time
import itertools

'''
This creates a dictionary of prices and products.
To avoid huge data hitback, only the price and the productUrl is retrieved from the APIs.
The types ['women', 'boots', 'jewelry', 'eyewear'] have been carefully chosen to represent a BROAD range of prices.
For example, men and women section vary slowly in prices, most are below $50, while jewelry and eyewear sections have expensive items.
so, they've been chosen keeping in mind all sort of users.

This file saves the catalog into a file catalog.txt
This is done for two reasons:
1. So that this file can run in background once or twice in a day (or even infrequently depending on how quickly the products at Zappos go outdated and how quickly new products get added.) and so that the actual user amount-items application runs lightening fast.
2. Because the APIs have a limit of 2,500 per day, so not a good idea to practice hitting the costly and heavy API service everytime.
Make sure that the file saved by connect.py is in the Python path or in the directory where Display.py file is located.

'''
def connect(start_page, end_page, hop_pages):
    time1 = time.time()
    types = ['women', 'boots', 'jewelry', 'eyewear']
    key = 'a73121520492f88dc3d33daf2103d7574f1a3166'
    
    exclude_list = '["styleId","originalPrice","colorId","productName","brandName","thumbnailImageUrl","percentOff","productId"]'
    sort = 'sort={"price":"asc"}'
    limit = 100
    response= []
    
    for i in range(0,len(types)):
        if(i == 1):
            start_page = 15
        if(i >= 2):
            start_page = 25
        for j in range(start_page, end_page, hop_pages):
            url = 'http://api.zappos.com/Search/term/'+types[i]+'?excludes='+exclude_list+'&'+sort+'&limit='+str(limit)+'&page='+str(j)
            resp = requests.get(url+'&key='+key)
            try:
                if(resp.json()["results"]):
                    response.append(resp)
            except:
                continue
   
    time2 = time.time()
    
    all_prices = []
    all_products = []
    all_prices.append(int(float((response[0].json()["results"][0]["price"].replace('$','')).replace(',',''))+0.5))
    for j in range(0,len(response)):
        for i in range(1, limit - 1):
            all_prices.append(int(float((response[j].json()["results"][i]["price"].replace('$','')).replace(',',''))+0.5))
            all_products.append(response[j].json()["results"][i]["productUrl"])
    #print(all_prices)
    catalog = dict(itertools.izip(all_prices,all_products))
    
    with open('Catalog.txt', 'w') as my_file:
        my_file.write(str(catalog))
    
    time3 = time.time()
    print(time2 - time1)
    print(time3 - time2)
    print("Total time taken is " + str(time3 - time1) + " second. \n Don't worry, this won't run every time. Just once in a day, in background. \n Doesn't run when user uses the main application which is Display.py")

'''
The main function.
It calls connect by sending the API's starting page number, ending page number and page frequency (hop_pages)
Page frequency is present because of the fact that a lot of products in 'men', 'women' and other sections have same price.
So, when returned in sorted order, many pages will have products of same price, which could be ignored to quicken the calculation.
'''    
def main():
    start_page = 0
    end_page = 100
    page_hop = 3
    connect(start_page, end_page, page_hop)    
    

if __name__ == "__main__":
    main()
