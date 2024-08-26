from problem2 import *
import sys
import math

'''
    Unit test 2:
    This file includes unit tests for problem2.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 2 (27 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

#---------------------------------------------------
def test_dataframe():
    ''' (3 points) dataframe'''
    x=dataframe()
    assert type(x) == pd.DataFrame
    assert x.shape == (3,2) 
    assert x.iloc[0,0] == 1
    assert x.iloc[0,1] == 4
    assert x.iloc[1,0] == 2
    assert x.iloc[1,1] == 5
    assert x.iloc[2,0] == 3
    assert x.iloc[2,1] == 6
#---------------------------------------------------
def test_load_csv():
    ''' (3 points) load_csv'''
    x=load_csv("A.csv")
    assert type(x) == pd.DataFrame
    assert x.shape == (3,2) 
    assert x.iloc[0,0] == 1
    assert x.iloc[0,1] == 4
    assert x.iloc[1,0] == 2
    assert x.iloc[1,1] == 5
    assert x.iloc[2,0] == 3
    assert x.iloc[2,1] == 6
    x=load_csv("B.csv")
    assert x.shape == (4,2) 
#---------------------------------------------------
def test_save_csv():
    ''' (3 points) save_csv'''
    x=dataframe()
    save_csv(x,"A1.csv") # save the data frame to file
    y=load_csv("A1.csv") # read the dataframe from the file
    assert x.equals(y) # check if the dataframes are identical
#---------------------------------------------------
def test_filter_height():
    ''' (3 points) filter_height'''
    x=dataframe()
    y=filter_height(x,t=2)
    assert type(y) == pd.DataFrame
    assert y.shape == (2,2) 
    assert y.iloc[0,0] == 2
    assert y.iloc[0,1] == 5
    assert y.iloc[1,0] == 3
    assert y.iloc[1,1] == 6
    y=filter_height(x,t=0)
    assert y.shape == (3,2) 
    assert y.iloc[0,0] == 1
    assert y.iloc[0,1] == 4
    assert y.iloc[1,0] == 2
    assert y.iloc[1,1] == 5
    assert y.iloc[2,0] == 3
    assert y.iloc[2,1] == 6
#---------------------------------------------------
def test_group_sum():
    ''' (3 points) group_sum'''
    x=load_csv("B.csv")
    y=group_sum(x,k="ID")
    assert type(y) == pd.DataFrame
    assert y.shape == (2,2)  # to convert an index into a column, you could use reset_index() method.
    assert y.iloc[0,0] == 1
    assert y.iloc[1,0] == 2
    assert y.iloc[0,1] == 9
    assert y.iloc[1,1] == 13
#---------------------------------------------------
def test_merge():
    ''' (3 points) merge'''
    x=load_csv("B.csv")
    x=group_sum(x,k="ID")
    y=load_csv("C.csv")
    z=merge(x,y,k="ID")
    assert type(z) == pd.DataFrame
    c = list(z.columns)
    assert c[0]=="ID"
    assert c[1]=="count"
    assert c[2]=="name"
    assert z.shape == (2,3)  
    assert z.iloc[0,0] == 1
    assert z.iloc[1,0] == 2
    assert z.iloc[0,1] == 9
    assert z.iloc[1,1] == 13
    assert z.iloc[0,2] == "Alex"
    assert z.iloc[1,2] == "Bob"
    x=load_csv("C.csv")
    y=load_csv("D.csv")
    z=merge(x,y,k="ID")
    assert z.shape == (2,3)  
    c = list(z.columns)
    assert c[0]=="ID"
    assert c[1]=="name_x"
    assert c[2]=="name_y"
#---------------------------------------------------
def test_sort_values():
    ''' (3 points) sort_values'''
    x=load_csv("B.csv")
    y=sort_values(x,k="count")
    assert y.shape == (4,2)
    assert y.iloc[0,0] == 2
    assert y.iloc[1,0] == 2
    assert y.iloc[2,0] == 1
    assert y.iloc[3,0] == 1
    assert y.iloc[0,1] == 7
    assert y.iloc[1,1] == 6
    assert y.iloc[2,1] == 5
    assert y.iloc[3,1] == 4
    y=sort_values(x,k="ID")
    assert y.shape == (4,2)
    assert y.iloc[0,0] == 2
    assert y.iloc[1,0] == 2
    assert y.iloc[2,0] == 1
    assert y.iloc[3,0] == 1
    assert y.iloc[0,1] == 6
    assert y.iloc[1,1] == 7
    assert y.iloc[2,1] == 4
    assert y.iloc[3,1] == 5
#---------------------------------------------------
def test_divide():
    ''' (3 points) divide'''
    x=load_csv("B.csv")
    y=divide(x,k="count",l="ID")
    assert len(y) == 4
    assert y.iloc[0] == 4
    assert y.iloc[1] == 5
    assert y.iloc[2] == 3
    assert y.iloc[3] == 3.5
    y=divide(x,k="ID",l="count")
    assert len(y) == 4
    assert y.iloc[0] == 0.25
    assert y.iloc[1] == 0.2
    assert y.iloc[2] == 1/3
    assert y.iloc[3] == 2/7
#---------------------------------------------------
def test_insert_column():
    ''' (3 points) insert_column'''
    x=load_csv("B.csv")
    y=divide(x,k="ID",l="count")
    insert_column(x,y,k="A")
    assert x.shape == (4,3)  
    assert x.iloc[0].A == 0.25
    assert x.iloc[1].A == 0.2
    assert x.iloc[2].A == 1/3
    assert x.iloc[3].A == 2/7

