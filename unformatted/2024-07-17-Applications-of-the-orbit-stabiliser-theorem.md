The orbit-stabiliser theorem is a theorem about group actions on sets but it really shines when applied to a group acting on itself.

# The conjugation action
We have already seen how a group $G$ acts on itself and on any collection of cosets $G/H$ by left-multiplication - the action is transitive and has stabiliser $H$. There is another action of $G$ on itself which always exists - the conjugation action. Specifically, we have any action
$$ G\times G \to G $$
$$ g.h := ghg^{-1}$$
This action has the advantage that conjugation is always an automorphism - so its "curried" form gives a map $G \to \textrm{Hom}_{\textrm{Grp}}(G,G)$ rather than simply a map $G \to \textrm{Hom}_{\textrm{Set}}(G,G)$ which one would normally have for a group action[^quotients]. 

When we see a new group action we should always compute its orbits, stabilisers and fixed points.

*Definition and notation*[^notation]:\
Let $G$ be a group and $g\in G$. We define:
 - The conjugacy class $$C(g) = \{hgh^{-1}: h\in G\} $$
 - The centraliser $$ C_G(g) = \{h\in G: hgh^{-1}\} = \{h\in G: hg=gh\} $$
 - The centre $$Z(G)=\{g\in G: gh=hg \text{ for all } h\in G\} = \{g\in G: ghg^{-1}=h \text{ for all } h\in G\}$$

 *Proposition*: \
 Consider a group $G$ acting on itself by conjugation and let $g\in G$. Then:
 - (i) $\textrm{Orb}(g) = C(g)$
 - (ii) $\textrm{Stab}(g) = C_G(g)$
 - (iii) $\textrm{Fix}(g) = C_G(g)$
 - (iv) $g\in \textrm{Stab}(h) \Leftrightarrow h\in \textrm{Stab}(g) \Leftrightarrow g\in \textrm{Fix}(h) \Leftrightarrow h\in \textrm{Stab}(g) \Leftrightarrow g, h \text{ commute }$
 - (v) $ Z(G) = \textrm{Fix}(G) = \bigcap_{g\in G} C_G(g) $[^consequence]

 Proof: Exercise

 The above proposition may seem rather trivial but it is worth stopping to reflect on a few things:
  - There is evidently a very strong link between commutation and conjugation. This link plays an important role in elementary group theory.
  - The centraliser shows up as _both_ the stabiliser and the fixed-points! This turns out to be unreasonably important. Specifically, for a generic group action of $G$ on a set $X$, the set of fixed-points is just a plain set, whereas the stabilisers are always subgroups of $G$. However in our case the fixed-points also form a subgroup![^automorphisms]. We will return to this later.

We can extend these notions to subsets of $G$, and doing so leads to another concept which will be important to us - the _normaliser_.

*Definition: Centraliser and normaliser*\
Let $G$ be a group and $S\subseteq G$. We define:
 - The centraliser of $S$ to be $$C_G(S):=\{g\in G: gsg{-1}=s \text{ for all } s\in S\} = \bigcap_{s\in S} C_G(s) $$
 - The normaliser of $S$ to be $$N_G(S):=\{ g\in G: gSg^{-1}= S\} $$

When $H$ is a subgroup of $G$, the normaliser $N_G(H)$ is the largest subgroup of $G$ in which $H$ is normal. However the centraliser is _not_ the largest subgroup of $G$ in which $S$ is central. However if $S$ is _commutative_, then $N_G(S)$ is the largest subgroup of $G$ such that $N_G(S)$ in which $S$ is central.

The above definitions are best understood as follows: Since $G$ acts on $G$ by conjugation, it therefore also acts on $\mathcal{P}(G)$. The normaliser $N_G(S)$ is then the stabiliser of $S$. The difference between the centraliser and normaliser of $S$ is the difference between a set being fixed _as a set_ and being fixed _pointwise_.

## Orbit decomposition of the conjugation action
Whenever a group $G$ acts on a set $X$, we should think about the orbit decomposition of $X$. 

The very smallest orbits contain the most "special" elements of $X$ - their stabiliers are largest, so they are the "most symmetrical". I like to think of these elements as lying in the "heart" of the set $X$; the two pictures I keep in mind are the centre of a rotation (say, under the usual action of $S^1$ on the plane by rotations) or the axis of a reflection (say, under the action of $\mathbb{Z}/2\mathbb{Z}$ by a reflection). The point (resp. the axis) are the only points with nontrivial stabiliser, and all the other points revolve around them.

The largest orbits contain the most "generic" elements of $X$ - in most real-life situations, especially geometrical ones, only a finite/discrete set have non-trivial stabilisers[^example]. Actions by finite groups tend to have larger stabilisers but the intuition is good to bear in mind.

When $G$ is a $p$-group[^definition], this decomposition is especially simple and powerful: the stabilisers are all powers of $p$ and so we can image $X$ as having a "filtration" by powers of $p$ according to the size of the stabiliser.We can view the lower powers of $p$ as being "leading terms" in a kind of power series expansion, and many arguments consist of comparing these leading terms[^adic]. 

In this vein, we now come to possibly the most important application of the orbit-stabiliser theorem to finite group theory.

*Lemma: The $p$-group fixed-point lemma*\
Let $G$ be a finite $p$-group acting on a finite set $X$. Then
$$|X| \equiv |\textrm{Fix}(X)| \text{ mod } p$$

Proof:\
We have 
$$X = \coprod_{\mathcal{O} \in \textrm{Orbit}(X)} \mathcal{O} = \textrm{Fix}(X) \coprod \left(\coprod_{\mathcal{O} \in \textrm{Orbit}(X)} \mathcal{O}\right)$$
so
But by the orbit stabiliser theorem $|\mathcal{O}|$ divides $|G|$, so when $|\mathcal{O}|>1$, we have $p$ divides $|\mathcal{O}|$.

The same logic of splitting into trivial versus non-trivial orbits underlies a classic result called the "class equation".

*Proposition: The class equation*\
For a finite group $G$ we have
$$|G| =  \sum\limits_{\text{conjugacy classes}} [G:C_G(g)] = |Z(G)| + \sum\limits_{\text{non-trivial conjugacy classes}} [G:C_G(g)]$$

Proof: use the orbit-stabiliser theorem and the orbit decomposition.

# Some consequences in finite group theory
Applying our fixed-point theorem for $p$-groups acting on themselves by conjugation immediately gives the following:

*Proposition: The centre of a $p$-group*\
$p$-groups have non-trivial centre.

Proof:\
By the $p$-group fixed-point lemma, $p$ divides $|Z(G)|$. But $e\in Z(G)$ so $|Z(G)|\geq p$.

Corollary: $p$-groups are nilpotent, and in particular are solvable.

*Proposition:*\
Suppose that $G$ is a group and $|G|=p^2$. Then $G\cong C_{p^2}$ or $G\cong C_p \times C_p$.

Proof:\
By the previous result, we have $Z(G) \neq \{e\}$ so fix $x\in Z(G)\setminus\{e\}$. If $G$ is cylic we're done, so suppose $y \in G\setminus \langle x \rangle$. Since $G$ is not cyclic and $x,y\neq e$ we have by Lagrange that $\textrm{ord}(x)=\textrm{ord}(y)=p$. Now $\langle x \rangle \cap \langle y \rangle = 1 \text{ or } p$ and $|\langle x,y \rangle| = p \text{ or } p^2$. But $y \not\in \langle x \rangle$ so $\langle x \rangle \cap \langle y \rangle = 1$ and $|\langle x,y \rangle| = p^2$. Define
$$\phi: C_p\times C_p \to G $$
$$(n,m) \mapsto x^ny^m $$
Then $\phi$ is:
 - A homomorphism since $x,y$ commute 
 - Injective since $\langle x \rangle \cap \langle y \rangle = 1$
 - Surjective since $|\langle x,y \rangle| = p^2$

Note that the final part of this argument is entirely generic: whenever $H,K$ are subgroups of $G$ such that elements of $H$ commute with elements of $K$ and $H\cap K = \{e\}$, we have $G\cong H\times K$ via an analogous map.



[^quotients]: Similarly to the left-multiplication action of $G$ on the cosets $G/H$, one can have a conjugation action of $G$ on $G/H$ but it is only well-defined when $H$ is a normal subgroup of $G$ - thus, it is also an action of $G$ on  the group $G/H$ by group automorphisms. 

[^notation]: The notation here is awful: $C(G)$ and $C_G(g)$? Really? What if I have a subgroup $H \subseteq G$ and I want to compare the conjugacy class of $h\in H$ with respect to $H$ and $G$? I can't use $C_H(g)$ and $C_G(g)$. There are probably alternative notations but I am lazy.

[^automorphisms]: This is ultimately a consequence of the action of $G$ on itself being by _automorphisms_. More generally you can check that for any group $G$ acting on a group $H$ by automorphisms, $\textrm{Fix}(g)$ is always a subset of $H$.

[^consequence]: This is just a consequence of the general fact that $\textrm{Fix}(G) = \bigcap_{g\in G} \textrm{Fix}(g)$.

[^example]: The two following examples are prime examples of this phenomenon. A slightly more advanced example is the action of $\textrm{SL}_2(\mathbb{Z})$ on the upper half-plane by Mobius transformations - the analysis of the stabilisers of this action is an elementary part of the theory of modular forms.

[^definition]: That is, the order of $G$ is a power of $p$.

[^adic]: This power series analogy is the concept underlying $p$-adic numbers.