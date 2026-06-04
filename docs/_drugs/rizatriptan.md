---
layout: default
title: Rizatriptan
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 2
---

# Rizatriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# RIZATRIPTAN: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Rizatriptan is a second-generation triptan (5-HT₁B/1D receptor agonist) established as a standard acute migraine treatment, but historically avoided in migraine subtypes involving brainstem symptoms due to theoretical vascular concerns.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (formerly known as basilar-type migraine),
with **0 registered clinical trials** and **19 publications** currently available to evaluate this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute migraine (with or without aura) — based on published literature; drug not registered in Italy |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, structured MOA data is not available from the regulatory dataset. Based on published literature within this evidence pack, rizatriptan is an oral serotonin 5-HT₁B/1D receptor agonist of the triptan class. It acts on receptors located on intracranial blood vessels and trigeminal nerve terminals, simultaneously inducing cranial vasoconstriction and inhibiting the release of pro-inflammatory neuropeptides — most notably CGRP (calcitonin gene-related peptide) and substance P. This combined vascular-neurogenic mechanism is the basis of its efficacy in standard acute migraine.

Migraine with brainstem aura (formerly "basilar-type migraine") shares the same core trigeminovascular pathophysiology as standard migraine. Critically, the brainstem aura symptoms — vertigo, diplopia, ataxia, dysarthria — are now understood to arise from cortical spreading depression extending into the brainstem, not from basilar artery vasospasm as previously theorised. This mechanistic reinterpretation directly undermines the traditional contraindication against triptan use in this subtype. Rizatriptan's 5-HT₁B/1D targeting of trigeminal neuroinflammation is thus directly relevant to the pathophysiology of migraine with brainstem aura.

Real-world clinical data supports this position. A 2001 retrospective analysis (PMID 11903526) specifically examined the use of triptans — including rizatriptan — in basilar migraine and migraine with prolonged aura, providing early but directly relevant evidence. International headache societies have progressively re-evaluated the blanket contraindication, with some current guidelines permitting cautious triptan use in this population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rizatriptan in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Retrospective Case Series | Headache | Directly reports on triptan use (including rizatriptan) in basilar migraine and migraine with prolonged aura — most disease-specific evidence available |
| [11687054](https://pubmed.ncbi.nlm.nih.gov/11687054/) | 2001 | Systematic Review | Cochrane Database Syst Rev | Comprehensive evidence-based assessment of rizatriptan across multiple RCTs for acute migraine; evaluates benefit–harm balance |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence Assessment / Guideline | Headache | American Headache Society updated review of evidence for all acute migraine pharmacotherapies, including the triptan class |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Meta-analysis | J Headache Pain | Compares frovatriptan vs rizatriptan in migraine with aura; evaluates whether triptans are efficacious during the headache phase in aura-type migraine |
| [15209688](https://pubmed.ncbi.nlm.nih.gov/15209688/) | 2004 | RCT (Phase 3) | Headache | Placebo-controlled study evaluating early rizatriptan administration during a migraine attack; supports rapid treatment approach relevant to aura variants |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | Frontiers in Neurology | Summarises treatment options for vestibular migraine, which overlaps clinically with brainstem aura; discusses triptan use in this population |
| [32952420](https://pubmed.ncbi.nlm.nih.gov/32952420/) | 2020 | Observational Study | Noro Psikiyatri Arsivi | Investigates cerebral hemodynamic changes during migraine attacks and following rizatriptan treatment; provides mechanistic hemodynamic data |
| [22211870](https://pubmed.ncbi.nlm.nih.gov/22211870/) | 2012 | Review | Headache | Reviews acute migraine rescue therapy with triptans and DHE across emergency and urgent care settings |
| [16336021](https://pubmed.ncbi.nlm.nih.gov/16336021/) | 2005 | Pharmacoeconomic Review | PharmacoEconomics | Confirms rizatriptan 5-HT₁B/1D agonist pharmacology; documents faster pain relief than several comparators with similar tolerability |
| [15613223](https://pubmed.ncbi.nlm.nih.gov/15613223/) | 1999 | PK Study | Headache | Pharmacokinetics of rizatriptan during vs between migraine attacks; demonstrates preserved absorption despite gastric stasis — relevant to acute aura management |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score is exceptionally high (99.94%) and the mechanistic basis — 5-HT₁B/1D receptor agonism suppressing trigeminovascular neuroinflammation — is directly applicable to migraine with brainstem aura given updated understanding that brainstem aura symptoms arise from spreading depression, not vasospasm. However, dedicated clinical trial data for this specific subtype is entirely absent, and the historical safety contraindication warrants structured clinical monitoring before broad use.

**To proceed, the following is needed:**

- **Prospective clinical trial data** specifically evaluating rizatriptan in migraine with brainstem aura (no registered trials currently exist)
- **Formal MOA documentation** from DrugBank to complete the pharmacological rationale dossier
- **Italy regulatory review** — retrieve the manufacturer's package insert to extract approved warnings, contraindications, and any existing guidance on brainstem aura
- **Expert neurology consultation** to formally reconcile the historical triptan contraindication in brainstem aura with current IHS diagnostic and treatment guideline revisions
- **Safety monitoring protocol** defining which brainstem aura presentations (e.g., concurrent motor weakness, severe ataxia) should remain excluded even if cautious use is adopted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

