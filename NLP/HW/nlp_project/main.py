from stanfordcorenlp import StanfordCoreNLP

import speech_recognition as sr
import os

from frame_cleaning import cleaningframe
from rules_cleaning import CleaningRules
from dependency     import Dependency

USE_MICROPHONE = False

class CleanRobert:
    def __init__(self, frames = None, rules_sets = None):
        self.current_frame = None
        self.current_rules_set = None
        
        self.frames = frames
        self.rules_sets = rules_sets
    
    
    def add_frame(self, frame, rules_set):
        if frame == None or rules_set == None:
            return
        
        if self.frames == None:
            self.frames = []
            
        if self.rules_sets == None:
            self.rules_sets = []
            
        self.frames.append(frame)
        self.rules_sets.append(rules_set)
    
    
    def text_to_speech(self, text):
        os.system("echo " + text + " | espeak -s160")
        
        
    def speech_to_text(self):
        text = None
        if USE_MICROPHONE:
            loops_of_silence = 0
            
            while text == None:
                # obtain audio from the microphone
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("I'm listening")
                    audio = r.listen(source)
                    print("I'm not listening anymore")
                
                # recognize speech using Google Speech Recognition
                try:
                    text = r.recognize_google(audio)
                    print("I think you said: " + text)
                    
                except sr.UnknownValueError:
                    print("I can not understand audio")
                    loops_of_silence += 1
                    
                    # if for three times there's no audio then ask what to do
                    if loops_of_silence == 3:
                        print("Hey! Are you are there? What can I do for you?")
                        self.text_to_speech("Hey! Are you are there? What can I do for you?")
                        
                        loops_of_silence = 0
                        
                except sr.RequestError as e:
                    print("I'm offline")
        else:
            text = input("Input: ")
        
        return text
    
    
    # check the current_frame status, return the new target slot
    def check_state(self):
        if self.current_frame == None:
            return None
        
        for slot in self.current_frame.listslots():
            if self.current_frame.isempty(slot):
                return slot
        
        return None
    
    
    # if frame_slots is not filled, ask for more info frome the user
    def isfilled(self):
        if self.current_frame == None:
            return False
        else:
            for slot in self.current_frame.listslots():
                if self.current_frame.isempty(slot):
                    return False
            return True
    
    
    def extract_slot(self, nlp, sentence, target_slot):
        sentence = str.lower(sentence)
        
        tokens_nlp = nlp.word_tokenize(sentence)
        dependency_nlp = nlp.dependency_parse(sentence)

        dependency = Dependency(sentence, dependency_nlp, tokens_nlp)

        self.current_rules_set.update(dependency)
        fillers = self.current_rules_set.apply(target_slot)
        
        return zip(self.current_frame.listslots(), fillers)

    
    def determinate_domain(self, text):
        self.current_frame = self.frames[0]
        self.current_rules_set = self.rules_sets[0]
        return True
    
    
    def start(self):
        nlp = StanfordCoreNLP(r'/home/simone/Scrivania/stanford-corenlp-full-2018-10-05')
        
        text_input = self.speech_to_text()
        
        flag = self.determinate_domain(text_input)
        
        target_slot = None
        while flag and not self.isfilled():
            
            # extract slot
            slots = self.extract_slot(nlp, text_input, target_slot)
            
            # update the frame status
            for slot, value in slots:
                if value != None:
                    if type(value) == list:
                        self.current_frame.fillslot(slot, *value)
                    else:
                        self.current_frame.fillslot(slot, value)
            
            print()
            cleaningframe.pprint()
            print()
            
            # check the slots status
            target_slot = self.check_state()
            
            # when slots are filled, check_state will return None
            if(target_slot != None):
                new_question = self.current_frame.getquestion(target_slot)
                
                print(new_question)
                self.text_to_speech(new_question)
                
                text_input = self.speech_to_text()
                if(text_input == 'None'):
                    print('Input error. System exits!')
                    break
        
        nlp.close()
        #clean the kitchen quickly and the living room at 17 and at 18 on monday and tuesday
        print(self.current_rules_set.frame_to_text())
        self.text_to_speech(self.current_rules_set.frame_to_text())
 

if __name__ == "__main__":
    cleaningrules = CleaningRules(None)
    robot = CleanRobert([cleaningframe], [cleaningrules])
    robot.start()
