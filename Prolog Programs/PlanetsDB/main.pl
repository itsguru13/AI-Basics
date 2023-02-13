planet(name('Mercury'), planet_no(1)).
planet(name('Venus'), planet_no(2)).    
planet(name('Earth'), planet_no(3)).
planet(name('Mars'), planet_no(4)).
planet(name('Jupiter'), planet_no(5)).
planet(name('Saturn'), planet_no(6)).
planet(name('Uranus'), planet_no(7)).
planet(name('Neptune'), planet_no(8)).

planetDB(Name, Position):-
    planet(name(Name), planet_no(POS)),
    Position is POS.