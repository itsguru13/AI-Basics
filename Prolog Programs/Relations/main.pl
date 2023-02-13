male(tom).
male(bob).
male(jim).
female(pam).
female(liz).
female(ann).

husband(tom):- female(pam).
husband(tom):- female(liz).
parents(tom, pam):- male(bob).
parents(bob, liz):- male(jim), female(ann). 
grandparents(tom, pam):- male(jim), female(ann).

    