---
layout: default
title: Flecainide
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Flecainide
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

The txgnn-pipeline skill is loaded. This is a report generation task, so I'll proceed directly with producing the pharmacist evaluation report from the Evidence Pack.

---

# Flecainide: From Cardiac Arrhythmia to Stroke Disorder

## One-Sentence Summary

Flecainide is a Class IC antiarrhythmic drug established for treating atrial fibrillation (AF) and paroxysmal supraventricular tachycardia, working by blocking cardiac sodium channels to restore and maintain normal sinus rhythm.
The TxGNN model predicts it may be effective for **stroke disorder** — through an indirect mechanism in which AF rhythm control reduces cardioembolic stroke risk — with **19 clinical trials** and **20 publications** currently supporting this direction.
However, no randomized trial has tested flecainide with stroke as a *primary* endpoint; all current evidence is indirect, derived from AF management trials in which stroke appears as a secondary or safety outcome.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Italian regulatory records (0 authorizations); established in clinical literature as atrial fibrillation and paroxysmal supraventricular tachycardia |
| Predicted New Indication | Stroke Disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| Italy Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Flecainide is a Class IC antiarrhythmic drug that blocks cardiac voltage-gated sodium channels (Nav1.5), slowing electrical conduction velocity and suppressing ectopic impulses in the atria. Although detailed MOA data is not available from DrugBank in this evidence pack, its clinical profile is well-characterized: it converts and maintains sinus rhythm primarily in patients with atrial fibrillation or paroxysmal supraventricular tachycardia, and is recommended only in patients without structural heart disease.

The mechanistic pathway linking flecainide to stroke disorder is indirect but biologically coherent: AF is responsible for approximately 20–30% of all ischemic strokes, generating cardioembolic clots within the left atrial appendage during chaotic atrial activity. By restoring and sustaining sinus rhythm, flecainide eliminates the stasis conditions that drive thrombus formation, thereby reducing downstream embolic events. This rationale was put to the test in the landmark EAST-AFNET 4 trial (N > 2,800), in which early rhythm control — with flecainide as one of the antiarrhythmic options — significantly reduced a composite endpoint that included stroke and TIA. A 2024 pre-specified sub-analysis (PMID 38702961) further confirmed that long-term sodium channel blocker therapy within this framework was both safe and effective.

The most direct current evidence comes from the ongoing ALPACA trial (NCT05213104, Phase 3, N=186), which is explicitly testing flecainide to prevent atrial arrhythmias after patent foramen ovale (PFO) closure in patients with cryptogenic ischemic stroke — directly combining a cerebrovascular intervention with flecainide as the antiarrhythmic adjunct. Additionally, NCT05293080 (EAST in acute STROKE, Phase 3, N=1,746) is designed to determine whether early rhythm control prevents adverse cardiovascular outcomes in AF patients presenting with acute ischemic stroke. If this trial is positive, it will elevate the evidence to L1 and substantially change the repurposing case.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Phase 4 | Unknown | 70 | Only trial directly comparing flecainide vs. vernakalant on atrial contractility in AF patients after cardioversion; improved post-cardioversion contractility may reduce short-term stroke risk window |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST Trial: early structured rhythm control (flecainide as one option) vs. usual care in AF; stroke/TIA was a component of the primary composite cardiovascular endpoint — the strongest completed indirect RCT evidence |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | NA | Completed | 2,204 | CABANA Trial: catheter ablation vs. antiarrhythmic drugs including flecainide for AF; stroke/TIA was a pre-specified secondary endpoint in this large high-quality multicenter trial |
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Phase 3 | Active, not recruiting | 186 | ALPACA Trial: directly tests whether flecainide reduces atrial arrhythmias after PFO closure in cryptogenic stroke patients — the most direct current clinical linkage between flecainide and cerebrovascular event prevention |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not yet recruiting | 1,746 | EAST in Acute STROKE: early AF rhythm control (including flecainide) in patients with acute ischemic stroke and newly diagnosed AF; if positive, this will constitute Level 1 evidence for flecainide in cerebrovascular indication |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | NA | Active, not recruiting | 484 | Pulsed field ablation vs. antiarrhythmic drugs (flecainide potentially in drug arm) for persistent AF; cerebrovascular events are a pre-specified secondary safety endpoint |
| [NCT02294955](https://clinicaltrials.gov/study/NCT02294955) | NA | Unknown | 152 | Multicenter RCT comparing catheter ablation vs. optimized pharmacological therapy (flecainide eligible) for symptomatic AF; parallel-group design |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Phase 4 | Not yet recruiting | 988 | RECA-FAST: evaluates whether flecainide is as safe as sotalol/amiodarone in AF patients with stable coronary artery disease — directly addresses the key safety barrier limiting flecainide's use in cerebrovascular patients with atherosclerotic comorbidities |
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | Not yet recruiting | 100 | SAVE STROKE Phase II: neurological outcomes after AF ablation vs. drug therapy in recent stroke patients; provides comparative background for flecainide-based antiarrhythmic strategies in post-stroke AF |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Phase 3 | Completed | 245 | STOP AF: cryoablation vs. antiarrhythmic drug therapy (flecainide, propafenone, or sotalol in control arm) for paroxysmal AF; primary endpoint was AF recurrence, not stroke |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | RCT Sub-analysis | Europace | Pre-specified EAST-AFNET 4 sub-analysis: long-term flecainide/propafenone (sodium channel blockers) for early rhythm control was safe and effective; addresses clinical concerns about proarrhythmic risk in cardiovascular disease patients |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort Study | J Atrial Fibrillation | Real-world cohort (N=10,455 AF patients): compared stroke, CHF, and cardiovascular event risks across antiarrhythmic agents including flecainide in US clinical practice |
| [37109225](https://pubmed.ncbi.nlm.nih.gov/37109225/) | 2023 | RCT | J Clinical Medicine | Multicenter randomized open-label pilot comparing flecainide vs. carvedilol for idiopathic premature ventricular complexes; confirms flecainide's antiarrhythmic efficacy in non-structural heart disease |
| [27159789](https://pubmed.ncbi.nlm.nih.gov/27159789/) | 2016 | Comprehensive Review | Nature Reviews Disease Primers | Authoritative primer on AF epidemiology and management; establishes the stroke risk mechanism of AF and the rationale for rhythm control as a stroke prevention strategy |
| [35114252](https://pubmed.ncbi.nlm.nih.gov/35114252/) | 2022 | Mechanistic Study | J Mol Cell Cardiology | Demonstrates intrinsic biophysical differences between atrial and ventricular Nav1.5 channels that explain flecainide's relative atrial selectivity and lower ventricular proarrhythmic risk; supports its targeted use in atrial arrhythmias |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Clinical Review | BMJ Clinical Evidence | Evidence-based review of acute AF: documents increased stroke and heart failure risk during AF episodes, reviews antiarrhythmic options including flecainide for cardioversion and sinus rhythm maintenance |
| [39077579](https://pubmed.ncbi.nlm.nih.gov/39077579/) | 2023 | Review | Reviews in Cardiovascular Medicine | Reviews AF management in pregnancy including flecainide; highlights the overarching challenge of thromboembolism prevention requiring individualized antiarrhythmic treatment decisions |
| [19265095](https://pubmed.ncbi.nlm.nih.gov/19265095/) | 2009 | Clinical Review | Chest | Acute AF management in critical care: emphasizes haemodynamic instability and thromboembolism as the two key sequelae driving the choice between rate control and rhythm control strategies |
| [8199770](https://pubmed.ncbi.nlm.nih.gov/8199770/) | 1994 | Review | Heart Disease and Stroke | Classic reference on flecainide's dual nature: potent efficacy for paroxysmal SVT without structural heart disease, alongside its proarrhythmic danger in patients with structural disease — foundational safety context |
| [19450312](https://pubmed.ncbi.nlm.nih.gov/19450312/) | 2008 | Clinical Review | BMJ Clinical Evidence | Earlier systematic clinical evidence review of acute AF: documents >50% spontaneous resolution within 24–48 hours and the interventional rationale for antiarrhythmic use in the remainder |

---

## Italy Market Information

Flecainide currently holds **no marketing authorizations** in Italy. There are no AIFA-approved products on the Italian market. Any potential clinical use would require a compassionate use application, off-label protocol under physician responsibility, or an import authorization (Article 648 procedure in Italy). This is a significant practical barrier to clinical deployment.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical context from evidence base:** The CAST trial (Cardiac Arrhythmia Suppression Trial) established that flecainide significantly increased mortality in patients with structural heart disease and prior myocardial infarction — a finding that fundamentally limits its use. Many patients with stroke disorder carry concurrent cardiovascular comorbidities (atherosclerosis, ischaemic heart disease, heart failure) that would constitute contraindications. Furthermore, flecainide can unmask Brugada syndrome (documented in PMID 27884575) and carries dose-dependent proarrhythmic risk including ventricular tachycardia (PMID 40800559). A notable TxGNN false-positive alert: sick sinus syndrome type 2 (SCN5A loss-of-function) was predicted as an indication (rank 3) but should be treated as a **contraindication** — flecainide would further suppress already dysfunctional Nav1.5 channels in this condition. Strict patient selection is essential.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic pathway from flecainide → AF rhythm control → reduced cardioembolic stroke is biologically sound and supported by indirect RCT evidence (EAST-AFNET 4, CABANA), but no trial has been designed with stroke as a primary endpoint for flecainide specifically. The CAST-trial safety legacy creates a substantial risk barrier in cerebrovascular patients, who frequently carry the structural heart disease comorbidities that make flecainide dangerous.

**To proceed, the following is needed:**

- **Await pivotal trial results:** NCT05293080 (EAST in Acute STROKE, Phase 3, N=1,746, completion 2029) and NCT05213104 (ALPACA, Phase 3, N=186, completion 2026-07) are the decisive trials — proceed to re-evaluation once data are available
- **Complete MOA documentation:** retrieve full pharmacological and toxicology profile from DrugBank (currently a High-severity data gap)
- **Safety data package:** obtain TFDA/AIFA package insert warnings and contraindications (currently a Blocking data gap that prevents S1 safety screening)
- **Patient selection criteria:** pre-define exclusion criteria for any future protocol — structural heart disease, ischaemic heart disease, conduction abnormalities, Brugada pattern, and SCN5A channelopathies must all be excluded
- **Consider cerebrovascular disorder instead:** the rank-9 prediction for *cerebrovascular disorder* carries L2 evidence with a "Proceed with Guardrails" recommendation and may be the more immediately actionable repurposing target given the ALPACA trial's direct PFO-stroke-flecainide design
- **Italy regulatory pathway:** if evidence becomes supportive, initiate regulatory intelligence on Article 648 (off-label use reimbursement) or compassionate use procedures, given zero current Italian authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

