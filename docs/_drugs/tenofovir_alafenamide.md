---
layout: default
title: Tenofovir Alafenamide
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
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

# TENOFOVIR ALAFENAMIDE: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tenofovir alafenamide (TAF) is a novel prodrug of tenofovir, established as a core component of antiretroviral therapy (ART) for HIV-1 infection and chronic hepatitis B in humans.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
with **1 clinical trial** (indirect, Phase 1/2) and **9 preclinical publications** from macaque animal models currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection and chronic hepatitis B (core ART component) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (preclinical animal studies only) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

TAF is a prodrug of tenofovir that, following intracellular phosphorylation, generates tenofovir diphosphate — a potent inhibitor of viral reverse transcriptase (classified as a Nucleotide Reverse Transcriptase Inhibitor, NtRTI). This mechanism blocks the conversion of viral RNA into DNA, interrupting replication at a fundamental and conserved step across retroviruses.

SIV and HIV both belong to the primate lentivirus family (*Lentivirus* genus) and share highly homologous reverse transcriptase sequences. This structural conservation means TAF's inhibitory mechanism applies almost directly to SIV replication. In practice, macaque SIV/SHIV infection models serve as the gold-standard preclinical bridge for validating HIV antiretrovirals before human trials — TAF has been systematically deployed across these models to test oral PrEP regimens, long-acting formulations (implants, vaginal inserts), and early ART-driven remission strategies.

However, the practical repurposing value for human clinical application is limited: SIV infection primarily affects non-human primates in research and veterinary settings, not human patients. This prediction carries strong mechanistic plausibility and clear scientific utility in the preclinical/translational research context, but does not correspond to an unmet human clinical indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Evaluated vedolizumab combined with ART (TAF used as ART backbone, not the primary investigational agent) in HIV-infected subjects for gut immune reconstitution and virological remission post-ART interruption. Indirect relevance: TAF's role is as background antiviral suppression, not the intervention under study. Trial ended at unknown status; enrollment too small for statistical conclusions. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Animal Study | J Infect Dis | TAF/EVG vaginal inserts provided 93–100% protection against repeated SHIV vaginal challenges in macaques when administered 4 hours before or after exposure, demonstrating strong extended post-exposure prophylaxis |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Animal Study | Nat Commun | Oral FTC/TAF combined with long-acting cabotegravir/rilpivirine achieved SHIV remission in macaques when treatment was initiated early; robust tissue reservoir penetration was highlighted as a key advantage of TAF |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Animal Study | Front Immunol | Humanized mouse model validated TAF-based ART efficacy against both SIV and HIV, supporting cross-species applicability for antiviral combination screening |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | Animal Study | J Antimicrob Chemother | Biodegradable polycaprolactone implants releasing TAF protected macaques from vaginal SHIV infection, establishing proof-of-concept for long-acting sustained-release PrEP |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Animal Study | J Infect Dis | Oral TAF alone and TAF/FTC combination both prevented vaginal SHIV infection in macaques under repeated exposure; the TAF/FTC combination demonstrated superior protection rates |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | Animal Study | PLoS One | Developed a reliable protocol for daily oral ART administration in macaques with high adherence rates, directly enabling reproducible TAF-based HIV/SIV prevention and treatment research |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal Study | J Infect Dis | Oral FTC/TAF protected macaques against rectal SHIV infection across 19 weekly exposures; TAF delivered substantially higher intracellular tenofovir diphosphate concentrations in lymphoid tissues compared to TDF |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | Animal Study | J Infect Dis | Oral PrEP during acute SHIV infection in macaques significantly reduced systemic inflammation and CD4 T-cell loss compared to untreated infection, indicating immunological benefit beyond viral suppression |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Animal Study | J Acquir Immune Defic Syndr | Oral TDF and topical GS-7340 (early precursor to TAF) evaluated against repeated SIV oral challenges in infant macaques; demonstrated meaningful chemoprophylactic protection in a pediatric mother-to-infant transmission model |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All current evidence for TAF in SIV infection derives from non-human primate preclinical models; no direct human clinical trials for this indication exist, and SIV infection is itself a non-human primate disease that does not represent an actionable unmet need in human medicine.

**To proceed, the following is needed:**

- **Clarify repurposing goal**: If the intent is veterinary application (e.g., treating SIV in research colony animals or exploring cross-species lentiviral therapy), conduct species-specific pharmacokinetic and in vitro sensitivity studies for TAF against the relevant SIV strain
- **Expand to human-applicable lentiviral indications**: If seeking a genuinely novel human indication within the lentivirus family, redirect investigation toward HTLV-associated conditions or other human retroviruses not currently covered by existing TAF approvals
- **Complete the safety profile**: Obtain and parse the TFDA/AIFA package insert and DrugBank MOA data to resolve the current [Data Gap] in mechanism and warning information before any regulatory or clinical planning
- **Taiwan registration pathway**: If any downstream human application is identified, an TFDA NDA/supplemental application strategy will be required given zero existing local authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

