import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


#"name.txt" is a file contains the names of all the individual stock files
#This function returns a list of stock files' name
#The list can be used to loop through all the stocks in later stages
def readName(filename):
    StockList = []
    file = open(filename)
    for line in file:
        StockList.append(line.rstrip())
    file.close()
    return StockList


#This function is a helper function for getInput function
#This function take in the name of an individual historial data file
#The function read the file and then returns a dictionary 
#which has the date as keys, and the corresponding return as it's value
#return for day[i] the percentage change of "adjusted close value"
#from day[i] to day[i+1]
def individualDict(line):
    subDict={}
    file=open(line)
    file.readline()    
    List=[]
    for k in file:
        k=k.split(",")
        List.append(k)
    for i in range(len(List)-1):
        subDict[List[i][0]]=(float(List[i+1][5])-
                             float(List[i][5]))/float(List[i][5])
    return subDict

#The function take in a a list of stock files' name
#calls individualDict function to generate individual dictionary for each stock 
#The function returns a big dictionary which is a dictionary of 
#many individual stock dictionaries
#I chose to use dictionary instead of list to store data, 
#because I want to bond the value with the key: date
#So I would be able to safely relate the data reflecting different features of 
#a same day
def getInput(StockList):
    BigDict={}    
    for line in StockList:
        line=line.replace("\n","") 
        subDict=individualDict(line)
        name=line[:-4]
        BigDict[name]=subDict
    return BigDict

#The function takes in the market dictionary and a individual stock dictionary
#Codes are modified from simple linear regression example copied from scikit
#I tried to input data to array to run regression
#I printed the array in the example to see what it should be looks like
#I failed to modify my data into the same form of array in the example due to 
#"list assignment index out of range"
#I also modified the ploting codes
def regression(MarketDictionary, StockDictionary):
    regr=linear_model.LinearRegression()
    j=0
    p=0
    array_market=[0 for x in range (0, 1000)]
    array_stock= [[] for n in range(0, 1000)]
    for i in MarketDictionary.values():
        array_market[j]=i
        j=j+1
    for i in StockDictionary.values():
        array_stock[p][0]=i
        p=p+1
    regr.fit(array_market, array_stock)
    print('Coefficients: \n', regr.coef_)
    array_market_pred = regr.predict(array_stock)    
    plt.scatter(array_stock, array_market,  color='black')
    plt.plot(array_stock, array_market_pred, color='blue', linewidth=3)
    
    plt.xticks(())
    plt.yticks(())
    
    plt.show()    

#This is the main function
#It loop though the list of stocks, call regressionn function for each of them
#and record the result(correlation coefficient) into a new file
def loopDicts(BigDict,Newfilename):
    file = open(Newfilename, 'w')
    for key in BigDict.keys():
        regression(BigDict["MARKET"], BigDict[key])
        file.write("key"+'\n'+'Coefficients:'+ "regr.coef_"'\n')
        file.close()        

def main():
    StockList=readName("name.txt")
    BigDict=getInput(StockList)
    Newfilename="result"
    loopDicts(BigDict,Newfilename)

main()