from frame import Frame

NAME = "Cleaning Frame"

VERBS = ["clean"]
ROOMS = ["kitchen", "bathroom", "living room"]
MODES = ["quick", "quickly", "fast", "in-depth", "deep cleaning", "deeper cleaning", "deep"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
TIMES = range(0,24)
PERMANENT = ["yes", "no"]

QUESTIONS = [ 
 "Which room do you want to clean?", 
 "Do you want a quick or deep cleaning?",
 "Which days do you want to clean?", # Check: Default?: "today"
 "At what time do you prefer?",
 "Do you want to set this task as permanent?"]

SLOTS  = ["room", "mode", "day", "time", "permanent"]
VALUES = [ROOMS, MODES, DAYS, TIMES, PERMANENT] 

cleaningframe = Frame(NAME, SLOTS, VALUES, QUESTIONS)


# Testing below
if __name__ == "__main__":
    """ Testing frames """
    cleaningframe.pprint()

    print(cleaningframe.isempty("room"))

    cleaningframe.fillslot("room", *["kitchen", "living room"])
    cleaningframe.fillslot("mode", "quick")
    cleaningframe.fillslot("day", *["monday", "sunday"])
    cleaningframe.fillslot("time", 17)
    cleaningframe.fillslot("permanent", "yes")

    cleaningframe.pprint()

    print(cleaningframe.isempty("room"))

    print(cleaningframe.getslot("room"))

    print(cleaningframe.listslots())

    print(cleaningframe.listpossible("room"))

    print(cleaningframe.getquestion("room"))

    cleaningframe.reset()

    cleaningframe.pprint()
