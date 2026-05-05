---
layout: default
title: Fremanezumab
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 2
---

# Fremanezumab
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

The txgnn-pipeline skill confirms this is a TxGNN report generation task. Now I'll produce the full evaluation report based on the Evidence Pack.

---

# Fremanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Fremanezumab is a humanized anti-CGRP monoclonal antibody approved in the US and EU as a preventive treatment for episodic and chronic migraine, though it is not currently registered in Italy.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** — a distinct and difficult-to-treat migraine subtype involving brainstem involvement — with a prediction confidence of **99.94%**.
Currently **no dedicated clinical trials** have been registered for this specific subtype, but **20 publications** spanning mechanistic, real-world, and case-series data provide supporting biological plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine prevention (episodic and chronic) — not registered in Italy |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 — observational studies and case series |
| Italy Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from our regulatory sources. Based on known published information, fremanezumab is a fully humanized IgG2Δa monoclonal antibody that selectively targets **calcitonin gene-related peptide (CGRP)** — a potent vasodilator and neuromodulator densely expressed throughout the trigeminovascular system. By binding CGRP directly (rather than its receptor), fremanezumab blocks peripheral sensitization of trigeminal afferents and reduces the neuroinflammatory cascade that drives migraine headache. Preclinical work (PMID 28642283) has confirmed that fremanezumab selectively suppresses both C-fiber and Aδ-fiber trigeminovascular neurons, the primary pain relay in migraine.

**Migraine with brainstem aura** (formerly "basilar-type migraine") is a subtype in which aura symptoms arise from brainstem dysfunction — including dysarthria, vertigo, diplopia, and ataxia. CGRP is abundantly expressed in brainstem nuclei and perivascular nerve terminals adjacent to the basilar artery, making it a theoretically sound pharmacological target. The link between cortical spreading depression (CSD) — the electrophysiological correlate of migraine aura — and CGRP has been investigated directly using fremanezumab: while fremanezumab did not block CSD-induced arterial dilation or plasma protein extravasation in one model (PMID 31127003), a second study showed it did slow CSD propagation velocity and shorten cortical recovery time (PMID 31895266). These findings suggest partial, rather than complete, modulation of the aura-generating process.

Clinically, the evidence base extends from general migraine with aura to related brainstem and hemiplegic subtypes. A post-hoc analysis of the Phase 3b FOCUS trial (PMID 35302681) confirmed fremanezumab efficacy in patients with aura or neurological dysfunction, and a case series with literature review (PMID 35268319) reported promising aura-frequency reductions with anti-CGRP monoclonal antibodies including fremanezumab. Real-world data from patients with hemiplegic migraine — the most pharmacologically challenging aura variant — also show meaningful response (PMID 41618146). Collectively, these data support biological plausibility, though no trial has prospectively enrolled patients specifically diagnosed with migraine with brainstem aura.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for fremanezumab in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Post-hoc RCT Analysis | *European Journal of Neurology* | Post-hoc analysis of Phase 3b FOCUS study: fremanezumab demonstrated significant efficacy in patients with aura or associated neurological dysfunction who had inadequate response to 2–4 prior preventive treatments |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Series + Literature Review | *Journal of Clinical Medicine* | Anti-CGRP mAbs (including fremanezumab, eptinezumab, galcanezumab) may reduce aura frequency; case reports show partial to complete aura suppression; mechanism via CGRP-mediated cortical sensitization proposed |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Observational Case Series | *CNS Neuroscience & Therapeutics* | Anti-CGRP therapy reduced both headache days and aura frequency in observational patients; suggests CGRP pathway modulates aura generation beyond headache phase alone |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Individual Patient Quantitative Analysis | *The Journal of Headache and Pain* | Anti-CGRP mAbs showed effectiveness in hemiplegic migraine (severe aura subtype with motor weakness); supports generalizability to brainstem aura variants |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Case Report + Literature Review | *Frontiers in Neurology* | Case of chronic hemiplegic migraine responding to anti-CGRP mAb; discusses implications for rare aura subtypes excluded from pivotal RCTs |
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Preclinical / Mechanistic | *Journal of Neuroscience* | Fremanezumab did **not** block CSD-induced arterial dilation or plasma protein extravasation; raises questions about direct CGRP-CSD coupling; important negative mechanistic signal |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Preclinical / Mechanistic | *Pain* | Fremanezumab slowed CSD propagation rate and shortened cortical recovery period in BBB-compromised rats, but did not prevent CSD occurrence; partial modulation of aura physiology demonstrated |
| [37638190](https://pubmed.ncbi.nlm.nih.gov/37638190/) | 2023 | Real-World Observational | *Frontiers in Neurology* | 3-month single-center prospective study: fremanezumab showed meaningful reduction in monthly migraine days in chronic migraine real-world patients; confirms post-marketing tolerability and efficacy |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | *Handbook of Experimental Pharmacology* | Comprehensive review of CGRP's role in migraine including aura subgroups; establishes CGRP as a central mediator in trigeminal pain and vasodilation relevant across migraine subtypes |
| [28642283](https://pubmed.ncbi.nlm.nih.gov/28642283/) | 2017 | Preclinical / Mechanistic | *Journal of Neuroscience* | Fremanezumab selectively inhibited both C-fiber and Aδ-fiber trigeminovascular neurons in a dose-dependent manner; foundational mechanistic study demonstrating peripheral anti-nociceptive action |

---

## Italy Market Information

Fremanezumab currently holds no authorizations registered in Italy. No license table can be generated.

> **Note:** Fremanezumab (brand name Ajovy®) has received regulatory approval in the United States (FDA, 2018) and the European Union (EMA, 2019) for preventive treatment of migraine in adults. Italy-specific AIFA registration data was not found in the current data pull.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction data, contraindications, or key warnings were retrievable from the current data sources for fremanezumab.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score of 99.94% is strongly supported by a coherent mechanistic rationale — CGRP is expressed in brainstem trigeminovascular terminals directly implicated in brainstem aura pathophysiology — and by an emerging body of real-world and case-series evidence showing anti-CGRP antibodies benefit patients with aura-associated migraine subtypes. However, no dedicated prospective trial exists for migraine with brainstem aura specifically, and preclinical data show only partial (not complete) modulation of the aura-generating CSD process by fremanezumab.

**To proceed, the following is needed:**

- **Italy/AIFA registration data**: Confirm whether fremanezumab (Ajovy®) has an active AIFA authorization; current query returned 0 records but the EU-wide EMA approval may warrant manual AIFA registry verification
- **Full mechanism of action (MOA) data**: DrugBank API query flagged as a data gap (DG002); retrieving the complete pharmacodynamic profile will strengthen the mechanistic section
- **Package insert warnings and contraindications**: TFDA/AIFA label text was not retrieved (DG001); critical for safety assessment before any clinical recommendation
- **Prospective registry or chart review**: A targeted chart review of migraine with brainstem aura patients treated with anti-CGRP mAbs (any class) would upgrade evidence from L3 toward L2 and reduce residual uncertainty
- **Expert neurology consultation**: Given that migraine with brainstem aura patients are systematically excluded from pivotal RCTs (as noted for hemiplegic migraine), clinical neurologist review of the indirect evidence is advisable before formal indication expansion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

