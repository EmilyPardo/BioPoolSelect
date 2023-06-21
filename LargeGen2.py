import pandas as pd
import csv

'''
    tova e niakakva primerna funkcia no e binary
    def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data
        '''

file_2 = r'D:\Doctorantura\DimSerbezov\allf.eigenstratgeno'
#file_2 = r'D:\Doctorantura\DimSerbezov\test.txt'
file_3 = 'output.csv'
listColumns = ['204', '205', '535', '1271', '2463', '2464', '2465', '3727', '4855', '7482', '7775', '10945', '11387', '12567', '12568']
#listColumns = ['2', '4', '5']

with open(file_3, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(listColumns)


    #with open(file_2, newline='\n') as f1:
    with pd.read_csv(file_2, chunksize=1000, on_bad_lines='warn') as reader:
      reader
        #reader = csv.reader(f1)
         #for chunk in reader:
            #chunk.to_csv(SecondFileName(), columns=cblist, mode='a', index=False, na_rep='')
    '''
    TUK PROBvAH ITERACIA po redove no mi dava 
    Process finished with exit code -1073741819 (0xC0000005)
        for chunk in reader:
        for index, row in chunk.iterrows():
            print(row)
        '''


        '''
        ***********************************************************************
        TOVA RABOTI ZA MALUK FILE - prosto promenliata file_2 se smenia
        for row in reader:
            s = " ".join(row)
            #print(s[2])
            #print(listColumns[0])
            rowCSVFormat = ''
            i=0

            for i in range(len(listColumns)):
                #print(listColumns[i])
                ind = int(listColumns[i])-1
                #print(ind)
                rowCSVFormat = rowCSVFormat + s[ind]
            writer.writerow(rowCSVFormat)
            *************************************
'''



'''
with open('output.csv', 'w') as f:
    print('204')
    print(f.iloc[204])

    # exit(0)
    print('205')
    print(f.iloc[205])
    print('1271')
    print(f.iloc[1271])
    print('2463')
    print(f.iloc[2463])
    print('2464')
    print(f.iloc[2464])
    print('2465')
    print(f.iloc[2465])
    print('4855')
    print(f.iloc[4855])
    print('7482')
    print(f.iloc[7482])
    print('7775')
    print(f.iloc[7775])
    print('10945')
    print(f.iloc[10945])
    print('12567')
    print(f.iloc[12567])
    print('12568')
    print(f.iloc[12568])
    exit( 0)'''
