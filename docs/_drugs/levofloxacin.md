---
layout: default
title: Levofloxacin
parent: Prove moderate (L3-L4)
nav_order: 267
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-28
description: "Levofloxacin: nuova indicazione prevista, Cheratocongiuntivite epiteliale puntata (livello di evidenza L5). Indicazione originale: Infezioni batteriche (streptococciche, stafilococciche…"
monitor_inn: "Levofloxacin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Levofloxacin
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **10** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relazione di valutazione farmaceutica

</div>

## Levofloxacina: dalle infezioni batteriche alla cheratocongiuntivite epiteliale puntata
{: .text-alpha }

## Sintesi

La levofloxacina è un antibiotico fluorochinolonico, originariamente usato per infezioni batteriche come polmonite, sinusite, pielonefrite, congiuntivite e infezione da antrace.
Il modello TxGNN per la prima predizione indica la **cheratocongiuntivite epiteliale puntata** (punteggio 0,9992), ma i dati compilati non mostrano alcuno studio clinico e una sola pubblicazione, **che non ne sostiene l'efficacia** (focolaio da microsporidi, non sensibili ai fluorochinoloni).
Tra le predizioni successive, le più documentate sono la **peste setticemica** (solo dati su modelli animali) e la **gammopatia monoclonale** (profilassi antibatterica nel mieloma, con uno studio di fase 3).

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezioni batteriche (streptococciche, stafilococciche, polmonite batterica, sinusite mascellare, congiuntivite, pielonefrite, antrace). Il testo dell'indicazione autorizzata AIFA non è disponibile nei dati compilati. |
| Nuova indicazione predetta | Cheratocongiuntivite epiteliale puntata |
| Punteggio di predizione TxGNN | 0,9992 |
| Livello di evidenza | L4 (L5 per assenza di studi clinici sull'indicazione specifica; l'unica pubblicazione è un rapporto di focolaio non favorevole) |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione nei dati compilati. Per conoscenza generale, la levofloxacina è un fluorochinolone battericida che inibisce la DNA girasi e la topoisomerasi IV. È già usata nella congiuntivite batterica, per cui un legame con infezioni oculari è plausibile.

Tuttavia, la cheratocongiuntivite epiteliale puntata descritta nell'unica pubblicazione disponibile è di origine microsporidica, e i microsporidi non sono sensibili ai fluorochinoloni come classe. L'elevato punteggio TxGNN riflette probabilmente la vicinanza nella rete di conoscenza con l'indicazione di congiuntivite già esistente, più che un'evidenza terapeutica reale.

## Evidenze dagli studi clinici

Al momento non risulta alcuno studio clinico registrato correlato a questa indicazione.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Rapporto di focolaio | American Journal of Ophthalmology | Focolaio di cheratocongiuntivite microsporidica associato a contaminazione dell'acqua di piscine a Taiwan; nessun supporto all'efficacia della levofloxacina |

## Altre predizioni con evidenze rilevanti

| Indicazione predetta | Punteggio TxGNN | Livello | Evidenza principale | Valutazione |
|------|------|------|------|------|
| Peste setticemica | 0,9980 | L3 | Levofloxacina ha curato la peste polmonare sperimentale in scimmie verdi africane ([PMID 21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/)); studio sul ritardo del trattamento ([PMID 32435805](https://pubmed.ncbi.nlm.nih.gov/32435805/)); modello usato per l'approvazione FDA secondo l'Animal Rule ([PMID 32435803](https://pubmed.ncbi.nlm.nih.gov/32435803/)). Dati murini discordanti ([PMID 21574421](https://pubmed.ncbi.nlm.nih.gov/21574421/)) | Proceed with Guardrails: nessuno studio clinico sull'uomo; verificare la sensibilità e seguire le indicazioni di sanità pubblica |
| Gammopatia monoclonale | 0,9981 | L1 | Studio di fase 3 TEAMM, in doppio cieco e controllato con placebo, in mieloma di nuova diagnosi ([PMID 31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/), [PMID 31690402](https://pubmed.ncbi.nlm.nih.gov/31690402/)); studi di coorte in contesto trapiantologico | Research Question: è una profilassi antibatterica di supporto, non una terapia della malattia; l'evidenza non si estende a MGUS o forme smoldering; restano dubbi su resistenze ed eventi avversi |
| Incompatibilità di gruppo sanguigno | 0,9985 | L4 | Un solo caso clinico di batteriemia da *Campylobacter lari* ([PMID 40350274](https://pubmed.ncbi.nlm.nih.gov/40350274/)) | Hold: non dimostra efficacia sull'incompatibilità |

Le altre predizioni (sindrome da iperviscosità policlonale, iperamilasemia, analbuminemia congenita, malattia ematologica premaligna, neuropatia periferica acquisita di origine ematologica, disturbo ematologico congenito) non hanno studi né letteratura e non presentano un meccanismo plausibile: Hold. Per la neuropatia periferica, i fluorochinoloni riportano anzi un'avvertenza specifica.

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano **cancellate**; non ci sono autorizzazioni valide. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati compilati. Principali autorizzazioni (compresse rivestite):

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 033634039 | TAVANIC 5 cpr rivestite 500 mg | Sanofi Srl | Valida |
| 040039024 | Levofloxacina 5 cpr rivestite 500 mg | Zentiva Italia Srl | Valida |
| 040219139 | Levofloxacina 5 cpr rivestite 500 mg | Sandoz SpA | Valida |
| 039686136 | Levofloxacina 5 cpr rivestite div 500 mg | Teva Italia Srl | Valida |
| 040361053 | FALEV 5 cpr rivestite 500 mg | Lanova Farmaceutici Srl | Valida |

## Considerazioni di sicurezza

Le informazioni del foglio illustrativo AIFA (avvertenze e controindicazioni) non sono disponibili nei dati compilati; si rimanda al foglio illustrativo.

- **Condizioni associate a controindicazione o cautela (dal modello TxGNN (deep learning), non da testo di etichetta; possono riflettere similarità apprese dal modello tra malattie correlate, non evidenze biologiche)**: sindrome del QT lungo e torsioni di punta, epilessia, malattie epatiche e danno epatico da farmaci, tendinite e disturbi tendinei, neuropatia periferica, miastenia gravis, rabdomiolisi, diabete e chetoacidosi diabetica, insufficienza renale, colite da *Clostridium difficile*, ischemia miocardica e coronaropatia, discrasie ematiche (trombocitopenia, leucopenia, pancitopenia, anemia), carenza di potassio.
- **Interazioni farmacologiche**: individuate 100 interazioni; tra le prime 20 mostrate, quelle di livello **maggiore** sono con **tramadolo** e **idrocortisone**. Numerose interazioni moderate riguardano antidiabetici (metformina, pioglitazone, acarbosio, alogliptin, albiglutide), beta-agonisti (formoterolo, salbutamolo), FANS (ibuprofene, ketorolac), famotidina, adenosina, alfuzosina, abiraterone, etinilestradiolo e amifampridina. Minori: paclitaxel, aldesleuchina, altretamina.

## Conclusione e prossimi passi

**Decisione: Hold** (per l'indicazione di primo rango, cheratocongiuntivite epiteliale puntata)

**Motivazione:**
- Non esistono studi clinici e l'unica pubblicazione riguarda un patogeno (microsporidi) non sensibile ai fluorochinoloni; il punteggio elevato è verosimilmente un artefatto di prossimità con l'indicazione di congiuntivite batterica. Tutte le autorizzazioni italiane sono inoltre cancellate.
- Tra le alternative, la peste setticemica (Proceed with Guardrails, L3) è la più solida sul piano meccanicistico, e la profilassi nel mieloma (L1) è un'ipotesi di ricerca.

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione dal database DrugBank
- Avvertenze e controindicazioni dal foglio illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Chiarimento dello stato regolatorio italiano (autorizzazioni cancellate) e delle vie di somministrazione disponibili
- Per la peste: dati clinici umani, conferma della sensibilità e piano di sorveglianza delle resistenze
- Per la gammopatia monoclonale: valutazione di efficacia in MGUS/smoldering e del bilancio rischio-beneficio rispetto a resistenze ed eventi avversi
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

