"""
Load module to filter data on fly
"""
from __future__ import print_function
#import os
#import sys
import pandas as pd
#import numpy as np
#import re

class Load():
    """
    Load class is used for exclusive dataframe filtering
    which takes `df` a csv file and convert into dataframe
    """
    def __init__(self, filename):
        self.version = open('VERSION').readlines()[0]
        self.df = pd.read_csv(filename)
        self.data = """W_A11,2000-02,Moving average,59.66666667,50.92582302,
                        68.40751031,Injuries,Number,Assault,Validated,Whole 
                        pop,All ages,FatalW_A11,2001-03,Moving average,60,10,
                        20,30,33,31,12,51.23477459,68.76522541,Injuries,
                        Number,Assault,Validated,Whole pop,All ages,Fatale 
                        50, 50, 60,pop,All ages,Fatal"""


    def get_version(self):
        """ Get current `version` of library"""
        return self.version
    def pick_numbers(self):
        """
        From self.data extract all numbers as a list
        :eg:
            data = "W_A11,2000-02,Moving average,59.66666667,50.92582302,68.40751031,
                       Injuries,Number,Assault,Validated,Whole pop,All ages,Fatal"

        :returns: [59.66666667,50.92582302,68.40751031]

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.pick_numbers()
            >> [1,2,3,4,5,6]

        """
        # complete code here
        li = []
        for i in self.data.split(","):
            try:
                li.append(float(i))
            except ValueError:
                pass
        return li
    def sum_all_numbers(self):
        """
        From `self.data` extract all numbers and return the sum of all numbers

        :eg:
            data = "W_A11,2000-02,Moving average,59.66666667,50.92582302,68.40751031,
                       Injuries,Number,Assault,Validated,Whole pop,All ages,Fatal"
        :returns 179.0

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.sum_all_numbers()
            >> 179.0
        """
        #complete the code
        li = []
        for i in self.data.split(","):
            try:
                li.append(float(i))
            except ValueError:
                pass
        return sum(li)
    def extract_vowels(self):
        """
        Return all vowels in the given string `self.data`

        :returns [] all vowels as list
        Usage:
        ======
            >> df = Load('data.csv')
            >> df.extract_vowels()
            >> ['A', 'E', 'I', 'O']
        """
        #complete the code
        li = []
        for vowel in 'aeiou':
            if vowel in self.data:
                li.append(vowel)
        return li
    def pick_odd_numbers(self):
        """
        Take the string from `self.data` and extract all odd numbers and return
        list of all odd numbers from the string

        :returns: [1, 3, 5]

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.pick_odd_numbers()
            >> [1, 3, 5]
        """
        # complete code here
        li = []
        odd = []
        for i in self.data.split(","):
            try:
                li.append(float(i))
            except ValueError:
                pass
        for i in li:
            if i%2 != 0:
                odd.append(i)
        return odd
    def get_mean(self):
        """
        Take the string from `self.data` and extract all numbers and return
        the mean of extracted list of numbers.
        :returns: 50
        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_mean()
            >> 50
        """
        # complete code here
        li = []
        for i in self.data.split(","):
            try:
                li.append(float(i))
            except ValueError:
                pass
        mean = sum(li)/len(li)
        return mean
    def get_all_categorical(self):
        """
        Take the pandas dataframe from `self.df` and return all
        the columns which are categorical variables
        :returns:   All categorical.
        :rtype:     List
        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_all_categorical()
            >> ['Series_reference', 'Type']
        """
        # complete code here
        return self.df.drop(columns=self.df._get_numeric_data()).columns
    def get_all_continuous(self):
        """
        Take the pandas dataframe from `self.df` and return all
        the columns which contain categorical variables
        :returns:   All continuous.
        :rtype:    List
        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_all_continuous()
            >> ['Lower_CI', 'Upper_CI', 'Units']
        """
        # complete code here
        return self.df._get_numeric_data().columns
    @classmethod
    def addition(cls, x, y):
        """
        Take X and Y as input and now return the sum of both
        :param      x:    { first number}
        :type       x:    { integer}
        :param      y:    { secon number }
        :type       y:    { type_description }
        Usage:
        ======
            >> df = Load('data.csv')
            >> df.addition(10, 20)
            >> 30
        """
        # complete code here
        return x+y
if __name__ == '__main__':
    # instantiate the object
    df = Load('data.csv')
    print(df.addition(10, 20))
    print(df.pick_numbers())
    print(df.sum_all_numbers())
    print(df.extract_vowels())
    print(df.pick_odd_numbers())
    print(df.get_mean())
    print(df.get_all_categorical())
    print(df.get_all_continuous())
