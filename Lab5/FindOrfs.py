#!/usr/bin/env python3
# Name: Your full name (cruzid account )
# Group Members: List full names (cruzid usernames) or “None”


########################################################################
# CommandLine
########################################################################
import sys
from SequenceAnalysis import FastAreader, OrfFinder
class CommandLine() :
    '''
    Handle the command line, usage and help requests.

    CommandLine uses argparse, now standard in 2.7 and beyond. 
    it implements a standard command line argument parser with various argument options,
    a standard usage and help.

    attributes:
    all arguments received from the commandline using .add_argument will be
    avalable within the .args attribute of object instantiated from CommandLine.
    For example, if myCommandLine is an object of the class, and requiredbool was
    set as an option using add_argument, then myCommandLine.args.requiredbool will
    name that option.
 
    '''
    
    def __init__(self, inOpts=None) :
        '''
        Implement a parser to interpret the command line argv string using argparse.
        '''
        
        import argparse
        self.parser = argparse.ArgumentParser(description = 'Program prolog - a brief description of what this thing does', 
                                             epilog = 'Program epilog - some other stuff you feel compelled to say', 
                                             add_help = True, #default is True 
                                             prefix_chars = '-', 
                                             usage = '%(prog)s [options] -option1[default] <input >output'
                                             )
        self.parser.add_argument('-lG', '--longestGene', action = 'store', nargs='?', const=True, default=False, help='longest Gene in an ORF')
        self.parser.add_argument('-mG', '--minGene', type=int, choices= (0,100,200,300,500,1000), default=300, action = 'store', help='minimum Gene length')
        self.parser.add_argument('-s', '--start', action = 'append', default = ['ATG'],nargs='?',  help='start Codon') #allows multiple list options
        self.parser.add_argument('-t', '--stop', action = 'append', default = ['TAG','TGA','TAA'],nargs='?', help='stop Codon') #allows multiple list options
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')  
        if inOpts is None :
            self.args = self.parser.parse_args()
        else :
            self.args = self.parser.parse_args(inOpts)

########################################################################
# Main
# Here is the main program
# 
#
########################################################################
   
def main(inFile = None, options = None):
    '''
    Takes in an infile name and a series of options and returns all gene candidates that fit the options 
    '''
    thisCommandLine = CommandLine(options) #initializing commandline object to handle the options input from the command line
    reader = FastAreader(inFile) #fasta read the infie
    for head,seq in reader.readFasta(): #print all gene candidates in each fasta sequence fragment in the file 
        print(head)
        myOrfFinder = OrfFinder(seq,thisCommandLine.args.longestGene,thisCommandLine.args.minGene,thisCommandLine.args.start,thisCommandLine.args.stop)
        myOrfFinder.printer()

if __name__ == "__main__":
    main() 
