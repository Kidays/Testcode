import pandas as pd
books = pd.read_excel('filling.xlsx', index_col='DATE')
for i in books.index:
    books['TPRICE'].at[i] = books['PRICE'].at[i]*books['NUM'].at[i]
books['TPRICE'] = books['TPRICE'].apply(lambda x: x+2)
print(books)
# ------------------------------------------------------
# books.sort_values(by='TPRICE', inplace=True, ascending=False)
books.sort_values(by=['INSTORE', 'TPRICE'],
                  inplace=True, ascending=[True, False])
print(books)
# ------------------------------------------------------


# def price_20_40(a):
#     return a >= 20 and a <= 40


# def level_a(s):
#     return s >= 100 and s <= 1000


# books = books.loc[books['PRICE'].apply(
#     price_20_40)].loc[books['TPRICE'].apply(level_a)]
# books = books.loc[books.PRICE.apply(
#     price_20_40)].loc[books.TPRICE.apply(level_a)]
books = books.loc[books.PRICE.apply(
    lambda a:a >= 20 and a <= 40)].loc[books.TPRICE.apply(lambda x:x >= 100 and x <= 1000)]
print(books)
#--------------------------------------------------------
#