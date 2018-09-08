%% Name:        Ben Belden
%% Class ID#:   bpb2v
%% Section:     CSCI 6180-001
%% Assignment:  Lab #4
%% Due:         16:20:00, November 1, 2017
%% Purpose:     Write a PROLOG program that provides the same functionaLity as p3, 
%%				i.e. determines satisfiabiLity for a set of propositional Clauses. 
%%				It must run with gprolog on system64.
%% Input:       From preformatted file.  
%% Outut:       To terminal.
%% 
%% File:        p4.pl

deleteSats([Clause|ClausesLeft], Lit, ClauseList) :-
    member(Lit, Clause),
    deleteSats(ClausesLeft, Lit, ClauseList).
deleteSats([Clause|ClausesLeft], Lit, ClauseList) :-
    \+ member(Lit, Clause),
    ClauseList = [Clause|TempClauseList],
    deleteSats(ClausesLeft, Lit, TempClauseList).
deleteSats([], _, []).

sat([Clause|ClausesLeft], TempSol, Solution) :-
    member(X, Clause),
    NegX is -X,
    \+ member(NegX, TempSol),
    deleteSats(ClausesLeft, X, UpdatedClausesLeft),
    sat(UpdatedClausesLeft, [X|TempSol], Solution).

sat([], V, V).

outputSolution([Lit|LitsLeft]) :-
    Lit > 0,
    format('assignment ~d 1\n', [Lit]),
    outputSolution(LitsLeft).
outputSolution([Lit|LitsLeft]) :-
    Lit < 0,
    format('assignment ~d 0\n', [-Lit]),
    outputSolution(LitsLeft).
outputSolution([]).

sat_with_print(Clauses) :-
    sat(Clauses, [], Solution),
    setof(Lit, member(Lit, Solution), UniqueSol),
    !,
    outputSolution(UniqueSol).

sat_with_print(Clauses) :-
    \+ sat(Clauses, [], _),
    print('UNSATISFIABLE').


