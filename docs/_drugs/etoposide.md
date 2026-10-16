---
layout: default
title: Etoposide
parent: Solo previsione del modello (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Etoposide: nuova indicazione prevista, Sarcoma di Ewing (la predizione con il punteggio più alto… (livello di evidenza L5). Indicazione originale: Carcinoma polmonare a piccole cellule"
monitor_inn: "ETOPOSIDE"
predicted_indications: ["well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "Ewing sarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma"]
---

# Etoposide
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

# Etoposide: dal carcinoma polmonare a piccole cellule al sarcoma di Ewing

## Sintesi

L'etoposide è un chemioterapico antineoplastico originariamente impiegato nel carcinoma polmonare a piccole cellule e nei tumori germinali del testicolo (seminoma, tumore del sacco vitellino, teratoma). Il modello TxGNN, tra le 10 indicazioni candidate, ne prevede l'efficacia in particolare nel **sarcoma di Ewing**, con **oltre 30 studi clinici registrati** (di cui diversi di fase 3) e **numerose pubblicazioni**, tra cui più RCT di fase 3. In questo caso l'impiego è già pratica clinica consolidata e non una vera novità di riposizionamento.

> Nota: la predizione rank 1 del modello (adenocarcinoma fetale ben differenziato del polmone) ha una sola evidenza (case report) e decisione "Hold". Questo report si concentra sull'indicazione con le evidenze più solide, il sarcoma di Ewing, e riassume le altre in una tabella.

---

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Carcinoma polmonare a piccole cellule; tumori germinali del testicolo (il testo dell'indicazione approvata AIFA non è disponibile nei dati compilati) |
| Nuova indicazione prevista | Sarcoma di Ewing (la predizione con il punteggio più alto, "adenocarcinoma fetale ben differenziato del polmone", ha evidenza L4 e decisione Hold) |
| Punteggio di predizione TxGNN | 99,85% (sarcoma di Ewing); 99,94% per la prima predizione in classifica |
| Livello di evidenza | L1 (sarcoma di Ewing) |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 2 (0 valide, 2 revocate) |
| Decisione raccomandata | Proceed with Guardrails (procedere con cautele) |

---

## Perché la predizione è ragionevole?

Il dato dettagliato sul meccanismo d'azione non è disponibile nei dati compilati. In base alle informazioni note, l'etoposide è un inibitore della topoisomerasi II, la cui efficacia nel carcinoma polmonare a piccole cellule e nei tumori germinali è dimostrata. Meccanisticamente può essere applicabile ai tumori a piccole cellule rotonde, a rapida proliferazione e chemiosensibili, come il sarcoma di Ewing.

Il sarcoma di Ewing è noto per l'elevata sensibilità ad agenti genotossici come l'etoposide (Gorthi et al., *Nature* 2018). L'aggiunta di ifosfamide ed etoposide alla chemioterapia standard ha migliorato la sopravvivenza libera da eventi nella malattia non metastatica (RCT di fase 3 INT-0154, PMID 12594313). I regimi con etoposide (per es. VDC/IE) sono standard di cura e compaiono nelle raccomandazioni di consenso. Si tratta quindi di pratica clinica già stabilita più che di riposizionamento in senso stretto.

---

## Evidenze da studi clinici (sarcoma di Ewing)

Selezione dei più rilevanti tra gli studi registrati (massimo 10):

| Numero studio | Fase | Stato | Arruolamento | Risultati chiave |
|---------|------|------|------|---------|
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Fase 3 | Sconosciuto | N/D | EICESS 92: confronto randomizzato di regimi chemioterapici con etoposide in Ewing, più chirurgia e radioterapia |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Fase 3 | Sconosciuto | 1200 | EURO-E.W.I.N.G.99: chemioterapia con o senza radioterapia/chirurgia e trapianto di cellule staminali |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Fase 3 | Completato | 587 | Intensificazione della chemioterapia per compressione degli intervalli in Ewing e tumori correlati |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Fase 3 | Completato | 642 | Aggiunta di vincristina-topotecan-ciclofosfamide al regime standard a 5 farmaci (incluso etoposide) nella malattia non metastatica |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Fase 3 | Completato | 278 | Intensificazione della dose nella malattia non metastatica: trattamento standard vs intensivo |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Fase 3 | Attivo, non in arruolamento | 312 | Aggiunta di ganitumab alla chemioterapia multi-agente (con etoposide) nella malattia metastatica |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Fase 2 | Completato | 155 | Alte dosi di chemioterapia, radioterapia e consolidamento nel sarcoma di Ewing metastatico |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Fase 2 | Completato | N/D | Ciclofosfamide, doxorubicina, vincristina, etoposide e ifosfamide seguiti da resezione e radioterapia in PNET/Ewing |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Fase 2 | Attivo, non in arruolamento | 83 | Irinotecan e temozolomide aggiunti a chemioterapia ad alte dosi in Ewing di nuova diagnosi |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Fase 2 | Completato | 130 | Terapia intensiva con supporto di fattori di crescita in Ewing metastatico alla diagnosi |

---

## Evidenze dalla letteratura (sarcoma di Ewing)

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT fase 3 | N Engl J Med | L'aggiunta di ifosfamide ed etoposide alla chemioterapia standard migliora la sopravvivenza in Ewing/PNET dell'osso di nuova diagnosi |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT fase 3 | Lancet | EE2012: confronto di due regimi chemioterapici standard (europeo e USA) in Ewing di nuova diagnosi |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT fase 3 | J Clin Oncol | Ganitumab con chemioterapia a intervalli compressi nel sarcoma di Ewing metastatico |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Chemioterapia a intervalli compressi (alternanza VDC e IE) nel sarcoma di Ewing localizzato |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | Protocollo RCT | Trials | Protocollo EURO EWING 2012 per Ewing di nuova diagnosi |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Linee guida di consenso | Cancer | Raccomandazioni del National Ewing Sarcoma Tumor Board sulla gestione del sarcoma di Ewing |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Revisione | J Clin Oncol | Gestione attuale e approcci futuri nel sarcoma di Ewing |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | Analisi retrospettiva | Sarcoma | Etoposide orale in 33 pazienti adolescenti e adulti con Ewing recidivante o refrattario |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | Studio meccanicistico | Nature | EWS-FLI1 causa R-loop e blocca la riparazione BRCA1, spiegando la sensibilità all'etoposide |
| [37651654](https://pubmed.ncbi.nlm.nih.gov/37651654/) | 2023 | Follow-up a lungo termine | J Clin Oncol | Esiti a lungo termine in Ewing localizzato trattato con chemioterapia a intervalli compressi (AEWS0031) |

---

## Altre indicazioni previste dal modello

| Indicazione | Punteggio | Evidenza | Decisione | Nota |
|------|------|------|------|------|
| Adenocarcinoma fetale ben differenziato del polmone | 99,94% | L4 | Hold | Un solo case report/revisione; nessuno studio registrato |
| Linfoma polmonare primitivo | 99,94% | L4 | Hold | Letteratura prevalentemente su altri sottotipi di linfoma; nessuno studio specifico |
| Blastoma polmonare | 99,94% | L4 | Hold | Solo case report e piccole serie; malattia rara |
| Rabdomiosarcoma (generale) | 99,79% | L1 | Proceed with Guardrails | Ifosfamide/etoposide superiore a vincristina/melfalan nella malattia metastatica (PMID 11846301); studio di fase 3 NCT00003052; il contributo indipendente dell'etoposide non è isolato e il backbone standard resta VAC |
| Rabdomiosarcoma embrionale botrioide della vagina | 99,80% | L4 | Hold | Solo un case report (cervice uterina) |
| Rabdomiosarcoma embrionale parameningeo | 99,76% | L4 | Hold | Letteratura generale, indiretta |
| Rabdomiosarcoma embrionale prostatico | 99,74% | L4 | Hold | Una sola revisione del 1987 |
| Rabdomiosarcoma embrionale dei dotti biliari extraepatici (due voci) | 99,76% / 99,75% | L5 | Hold | Nessuno studio né letteratura; segnale solo predittivo |

---

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 024639039 | VEPESID 20 capsule molli da 50 mg (CHEPLAPHARM ARZNEIMITTEL GMBH) | Capsula molle | Non disponibile; autorizzazione revocata |
| 024639041 | VEPESID 10 capsule molli da 100 mg (CHEPLAPHARM ARZNEIMITTEL GMBH) | Capsula molle | Non disponibile; autorizzazione revocata |

Entrambe le autorizzazioni risultano revocate: attualmente non vi è una specialità monocomponente valida in Italia nei dati compilati.

---

## Citotossicità

| Voce | Contenuto |
|------|------|
| Classificazione di citotossicità | Citotossico convenzionale (inibitore della topoisomerasi II, epipodofillotossina) |
| Rischio di mielosoppressione | Alto (i dati sulle controindicazioni del grafo di conoscenza segnalano neutropenia, trombocitopenia, leucopenia, agranulocitosi e anemia) |
| Classificazione emetogenica | Bassa-moderata (secondo la classe del farmaco; consultare il foglietto illustrativo) |
| Parametri da monitorare | Emocromo con formula, funzionalità epatica e renale, equilibrio acido-base |
| Protezione nella manipolazione | Necessarie le misure previste per la manipolazione dei farmaci citotossici |

---

## Considerazioni di sicurezza

**Controindicazioni/condizioni a rischio (dal grafo di conoscenza TxGNN, non dal foglietto illustrativo):** trombocitopenia, neutropenia, agranulocitosi, anemia (inclusa macrocitica), leucopenia, malattia polmonare interstiziale, fibrosi polmonare (anche post-infiammatoria), compromissione della funzione renale, acidosi (inclusa metabolica), danno epatico indotto da farmaci.

**Interazioni farmacologiche** (100 interazioni totali rilevate; principali di livello moderato):
- Aprepitant, rolapitant (antiemetici)
- Metronidazolo, tinidazolo
- Eliglustat
- Rosuvastatina, simvastatina

Sono presenti anche interazioni minori (levofloxacina) e di livello non noto (per es. calcitriolo, vitamina A, doxiciclina, cimetidina, amfotericina B, morfina).

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo AIFA, non disponibile nei dati compilati.

---

## Conclusione e prossimi passi

**Decisione: Proceed with Guardrails**

**Motivazione:**
- Per il sarcoma di Ewing esistono più RCT di fase 3 (evidenza L1) e raccomandazioni di consenso che includono regimi con etoposide: l'uso è già standard di cura.
- Le altre indicazioni previste sono per lo più supportate solo da case report o da estrapolazione (Hold); il rabdomiosarcoma generale è L1 ma con contributo dell'etoposide non isolato.

**Per procedere sono necessari:**
- Avvertenze e controindicazioni ufficiali dal foglietto illustrativo AIFA (lacuna bloccante per lo screening di sicurezza)
- Dati dettagliati sul meccanismo d'azione (MOA) da DrugBank
- Chiarimento dello stato regolatorio in Italia (autorizzazioni attualmente revocate; verificare formulazioni alternative disponibili)
- Piano di monitoraggio: mielosoppressione, rischio di leucemia secondaria, dosaggio e schedula adeguati all'età
- Utilizzo in protocolli specializzati di oncologia pediatrica
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

