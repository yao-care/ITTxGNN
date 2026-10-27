---
layout: default
title: Amiloride
parent: Solo previsione del modello (L5)
nav_order: 38
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Amiloride: nuova indicazione prevista, Ipertensione renovascolare maligna (livello di evidenza L5). Indicazione originale: Ipertensione, scompenso cardiaco congestizio (dal grafo di conoscenza"
monitor_inn: "amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Amiloride
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

## Amiloride: dall'ipertensione alla ipertensione renovascolare maligna
{: .text-alpha }

## Sintesi in una frase

L'amiloride è un diuretico risparmiatore di potassio, originariamente usato per ipertensione e scompenso cardiaco congestizio. Il modello TxGNN prevede che possa essere efficace per la **ipertensione renovascolare maligna**, ma per questa indicazione **non risultano studi clinici** e l'unico articolo reperito riguarda l'ipertensione mineralcorticoide, quindi il supporto è solo indiretto.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Ipertensione, scompenso cardiaco congestizio (dal grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Ipertensione renovascolare maligna |
| Punteggio di predizione TxGNN | 99,82% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate |
| Numero di autorizzazioni | 1 (revocata) |
| Decisione raccomandata | Hold |

## Perché questa predizione è plausibile?

I dati compilati per questo report non contengono una descrizione dettagliata del meccanismo d'azione. In base alle informazioni disponibili, l'amiloride blocca i canali epiteliali del sodio (ENaC) nel nefrone distale, riducendo il riassorbimento di sodio e abbassando la pressione arteriosa, con effetto risparmiatore di potassio.

Il legame con l'ipertensione renovascolare maligna è plausibile ma indiretto: questa forma è guidata dall'attivazione del sistema renina-angiotensina-aldosterone, e l'amiloride è consolidata nell'ipertensione correlata ai mineralcorticoidi. L'unico articolo recuperato (Nussberger, 2003) è una revisione sull'ipertensione mineralcorticoide, non sull'ipertensione renovascolare maligna.

Il punteggio elevato riflette quindi probabilmente la sovrapposizione con l'indicazione antipertensiva già approvata, più che prove dirette per la nuova indicazione.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Revisione | J Hypertens Suppl | Come indagare l'ipertensione mineralcorticoide: causa più frequente è l'aldosteronismo primario, con ipokaliemia e bassa attività reninica. Non riguarda direttamente l'ipertensione renovascolare maligna |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 023070016 | MODURETIC*20 cpr 5 mg + 50 mg (NEOPHARMED GENTILI SpA) | Non indicata | Non indicata (autorizzazione revocata) |

## Considerazioni sulla sicurezza

- **Controindicazioni (dal grafo di conoscenza, non dal foglietto illustrativo)**: malattia renale, anuria, nefropatia diabetica, diabete mellito e chetoacidosi diabetica, carenza di potassio, malattie epatiche, encefalopatia/coma epatico, gotta e iperuricemia, acidosi (incluse acidosi lattica acquisita), pancreatite, malattie della colecisti, lupus eritematoso sistemico, iperparatiroidismo, osteite fibrosa, ittero neonatale, piureter.
- **Interazioni farmacologiche**: sono segnalate 136 interazioni. Tra quelle di livello moderato: idrocortisone, betametasone, desametasone, budesonide, metformina, bupropione, inibitori SGLT2 (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), exenatide, dronabinolo, bisacodile, lattulosio, lattitolo, glicerina e olio di ricino. Tra quelle minori: doxiciclina, amoxicillina, cimetidina.
- **Rischio di iperkaliemia**: rilevante soprattutto in caso di insufficienza renale e con farmaci interagenti, in particolare nella ipertensione renale maligna.

Per avvertenze e controindicazioni ufficiali, consultare il foglietto illustrativo.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
L'evidenza è solo di livello L5 (predizione del modello): nessuno studio clinico, un solo articolo non pertinente, e il prodotto italiano ha solo autorizzazione revocata. Il rischio di iperkaliemia nei pazienti con compromissione renale è un ulteriore freno.

**Per procedere sono necessari:**
- Dati del foglietto illustrativo AIFA su avvertenze e controindicazioni
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Studi preclinici e clinici mirati sull'ipertensione renovascolare maligna
- Piano di monitoraggio di potassio e funzione renale

## Altre indicazioni previste (riepilogo)

| Indicazione prevista | Punteggio TxGNN | Livello di evidenza | Raccomandazione |
|------|------|------|------|
| Malattia renale ipertensiva maligna | 99,82% | L5 | Hold |
| Ipertensione polmonare da malattia polmonare e/o ipossia | 99,81% | L4 | Domanda di ricerca (ipotesi preclinica su ENaC e ASIC1a, nessuno studio clinico) |
| Ipertensione polmonare con meccanismo multifattoriale non chiaro | 99,81% | L5 | Hold |
| Sindrome di Braddock | 99,75% | L5 | Hold |
| Cuore polmonare cronico | 99,68% | L3 | Domanda di ricerca (studi del 1987-1991 sullo scompenso cardiaco in generale, evidenza indiretta) |
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

