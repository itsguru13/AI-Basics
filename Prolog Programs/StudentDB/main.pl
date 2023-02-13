student(name('guru'), born(2003)).
student(name('nithik'), born(2002)).
student(name('nikhil'), born(2001)).

getDB(Name, Age):-
    student(name(Name), born(Year)),
    writeq(Name),
    write(' and '),
    Age is 2023 - Year.
    
    
    