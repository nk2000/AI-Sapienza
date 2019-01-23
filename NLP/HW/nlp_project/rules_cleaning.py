from frame_cleaning import cleaningframe

from datetime import date
import calendar

class CleaningRules:
    """ Rules """
    def __init__(self, dependency):
        self.dependency = {}
        self.update(dependency)
        values = []
        for slot in cleaningframe.listslots():
            values.append(cleaningframe.listpossible(slot))
        self.possible = dict(zip(cleaningframe.listslots(), values))

    def update(self, dependency):
        if dependency != None:
            self.dependency = dependency

    def lookup(self, word_index, mod): # This should return a list! Fix!
        for item in self.dependency.getdependency():
          if(  item[self.dependency.relation] == mod 
             and item[self.dependency.origin] == word_index):
                return self.dependency.gettoken(item[self.dependency.dest]), item[self.dependency.dest]
        return None, None

    def check_compound(self, word):
        cword, _ = self.lookup(word, "compound")
        if (cword):
            return cword + " " + self.dependency.gettoken(word)
        return self.dependency.gettoken(word)
    
    def rooms(self):
        sentence_rooms = []
        for relation in self.dependency.getdependency():
            mod, w1, w2 = relation
            if mod == "amod" or mod == "dobj":
                if self.dependency.gettoken(w2) == "clean":
                    conj, iconj = self.lookup(w1, "conj")
                    
                    word = self.check_compound(w1)
                    if (conj):
                        conj = self.check_compound(iconj)
                        sentence_rooms = [word, conj]  
                    #map((lambda word: check_compound(dependency, word)), sentence_rooms) 
                    else:
                        sentence_rooms = [word]
            if mod == "dobj" and sentence_rooms == []:
                if self.dependency.gettoken(w1) == "clean":
                    word = self.dependency.gettoken(w2)
                    sentence_rooms = [word]
        return sentence_rooms

    def mode(self):
        mode = None
        for relation in self.dependency.getdependency():
            mod, w1, w2 = relation
            if mod == "advmod":
                word = self.dependency.gettoken(w1)
                if word in ["clean", "do"]+self.possible["room"]:
                    mode = self.dependency.gettoken(w2)
            if mod == "nsubj":
                word = self.dependency.gettoken(w1)
                if word in self.possible["room"]:
                    mode = self.dependency.gettoken(w2)
            if mod == "amod":
                word = self.dependency.gettoken(w1)
                if word == "cleaning":
                    mode = self.dependency.gettoken(w2)
        if mode == None: mode = self.mode_one()
        if (mode): return(mode)
        return None

    def mode_one(self):
        mode = None
        tokens = self.dependency.gettokens()
        if len(tokens) == 1 and tokens[0] in self.possible["mode"]:
            mode = tokens[0]
        return mode

    def lookup_relation(self, origin_index, destination_index):
        for item in self.dependency.getdependency():
            if item[self.dependency.origin] == origin_index and item[self.dependency.dest] == destination_index:
                return item[self.dependency.relation]
        return None
    
    def lookup_origin(self, mod, destination_index):
        for item in self.dependency.getdependency():
            if item[self.dependency.relation] == mod and item[self.dependency.dest] == destination_index:
                return item[self.dependency.origin], self.dependency.gettoken(item[self.dependency.origin])
        return None, ""
    
    def lookup_destination(self, mod, origin_index):
        for item in self.dependency.getdependency():
            if item[self.dependency.relation] == mod and item[self.dependency.origin] == origin_index:
                return item[self.dependency.dest], self.dependency.gettoken(item[self.dependency.dest])
        return None, ""
    
    def day(self):
        time_adverbs = ["today", "tomorrow"]
        days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        
        days = []
        tokens = self.dependency.gettokens()
        for token_index, token in enumerate(tokens): 
            is_time_adverb = token in time_adverbs
            is_day_of_week = token in days_of_week
            has_preposition = self.lookup_destination("case", token_index)[1] == "on"
            has_determiner = self.lookup_destination("det", token_index)[1] == "every" or self.lookup_destination("det", token_index)[1] == "each"
            
            clean_index = self.lookup_origin("nmod", token_index)[0]
            has_negation = (self.lookup_destination("neg", token_index)[0] is not None) or (clean_index is not None and self.lookup_destination("neg", clean_index)[0] is not None)
            
            if is_day_of_week and has_preposition and not has_negation:
                days.append(token)
                
            if is_day_of_week and has_determiner and not has_negation:
                days.append(token)
            
            if is_time_adverb and not has_negation:
                days.append(token)
            
            if is_day_of_week and not has_negation:
                days.append(token)
        
        today_number = date.today().weekday()
        tomorrow_number = (today_number + 1) % 7
        today_weekday = calendar.day_name[today_number].lower()
        tomorrow_weekday = calendar.day_name[tomorrow_number].lower()
        
        for i, day in enumerate(days):
            if day == "today":
                days[i] = today_weekday
            if day == "tomorrow":
                days[i] = tomorrow_weekday
        
        return days
    
    def time(self):
        times = []
        tokens = self.dependency.gettokens()
        for token_index, token in enumerate(tokens):
            try: 
                time = int(token)
                if time > -1 and time < 25:
                    is_time = True
                else:
                    is_time = False
            except ValueError:
                is_time = False
            
            has_preposition = self.lookup_destination("case", token_index)[1] == "at"
            
            clean_index = self.lookup_origin("nmod", token_index)[0]
            has_negation = (self.lookup_destination("neg", token_index)[0] is not None) or (clean_index is not None and self.lookup_destination("neg", clean_index)[0] is not None)
            
            if is_time and has_preposition and not has_negation:
                times.append(time)
            
            if is_time and not has_negation and len(tokens) == 1:
                times.append(time)
            
        return times
    
    def permanent_one(self):
        tokens = self.dependency.gettokens()
        #assert(len(tokens)==1)
        if len(tokens) == 1:
            if tokens[0] == 'yes': answer = 'yes'
            else: 
              if tokens[0] == 'no': answer = 'no'
              else: answer = None 
        return [None, None, None, None, answer]

    def permanent(self):
        days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        
        permanent_days = None
        permanent_flag = None
        for token_index, token in enumerate(self.dependency.gettokens()): 
            is_day_of_week = token in days_of_week
            is_day = (token == 'day')
            has_every_each = self.lookup_destination('det',token_index)[1] in ['every','each']
            
            clean_index = self.lookup_origin("nmod", token_index)[0]
            has_negation = (self.lookup_destination("neg", token_index)[0] is not None) or (clean_index is not None and self.lookup_destination("neg", clean_index)[0] is not None)
            
            if has_every_each and is_day_of_week and not has_negation:
                permanent_flag = 'yes'
            
            if is_day and has_every_each:
                permanent_flag = 'yes'
                permanent_days = days_of_week

        return permanent_flag, permanent_days
    
    def all(self):
        rooms = self.rooms()
        mode = self.mode()
        days = self.day()
        times = self.time()
        permanent, permanent_days = self.permanent()
        if permanent_days != None:
            days = permanent_days
        return [rooms, mode, days, times, permanent]

    def apply(self, slot):
        if (slot == None):
            return self.all()
        if (slot == 'permanent'):
            return self.permanent_one()
        if (slot == 'room'):
            fillers = self.all()
            if fillers[0] == [] or fillers[0] == None:
                return [None] * 5
            else:
                return fillers
        if (slot == 'mode'):
            fillers = self.all()
            if fillers[1] == [] or fillers[1] == None:
                return [None] * 5
            else:
                return fillers
        if (slot == 'day'):
            fillers = self.all()
            if fillers[2] == [] or fillers[2] == None:
                return [None] * 5
            else:
                return fillers
        if (slot == 'time'):
            fillers = self.all()
            if fillers[3] == [] or fillers[3] == None:
                return [None] * 5
            else:
                return fillers

    # the input is the return of cleaningframe.getslot('day')
    def convert_data(self, day):
        days = ''
        #print(len(day))
        
        if len(day) == 7:
            days = 'day'
        else:
            for i in range(len(day)):
                # join date with and if list is not from Monday to Sunday
                if i == 0:
                    days = days + day[i]
                else:
                    days = days + ' and ' + day[i]
        
        return days

    def frame_to_text(self):
        rooms = list(cleaningframe.getslot('room'))
        mode = list(cleaningframe.getslot('mode'))
        days = list(cleaningframe.getslot('day'))
        times = list(cleaningframe.getslot('time'))
        permanent = list(cleaningframe.getslot('permanent'))
        
        text = "Ok, I will {} clean the {} ".format(mode[0], rooms.pop(0))
        while len(rooms) > 0:
            text += "and the {} ".format(rooms.pop(0))
            
        text += "at {} ".format(times.pop(0))
        while len(times) > 0:
            text += "and at {} ".format(times.pop(0))
        
        if permanent[0] == "no":
            text =  text + 'on ' + self.convert_data(days)
        else:
            text =  text + 'every ' + self.convert_data(days)
        
        return text
            
            
            
            
