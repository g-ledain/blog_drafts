The orbit-stabiliser theorem is a theorem about group actions on sets but it really shines when applied to a group acting on itself.

# The conjugation action
We have already seen how a group <span>$G$</span> acts on itself and on any collection of cosets <span>$G/H$</span> by left-multiplication - the action is transitive and has stabiliser <span>$H$</span>. There is another action of <span>$G$</span> on itself which always exists - the conjugation action. Specifically, we have any action
<div>$$ G\times G \to G $$</div>
<div>$$ g.h := ghg^{-1}$$</div>
This action has the advantage that conjugation is always an automorphism - so its "curried" form gives a map <span>$G \to \textrm{Hom}_{\textrm{Grp}}(G,G)$</span> rather than simply a map <span>$G \to \textrm{Hom}_{\textrm{Set}}(G,G)$</span> which one would normally have for a group action[^quotients]. 

When we see a new group action we should always compute its orbits, stabilisers and fixed points.

*Definition and notation*[^notation]:\
Let <span>$G$</span> be a group and <span>$g\in G$</span>. We define:
 - The conjugacy class 
<div>$$C(g) = \{hgh^{-1}: h\in G\} $$</div>
 - The centraliser 
<div>$$ C_G(g) = \{h\in G: hgh^{-1}\} = \{h\in G: hg=gh\} $$</div>
 - The centre 
<div>$$Z(G)=\{g\in G: gh=hg \text{ for all } h\in G\} = \{g\in G: ghg^{-1}=h \text{ for all } h\in G\}$$</div>

 *Proposition*: \
 Consider a group <span>$G$</span> acting on itself by conjugation and let <span>$g\in G$</span>. Then:
 - (i) <span>$\textrm{Orb}(g) = C(g)$</span>
 - (ii) <span>$\textrm{Stab}(g) = C_G(g)$</span>
 - (iii) <span>$\textrm{Fix}(g) = C_G(g)$</span>
 - (iv) <span>$g\in \textrm{Stab}(h) \Leftrightarrow h\in \textrm{Stab}(g) \Leftrightarrow g\in \textrm{Fix}(h) \Leftrightarrow h\in \textrm{Stab}(g) \Leftrightarrow g, h \text{ commute }$</span>
 - (v) <span>$ Z(G) = \textrm{Fix}(G) = \bigcap_{g\in G} C_G(g) $</span>[^consequence]

 Proof: Exercise

 The above proposition may seem rather trivial but it is worth stopping to reflect on a few things:
  - There is evidently a very strong link between commutation and conjugation. This link plays an important role in elementary group theory.
  - The centraliser shows up as _both_ the stabiliser and the fixed-points! This turns out to be unreasonably important. Specifically, for a generic group action of <span>$G$</span> on a set <span>$X$</span>, the set of fixed-points is just a plain set, whereas the stabilisers are always subgroups of <span>$G$</span>. However in our case the fixed-points also form a subgroup![^automorphisms]. We will return to this later.

We can extend these notions to subsets of <span>$G$</span>, and doing so leads to another concept which will be important to us - the _normaliser_.

*Definition: Centraliser and normaliser*\
Let <span>$G$</span> be a group and <span>$S\subseteq G$</span>. We define:
 - The centraliser of <span>$S$</span> to be 
<div>$$C_G(S):=\{g\in G: gsg{-1}=s \text{ for all } s\in S\} = \bigcap_{s\in S} C_G(s) $$</div>
 - The normaliser of <span>$S$</span> to be 
<div>$$N_G(S):=\{ g\in G: gSg^{-1}= S\} $$</div>

When <span>$H$</span> is a subgroup of <span>$G$</span>, the normaliser <span>$N_G(H)$</span> is the largest subgroup of <span>$G$</span> in which <span>$H$</span> is normal. However the centraliser is _not_ the largest subgroup of <span>$G$</span> in which <span>$S$</span> is central. However if <span>$S$</span> is _commutative_, then <span>$N_G(S)$</span> is the largest subgroup of <span>$G$</span> such that <span>$N_G(S)$</span> in which <span>$S$</span> is central.

The above definitions are best understood as follows: Since <span>$G$</span> acts on <span>$G$</span> by conjugation, it therefore also acts on <span>$\mathcal{P}(G)$</span>. The normaliser <span>$N_G(S)$</span> is then the stabiliser of <span>$S$</span>. The difference between the centraliser and normaliser of <span>$S$</span> is the difference between a set being fixed _as a set_ and being fixed _pointwise_.

## Orbit decomposition of the conjugation action
Whenever a group <span>$G$</span> acts on a set <span>$X$</span>, we should think about the orbit decomposition of <span>$X$</span>. 

The very smallest orbits contain the most "special" elements of <span>$X$</span> - their stabiliers are largest, so they are the "most symmetrical". I like to think of these elements as lying in the "heart" of the set <span>$X$</span>; the two pictures I keep in mind are the centre of a rotation (say, under the usual action of <span>$S^1$</span> on the plane by rotations) or the axis of a reflection (say, under the action of <span>$\mathbb{Z}/2\mathbb{Z}$</span> by a reflection). The point (resp. the axis) are the only points with nontrivial stabiliser, and all the other points revolve around them.

The largest orbits contain the most "generic" elements of <span>$X$</span> - in most real-life situations, especially geometrical ones, only a finite/discrete set have non-trivial stabilisers[^example]. Actions by finite groups tend to have larger stabilisers but the intuition is good to bear in mind.

When <span>$G$</span> is a <span>$p$</span>-group[^definition], this decomposition is especially simple and powerful: the stabilisers are all powers of <span>$p$</span> and so we can image <span>$X$</span> as having a "filtration" by powers of <span>$p$</span> according to the size of the stabiliser.We can view the lower powers of <span>$p$</span> as being "leading terms" in a kind of power series expansion, and many arguments consist of comparing these leading terms[^adic]. 

In this vein, we now come to possibly the most important application of the orbit-stabiliser theorem to finite group theory.

*Lemma: The <span>$p$</span>-group fixed-point lemma*\
Let <span>$G$</span> be a finite <span>$p$</span>-group acting on a finite set <span>$X$</span>. Then
<div>$$|X| \equiv |\textrm{Fix}(X)| \text{ mod } p$$</div>

Proof:\
We have 
<div>$$X = \coprod_{\mathcal{O} \in \textrm{Orbit}(X)} \mathcal{O} = \textrm{Fix}(X) \coprod \left(\coprod_{\mathcal{O} \in \textrm{Orbit}(X)} \mathcal{O}\right)$$</div>
so
But by the orbit stabiliser theorem <span>$|\mathcal{O}|$</span> divides <span>$|G|$</span>, so when <span>$|\mathcal{O}|>1$</span>, we have <span>$p$</span> divides <span>$|\mathcal{O}|$</span>.

The same logic of splitting into trivial versus non-trivial orbits underlies a classic result called the "class equation".

*Proposition: The class equation*\
For a finite group <span>$G$</span> we have
<div>$$|G| =  \sum\limits_{\text{conjugacy classes}} [G:C_G(g)] = |Z(G)| + \sum\limits_{\text{non-trivial conjugacy classes}} [G:C_G(g)]$$</div>

Proof: use the orbit-stabiliser theorem and the orbit decomposition.

# Some consequences in finite group theory
Applying our fixed-point theorem for <span>$p$</span>-groups acting on themselves by conjugation immediately gives the following:

*Proposition: The centre of a <span>$p$</span>-group*\
<span>$p$</span>-groups have non-trivial centre.

Proof:\
By the <span>$p$</span>-group fixed-point lemma, <span>$p$</span> divides <span>$|Z(G)|$</span>. But <span>$e\in Z(G)$</span> so <span>$|Z(G)|\geq p$</span>.

Corollary: <span>$p$</span>-groups are nilpotent, and in particular are solvable.

*Proposition:*\
Suppose that <span>$G$</span> is a group and <span>$|G|=p^2$</span>. Then <span>$G\cong C_{p^2}$</span> or <span>$G\cong C_p \times C_p$</span>.

Proof:\
By the previous result, we have <span>$Z(G) \neq \{e\}$</span> so fix <span>$x\in Z(G)\setminus\{e\}$</span>. If <span>$G$</span> is cylic we're done, so suppose <span>$y \in G\setminus \langle x \rangle$</span>. Since <span>$G$</span> is not cyclic and <span>$x,y\neq e$</span> we have by Lagrange that <span>$\textrm{ord}(x)=\textrm{ord}(y)=p$</span>. Now <span>$\langle x \rangle \cap \langle y \rangle = 1 \text{ or } p$</span> and <span>$|\langle x,y \rangle| = p \text{ or } p^2$</span>. But <span>$y \not\in \langle x \rangle$</span> so <span>$\langle x \rangle \cap \langle y \rangle = 1$</span> and <span>$|\langle x,y \rangle| = p^2$</span>. Define
<div>$$\phi: C_p\times C_p \to G $$</div>
<div>$$(n,m) \mapsto x^ny^m $$</div>
Then <span>$\phi$</span> is:
 - A homomorphism since <span>$x,y$</span> commute 
 - Injective since <span>$\langle x \rangle \cap \langle y \rangle = 1$</span>
 - Surjective since <span>$|\langle x,y \rangle| = p^2$</span>

Note that the final part of this argument is entirely generic: whenever <span>$H,K$</span> are subgroups of <span>$G$</span> such that elements of <span>$H$</span> commute with elements of <span>$K$</span> and <span>$H\cap K = \{e\}$</span>, we have <span>$G\cong H\times K$</span> via an analogous map.



[^quotients]: Similarly to the left-multiplication action of <span>$G$</span> on the cosets <span>$G/H$</span>, one can have a conjugation action of <span>$G$</span> on <span>$G/H$</span> but it is only well-defined when <span>$H$</span> is a normal subgroup of <span>$G$</span> - thus, it is also an action of <span>$G$</span> on  the group <span>$G/H$</span> by group automorphisms. 

[^notation]: The notation here is awful: <span>$C(G)$</span> and <span>$C_G(g)$</span>? Really? What if I have a subgroup <span>$H \subseteq G$</span> and I want to compare the conjugacy class of <span>$h\in H$</span> with respect to <span>$H$</span> and <span>$G$</span>? I can't use <span>$C_H(g)$</span> and <span>$C_G(g)$</span>. There are probably alternative notations but I am lazy.

[^automorphisms]: This is ultimately a consequence of the action of <span>$G$</span> on itself being by _automorphisms_. More generally you can check that for any group <span>$G$</span> acting on a group <span>$H$</span> by automorphisms, <span>$\textrm{Fix}(g)$</span> is always a subset of <span>$H$</span>.

[^consequence]: This is just a consequence of the general fact that <span>$\textrm{Fix}(G) = \bigcap_{g\in G} \textrm{Fix}(g)$</span>.

[^example]: The two following examples are prime examples of this phenomenon. A slightly more advanced example is the action of <span>$\textrm{SL}_2(\mathbb{Z})$</span> on the upper half-plane by Mobius transformations - the analysis of the stabilisers of this action is an elementary part of the theory of modular forms.

[^definition]: That is, the order of <span>$G$</span> is a power of <span>$p$</span>.

[^adic]: This power series analogy is the concept underlying <span>$p$</span>-adic numbers.