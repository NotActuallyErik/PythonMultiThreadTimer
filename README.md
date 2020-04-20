# PythonMultiThreadTimer
A simple multi-thread Python timer. Useful for running independent timers in code

Instantiate by assigning class call to variable

    Example: x = Time()
    
then proceed to call Timer-methods by x.classMethod(args, kwargs)




    getTimer()

returns the timers current value


    resetTimer() 

resets the timer to zero


    setResetTimer(endtime: float) 

resets the timer in endtime-amount of seconds, starts a new thread


    getBool() 

returns the timers boolean value


    setBool(setTo: bool) 

sets the timers boolean value to SetTo


    setBoolTimer(endTime: float, arg: bool, name: str) 

sets the timers boolean value to arg after endTime-amount of seconds, starts a new nameable thread

