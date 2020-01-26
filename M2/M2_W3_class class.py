# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 16:53:14 2019

@author: momills
"""


class Robot:
    
    def __init__(self):
        self.recordings = []
    
    def listen(self, string):
        self.recordings.append(string)
        
    def play_recordings(self):
        print(self.recordings)
        
    def delete_recordings(self):
        self.recordings = []
        

r1 = Robot()
r2 = Robot()

r1.listen('tell me whats my flavour')
r1.listen('hahaha')

r2.listen('loool')
r2.listen('ok ok !')
        
r1.play_recordings()
r2.play_recordings()

r1.delete_recordings()
r1.play_recordings()
r1.listen('after delete')
r1.play_recordings()

class LectureRoom:
    
    def __init__(self):
        self.capacity = 40 
        
    def increase_capacity(self, amount)
        
        
        
        
        
        