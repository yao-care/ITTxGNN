---
layout: default
title: Gliquidone
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 2
---

# Gliquidone
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

The txgnn-pipeline skill is noted — this task is report generation from an Evidence Pack, which is squarely within the TxGNN pipeline scope. Proceeding to generate the report now.

---

# Gliquidone: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Gliquidone is a second-generation sulfonylurea antidiabetic agent that stimulates insulin secretion by blocking ATP-sensitive potassium (K-ATP) channels in pancreatic β-cells, and has long been used in the management of type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome** (and the closely related **Classic Stiff Person Syndrome**), both at a prediction score of **99.00%**; however, there are currently **no clinical trials** and **no published literature** supporting this direction — this prediction rests on model inference alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (sulfonylurea class) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| Italy Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the Evidence Pack. Based on established pharmacology, gliquidone belongs to the sulfonylurea class and exerts its antidiabetic effect by binding to the sulfonylurea receptor 1 (SUR1) subunit of ATP-sensitive potassium (K-ATP) channels on pancreatic β-cells. This binding closes the channel, triggers membrane depolarization, and stimulates insulin release. Its efficacy in lowering blood glucose in type 2 diabetes is well-established across decades of clinical use.

The proposed bridge to focal stiff limb syndrome (FSLS) — a focal variant of the stiff person syndrome (SPS) spectrum — is built on a shared molecular antigen: glutamic acid decarboxylase 65 (GAD65). GAD65 is expressed both in pancreatic β-cells (where it is co-located with gliquidone's SUR1 target) and in GABAergic inhibitory interneurons of the spinal cord and brainstem, which are the primary sites of autoimmune attack in SPS-spectrum disorders. The TxGNN knowledge graph appears to have inferred this connection through the GAD65 → SUR1 → K-ATP channel node chain — essentially treating the shared autoantigen as an evidence bridge between diabetes pharmacology and neuroimmunological disease.

However, the mechanistic hypothesis faces a critical pharmacological obstacle. Gliquidone is highly protein-bound and demonstrates poor blood-brain barrier (BBB) penetration, resulting in negligible CNS drug exposure under standard oral dosing. Its peripheral mechanism targeting pancreatic K-ATP channels does not directly translate to central GABAergic modulation, and no experimental evidence currently validates the central pathway hypothesis. The prediction is intellectually interesting but mechanistically speculative at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Italy Market Information

Gliquidone is currently **not marketed in Italy**. No AIFA authorizations have been identified, and no product licenses are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based entirely on TxGNN knowledge-graph inference (Evidence Level L5), with zero supporting clinical trials or peer-reviewed publications. While the GAD65 autoantigen hypothesis provides a theoretical bridge between gliquidone's pharmacological target and the SPS disease mechanism, the drug's poor CNS penetration represents a fundamental pharmacokinetic barrier that would need to be resolved before any translational work could proceed.

**To proceed, the following is needed:**

- **CNS pharmacokinetics data**: Confirm or quantify gliquidone's BBB penetration and CSF exposure; evaluate whether any formulation strategy (e.g., CNS-targeted delivery) could achieve therapeutic concentrations in GABAergic circuits
- **Preclinical validation**: Conduct mechanistic studies in GAD65-antibody-positive animal models of SPS to test whether K-ATP channel modulation influences GABAergic inhibitory tone in the spinal cord
- **MOA documentation**: Complete the DrugBank API query (DG002 remediation) to obtain full mechanistic annotation, including known off-target effects
- **Full safety profile**: Retrieve the AIFA/Italian package insert (DG001 remediation) to complete contraindication, warning, and DDI assessment before any clinical hypothesis can be evaluated
- **Epidemiological feasibility check**: FSLS and classic SPS are both ultra-rare diseases; confirm whether patient population size would support even an investigator-initiated proof-of-concept study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

