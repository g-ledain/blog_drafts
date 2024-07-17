In the previous post, we applied the orbit-stabiliser theorem to groups whose order is divisible by a single prime $p$. However, it can also be applied to get information about the behaviour of a prime $p$ dividing the order of an arbitrary group $G$. In particular:
 - (i) Cauchy's theorem states that if $p$ divides $|G|$, then $G$ has an element of order $p$ (and hence a subgroup of order $p$)
  - (ii) At the other extreme, Sylow's (first) theorem states that if $p^n$ is the largest power of $p$ dividing $|G|$, then $G$ has a subgroup of order $p^n$
  - (iii) In fact, for *any* prime power $p^k$ dividing $|G|$, $G$ has a subgroup of order $p^k$.[^incredible]
In fact, we can already deduce (iii) conditionally on (ii): Suppose $P$ has order $p^n$. We saw in a previous post that $P$ is therefore solvable. Hence, it has a filtration $\{e\}\subseteq P_1 \subseteq P_2 \subseteq \ldots P_{n-1} \subseteq P_n = P$ with $P_k/P_{k-1} \cong C_p$. Then $P_k$ has order $p^k$. 

*Theorem: Cauchy's theorem*\
Let $G$ be a finite group and suppose $p$ divides $|G|$. Then $G$ has an element of order $p$.

Proof 1:\
Define 
$$X = \{(g_1,\ldots, g_p) \in G^p: g_1g_2\ldots g_p = e\} $$
and let $C_p$ act on $X$ by cyclic permutation; this action is well-defined since
$$g_2\ldots g_pg_1 = g_1^{-1}g_1\ldots g_pg_1 = g^{-1}g_1 = e $$
But by the $p$-group fixed-point lemma
$$|\textrm{Fix}(X)| \cong |X| = |G|^{p-1} \cong 0 \textrm{ mod } p$$
and
$$\textrm{Fix}(X) = \{(g,g,\ldots,g): g\in G \text{ has order } 1 \text{ or } p\} $$
Now $e\in \textrm{Fix}(X)$ so $|\textrm{Fix}(X)| \geq p$ and any non-identity element of $\textrm{Fix}(X)$ then has order $p$.

This argument is almost *too* slick to be easily understood. To get a better grasp on it, consider the case $n=2$; then the fibres of the map $x\mapsto x^2$ partition $G$ into self-inverse elements and element-inverse pairs. The identity element is always self-inverse, so when $|G|$ is even, we then know that there has to be another self-inverse element i.e. an element of order $2$. The above proof should be seen as an adaptation of this strategy to deal with other primes.

We can also give a less slick argument, which I prefer:#

Proof 2:\
By induction on $|G|$[^hate]. \
Case $G$ is Abelian: Pick $g\in G$. We have three possibilities:
 - (i) $\textrm{ord}(g) = p$, we're done
 - (ii) $p|\textrm{ord}(g)$. Then some power of $g$ has order $p$
 - (iii) $p\not |\textrm{ord}(g)$. Then since $G$ is Abelian, the subgroup $\langle g\rangle$ is normal so we have the quotient group $G/\langle g\rangle$. By induction, G/\langle g\rangle has an element of order $p$, whose preimage in $G$ has order divisible by $p$, and we're in case (ii).
Case $G$ is not Abelian: Note that $|Z(G)| < |G|$. If $p$ divides $|Z(G)|$, then by induction $Z(G)$ has an element of order $p$ and we're done. So suppose that $p$ does not divide $|Z(G)|$. By the class equation
$$|G| =  \sum\limits_{\text{conjugacy classes}} [G:C_G(g)] = |Z(G)| + \sum\limits_{\text{non-trivial conjugacy classes}} [G:C_G(g)]$$
and $p$ divides $|G|$ so there exists $g\in G\setminus Z(G)$ such that $p$ does not divide $\frac{|G|}{|C_G(g)|}$, hence $p$ divides $|C_G(g)|$. By assumption $g\not \in Z(G)$ so $|C_G(g)| < |G|$ and by induction $C_G(g)$ has an element of order $p$.

The main idea (for the non-Abelian case) is to find a proper subgroup of $G$ which also has order divisible by $p$. The class equation allows us to play the centre and centralisers against one another in this regard. Notice how it is very important then that the fixed points of the conjugation action form a group! In fact, in both the Abelian and non-Abelian case, one is making use of the duality between substructures and quotient structures - in the Abelian case this is subgroups and quotient groups and in the non-Abelian case this is in the category of $G$-sets. Specifically, fixed-points form a sub-$G$-set and the stabiliser $C_G(g)$ is like a kind of kernel for the $G$-action on that orbit (that is, conjugacy class) and thus represents how the conjugacy class arises as a quotient $G$-set of $G$ (under the conjugation action).

Next time we'll look at some proofs of Sylow's theorems, many of which are souped-up versions of the above proofs.


[^incredible]: This is one of those slightly incredible facts which makes me say: *why did no one tell me?*

[^hate]: I actually really hate to put this at the start of the proof - it's much nicer to start the argument and let the idea to use induction fall out of it naturally. But the argument isn't technically correct if you only start inducting halfway through.