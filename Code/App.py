import requests
import pandas as pd
from math import ceil
import msvcrt

def pairs(z:int)->None:
    #Download dataset
    url  = 'https://mach-eight.uc.r.appspot.com/'
    resp = requests.get(url)
    df = pd.DataFrame.from_dict(resp.json()['values'])
    #list of pairs
    X = []
    Y = []
    #min and max of height
    h_min = int(df['h_in'].min())
    h_max = int(df['h_in'].max())
    #there are no matches when z>2*h_max and z<2*h_min
    if(h_min*2<=z and  h_max*2>=z):
        #find heights pairs which x+y=z where x and y are the player's heights and z is our target
        for x in range(h_max,ceil(z/2)-1,-1):
            y = -x + z
            #if our y found is < than h_min that height does not exist and go to the next iterator
            if y < h_min:
                continue
            X.append(x)
            Y.append(y)
        comp = True
        for i in range(len(X)):
            #find a group of players which heights are X and Y
            df2 = df.loc[df['h_in'].eq(str(X[i]))]
            df3 = df.loc[df['h_in'].eq(str(Y[i]))]
            #if any group is empty that pairs of heights do not have players and go to the next iterator
            if df2.empty or df3.empty:
                continue
            #let's pair all players found with the heights X and Y
            for indexX, rowX in df2.iterrows():
                for indexY, rowY in df3.iterrows():
                    #if the indexes are the same that means that they are the same player and go to the next iterator
                    if indexX == indexY:
                        continue
                    comp = False
                    print("- {}         {}".format(rowX['first_name']+' '+rowX['last_name'],rowY['first_name']+' '+rowY['last_name']))
        #if comp do not change its state then there are no matches
        if comp:
            print('No matches found')
    else:
        print('No matches found')

if __name__ == '__main__':
    try:
        pairs(int(input(">App ")))
    except:
        print('No matches found')
    print("Press a key to finish...")
    msvcrt.getch()

