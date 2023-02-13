teacher(name('kalyan'), student(1), class('maths')).
teacher(name('nalini'), student(2), class('physics')).
teacher(name('puviarasi'), student(3), class('chemistry')).

teacherDB(Name, Student, Class):-
    teacher(name(Name), student(Year), class(Class)),
    format("Name: ~w~n", [Name]),
    format("Year: ~d\n", [Year]),
    format("Class: ~w~n", [Class]).