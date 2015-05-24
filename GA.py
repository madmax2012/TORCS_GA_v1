#!/usr/bin/env python
import sys
import os
import time
import csv
import random
import logging
import operator
import shutil
import glob
import matplotlib.pyplot as plt
import  math
import individual
import batch_drive
#from datashape.coretypes import String

import numpy as np

class RunGA():
    def __init__(self, rep_length, popsize, sp, mut, fitfun, maxgen, cross, nr_processes, run_id , path):

        self.nr_processes = nr_processes
        self.currentIteration=0
        self.fitfun =fitfun
        self.maxIterations=maxgen
        self.popsize=popsize
        self.cars = []
        self.car1 = individual.individual(random.uniform(0,200), random.uniform(0,1), random.uniform(0,20), random.uniform(0,1), random.uniform(0,100), random.uniform(0,1), random.uniform(0,1), random.uniform(0,20), random.uniform(0,1))
        '''
        for i in range(self.popsize):
            self.driver = "\""+str(random.uniform(0,200))+"\","+"\""+str(random.uniform(0,1))+"\","+"\""+str(random.uniform(0,20))+"\","+"\""+str(random.uniform(0,1))+"\","+"\""+str(random.uniform(0,100))+"\","+"\""+str(random.uniform(0,1))+"\","+"\""+str(random.uniform(0,1))+"\","+"\""+str(random.uniform(0,20))+"\","+"\""+str(random.uniform(0,1))+"\""
            self.cars.append(self.driver)
        '''

    def step(self):
        pass

    def stop(self):
        pass

    def run(self):
        while True:
            self.step()
            if self.stop():
                break
        return

    def get_current_iteration(self):
        return self.current_iteration

class gax(RunGA):
    def __init__(self, *args, **kwargs):
        RunGA.__init__(self, *args,**kwargs)
        print("dfg")
        print ""+str(self.nr_processes)
        self.stop_reached = False

    def step(self):
        # Simple stopping condition
       # self.current_iteration = self.current_iteration + 1
       # if self.current_iteration >= self.max_iterations:
       #     self.stop_reached = True
        print "nb of processes: "+str(self.nr_processes)
        print "iteration:        "+str(self.currentIteration)

       # print  "Driver:"+str(self.driver)



        print self.fitfun(['199.619642851', '0.526741925378', '19.6857890654', '0.597455592796', '61.3993866916', '0.621674369537', '0.903683282268', '18.4182020224', '0.113106885666'], (self.nr_processes-self.nr_processes)+self.currentIteration)

        ba = [["87.7387897084","0.200804630457","4.20105212553","0.650334796388","12.5515800035","0.250865270024","0.937916693503","14.0768882757","0.612841339211"],["300","0.05","10","0.10","50","0.01","0.01","5", "0.2"]]
        foos = [self.car1,ba[1],["100","0.05","10","0.10","50","0.01","0.01","5", "0.2"],["100","0.05","10","0.10","50","0.01","0.01","5", "0.2"],["100","0.05","10","0.10","50","0.01","0.01","5", "0.2"]]
        bars = [1,2,3]

        def maptest(foo):
            print foo
            self.fitfun(foo, (self.nr_processes-self.nr_processes)+self.currentIteration)


        for i in range (len(self.cars)):
         #   print self.cars[i]
             pass
        print self.car1.parameters
       # map(maptest, foos)




        self.currentIteration=self.currentIteration+1
        if self.currentIteration >= self.maxIterations:
            print "stop"
            self.stop_reached = True

    def stop(self):
        return self.stop_reached
        pass
