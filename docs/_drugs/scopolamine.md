---
layout: default
title: Scopolamine
parent: Solo previsione del modello (L5)
nav_order: 400
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Scopolamine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "atopic conjunctivitis", "rosacea conjunctivitis", "vernal conjunctivitis"]
description: "Scopolamine: nuova indicazione prevista, Sindrome della cauda equina (cauda equina syndrome) (livello di evidenza L5). In Italia, confezioni AIFA: 1 (autorizzate: 1)"
---

# Scopolamine
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **6** 
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

## Scopolamine: Sindrome della cauda equina (cauda equina syndrome)
{: .text-alpha }

## Sintesi

La scopolamina è un antimuscarinico non selettivo, originariamente impiegato per la cinetosi, la sindrome dell'intestino irritabile, l'ulcera peptica e diverse patologie oculari e delle vie respiratorie superiori. Il modello TxGNN ne prevede una possibile efficacia nella **sindrome della cauda equina**, ma questa previsione non è supportata da **nessuno studio clinico** né da **alcuna pubblicazione** nei dati compilati per questo report.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Sindrome della cauda equina (cauda equina syndrome) |
| Punteggio di previsione TxGNN | 0.9999 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 1 su 1) |
| Numero di autorizzazioni | 1 (valide: 1) |
| Decisione raccomandata | Hold (sospendere) |

## Perché questa previsione potrebbe essere plausibile?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Scopolamine (traduzione non ufficiale): «Scopolamina, un alcaloide della belladonna, è un anticolinergico. Scopolamina agisce: i) come inibitore competitivo a livello dei siti recettoriali muscarinici postgangliari del sistema nervoso parasimpatico, e ii) sui muscoli lisci che rispondono all'acetilcolina ma sono privi di innervazione colinergica.» Testo originale in inglese: "Scopolamine, a belladonna alkaloid, is an anticholinergic. Scopolamine acts: i) as a competitive inhibitor at postganglionic muscarinic receptor sites of the parasympathetic nervous system, and ii) on smooth muscles that respond to acetylcholine but lack cholinergic innervation." ([DailyMed: Transderm Scop (scopolamine) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b877a694-a1d0-4280-937a-a06820b12a88), versione del 2025-06-10; consultato il 2026-11-19). È noto che la scopolamina è un antagonista muscarinico non selettivo: i dati farmacologici la mostrano attiva sui recettori M1, M2, M3, M4 e M5, con effetti anche sul sistema nervoso centrale.

Il possibile legame teorico con la sindrome della cauda equina passa per la modulazione dell'attività del detrusore vescicale, cioè la riduzione di iperattività e urgenza nella disfunzione vescicale neurogena. Tuttavia, la sindrome della cauda equina è soprattutto un'emergenza chirurgica compressiva. Un antimuscarinico potrebbe al massimo agire su un sintomo urinario a valle, e potrebbe persino peggiorare la ritenzione urinaria, frequente in questa condizione.

Il punteggio molto alto di TxGNN è quindi solo una previsione computazionale, senza riscontro in studi o pubblicazioni.

### Altre indicazioni previste

Le altre cinque previsioni del modello hanno tutte livello di evidenza L5, senza studi né letteratura, e raccomandazione Hold:

| Posizione | Indicazione prevista | Punteggio | Osservazioni |
|------|------|------|------|
| 2 | Vescica neurogena (termine obsoleto) | 0,9998 | Il razionale è plausibile (blocco muscarinico del detrusore), ma la scopolamina ha forte penetrazione nel sistema nervoso centrale e scarsa tollerabilità nell'uso cronico; esistono alternative più selettive. Il termine è obsoleto nell'ontologia. |
| 3 | Congiuntivite papillare | 0,9998 | Patologia mediata da mastociti e istamina o da irritazione meccanica; gli antimuscarinici non agiscono sul meccanismo e possono causare midriasi, cicloplegia e secchezza oculare. |
| 4 | Congiuntivite atopica | 0,9980 | Malattia IgE- e mastocita-mediata; il blocco muscarinico non interviene su questa via. |
| 5 | Congiuntivite rosacea | 0,9940 | Nessun razionale meccanicistico chiaro; la riduzione della secrezione lacrimale potrebbe peggiorare la malattia della superficie oculare. |
| 6 | Congiuntivite vernale | 0,9908 | Malattia allergica cronica Th2; un beneficio sintomatico dalla cicloplegia sarebbe indiretto e speculativo. |

## Evidenze da studi clinici

Attualmente non risulta alcuno studio clinico registrato correlato.

## Evidenze dalla letteratura

Attualmente non è disponibile alcuna letteratura correlata.

## Informazioni sul mercato italiano

<!-- licenses:begin -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|------|------|------|------|
| 006979037 | BUSCOPAN\*6 fiale IM EV 20 mg 1 ml | OPELLA HEALTHCARE ITALY Srl | Autorizzata |

Fonte: AIFA, elenco delle confezioni autorizzate (open data), stato amministrativo; confezioni autorizzate per prime.

<!-- licenses:end -->

## Considerazioni sulla sicurezza

I dati compilati non contengono avvertenze o controindicazioni tratte dal foglietto illustrativo. Sono disponibili le seguenti informazioni:

- **Controindicazioni segnalate dal grafo di conoscenza** (non derivanti dal testo dell'etichetta): ipertensione, insufficienza epatica e malattie epatiche, coma epatico, epilessia, broncopneumopatia cronica ostruttiva, ulcera gastrica, disturbi d'ansia e nevrotici, disturbo distimico, porfiria, malattie renali, piouretere, pancreatite, malattie della colecisti, trombocitopenia, neutropenia e agranulocitosi, glaucoma ad angolo aperto, disturbi psicotici (inclusi schizoaffettivo e schizofreniforme) e altri disturbi mentali, diabete mellito e chetoacidosi diabetica, iperplasia prostatica benigna.
- **Interazioni**: i dati disponibili riguardano solo il legame con i recettori muscarinici M1–M5; non sono state identificate interazioni con altri farmaci.
- **Rilievi specifici per le nuove indicazioni**: gli effetti anticolinergici (ritenzione urinaria, sedazione, confusione, secchezza delle fauci, midriasi, visione offuscata, ridotta lacrimazione) sono rilevanti soprattutto per la sindrome della cauda equina e per le patologie congiuntivali.

Per le informazioni complete sulla sicurezza, consultare il foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul modello computazionale (L5), senza studi né pubblicazioni. Il razionale meccanicistico è debole o addirittura sfavorevole: gli anticolinergici possono peggiorare la ritenzione urinaria nella sindrome della cauda equina.

<!-- review:begin it-lic-20261106-scopolamine-1 -->

> **Correzione di verifica (2026-11-24)**: Testo originale: «Il razionale meccanicistico è debole o addirittura sfavorevole: gli anticolinergici possono peggiorare la ritenzione urinaria nella sindrome della cauda equina. Inoltre l'unica autorizzazione italiana è revocata.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). I numeri aggiornati delle autorizzazioni sono nella panoramica rapida e nella tabella delle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-scopolamine-1 -->

**Per procedere sarebbe necessario:**
- Reperire e analizzare il foglietto illustrativo AIFA (avvertenze e controindicazioni), attualmente un blocco per lo screening di sicurezza
- Ottenere i dati sul meccanismo d'azione da DrugBank
- Condurre una revisione sistematica della letteratura e una ricerca di studi per la sindrome della cauda equina e per la vescica neurogena
- Valutare se l'indicazione più plausibile (vescica neurogena) sia davvero preferibile alle alternative antimuscariniche selettive già disponibili
- Verificare la compatibilità di via di somministrazione e formulazione, oggi non valutata

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale).

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-24 | Rimosso: «Inoltre l'unica autorizzazione italiana è revocata» | Corretto (rivisto il 2026-11-24; versione precedente conservata nel registro) | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: Transderm Scop (scopolamine) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b877a694-a1d0-4280-937a-a06820b12a88) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

