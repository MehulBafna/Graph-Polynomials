# Graph-Polynomials

##**Independence polynomial** 

To delve into the concept of independence polynomial, it is required to go through the notion of independent sets.  

For a given graph G = (V,E), a vertex subset V′⊆ V is termed as an independent set if the graph induced by V′ i.e., G[V′] is an empty graph. 
The independent set with the maximum cardinality is defined as the maximum independent set and the cardinality of such maximum independent set is described as independence number denoted by α(G).

For a given graph G = (V,E), independence polynomial in terms of independent sets and independence number is defined as I(G,x) = ∑ m<sub>j</sub>(G)x<sup>j</sup> from j = 0 to α(G), and the coefficients m<sub>j</sub>(G) gives the total number of independent sets with cardinality j, ∀ j ∈{0,···,α(G)}

##**Domination polynomial** 

Below are the required notations for domination polynomial. 

Open neighborhood (N(v)) :∀ v ∈ V, N(v) = {u ∈ V| {u,v} ∈ E}
Closed neighborhood (N[v]) : N(v)∪{v}

A vertex subset V′⊆ V is termed as a dominating set if N[V′] =V. The dominating set with the minimum cardinality is defined as the minimum dominating set, and cardinality of such minimum dominating set is described as domination number that is denoted by γ(G).

For a given graph G= (V,E), domination polynomial in terms of dominating sets and domination number is defined as D(G,x) = ∑d<sub>j</sub>(G)x<sup>j</sup> from j = γ(G) to |V|, and the coefficients d<sub>j</sub>(G) gives the total number of dominating sets with cardinality j, ∀ j ∈{γ(G),···,|V|}.

