---
layout: default
title: Catridecacog
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 3
---

# Catridecacog
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

---

# Catridecacog: From Congenital Factor XIII Deficiency to Primary Release Disorder of Platelets

## One-Sentence Summary

Catridecacog (rFXIII-A₂) is a recombinant coagulation Factor XIII A-subunit, approved in other markets for prophylaxis of bleeding in patients with congenital Factor XIII A-subunit deficiency.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets** (score 99.29%), with **no clinical trials** and **no publications** currently supporting this direction.
Notably, among the three predicted indications in this pack, **Glanzmann thrombasthenia** carries the strongest mechanistic rationale and may warrant prioritisation as a research hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Congenital Factor XIII A-subunit deficiency (bleeding prophylaxis) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Catridecacog is a recombinant form of the Factor XIII A-subunit (rFXIII-A₂), a plasma transglutaminase whose principal role is to crosslink fibrin strands and incorporate α₂-antiplasmin into the nascent clot. These actions render the clot mechanically resistant to deformation and protected against fibrinolysis. In its approved indication — congenital FXIII A-subunit deficiency — the absence of functional FXIII leads to clots that dissolve prematurely, causing delayed and recurrent bleeding.

The biological bridge to primary platelet release disorder lies in the dual location of FXIII-A₂: it circulates in plasma but is also stored in platelet α-granules, from which it is released upon platelet activation to reinforce local fibrin crosslinking at the site of injury. In primary platelet release disorders (e.g., δ-storage pool deficiency, gray platelet syndrome), the release of granule contents — including platelet-derived FXIII — is impaired. Supplying exogenous rFXIII-A₂ could theoretically compensate for this local fibrin-stabilisation deficit.

However, the mechanistic case is weak for the rank-1 prediction. The core pathophysiology of platelet release disorders is deficient secondary activation signalling (ADP, serotonin, TXA₂), not insufficient fibrin crosslinking. **Glanzmann thrombasthenia** (the rank-3 prediction) presents a more compelling pharmacological rationale: GPIIb/IIIa loss abolishes platelet aggregation entirely, making haemostasis wholly dependent on fibrin matrix strength — exactly where rFXIII-A₂ exerts its effect. The known synergy between rFVIIa and FXIII-mediated fibrin stabilisation in GT patients further supports this as the most mechanistically grounded hypothesis of the three.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

No marketing authorizations on record. Catridecacog is not approved or commercially available in Italy.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications rest on model prediction alone (Evidence Level L5), with zero registered clinical trials and zero supporting publications. The mechanistic link between rFXIII-A₂ and primary platelet release disorder is biologically conceivable but highly indirect, and the drug is not available in the Italian market.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve full mechanism of action from DrugBank API and the package insert to enable formal mechanistic plausibility scoring
- **Safety baseline**: Extract warnings, contraindications, and drug interactions from the package insert PDF to complete the S1 safety screening
- **Regulatory mapping**: Confirm European Medicines Agency (EMA) authorisation status (Tretten / NovoThirteen) and available routes of administration
- **Indication reprioritisation**: Consider pivoting the primary hypothesis to **Glanzmann thrombasthenia** — which has the strongest pharmacological rationale among the three predicted indications — before committing to further evidence searches
- **Preclinical / case literature sweep**: Conduct a broader PubMed search using FXIII + platelet disorder / Glanzmann thrombasthenia to identify any indirect evidence not captured by the current drug-specific query
- **Expert consultation**: Engage a haematologist specialising in rare bleeding disorders to validate whether the fibrin-stabilisation hypothesis is considered clinically plausible in any of these conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

