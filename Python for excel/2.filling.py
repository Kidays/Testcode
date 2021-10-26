from numpy import dtype
from datetime import date, timedelta
import pandas as pd
books = pd.read_excel('filling.xlsx', skiprows=2, usecols='B:F', index_col=None, dtype={
                      'DATE': str, 'INSTROE': str, 'PRICE': str})
start = date(2021, 10, 10)

print(books)


def add_month(d, md):  # month increments # d:date md:add month
    yd = md//12
    m = d.month+md % 12
    if m != 12:
        yd += m//12
        m = m % 12
    return date(d.year+yd, m, d.day)


for i in books.index:
    # books['DATE'].at[i]=start+timedelta(days=2*i)
    # books['DATE'].at[i] = date(start.year+i, start.month, start.day+i)
    # books['DATE'].at[i] = add_month(start, i)
    books.at[i,'DATE']=add_month(start,5*i)
    books['INSTORE'].at[i] = 'Yes'if i % 2 == 0 else'No'
    # books.at[i,'INSTORE']='Yes'if i % 2 == 0 else'No' # value error
    # books['PRICE'].at[i] = 10*i+1
    books.at[i,'PRICE']=10*i+1
print(books)
books.set_index('DATE', inplace=True)
books.to_excel('filling.xlsx')

