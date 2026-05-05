---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Miglustat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using the txgnn-pipeline skill as context. Now generating the report based on the Evidence Pack, with **Tay-Sachs disease** (rank 7 in the predicted list) as the primary focus — it is the only indication with meaningful clinical evidence (L2, 5 trials, 20 publications), making it the actionable candidate.

---

# Miglustat: From Gaucher Disease to Tay-Sachs Disease

## One-Sentence Summary

Miglustat (Zavesca®) is an oral substrate reduction therapy originally approved for type 1 Gaucher disease, acting by inhibiting glucosylceramide synthase (GCS) to reduce glycosphingolipid production in lysosomally stressed cells.
The TxGNN model predicts it may be effective for **Tay-Sachs disease** (GM2 gangliosidosis), supported by **5 clinical trials** and **20 publications**.
While the mechanistic rationale is scientifically compelling, Phase 3 trials in the infantile form were terminated early — the most realistic opportunity lies in the **late-onset variant**, where residual enzyme activity gives SRT more room to work.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 1 Gaucher disease (per published literature; no Italy marketing authorization on record) |
| Predicted New Indication | Tay-Sachs disease |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L2 |
| Italy Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Miglustat is a small-molecule iminosugar that inhibits glucosylceramide synthase (GCS), the first committed enzyme in glycosphingolipid biosynthesis. Rather than replacing a deficient enzyme, it works as a **substrate reduction therapy (SRT)**: by slowing the rate at which substrate is produced, it reduces the lysosomal burden to a level where residual enzyme activity can maintain metabolic balance.

Tay-Sachs disease is caused by deficiency of β-hexosaminidase A (HexA, encoded by *HEXA*), which normally degrades GM2 ganglioside in lysosomes. Without functional HexA, GM2 accumulates relentlessly in neurons, driving progressive neurodegeneration. Since GM2 is synthesized **downstream** of glucosylceramide in the sphingolipid pathway, GCS inhibition by miglustat reduces the upstream supply of GM2 precursors — directly targeting the accumulation cascade that HexA can no longer resolve.

This is precisely the same mechanistic principle behind miglustat's approved use in Gaucher disease, where glucocerebrosidase deficiency leads to glucosylceramide storage. Both Gaucher disease and Tay-Sachs are lysosomal storage disorders caused by defects in glycosphingolipid catabolism enzymes, making the SRT concept mechanistically transferable. The critical clinical distinction is that **late-onset Tay-Sachs** (with residual HexA activity and slower accumulation) represents a far more tractable target than the acute infantile form, where near-complete enzyme deficiency and rapid disease progression make SRT insufficient on its own.

> Formal MOA data from DrugBank was not available for this report. The mechanistic analysis above is derived from published literature contained in the evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | Completed | 5 | PK and tolerability of miglustat in juvenile GM2 gangliosidosis; confirms CNS drug penetration but sample is too small for efficacy conclusions |
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | Completed | 10 | PK and safety in infantile GM2 gangliosidosis (Tay-Sachs/Sandhoff); establishes dosing feasibility but not designed to assess efficacy |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | Terminated | 30 | Miglustat efficacy in infantile Sandhoff/Tay-Sachs — terminated early; significant negative signal for the infantile phenotype |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | Terminated | 16 | Syner-G trial: miglustat + ketogenic diet in gangliosidoses — terminated early; combination strategy remains unresolved |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Phase 2 | Recruiting | 21 | Long-term safety of Nizubaglustat (AZ-3102) in GM2/NPC; includes cohort transitioning from stable miglustat — signals active next-generation SRT competition |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT (Phase 2) | Genetics in Medicine | 12-month RCT + 24-month extension evaluating miglustat safety and efficacy in **late-onset** GM2 gangliosidosis (Tay-Sachs/Sandhoff); primary evidence base for this indication |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Systematic Review | European Journal of Neurology | Comprehensive systematic review of miglustat in GM2 gangliosidosis; results inconsistent across studies — overall mixed efficacy picture |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Review | Int J Molecular Sciences | Clinical features, pathophysiology, and current therapeutic options across all GM2 gangliosidoses; useful disease overview |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Review | Frontiers in Physiology | Emerging therapeutic approaches for Tay-Sachs including SRT, gene therapy, and enzyme enhancement — SRT positioned as bridge therapy |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Drug Profile Review | Curr Opin Investigational Drugs | Early miglustat drug profile; documents original Gaucher approval and early-stage Tay-Sachs/Fabry/NPC development program |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Case Series | Neurology | Miglustat SRT in 2 infantile TSD patients; neurological deterioration not arrested, but CSF drug exposure confirmed — supports CNS access, not infantile efficacy |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Observational | Mol Genetics and Metabolism | Natural history of infantile GM2 gangliosidoses; notes miglustat limited by gastrointestinal side effects — relevant tolerability signal |
| [33738443](https://pubmed.ncbi.nlm.nih.gov/33738443/) | 2021 | Cohort/Multi-disease | Brain Communications | Acetyl-leucine in lysosomal storage disorders including GM2 gangliosidosis; context for combination therapy approaches with SRT |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Pilot Study | J Inherited Metabolic Disease | Neurocognitive testing in late-onset Tay-Sachs as a potential outcome measure; informs trial design for future miglustat studies |
| [9572057](https://pubmed.ncbi.nlm.nih.gov/9572057/) | 1998 | Basic Science Review | Molecular Medicine Today | Foundational biology of GM2 gangliosidoses and rationale for substrate reduction strategies; historical scientific basis |

---

## Italy Market Information

Miglustat holds no marketing authorization in Italy. No product licenses are on record.

> For reference: In other EU member states, miglustat (Zavesca®, Actelion/Janssen) is authorized for type 1 Gaucher disease in patients for whom enzyme replacement therapy is unsuitable, and for Niemann-Pick type C disease. Any repurposing application in Italy would need to proceed via AIFA's orphan drug or off-label access pathways.

---

## Safety Considerations

No formal safety data was retrieved for this report (package insert warnings and drug interaction database both returned no results).

Based on published literature within the evidence pack:
- **Gastrointestinal effects**: Diarrhea, flatulence, and abdominal pain are the most commonly reported adverse events; these have been significant enough to limit dosing in pediatric gangliosidosis patients.
- **Neurological effects**: Tremor has been reported; warrants monitoring in a neurodegenerative disease context.

> Please refer to the Zavesca® Summary of Product Characteristics (SmPC) for the complete safety profile before any clinical or prescribing decision.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for miglustat in Tay-Sachs disease is scientifically sound and directly analogous to its approved use in Gaucher disease — both are lysosomal glycosphingolipid storage disorders amenable to substrate reduction. A completed Phase 2 RCT and a 2023 systematic review provide real clinical evidence, though results are inconsistent and largely confined to the late-onset phenotype. The infantile form is not a viable target given premature Phase 3 termination.

**To proceed, the following is needed:**

- **Specify the target population**: Clinical development should focus exclusively on **late-onset (juvenile/adult) Tay-Sachs**, where residual HexA activity and slower accumulation make SRT mechanistically feasible; infantile Tay-Sachs has negative Phase 3 evidence (NCT03822013 terminated)
- **Fill DG001**: Obtain TFDA/AIFA package insert warnings and contraindications before any safety evaluation can advance to S1
- **Fill DG002**: Retrieve full MOA data from DrugBank for complete mechanistic dossier
- **Assess competitive landscape**: Nizubaglustat (AZ-3102, NCT07399704) is actively recruiting as a next-generation SRT and may supersede miglustat in this space
- **Define outcome endpoints**: Neurocognitive and neurological stability measures (informed by PMID 18618288) should anchor any prospective study design
- **Regulatory pathway**: Evaluate feasibility of AIFA orphan drug designation or Law 648 access prior to initiating any Italian-specific program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

