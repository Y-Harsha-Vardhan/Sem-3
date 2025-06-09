## Natural Deduction:

-  Given a set of **premises**, we deduce a **conclusion** which is also a formula using proof rules
-  $\phi_1,....,\phi_n \vdash \psi$  : This is called a sequent.   
-  $\phi_1,....,\phi_n$  are **premises**, and $\psi$ is the **conclusion** 

### Rules for Natural Deduction:

- The "and introduction rule" denoted by :-  $\land$i  :  $\phi$ and $\psi$  gives $\phi\land\psi$ 

- The "and elimination rules" denoted by :- $\land e_1$ and $\land e_2$  :  $\phi\land\psi$  gives either  $\phi$  (or)  $\psi$  for $e_1$ or $e_2$ respectively

- The "rule of double negation elimination" denoted by :-  $\neg\neg$ e  :  $\neg\neg\phi$  gives $\phi$

- The "rule of double negation introduction" denoted by :-  $\neg\neg$ i  :  $\phi$ gives $\neg\neg\phi$ 

- The "implies elimination rule" or "Modus Pones" denoted by :- MP :   $\phi$  and  $\phi\to\psi$  gives  $\psi$

- Another "implies elimination rule" or "Modulus Tollens" denoted by :- MT :  $\phi\to\psi$  and  $\neg \psi$  gives  $\neg \phi$ 

- The "implies introduction rule" denoted by :-  $\to$ i
This means:  "If assuming A leads to B, then  A $\to$ B"
A is a temporary assumption, once you derive B, then A implies B and hence, we discharge the assumption A, it no longer remains in the premises
#### Transforming Proofs:
Transform any proof  $\phi_1,....,\phi_n$ $\vdash$ $\psi$  to 
	$\vdash$ $\phi_1\to$ ($\phi_2\to$ . . . ($\phi_n\to\psi$) . . . ))  by adding n lines of the rule  $\to$ i



- The "or introduction rule" denoted by :-  $\lor i_1$  :   $\phi$  gives  $\phi \lor \psi$   
	and  $\lor i_2$  :  $\psi$  gives  $\phi\lor\psi$ 

- The "or elimination rule" denoted by :-  $\lor e$  :   
	$\phi\lor\psi$  ,  $\phi\vdash\chi$  and   $\psi\vdash\chi$   give   $\chi$

- The "copy rule" allows us to reiterate a previously proved statement without any justification

-  The notion of "contradictions", an expression of the form:  $\phi \land \neg\phi$ , where $\phi$ is any propositional logic formula. Any 2 contradictions are equivalent. Contradictions are denoted by $\perp$ . 
	$\perp$  $\to\phi$  for any formula $\phi$ 

 - The "$\perp$ elimination rule" denoted by :-  $\perp e$  :  $\perp$  gives  $\psi$ 
 
 - The  "$\perp$ introduction rule" denoted by :-  $\perp i$  :  $\phi$ and $\neg\phi$   gives   $\perp$ 

 -  In the course of a proof, if you assume $\phi$  (by opening a box) and obtain $\perp$ in the box, then we conclude $\neg\phi$ .  This rule is denoted:  $\neg$ i  and is read as  $\neg$ introduction. This is also known as Proof By Contradiction (PBC).
 
 -  Law of Excluded Middle (LEM) :  For a given propositional statement  $\phi$,  $\phi \lor \neg\phi$  i.e., the statement is either true / false, there is no middle ground.

 - All the above rules were used in a purely "syntactic" proof.
 
####  Semantics:
Each propositional variable is assigned values: true/false. Truth tables for each of the operators $\lor, \land, \neg, \to$ are used to determine truth values of complex formulae.

-   $\phi_1,...,\phi_n$  $\models$  $\psi$  iff whenever  $\phi_1,...,\phi_n$  evaluate to true, so does  $\psi$ .
	$\models$  is read as semantically entails

-  Formulae  $\phi$ and $\psi$  are provably equivalent  iff  $\phi\vdash\psi$  and  $\psi\vdash\phi$ 
	Formulae  $\phi$ and $\psi$  are semantically equivalent iff  $\phi\models\psi$ and $\psi\models\phi$ 