---
layout: default
title: Glecaprevir
parent: Solo previsione del modello (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Glecaprevir: nuova indicazione prevista, Infezione da HIV (livello di evidenza L5). Indicazione originale: Infezione cronica da virus dell'epatite C (dal grafo di conoscenza"
monitor_inn: "glecaprevir"
predicted_indications: ["HIV infectious disease", "hepatitis B virus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "Kyasanur forest disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Glecaprevir
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **10** 
{: .fs-6 .fw-300 }

---

## Indice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relazione di valutazione farmaceutica

</div>

# Glecaprevir: dall'epatite C cronica all'infezione da HIV

## Sintesi in una frase

Glecaprevir è un inibitore della proteasi NS3/4A del virus dell'epatite C (HCV), utilizzato in associazione con pibrentasvir per il trattamento dell'infezione cronica da HCV.
Il modello TxGNN lo predice come potenzialmente efficace per l'**infezione da HIV**, ma le **6 sperimentazioni cliniche** e le **20 pubblicazioni** collegate riguardano in realtà la cura dell'HCV in pazienti con coinfezione HIV/HCV, non un effetto anti-HIV.
Il punteggio elevato sembra riflettere una vicinanza nella rete di conoscenze tra classi di farmaci antivirali, più che un'evidenza biologica.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezione cronica da virus dell'epatite C (dal grafo di conoscenza; il testo dell'indicazione approvata non è presente nei dati AIFA) |
| Nuova indicazione prevista | Infezione da HIV |
| Punteggio di predizione TxGNN | 99,87% |
| Livello di evidenza | L3 (studi osservazionali e revisioni; nessuno studio testa un effetto anti-HIV) |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 2 (entrambe revocate) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione è ragionevole (o no)?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. Sulla base delle informazioni note, glecaprevir fa parte dell'associazione a dose fissa con pibrentasvir (inibitore di NS5A). La sua efficacia nell'epatite C è dimostrata, ma dal punto di vista meccanicistico non è applicabile in modo diretto all'HIV.

Glecaprevir agisce sulla proteasi NS3/4A dell'HCV e non ha un'attività nota contro la proteasi dell'HIV né altri bersagli del virus. Il punteggio TxGNN probabilmente deriva dalla prossimità, nella rete di conoscenze, tra le classi di inibitori delle proteasi antivirali e dalla frequente coesistenza di HIV e HCV.

Gli studi elencati arruolano pazienti coinfetti e misurano la guarigione dall'HCV (risposta virologica sostenuta, SVR), non il controllo dell'HIV. Le evidenze sostengono quindi un trattamento sicuro ed efficace dell'HCV nelle persone con HIV, ma non un effetto anti-HIV. Qualunque affermazione di riposizionamento per l'HIV in sé non è supportata.

Anche le altre predizioni del modello (epatite B, epatite E, epatite A, HIV felino e simiano, febbre emorragica di Omsk, malattia della foresta di Kyasanur, un disturbo del neurosviluppo raro) sono prive di una base meccanicistica solida o sono artefatti computazionali. Per l'epatite A, le 40 sperimentazioni associate riguardano l'HCV e sono state abbinate probabilmente per il termine generico «epatite».

---

## Evidenze dagli studi clinici

| Studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Fase 3 | Completato | 153 | EXPEDITION-2: efficacia e sicurezza di glecaprevir/pibrentasvir in adulti con HCV (genotipi 1-6) e coinfezione HIV-1; esito sull'HCV |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Fase 3 | Completato | 546 | Studio controllato con placebo in adulti asiatici non cirrotici con HCV, con o senza coinfezione HIV |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Fase 3 | Completato | 160 | Studio in aperto in adulti asiatici con HCV e cirrosi compensata, con o senza coinfezione HIV |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Fase 3 | Completato | 83 | Studio pilota su DAA in infezione da HCV di recente acquisizione, con o senza HIV; il regime include anche paritaprevir/ritonavir |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Fase 4 | Completato | 87 | Rischio cardiovascolare dopo eradicazione dell'HCV in persone con HIV; non testa un effetto anti-HIV |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Fase 2 | Completato | 45 | PURGE-C: glecaprevir/pibrentasvir per 4 settimane nell'HCV acuto, con o senza HIV-1 |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Fase 1/2 | In reclutamento | 30 | Farmacocinetica e sicurezza in gravidanza in donne con HCV, con o senza HIV |

In tutti questi studi l'esito misurato è la risposta contro l'HCV, non il controllo dell'HIV.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Revisione sistematica/meta-analisi | Int J Antimicrob Agents | 13 studi, 3082 pazienti: SVR12 complessivo del 97,8% con glecaprevir/pibrentasvir nell'HCV genotipi 1-6 |
| [42850633](https://pubmed.ncbi.nlm.nih.gov/42850633/) | 2026 | Revisione sistematica/meta-analisi | Virol J | Efficacia dei regimi DAA nell'HCV acuto, in particolare in MSM con HIV e persone che si iniettano droghe |
| [41297677](https://pubmed.ncbi.nlm.nih.gov/41297677/) | 2026 | Fase 3b a braccio singolo | J Hepatol | Glecaprevir/pibrentasvir per 8 settimane in adulti con HCV acuto |
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Coorte | J Antimicrob Chemother | Risposta a glecaprevir/pibrentasvir nella pratica clinica in pazienti coinfetti HIV/HCV |
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | Studio real-world | Clin Exp Hepatol | Efficacia di glecaprevir/pibrentasvir in pazienti HIV/HCV trattati con bictegravir/emtricitabina/tenofovir alafenamide |
| [32754824](https://pubmed.ncbi.nlm.nih.gov/32754824/) | 2020 | Coorte | Adv Ther | Uso reale di glecaprevir/pibrentasvir per 8 settimane in pazienti naïve con cirrosi compensata |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Revisione | Future Microbiol | Glecaprevir/pibrentasvir nell'infezione cronica da HCV |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revisione | Clin Pharmacokinet | Aspetti farmacocinetici e farmacodinamici della terapia anti-HCV |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Revisione | Expert Opin Pharmacother | Terapia con inibitori delle proteasi per l'HCV |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Revisione | Eur J Gen Pract | Diagnosi e trattamento dell'epatite C cronica |

Nessuna pubblicazione documenta un'attività di glecaprevir contro l'HIV.

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 045445018 | MAVIRET 4x21 cpr rivestite 100 mg + 40 mg, confezione multipla (ABBVIE DEUTSCHLAND) | Non indicata | Non indicata (autorizzazione revocata) |
| 045445032 | MAVIRET 28 bustine orali granulato 50 mg + 20 mg (ABBVIE DEUTSCHLAND) | Non indicata | Non indicata (autorizzazione revocata) |

---

## Citotossicità

Glecaprevir è un antivirale e non un farmaco antineoplastico: questa sezione non è applicabile.

---

## Considerazioni sulla sicurezza

**Interazioni farmacologiche**: dai dati compilati risultano 57 interazioni. Tra quelle di livello **maggiore** figurano:
- Rosuvastatina
- Simvastatina
- Edoxaban

Tra quelle di livello moderato, a titolo di esempio: desametasone, esomeprazolo, omeprazolo, apixaban, betrixaban, cobicistat, deferasirox, lusutrombopag e griseofulvina. Sono presenti anche interazioni minori (ad esempio fidaxomicina, naloxegol, procalopride, indacaterolo).

Per avvertenze e controindicazioni si rimanda al foglio illustrativo.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
- Le evidenze disponibili dimostrano l'efficacia di glecaprevir/pibrentasvir contro l'HCV, anche in pazienti con coinfezione HIV, ma nessuna indica un effetto anti-HIV. L'alto punteggio TxGNN appare un artefatto di rete e il riposizionamento per l'HIV non è supportato.
- In Italia le due autorizzazioni risultano revocate, quindi non c'è oggi un prodotto commercializzato a cui ricondurre un eventuale uso.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione (MOA) da DrugBank, e dati in vitro che mostrino attività su bersagli dell'HIV
- Il foglio illustrativo AIFA con avvertenze e controindicazioni, per completare la valutazione di sicurezza
- Chiarire lo stato regolatorio in Italia (motivi e data della revoca delle autorizzazioni)
- Considerare più realistica l'indicazione già supportata: la cura dell'HCV nei pazienti coinfetti HIV/HCV, valutando la gestione delle interazioni con gli antiretrovirali
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

