
from datetime import datetime
import pandas as pd
from pprint import pprint
import math

start = datetime.now()

#dask_df = dd.read_csv('1_AD_pool.snp.annot.AD.DP.csv')
#dask_df = pandas.read_csv('1_AD_pool.snp.annot.AD.DP.csv', on_bad_lines='skip')

#chete samo colonite
df = pd.read_csv('1_AD_pool.snp.annot.AD.DP.csv', nrows=0)
print(df.to_string())

#spisuk s kolonite
listColumns = list(df.columns)
countCol = len(listColumns)
print(countCol)
#pritnira imeto na 1-ta kolona
print(df.columns[0])

#####da se mahne nrows v original!!!!!!!!!!!!!
df2= pd.read_csv('1_AD_pool.snp.annot.AD.DP.csv', chunksize=200000,  on_bad_lines='warn')
for data in df2:
    pprint(data)


 #tova raboti
    # df3 = pd.read_csv('1_AD_pool.snp.annot.AD.DP.csv', chunksize=10000, nrows=20, \
     #                 on_bad_lines='warn', usecols=["Func", "Gene", "GERP++_RS"])
   # df3 = pd.read_csv('1_AD_pool.snp.annot.AD.DP.csv', chunksize=10000, nrows=20, on_bad_lines='warn', usecols=[0, 1, 50])
   # for data in df3:
      #  pprint(data)
end = datetime.now()
print("Read csv : ",(end-start),"sec")

numChunks = math.ceil(sum(1 for row in open('1_AD_pool.snp.annot.AD.DP.csv', 'r'))/200000)
print('***********************************')
print("Number of chunks with given chunksize 200000: ", numChunks)


#https://stackoverflow.com/questions/39386458/how-to-read-data-in-python-dataframe-without-concatenating/39386767#39386767
#https://stackoverflow.com/questions/59930804/pandas-csv-error-textfilereader-object-has-no-attribute-to-html