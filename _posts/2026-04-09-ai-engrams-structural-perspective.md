---
layout: post
title: "A Structural View of AI Engrams: Notes After a Conversation with Peter Dayan"
date: 2026-04-09
description: Floating thoughts on what kind of memory I am actually looking for when I search for engrams in AI models, sparked by a question I could not immediately answer.
tags: memory engram neuroscience
---

Yesterday I had a long discussion with Peter Dayan about AI engrams, and one of his questions stayed with me long after the conversation ended. I want to write down what I have been turning over in my head ever since. This is a set of floating thoughts more than a finished argument, but I have a feeling that writing it out is the only way I am going to figure out what I actually believe.

## The question that followed me home

Peter asked me a deceptively simple question.

In neuroscience, memory comes in different flavors. There is declarative memory, which splits into episodic memory and semantic memory. There is non-declarative memory, which includes procedural memory, priming, and several others. So which one, he wanted to know, is the engram I am looking for? Am I chasing something closer to the episodic engram that Tonegawa's lab has been working on, or something that lives inside a Complementary Learning Systems framework?

I did not have an immediate answer, and that bothered me. The question kept circling in my head for the rest of the day, and eventually I arrived at a kind of resolution. The reason I could not answer right away, I think, is that Peter was asking about the **functional** aspect of memory, while my interest has been quietly orbiting the **structural** aspect. Once I noticed the gap, the question stopped being a trap and became a starting point.

## Why I keep saying "structural"

Let me explain what I mean by structural versus functional, because this distinction is doing a lot of work in everything that follows.

In the brain, neurons can be functionally very different from one another. Dopaminergic neurons participate in the reward system. Cholinergic neurons regulate arousal. Noradrenergic neurons drive the fight-or-flight response. They live in different circuits, release different neurotransmitters, and play very different functional roles in cognition and behavior.

Underneath those functional differences, however, there is a structural definition that all of them share. What makes a cell a neuron, as opposed to any other cell type in the brain, is a set of structural principles. There is the basic excitability story: a dendrite, a soma, and an axon, equipped with the right ion channels and membrane capacitance, governed by the GHK equation, capable of firing regenerative action potentials. That structural definition holds whether you are looking at a dopamine neuron or a noradrenergic neuron or a sensory cortex pyramidal cell. The function differs. The structural identity is shared.

So here is the question Peter's question pushed me to ask out loud: **does memory have something analogous?** Is there a structural definition format for memory that exists prior to its functional taxonomy?

Maybe someone has already tried this. Maybe I am about to reinvent a wheel that already exists somewhere in the literature. But I want to do it anyway, because I think there is something important about trying to write down a structural account of memory in a way that would actually let me look for it inside an artificial neural network.

## Where I am coming from

For the last two years, my work has been an attempt to find memory traces, the engrams, inside artificial neural networks. I have learned an enormous amount in that time. I want to say a quick thank you here to Donkyum Kim and Jiwon Kim, with whom I have been working on the AI-Engram project. Our earlier writeup, [*In Search of the Engram in LLMs*](https://iclr-blogposts.github.io/2025/blog/engram/) (Kim et al., ICLR 2025 Blogpost Track), is the most concrete version of where this thinking started. The collaboration has been genuinely fun, and a lot of what I am about to write down has been shaped by our conversations.

What follows is me trying to write down, in plain language, the unshakable propositions about memory that I have been slowly converging on. I am betting that there is some shared principle living at the intersection of AI and neuroscience, and I want to find a way to express it that does not depend on which side of that intersection you happen to start from.

## You cannot talk about memory without talking about learning

The first thing I realized is that if I want a structural account of memory, I cannot avoid talking about learning. Memory and learning are not the same thing, but they are entangled in a way that makes it hard to define one without the other. Learning is necessary for intelligence to emerge. Without learning, you do not get intelligence. So before I try to pin down memory, I have to pin down learning.

What is learning? The answer depends on which field you ask. Machine learning, neuroscience, behavioral science, and psychology have all developed their own definitions. Barron et al. (2015) wrote a nice synthesis across these fields, and from their review, three definitions stand out:

1. **Learning as a change in behavior.**
2. **Learning as a change in behavioral mechanisms.**
3. **Learning as the processing of information or experience.**

{% include figure.liquid path="assets/img/blog/ai-engrams/01-three-definitions.png" class="img-fluid rounded z-depth-1" alt="The three definitions of learning from Barron et al. 2015" caption="The three definitions of learning that show up most often across machine learning, neuroscience, and behavioral science. From Barron et al. (2015)." zoomable=true %}

Let me walk through each one, because the progression matters.

The first definition is the most intuitive. If your test scores went up, you learned something. If your swimming improved, you learned something. Behavioral change is the most visible signature of learning, and historically it is where a lot of the early science started.

{% include figure.liquid path="assets/img/blog/ai-engrams/02-learning-as-behavior-change.png" class="img-fluid rounded z-depth-1" alt="Learning as a change in behavior diagram" caption="Definition 1: learning as a change in behavior. Only the output $Y$ is in view here. The system $f$ is not marked as changing, not because it stays the same, but because this perspective does not yet look inside. Behavioral change is the most visible signature of learning, but it is not a necessary one." zoomable=true %}

There is a problem with this definition, though. We can study and not see our test scores improve. We can practice and feel like nothing changed. Does that mean no learning happened? Probably not. Behavioral change is a sufficient indicator that learning occurred, but it is not necessary. Something can be deposited inside us without showing up in our behavior right away.

That is what motivated the second definition: learning as a change in behavioral mechanisms. The internal machinery shifted, even if the external output looks the same. I find a water analogy useful here. Think of a behavioral change as the moment water turns into ice or steam, a visible phase transition in the world. A change in behavioral mechanism is more like the gradual change in temperature that happens before that transition. The internal state is moving, but the visible phase has not flipped yet. In system terms, you could write it as $f_{t-1} \neq f_t$. The system at time $t-1$ is no longer the same system at time $t$, even if the outputs you can observe have not yet shifted.

{% include figure.liquid path="assets/img/blog/ai-engrams/03-learning-as-mechanism-change.png" class="img-fluid rounded z-depth-1" alt="Learning as a change in behavioral mechanisms diagram" caption="Definition 2: learning as a change in behavioral mechanisms. The system $f$ itself shifts from $f_{t-1}$ to $f_t$. This is the more fundamental view, because it allows for learning that has not yet shown up in the output." zoomable=true %}

The third definition takes things a step further. Learning as the processing of information or experience. When we move through the world, we accumulate experience, but not in the way a video camera accumulates frames. We do not store things with that kind of fidelity. Instead, we extract structure. We separate signal from noise. We compress. We build representations. Under this view, learning is the process by which those representations get formed and refined.

{% include figure.liquid path="assets/img/blog/ai-engrams/04-learning-as-information-processing.png" class="img-fluid rounded z-depth-1" alt="Learning as processing of information or experience diagram" caption="Definition 3: learning as the processing of information or experience. The system change is now driven by an explicit experience term $D$, which gets actively encoded into $f$." zoomable=true %}

If we squint, we can write all three definitions inside the same simple structure: $X \to f \to Y$. Learning, in the deepest sense, is a change in the system $f$ that sits between input $X$ and output $Y$. The first definition pays attention to changes in $Y$. The second pays attention to changes in $f$ that may or may not propagate to $Y$. The third pays attention to what $f$ is actually doing internally to produce $Y$ from $X$ in the first place. Memory, in my view, is what gets deposited into $f$ as a result of all this. It is the system change.

## A short detour into "essence"

I want to take a brief detour, because I keep using the word "essence" in my own head, and I should explain what I mean.

When I think about memory in the context of intelligence, I do not think the most intelligent memory system is the one that perfectly records its inputs. A perfect video recorder is, in a sense, a kind of memory. So is a database that returns exact rows. But I do not consider those particularly intelligent. If I had to choose between a system that perfectly stores 2D images of an object and a system that can take those 2D images and reconstruct, even imperfectly, the underlying 3D structure, I would call the second one more intelligent. The second system is doing something with the input. It is extracting the underlying structure. It is closer to the essence.

{% include figure.liquid path="assets/img/blog/ai-engrams/05-database-vs-neural-network.png" class="img-fluid rounded z-depth-1" alt="Information-Intelligence Paradox: database vs neural network" caption="The information-intelligence paradox. A database holds more information ($D = I$) but is not intelligent. A neural network holds less ($D \supset I$) but extracts something more useful: structure. Information and intelligence are not the same thing." zoomable=true %}

Maybe the best way to put it is this: there is something out there in the world that exists independently of the observer, and the question is what kind of vessel each brain uses to hold it.

Here is an analogy. Imagine an electronic device with a multilingual instruction manual. You hand the manual to a Korean reader, a Japanese reader, an American reader, and a French reader, and ask each of them to remember it later. Each person will remember the parts written in their own familiar language more vividly. Each one will retain the manual a little differently. But the manual itself is the same object. The essence of what the manual is describing has not changed. What changed is the vessel: the brain doing the encoding. The world exists, and each brain is its own simulation space, extracting and storing pieces of the world in its own way.

Anyway, the reason for the detour is this. Intelligence, as I am thinking about it, is the process by which a system takes in external experience and builds representations that capture the essence of the world as well as possible. And memory is the storage system that holds those representations in a form that can be retrieved later. Putting this complicated process under unshakable propositions feels important to me, and that is what I have been trying to do.

## Defining stimulus and experience

Let me try to lay down the foundations more carefully. I want to start by separating two concepts that often get blurred together: **stimulus** and **experience**.

The word "experience" already carries a sense of accumulation built into it. An experience leaves something behind. A stimulus, on the other hand, feels more like something that exists for an instant and then disappears. The same input $X$ can act as either a stimulus or an experience depending on what the system does with it.

In artificial neural networks, this distinction maps cleanly onto two phases. Inference is the stimulus phase: $X$ is fed into a frozen system $f$, the system produces an output, and nothing in $f$ changes. Training is the experience phase: $X$ is fed into the system, and as a result, $f$ itself is updated. Same $X$, different relationship to the system.

In the brain, the boundary is not as sharp, because there is no explicit frozen state. But you can still draw a similar line based on time horizon. Did the input pass through and dissipate, leaving the system roughly where it was? Or did it leave a trace that persists long enough to count as something the system has incorporated?

## Variable and invariant: $\mu$ and $\pi$

Now I want to talk about learning more precisely. If we accept the first definition, learning is $y_{t-1} \to y_t$, where the output before learning differs from the output after. But if we look more carefully, $y_{t-1}$ and $y_t$ can only differ if the system itself differs, that is, $f_{t-1} \neq f_t$. This is the second definition, and it is the more fundamental one. It is also worth noting that the second definition is strictly more permissive: $f_{t-1} \neq f_t$ does not require $y_{t-1} \neq y_t$. The system can change without the output changing.

The proposition I want to anchor everything on is this: **if learning happens, the system changes.**

What does that mean concretely? It means we have to be careful about how we define "the system." Any system has variable components and invariant components. If the system changed, then by definition, what changed is one of its variable components. That is almost too obvious to write down, but the consequences are not.

{% include figure.liquid path="assets/img/blog/ai-engrams/06-mutable-immutable.png" class="img-fluid rounded z-depth-1" alt="A system with mutable and immutable components" caption="Any system can be split into immutable components ($\pi$, e.g. architecture) and mutable components ($\mu$, e.g. parameters or synapses). When a system changes, by definition, only $\mu$ moves." zoomable=true %}

In artificial neural networks, the invariant components include the architecture and the activation functions. Things like the number of layers and the hidden dimension size. The variable components are the parameters, the weights and biases that get updated during training. (If you are doing neural architecture search, the architecture itself becomes variable, but I will set that aside for now.)

In the brain, this same distinction has been understood for over a century. Ramón y Cajal, sketching neurons by hand, already pointed out that the number of neurons and the broad structural pathways of the adult brain do not change very much. What changes is the strength of the connections. Synaptic weights are the variable components. The architecture, including the brain regions and the neuron counts, is relatively invariant. (In development, of course, even those are variable, but in the adult brain we can treat them as fixed.)

{% include figure.liquid path="assets/img/blog/ai-engrams/08-cajal.png" class="img-fluid rounded z-depth-1" alt="Cajal's sketches and his quote on fixed nerve paths" caption="Cajal's view, sketched and written more than a century ago: the nerve paths of the adult brain are fixed and immutable, but learning happens through changes in the strength of the connections. The structural insight is older than most of modern neuroscience." zoomable=true %}

To keep things simple, I will use the same notation for both AI and the brain. Let $\mu$ denote the variable components: the synapses in the brain, or the parameters in an artificial network. Let $\pi$ denote the invariant components: the architecture. The state of the system before learning is $\mu_{t-1}$, and the state after learning is $\mu_t$. In a network with $n$ parameters, both states live somewhere in an $n$-dimensional parameter space.

{% include figure.liquid path="assets/img/blog/ai-engrams/07-learning-changes-mu.png" class="img-fluid rounded z-depth-1" alt="Learning changes the mutable component of the system" caption="Learning is what happens when an experience $D$ pushes the mutable component from $\mu_{t-1}$ to $\mu_t$. The architecture $\pi$ stays put. The memory of the experience, if it lives anywhere, lives in the change." zoomable=true %}

## Is $\Delta \mu$ the engram?

Here is the move I want to make. If learning is defined as a change in $\mu$, and if memory is what learning leaves behind, then maybe the cleanest structural definition of memory is the change itself: $\Delta \mu = \mu_t - \mu_{t-1}$.

I want to be careful here. I am not claiming that $\Delta \mu$ is literally the memory in some metaphysical sense. What I am saying is that $\Delta \mu$ encodes the change produced by learning. If memory exists as a stored thing inside the system, then it has to live inside this delta. There is nowhere else for it to go.

This is not a wild claim, by the way. Two lines of work in machine learning have shown something very close to this. **Task arithmetic** ([Ilharco et al., 2023](https://arxiv.org/abs/2212.04089)) takes the difference between a finetuned model and its base, treats that delta as a "task vector," and shows that you can add or subtract these vectors to compose or remove skills in a roughly linear way. Adding the delta gives the model the skill. Subtracting it can take the skill away. **Skill localization** ([Panigrahi et al., 2023](https://arxiv.org/abs/2302.06600)) goes further: it shows that the relevant change often lives in a sparse subset of parameters, so you can graft a small piece of the finetuned weights back onto the base model and recover most of the new skill. This is exactly the kind of behavior you would expect if memory were structurally encoded as a directional shift in parameter space.

And on the neuroscience side, is there evidence that something similar happens in the brain? Yes, and the story goes back a long way.

The concept of the engram is more than a hundred years old. Richard Semon coined the term as a theoretical construct, describing the engram as the physical substrate of memory: an enduring change in the brain's structure that allows a specific memory to be stored, reactivated, and recalled.

{% include figure.liquid path="assets/img/blog/ai-engrams/09-semon-engram.png" class="img-fluid rounded z-depth-1" alt="Richard Semon and the original concept of the engram" caption="Richard Semon coined the word 'engram' more than a hundred years ago. He described it as the physical substrate of memory: an enduring imprint on neural networks, made by changes in neurons, synapses, and neural circuits, enabling the recall of a specific memory." zoomable=true %}

Karl Lashley then spent decades looking for it through lesion experiments. Lashley's work was the best science available at the time, but it was constrained by the technology. He could not selectively target the cells he needed to target, and so he ended up with a famous null result: he could not find the engram by removing pieces of cortex.

{% include figure.liquid path="assets/img/blog/ai-engrams/10-lashley.png" class="img-fluid rounded z-depth-1" alt="Karl Lashley and his search for the engram" caption="Karl Lashley spent decades hunting for the engram with lesion studies. He never found it, partly because his tools could not target the cells he needed to target. His famous null result is what later led researchers to conclude that memory must be distributed across the brain rather than stored in a single region." zoomable=true %}

What changed in the last two decades is the toolkit. Modern biotechnology, especially optogenetics, finally made selective targeting possible at the level of individual neurons and even individual synapses. With these tools, researchers have been able to control synaptic plasticity in specific connections and demonstrate that doing so can either trigger or block memory formation. [Hayashi-Takagi et al. (2015)](https://www.nature.com/articles/nature15257), published in Nature, used a photoactivatable Rac1 (AS-PaRac1) to selectively shrink the dendritic spines that had been potentiated during a motor learning task, and they showed that doing so erased the corresponding learned skill while leaving a different motor memory in the same area intact. A few years later, Bong-Kiun Kaang's group ([Choi et al., 2018](https://www.science.org/doi/abs/10.1126/science.aas9204), Science) developed a dual-eGRASP technique that lets you visualize the specific synapses connecting engram cells across brain regions, and showed that the size and number of those engram-to-engram synapses encode the strength of the memory.

The point I want to land on is this. From a structural perspective, an engram in the brain is best described as an ensemble of neurons and synapses, distributed across multiple brain regions, intertwined and overlapping. It is not pinned to any single functional category of memory. It is a substrate. And what I am asking, for AI, is the structural version of the same question: how should we think about engrams in this same substrate-level way, but inside an artificial neural network?

{% include figure.liquid path="assets/img/blog/ai-engrams/11-parameter-space-rule.png" class="img-fluid rounded z-depth-1" alt="Memory lives in the parameter space" caption="The rule I am converging on: memory lives in the parameter space. Each learned concept moves $\mu$ in some direction. Multiple concepts can entangle and overlap, and the operations of memory (formation, retrieval, modification, forgetting) become different ways of moving through this space." zoomable=true %}

## Memory CRUD: a bridge between two vocabularies

One last connection I want to make. There is a nice parallel between how computer science talks about memory and how neuroscience talks about memory. In CS we have CRUD: Create, Read, Update, Delete. In neuroscience we have a memory life cycle: formation, retrieval, consolidation, and forgetting. They line up almost perfectly.

- Memory formation is learning. It is **Create**.
- Memory retrieval is recall. It is **Read**.
- Memory consolidation is the slower restructuring that happens over time. It is **Update**, or **Edit**.
- Memory forgetting, or unlearning, is **Delete**.

{% include figure.liquid path="assets/img/blog/ai-engrams/12-memory-crud.png" class="img-fluid rounded z-depth-1" alt="The four memory operations: formation, retrieval, modification, forgetting" caption="The four operations of memory map almost one-to-one onto CRUD: formation = Create, retrieval = Read, modification = Update, forgetting = Delete. The substrate is the same. Only the operation differs. (Figure from Kim et al., ICLR 2025 Blogpost.)" zoomable=true %}

You can draw a state transition diagram from this if you want. Each phase corresponds to a different operation on $\mu$. Formation pushes $\mu_{t-1}$ to $\mu_t$. Retrieval reads from $\mu$ without modifying it. Consolidation reshapes $\mu$ on a longer time scale, sometimes after the original learning event has ended. Forgetting is the operation that removes structure from $\mu$, either passively or deliberately.

What I find compelling about this framing is that it works regardless of which functional category of memory you are talking about. Declarative or non-declarative, episodic or semantic or procedural, the structural picture is the same. Memory is a product of learning. Learning is a change in the variable components of a system. And the question I am asking, the question that I think connects AI and neuroscience at the deepest level, is this: **how do we characterize the product of learning, structurally, in any system that learns?**

## Where this leaves me

I am still very much in the middle of working this out. The notes above are floating thoughts, not a finished theory. But Peter's question gave me something I did not have before: a clearer sense of what kind of question I am actually asking. Not which functional flavor of memory I am chasing, but what shape memory has in the substrate where it lives. The answer to Peter's original question, if I had been quick enough in the moment, would have been something like this. I am not chasing a particular function of memory. I am chasing a structural definition of what makes any memory a memory at all. And I think that question has to be answered before we can ask the functional ones in a principled way.

That is where I am, anyway. More to come as I keep thinking.
