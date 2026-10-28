---
layout: default
title: Scopolamine
parent: Solo previsione del modello (L5)
nav_order: 400
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "Scopolamine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "atopic conjunctivitis", "rosacea conjunctivitis", "vernal conjunctivitis"]
description: "Scopolamine: nuova indicazione prevista, Sindrome della cauda equina (cauda equina syndrome) (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
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

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. È noto che la scopolamina è un antagonista muscarinico non selettivo: i dati farmacologici la mostrano attiva sui recettori M1, M2, M3, M4 e M5, con effetti anche sul sistema nervoso centrale.

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

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 006979037 | BUSCOPAN 6 fiale IM EV 20 mg 1 ml (OPELLA HEALTHCARE ITALY Srl) | Non indicata | Non indicata (autorizzazione valida) |

## Considerazioni sulla sicurezza

I dati compilati non contengono avvertenze o controindicazioni tratte dal foglietto illustrativo. Sono disponibili le seguenti informazioni:

- **Controindicazioni segnalate dal grafo di conoscenza** (non derivanti dal testo dell'etichetta): ipertensione, insufficienza epatica e malattie epatiche, coma epatico, epilessia, broncopneumopatia cronica ostruttiva, ulcera gastrica, disturbi d'ansia e nevrotici, disturbo distimico, porfiria, malattie renali, piouretere, pancreatite, malattie della colecisti, trombocitopenia, neutropenia e agranulocitosi, glaucoma ad angolo aperto, disturbi psicotici (inclusi schizoaffettivo e schizofreniforme) e altri disturbi mentali, diabete mellito e chetoacidosi diabetica, iperplasia prostatica benigna.
- **Interazioni**: i dati disponibili riguardano solo il legame con i recettori muscarinici M1–M5; non sono state identificate interazioni con altri farmaci.
- **Rilievi specifici per le nuove indicazioni**: gli effetti anticolinergici (ritenzione urinaria, sedazione, confusione, secchezza delle fauci, midriasi, visione offuscata, ridotta lacrimazione) sono rilevanti soprattutto per la sindrome della cauda equina e per le patologie congiuntivali.

Per le informazioni complete sulla sicurezza, consultare il foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si basa solo sul modello computazionale (L5), senza studi né pubblicazioni. Il razionale meccanicistico è debole o addirittura sfavorevole: gli anticolinergici possono peggiorare la ritenzione urinaria nella sindrome della cauda equina. Inoltre l'unica autorizzazione italiana è revocata.

**Per procedere sarebbe necessario:**
- Reperire e analizzare il foglietto illustrativo AIFA (avvertenze e controindicazioni), attualmente un blocco per lo screening di sicurezza
- Ottenere i dati sul meccanismo d'azione da DrugBank
- Condurre una revisione sistematica della letteratura e una ricerca di studi per la sindrome della cauda equina e per la vescica neurogena
- Valutare se l'indicazione più plausibile (vescica neurogena) sia davvero preferibile alle alternative antimuscariniche selettive già disponibili
- Verificare la compatibilità di via di somministrazione e formulazione, oggi non valutata
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

