sum(N,N,N).
sum(N1,N2,Sum) :- N1 < N2, N is N1+1,
 sum(N,N2,Sum_I),
 Sum is Sum_I + N1.