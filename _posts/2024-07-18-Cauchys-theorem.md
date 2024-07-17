In the previous post, we applied the orbit-stabiliser theorem to groups whose order is divisible by a single prime <span>$p$</span>. However, it can also be applied to get information about the behaviour of a prime <span>$p$</span> dividing the order of an arbitrary group <span>$G$</span>. In particular:
 - (i) Cauchy's theorem states that if <span>$p$</span> divides <span>$|G|$</span>, then <span>$G$</span> has an element of order <span>$p$</span> (and hence a subgroup of order <span>$p$</span>)
  - (ii) At the other extreme, Sylow's (first) theorem states that if <span>$p^n$</span> is the largest power of <span>$p$</span> dividing <span>$|G|$</span>, then <span>$G$</span> has a subgroup of order <span>$p^n$</span>
  - (iii) In fact, for *any* prime power <span>$p^k$</span> dividing <span>$|G|$</span>, <span>$G$</span> has a subgroup of order <span>$p^k$</span>.[^incredible]
In fact, we can already deduce (iii) conditionally on (ii): Suppose <span>$P$</span> has order <span>$p^n$</span>. We saw in a previous post that <span>$P$</span> is therefore solvable. Hence, it has a filtration <span>$\{e\}\subseteq P_1 \subseteq P_2 \subseteq \ldots P_{n-1} \subseteq P_n = P$</span> with <span>$P_k/P_{k-1} \cong C_p$</span>. Then <span>$P_k$</span> has order <span>$p^k$</span>. 

*Theorem: Cauchy's theorem*\
Let <span>$G$</span> be a finite group and suppose <span>$p$</span> divides <span>$|G|$</span>. Then <span>$G$</span> has an element of order <span>$p$</span>.

Proof 1:\
Define 
<div>$$X = \{(g_1,\ldots, g_p) \in G^p: g_1g_2\ldots g_p = e\} $$</div>
and let <span>$C_p$</span> act on <span>$X$</span> by cyclic permutation; this action is well-defined since
<div>$$g_2\ldots g_pg_1 = g_1^{-1}g_1\ldots g_pg_1 = g^{-1}g_1 = e $$</div>
But by the <span>$p$</span>-group fixed-point lemma
<div>$$|\textrm{Fix}(X)| \cong |X| = |G|^{p-1} \cong 0 \textrm{ mod } p$$</div>
and
<div>$$\textrm{Fix}(X) = \{(g,g,\ldots,g): g\in G \text{ has order } 1 \text{ or } p\} $$</div>
Now <span>$e\in \textrm{Fix}(X)$</span> so <span>$|\textrm{Fix}(X)| \geq p$</span> and any non-identity element of <span>$\textrm{Fix}(X)$</span> then has order <span>$p$</span>.

This argument is almost *too* slick to be easily understood. To get a better grasp on it, consider the case <span>$n=2$</span>; then the fibres of the map <span>$x\mapsto x^2$</span> partition <span>$G$</span> into self-inverse elements and element-inverse pairs. The identity element is always self-inverse, so when <span>$|G|$</span> is even, we then know that there has to be another self-inverse element i.e. an element of order <span>$2$</span>. The above proof should be seen as an adaptation of this strategy to deal with other primes.

We can also give a less slick argument, which I prefer:#

Proof 2:\
By induction on <span>$|G|$</span>[^hate]. \
Case <span>$G$</span> is Abelian: Pick <span>$g\in G$</span>. We have three possibilities:
 - (i) <span>$\textrm{ord}(g) = p$</span>, we're done
 - (ii) <span>$p|\textrm{ord}(g)$</span>. Then some power of <span>$g$</span> has order <span>$p$</span>
 - (iii) <span>$p\not |\textrm{ord}(g)$</span>. Then since <span>$G$</span> is Abelian, the subgroup <span>$\langle g\rangle$</span> is normal so we have the quotient group <span>$G/\langle g\rangle$</span>. By induction, G/\langle g\rangle has an element of order <span>$p$</span>, whose preimage in <span>$G$</span> has order divisible by <span>$p$</span>, and we're in case (ii).
Case <span>$G$</span> is not Abelian: Note that <span>$|Z(G)| < |G|$</span>. If <span>$p$</span> divides <span>$|Z(G)|$</span>, then by induction <span>$Z(G)$</span> has an element of order <span>$p$</span> and we're done. So suppose that <span>$p$</span> does not divide <span>$|Z(G)|$</span>. By the class equation
<div>$$|G| =  \sum\limits_{\text{conjugacy classes}} [G:C_G(g)] = |Z(G)| + \sum\limits_{\text{non-trivial conjugacy classes}} [G:C_G(g)]$$</div>
and <span>$p$</span> divides <span>$|G|$</span> so there exists <span>$g\in G\setminus Z(G)$</span> such that <span>$p$</span> does not divide <span>$\frac{|G|}{|C_G(g)|}$</span>, hence <span>$p$</span> divides <span>$|C_G(g)|$</span>. By assumption <span>$g\not \in Z(G)$</span> so <span>$|C_G(g)| < |G|$</span> and by induction <span>$C_G(g)$</span> has an element of order <span>$p$</span>.

The main idea (for the non-Abelian case) is to find a proper subgroup of <span>$G$</span> which also has order divisible by <span>$p$</span>. The class equation allows us to play the centre and centralisers against one another in this regard. Notice how it is very important then that the fixed points of the conjugation action form a group! In fact, in both the Abelian and non-Abelian case, one is making use of the duality between substructures and quotient structures - in the Abelian case this is subgroups and quotient groups and in the non-Abelian case this is in the category of <span>$G$</span>-sets. Specifically, fixed-points form a sub-<span>$G$</span>-set and the stabiliser <span>$C_G(g)$</span> is like a kind of kernel for the <span>$G$</span>-action on that orbit (that is, conjugacy class) and thus represents how the conjugacy class arises as a quotient <span>$G$</span>-set of <span>$G$</span> (under the conjugation action).

Next time we'll look at some proofs of Sylow's theorems, many of which are souped-up versions of the above proofs.


[^incredible]: This is one of those slightly incredible facts which makes me say: *why did no one tell me?*

[^hate]: I actually really hate to put this at the start of the proof - it's much nicer to start the argument and let the idea to use induction fall out of it naturally. But the argument isn't technically correct if you only start inducting halfway through.