from time import strftime

def myClock():
    # Run a perpetual loop for the clock
    while True:
        return strftime("%Z") + "\n" + strftime("%A, %B %d %Y") + "\n" + "" + strftime("%I:%M:%S %p")