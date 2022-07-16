# Lexicographers Without Borders - Quickstart
- **Created**: 2022-07-15T05:31:00Z

Note: this document is a quick draft of a top level overview. It migth take time to have a minimal usable description.

## Simplified explanation of operational stages 0, 1 and 2 for LSF

Visible to the external world, the deliverables and workflow of LSF can have two operational stages to allow continuous bootstrapping of new dictionaries while allowing different focused audiences.
Stage 0 is a special case, mostly for primitive self-checks.

Stage 1 tries to be a baseline to enable several stage 2 releases with localization beyond mere language.
However, as of 2022-07-15, LSF is creating stage 1 and even if this evolves to have endorsed stage 2, it could take years.

### From dictionary user perspective


#### Stage 0

LSF stage 0 can be explained as automated strategies to ensure correctness of releases from stage 1 and potentially simplistic checks for stage 2. 
At minimum, it can be as simple generic file format validations.
However, as the dictionaries themselves are able do document other dictionaries,
next automations of stage 0 can be based on previous releases.


#### Stage 1

As the goal of stage 1 operation mode is preparation for stage 2.

> TODO improve this part.

#### Stage 2

Stage 2 targets the actual end users of dictionaries not only in the natural language they prefer, but in a meaningful way they are useful under the jurisdiction (the "country/territory you live") or as existing areas of knowledge exchange (such as data about diseases between different regions) they would be used.

While the traditional dictionaries may be multilingual, not only we're already working with 100's of languages, but the way LSF dictionaries can be encoded allow for something called **semantic reasoning**. As the way Stage 1 allows for advanced localization and the dictionaries often would document concepts used for sensitive, personal data, the humans doing LSF work for Stage 2 would feel the need to fulfill needs that wouldn't have consensus at international level. 

Please note that LSF work targeting "international use" or "neutral" would be considered stage 2: even publications without an overly bureaucratic process done by IGOs tend to explicitly make disclaimer that they do not necessarily reflect the view of the nations which endorse the IGO.


<!--
Stage 0 must be fast, and designed to try fail in ways that allow previous version in use, yet it must allow for valid reasons for inconsistencies.
The main limitation of Stage 0 is that it cannot require human-in-the-loop unless under exceptional circumstances where a global schema change is necessary.

Stage 0 can be based on previous versions of LSF released work.
However, it cannot require _human-in-the-loop_:
not only this would delay releases,
but humans cannot have the dexterity to deal with the level of details OR the error revision would require wait feedback from other humans which may not be available.
-->


### Analogy to computer science bootstrapping

#### Stage 0
> @TODO give quick comment

#### Stage 1

- **Function (ontological sense: reason to exist)**:
  - Minimal functionality for Stage 2
  - Provide interlingual, language-neutral, taxonomy using controlled identifiers regardless of controlled vocabularies by external authority control.
- **Capabilities (ontological sense: may able to do, but optional)**:
  - Use external controlled vocabularies to document own taxonomy.
  - Provide linguitic terminology to document own taxonomy.

#### Stage 2
> @TODO draft this part

### Analogy to ethical points of view

#### Stage 0

Stage 0 would include most primitive _commom sense_ which regardless of moral points of view could lead to bad consequences. However, even if could be possible make rule-based inferences with implementations such as OWL, and also recommend humans to not abuse fallacious arguments, from a lexicographical point of view, we would label stage 0 strategies to mitigate very basic errors likely in automated ways or at least warn humans of something which may conflict with stage 1 or stage 2.

Humans should always have final say, even if it means allowing them to disable rules. However, humans can make typographic errors and the output of other programs can lead to inconsistent results if used on large systems. That's where stage 0 becomes relevant: attempt to validate basic reasoning, maybe even require that certain changes with higher impact would need to have digital signature.

A common point of stage 0 would be strategies to know if a content is stale and have ways to know the precedence of the information. Stage 2 and very likely derived works which could be endorsed by reference organizations Ina area or even in standard ways on how a governments have an official position in a subject are likely to not have entire metadata of how these decisions are made, but the ideal role of LSF would means we make easier to have copies of entire chain of decision (at least in case is based on public sources) which they could store privately.

Please note that the difference between what humans could consider stage 0 unlikely to have disagreements and what can realistically be done as part of automation workflows is huge. This can evolve over time.

#### Stage 1

SF stage 1 lexicography applies what in Western culture would be called **deontological ethics**. Good/bad are evaluated by the action itself, not by the consequences. It's a rigid thinking, often simplistic to a point of even when there's disagreement which could make stage 1 not direct reusable o stage 2, at least is predictable and, very important feature, **different world regions can have experts which can mimic this thinking** while they can still have personal biases or be aware of they jurisdiction.

In terminology, the direct impact would make it viable to be reusable for bootstrapping multiple stages 2 without becoming so generic and vague that it becomes useless. Already at stage 1, is viable the bootstrapping of rudimentar ontological rules such as "what is a territory", "what is a government'', and "what is an organization" and also provide suggested interlingual codes individuals in a way that at minimum allow disambiguation. Final works based on stage 2 can (and often will) use similar labels for different concepts, or group different concepts under obviously overly generic terminology, but stage 1 needs to be very critical to consistency. It should be done in such a way that even though implementations of stage 2 can't use some parts of it, it's easier and predictable to replace them.

This deontological approach makes things predictable, especially under stress. Another strong point (which is less moralistic) is to avoid exceptionalism: rules so specific which would apply to near one individual can't be encoded as stage 1.

#### Stage 2

LSF stage 2 lexicography not only can adhere to the opinion of the region of the target audience, but is free to apply other moral philosophies than the rigid deontological ethics. For example utilitarianism or consequentialism can forbid deontological justifications under certain circumstances far more common in the real world, such as what to do when resources are scarce.

Since data encoding in formats such as OWL allow for semantic reasoning, stage 2 can add further rules to public releases of stage 1 which might re-evaluate facts.

A common use case might evaluate a fact based on the opinion of an organization or opinion of another country (such as if an organization is embargoed, or if a country is considered independent). Under ideal circumstances, the entire chain of command of decision would be encoded (so a semantic reasoner could re-evaluate), but overly detailed reasoning (especially if most users don't want details) is computing intensive.