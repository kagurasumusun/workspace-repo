# Divergent Search and Pre-Commit Exploration

## Why this exists

Recent deep-research results show a failure mode that linear recovery does not fully solve: an agent commits to a plausible direction before enough alternative evidence has been collected, then later search reinforces that initial mistake.

Hypothesis-guided search addresses this with bounded, independent branches before commitment. A hypothesis is a search direction, not a claim to believe.

## Operational rule

At each meaningful search state, classify it as:

- `direct`: one next search/action is strongly constrained by current evidence;
- `divergent`: multiple materially different hypotheses/candidates/evidence perspectives remain plausible.

For `direct`, continue the normal single route.

For `divergent`:

1. generate a small set of concrete hypotheses/candidates;
2. preserve the original task contract as a hard constraint;
3. run bounded branches independently;
4. require each branch to return supporting evidence, contradictions, unresolved points, and a branch status;
5. compare evidence across branches before committing;
6. either commit with preserved reasons, or generate refined hypotheses and run another bounded round.

Do not let a branch's interim confidence suppress the other branches.

## Candidate grounding

Prefer concrete, testable targets over vague keyword expansion. A useful branch should name a candidate entity, implementation path, source family, compatibility hypothesis, artifact class, or other falsifiable direction.

## Direction switching

A branch should switch direction when its current path becomes weak, contradictory, or incomplete. Switching should preserve the old path as evidence and record the trigger.

Do not equate "changed direction" with "failed". It can be an explicit recovery action.

## Search-state fields

Extend the compact search state with:

`mode | hypotheses | active_branches | branch_budgets | comparison_status | commitment_reason`

## Budgeting

Use bounded branch budgets. The goal is not maximal branching; it is preventing premature lock-in while maintaining information gain per unit cost.

## Research basis

- Zhou et al., *Explore Before Committing: Hypothesis-Guided Search for Deep Research Agents*, arXiv:2609.01294, 2026-09-01.
- The paper reports that early exploration errors can dominate failures on some deep-research benchmarks and that concrete candidate grounding plus controlled direction switching are useful behaviors. It proposes bounded hypothesis branches with comparative evidence aggregation.

Source: https://arxiv.org/abs/2609.01294
