# Elliptic-Curve-Cryptography---Implementation

This repository contains the code for the following problem statement :-
We take a secure Elliptic Curve Ep (a,b), where p is a large (greater than 5000) prime number. We then implement point addition and multiplication algorithms on this curve.

Further, we pick a randomly chosen point P from the curve and calculate the order of the point. The point P should be such that Ord(P)
= q, where q is a large prime. Then a large set of Q values are generated using randomly chosen k-bit(k = ceil(log<sub>2</sub>)q) strings.The decimal values of these chosen strings are all lesser than q-1. The following tests are performed on the Q values :-

a) Whether the Q values are uniform-randomly distributed on the cyclic group generated by P.
b) Whether the Q values are uncorrelated even when there are high statistical correlations among the input k-bit strings.

(Please refer to the report and the presentation for a detailed understanding of the topic.)

Feel free to reach out to me in case you need any help with the topic.
