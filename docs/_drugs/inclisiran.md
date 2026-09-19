---
layout: default
title: Inclisiran
parent: Solo previsione del modello (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: Da Ipercolesterolemia a Malformazione Aortica

## Riassunto in Una Frase

L'inclisiran è una siRNA diretta agli epatociti che silenzia l'espressione di PCSK9, originariamente sviluppata per abbassare il colesterolo LDL nei pazienti con ipercolesterolemia e rischio cardiovascolare elevato.
La previsione di TxGNN con il punteggio più elevato (malattia da carenza di potassio, 99.93%) è stata valutata come un probabile falso positivo privo di base meccanicistica; la previsione più clinicamente rilevante è **malformazione aortica** (rango 8, 99.76%), con **2 trial clinici di Fase 3 attivi** attualmente a supporto di questa direzione.

## Panoramica Rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione Originale | Ipercolesterolemia / riduzione di LDL-C (approvazione globale; non ancora registrato in Italia) |
| Indicazione Nuova Prevista | Malformazione Aortica (previsione con miglior evidenza, rango 8) |
| Punteggio di Previsione TxGNN | 99.76% |
| Livello di Evidenza | L1 (2 RCT di Fase 3 in corso di reclutamento) |
| Stato del Mercato Italiano | Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | Procedere con Salvaguardie |

## Perché Questa Previsione È Ragionevole?

I dati dettagliati sul meccanismo d'azione non erano disponibili in questo dossier probatorio. Sulla base delle informazioni note, l'inclisiran è una siRNA a doppio filamento che viene assunta selettivamente dagli epatociti tramite coniugazione con GalNAc, dove dirige il complesso di silenziamento indotto da RNA (RISC) a degradare l'mRNA di PCSK9. Riducendo la proteina PCSK9 epatica, i recettori LDL sulla superficie dell'epatocita vengono riciclati anziché degradati, determinando riduzioni sostenute di LDL-C di circa 50% con sole iniezioni sottocutanee due volte all'anno. Questo è farmacologicamente equivalente agli inibitori di anticorpi monoclonali contro PCSK9 (evolocumab, alirocumab) ma con una modalità di somministrazione fondamentalmente diversa.

**Una nota sul panorama completo delle previsioni**: La previsione più elevata di TxGNN (rango 1: malattia da carenza di potassio) è stata valutata dalla pipeline probatoria come un tipico falso positivo — il percorso metabolico PCSK9/LDL non ha alcuna intersezione meccanicistica nota con l'omeostasi del potassio renale o intestinale. Il punteggio elevato riflette i pattern di co-occorrenza strutturali del grafo nel network di conoscenza piuttosto che la plausibilità farmacologica. I ranghi 2–7 e 9–10 sono similmente non supportati (L5, In Sospeso), e i 20 articoli della letteratura recuperati per il rango 7 (suscettibilità all'emicrania) sono esclusivamente articoli di genetica dell'epilessia senza relazione con inclisiran.

Il rango 8 "malformazione aortica" rappresenta la previsione più azionabile dal punto di vista clinico. L'etichetta della malattia riflette probabilmente un artefatto di mappatura dell'ontologia: l'ipercolesterolemia familiare grave (HoFH/HeFH) causa cambiamenti ateromasici gravi e accelerati nell'aorta che possono registrarsi come patologia aortica strutturale nei sistemi di classificazione delle malattie. Meccanicisticamente, l'inibizione di PCSK9 è plausibile qui su molteplici basi: la riduzione sostanziale di LDL-C rallenta la progressione ateromasica nella parete aortica; la proteina PCSK9 è espressa nelle cellule interstiziali della valvola aortica, dove la sua inibizione può attenuare la segnalazione osteogenica mediata da BMP2/Wnt e la calcificazione; e il miglioramento della funzione endoteliale dalla ridotta circolazione di LDL-C può ridurre l'infiammazione della parete aortica.

## Evidenza Clinica da Trial

| Numero dello Studio | Fase | Stato | Arruolamento | Risultati Chiave |
|----------|------|-------|--------------|-----------------|
| [NCT06597006](https://clinicaltrials.gov/study/NCT06597006) | Fase 3 | In corso di reclutamento | 9 | Studio doppio-cieco di inclisiran vs. placebo (Anno 1) seguito da inclisiran in aperto (Anno 2) in bambini di età 2–<12 anni con ipercolesterolemia familiare omozigote (HoFH) e LDL-C elevato; valuta sicurezza, tollerabilità ed efficacia |
| [NCT06597019](https://clinicaltrials.gov/study/NCT06597019) | Fase 3 | In corso di reclutamento | 51 | Stesso disegno doppio-cieco/in aperto di NCT06597006; rivolto a bambini di età 6–<12 anni con ipercolesterolemia familiare eterozigote (HeFH) e LDL-C elevato; completamento previsto Aprile 2029 |

> **Attenzione**: Entrambi i trial sono ancora in corso di reclutamento con dimensioni campionarie ridotte (n=9 e n=51). L'etichetta della malattia "malformazione aortica" nella mappatura TxGNN richiede verifica rispetto ai reali endpoint primari dei trial — i trial si concentrano sull'ipercolesterolemia familiare, non sulla malformazione aortica strutturale per se. La confidenza nel rating L1 riflette la base di evidenza di Fase 3 consolidata di inclisiran negli adulti (programma ORION), non solo questi trial pediatrici.

## Considerazioni sulla Sicurezza

Si prega di consultare il foglio illustrativo per le informazioni sulla sicurezza.

## Conclusione e Prossimi Passi

**Decisione: Procedere con Salvaguardie**

**Razionale:**
Due trial di Fase 3 attivi testano direttamente inclisiran nell'ipercolesterolemia familiare pediatrica — una condizione con conseguenze aortiche e cardiovascolari ben documentate — e inclisiran possiede già l'approvazione EMA negli adulti, fornendo una base consolidata di sicurezza ed efficacia. Tuttavia, entrambi i trial pediatrici sono ancora in corso di reclutamento con arruolamento limitato, l'etichetta della malattia "malformazione aortica" richiede chiarimento ontologico, e l'autorizzazione normativa specifica per l'Italia non è ancora stata stabilita.

**Per procedere sono necessari i seguenti elementi:**

- **Chiarire la mappatura della malattia**: Confermare se "malformazione aortica" in TxGNN si mappa all'aterosclerosi aortica, alla calcificazione della valvola aortica, o alla patologia aortica strutturale correlata all'ipercolesterolemia familiare — questo determina se la previsione è un vero segnale di riposizionamento o una scoperta di estensione dell'indicazione
- **Ottenere i dati sul meccanismo d'azione**: Recuperare il record completo del meccanismo d'azione da DrugBank per inclisiran (Lacuna di Dati DG002) per supportare l'analisi del collegamento meccanicistico
- **Ottenere i dati di sicurezza**: Scaricare e analizzare il foglio illustrativo completo da EMA/AIFA (Lacuna di Dati DG001) per completare lo screening di sicurezza, inclusi profili di gravidanza/allattamento, insufficienza epatica e reazioni nel sito di iniezione
- **Monitorare il completamento dei trial**: Sia NCT06597006 che NCT06597019 hanno completamento stimato per Aprile 2029; i rilasci di dati interim dovrebbero essere tracciati
- **Percorso di registrazione in Italia**: L'inclisiran (Leqvio®) possiede approvazione EMA; la registrazione AIFA e la classificazione di rimborsabilità (Fascia A/H) dovrebbero essere valutate separatamente da questa analisi di riposizionamento
- **Rivalutare le previsioni rango 1–7**: È consigliato una seconda revisione della letteratura specificamente combinando "inclisiran" + ogni termine di malattia per confermare l'assenza di eventuali segnali emergenti, in particolare per l'emicrania (rango 4/6/7) data l'ipotesi teorica di espressione neuronale di PCSK9

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

