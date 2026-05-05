---
layout: default
title: Metoclopramide
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 5
---

# Metoclopramide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

The txgnn-pipeline skill covers infrastructure concerns; the core task here is report generation per the system prompt format. I'll proceed directly with the Evidence Pack analysis.

---

# Metoclopramide: From Nausea & Gastroparesis to Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a well-established dopamine antagonist and prokinetic agent, widely used to manage nausea, vomiting, and delayed gastric emptying (gastroparesis).
The TxGNN model predicts it may have a beneficial adjunctive role in **Gastric Ulcer (disease)** by accelerating gastric emptying and reducing bile reflux — an independent pathological driver of gastric mucosal injury.
Supporting evidence currently includes **2 clinical trials** (of limited direct relevance to ulcer treatment) and **20 publications**, composed primarily of animal studies and narrative reviews.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antiemetic; gastroparesis management (no local authorization on record) |
| Predicted New Indication | Gastric Ulcer (disease) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Metoclopramide acts as a dopamine D2-receptor antagonist in both the central nervous system and the gastrointestinal tract. By blocking the inhibitory effect of dopamine on GI smooth muscle and augmenting acetylcholine release, it enhances gastric antral contraction, increases pyloric sphincter tone, and accelerates gastric emptying. This mechanism is well documented in the pharmacological literature (Albibi & McCallum, *Annals of Internal Medicine*, 1983 — PMID 6336644).

Gastric ulcers arise from an imbalance between mucosal-damaging factors (gastric acid, H. pylori infection, NSAID use, and bile reflux) and the stomach's protective mechanisms. Bile reflux is an independent pathological contributor: by shortening gastric acid-mucosal contact time and strengthening pyloric tone to prevent duodenogastric reflux, metoclopramide could theoretically reduce two of these damaging exposures. A clinical cohort study (Dippy et al., 1973 — PMID 4779253) provided direct observational evidence linking metoclopramide to reduced bile reflux in patients with gastric ulcer, lending biological plausibility to this prediction. Animal studies in rats and guinea pigs further confirmed a gastroprotective effect independent of acid secretion changes (PMID 2730234; PMID 6436177).

However, metoclopramide does not inhibit gastric acid secretion — a randomised double-blind study (Schneider et al., 1981 — PMID 6782467) showed no significant change in gastrin levels or acid output after administration — and it has no anti-*Helicobacter pylori* activity. Therefore, its role in gastric ulcer management, even if validated, would be strictly adjunctive to standard-of-care therapies (proton pump inhibitors, H. pylori eradication regimens). No dedicated clinical trial has evaluated metoclopramide as a gastric ulcer treatment, and caution is warranted given its known neurological adverse effect profile with prolonged use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Evaluated whether IV metoclopramide given before endoscopy improves gastric wall visibility and reduces the need for repeat procedures in upper GI bleeding (including gastric ulcer haemorrhage). Directly relevant to the gastric ulcer context, though the endpoint is endoscopic optimisation rather than ulcer healing. |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Pharmacist-led quality improvement programme in Scottish primary care using an informatics tool for medication review. Not a metoclopramide efficacy trial; relevance to gastric ulcer treatment is negligible. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | Clinical Cohort | Current Medical Research and Opinion | Observed that metoclopramide reduced bile reflux in patients with gastric ulcer — provides the most direct clinical evidence linking metoclopramide to a gastric ulcer-relevant endpoint. |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | RCT (double-blind) | MMW Münchener Medizinische Wochenschrift | Randomised crossover study in 12 healthy volunteers: neither domperidone nor metoclopramide significantly altered serum gastrin or acid secretion, confirming metoclopramide is not an acid suppressant. |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Annals of Internal Medicine | Comprehensive pharmacology review covering metoclopramide's dopamine antagonism, central antiemetic effect, and GI smooth muscle stimulation — the standard pharmacological reference for this drug. |
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT | Yonsei Medical Journal | Prospective double-blind RCT (n=40): IV metoclopramide + ranitidine reduced preoperative gastric volume and acidity vs. placebo, supporting its ability to modify intragastric conditions. |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Animal Study | Indian Journal of Physiology and Pharmacology | Metoclopramide protected against all three experimental gastric ulcer models in guinea pigs without affecting gastric acid secretion; protective effect attributed to improved gastric drainage and prevention of pyloric reflux. |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal Study | Archives Internationales de Pharmacodynamie et de Thérapie | Demonstrated anti-ulcer and antisecretory effects of metoclopramide (20–50 mg/kg) in aspirin-induced and pylorus-ligated gastric ulcer models in rats, with efficacy comparable to ranitidine at these doses. |
| [28652516](https://pubmed.ncbi.nlm.nih.gov/28652516/) | 2017 | Animal Study | Journal of Smooth Muscle Research | Investigated how ulcer position affected gastric emptying in rats and the impact of prokinetics; confirmed metoclopramide's role in improving gastric emptying impaired by ulceration. |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Review | Postgraduate Medicine | Reviewed strategies for refractory peptic lesions — mentions metoclopramide as an adjunctive option when gastric motility dysfunction contributes to treatment failure. |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Historical Review | Drugs | Early narrative review noting metoclopramide's potential role in hastening gastric ulcer healing by promoting gastric drainage, among other anti-ulcer agents of the era. |
| [11879596](https://pubmed.ncbi.nlm.nih.gov/11879596/) | 2002 | Review | Current Treatment Options in Gastroenterology | Discussed prokinetics including metoclopramide in functional dyspepsia, a condition pathophysiologically overlapping with motility-related gastric ulcer contributors. |

---

## Italy Market Information

Metoclopramide currently has **no recorded regulatory authorizations** in the available dataset (0 licenses, market status: not marketed). No authorization table is available for this drug.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data (key warnings, contraindications, drug-drug interactions) were not retrievable from the queried sources at the time of this report. This is a blocking data gap that must be resolved before any clinical feasibility assessment can proceed. Clinicians should be aware that metoclopramide carries a well-known class risk of **tardive dyskinesia** with long-term or high-dose use — a factor that substantially constrains its use in chronic gastric conditions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for metoclopramide in gastric ulcer consists entirely of animal models, historical reviews, and one clinical cohort observation on bile reflux — with no dedicated clinical trial demonstrating ulcer healing benefit in humans. Its mechanism (gastric motility enhancement, reduced bile reflux) is plausible and adjunctively relevant, but cannot substitute for acid suppression or H. pylori eradication, which are the established pillars of gastric ulcer therapy.

**To proceed, the following is needed:**

- **Package insert / safety data**: Retrieve TFDA (or EMA) prescribing information to complete key warnings and contraindications — currently a blocking gap for any safety assessment
- **Drug-drug interaction profile**: Assess compatibility with first-line anti-ulcer agents (PPIs, amoxicillin, clarithromycin) before any combination therapy is considered
- **Formal MOA documentation**: Obtain structured mechanism-of-action data from DrugBank to support mechanistic plausibility analysis
- **Dedicated clinical evidence**: Identify or commission a prospective observational study or pilot RCT evaluating metoclopramide as adjunctive therapy in H. pylori-eradicated or NSAID-related gastric ulcers with documented dysmotility
- **Tardive dyskinesia risk assessment**: Define a safe maximum treatment duration and monitoring protocol given the neurological risk with prolonged use — essential before any chronic adjunctive indication can be proposed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

