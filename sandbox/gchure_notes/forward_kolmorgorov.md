# Deriving The Forward-Kolmogorov Equation

In this document, we derive the Forward-Kolmogorov equation in a number of ways. 


## A Master Equation Approach (Spread the Butter)

### One-Dimensional Diffusion of a Particle
To begin, we can step out of the realm of population genetics and think of diffusion (though they are connected). In Einstein's treatise on Brownian motion of molecules, he posted the problem of diffusion by enumerating the probability of a particle being at position $x$ at a time $t$ given knowledge of the position probabilities of the molecules one short time interval prior $\delta t$. In this work, he posted the problem by writing a master equation over continuous space as 
$$
P(x, t + \delta t) = \int P(x - \delta x\vert t)\phi(\delta x, \delta t\,\vert\, t) d\delta x,
$${eq:continuum_master_eq}

where $P(x -\delta x\,\vert\, t)$ is the probability of the molecule being at position $x - \delta x$ at time $t$ and $\phi(\delta x, \delta t\, \vert t)$ is the conditional probability of the particle taking a jump of size $\delta x$ in a time interval $\delta t$.  To get a sense of the behavior of the function around our position $x$, we can do a Taylor expansion around $x$  up to the second order to obtain
$$
P(x, t + \delta t) = \int \delta x \left[ P(x) - {\partial P\over \partial x} \delta x- {1 \over 2}{\partial P^2 \over \partial^2} (\delta x)^2\right].
$${eq:taylor_exp}

We can do some tidying up by evaluating each integral in isolation. As we know that probability should add up to one, we can say that
$$
P(x)\int \delta x \phi(\delta x) = P(x).
$${eq:conserv_prob}

In the case of diffusion, we are ignoring any directional field (i.e. selection in our population genetic picture), meaning that the mean displacement of the particle should be zero. This arises because a jump to either the left or the right is equally likely. This allows us to make another simplification that
$$
{\partial P \over \partial x} \int d\delta x \phi(\delta x)\delta = 0.
$${eq:no_selec}

Finally, as $\delta x$ is not present in $P(x)$, we can say that the second order term evaluates to
$$
{1 \over 2}{\partial^2 P \over \partial x^2} \int d\delta x \phi(\delta x) (\delta x)^2 = \langle (\delta x)^2 \rangle).
$${eq:second order}

Substituting all of these evaluations into our expanded continuum master equation we arrive at 
$$
P(x, t + \delta t) = P(x, t) + {(\delta x)^2 \over 2} {\partial^2 P \over \partial x^2}.
$$
Following a little rearrangement and division by $\delta t$, we get
$$
{P(x, t + \delta t) - P(x, t) \over \delta t} = {\langle (\delta x)^2 \rangle \over 2 \delta t} {\partial^2 P \over \partial x^2}.
$$

When $\delta t \rightarrow 0$, we recover the one-dimensional diffusion relation,
$$ 
{\partial P \over \partial t} = {\langle (\delta x)^2 \rangle \over 2 \delta t}{\partial^2 P \over \partial x^2}.
$$

### The Population Genetics Picture
Rather than imagining the diffusion of particles, we can think of the
diffusion of alleles. We are a bit trapped in our mindset of distinct
organisms (choose your favorite ploidy) but as Wright wrightly-noted (heh),
we can abstract away from individuals and think of a community as a
collection of *allele frequencies*. We can approach this with a toy model where we imagine a single locus with only two alleles -- $A$ and $a$. The frequency of allele $A$ can be simply defined as 
$$
f_A =  {N_A \over N_A + N_a}. 
$$

As the frequency must add up to one, we can define the frequency of allele $a$ in terms of the frequency of allele $A$ as 
$$
f_a = 1 - f_A = {N_a \over N_A + N_a}
$$

To under the time-evolution of this probability density function, we can examine the Fokker-Planck equation. For this particular case of alleles, the Fokker-Planck equation is defined as 
$$
P(f, t + \delta t) = \int P(f - \delta f) \phi(f - \delta f, \delta f) d \delta f.
$$

This is a bit different than in our one-dimensional diffusion equation above. The joint probability of taking a jump $\delta f$ in a time interval $\delta t$ is now *dependent* on where you are in the frequency space! This is akin to saying (in our 1D diffusion language) that the probability taking a jump to the left or the right is dependent on *where* you are along the dimension.