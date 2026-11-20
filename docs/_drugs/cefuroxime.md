---
layout: default
title: Cefuroxime
parent: Solo previsione del modello (L5)
nav_order: 99
evidence_level: L5
indication_count: 8
monitor_inn: "Cefuroxime"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy"]
last_modified_at: 2026-11-20
description: "Cefuroxime: nuova indicazione prevista, Sindrome da iperviscosità policlonale (polyclonal hyperviscosity syndrome) (livello di evidenza L5). In Italia, confezioni AIFA: 14 (autorizzate: 12)"
---

# Cefuroxime
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **8** 
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

## Cefuroxima: cefalosporina di seconda generazione → sindrome da iperviscosità policlonale (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Sintesi

Cefuroxima è una cefalosporina di seconda generazione, antibiotico che inibisce la sintesi della parete cellulare batterica.
Il modello TxGNN la associa come principale predizione alla **sindrome da iperviscosità policlonale (polyclonal hyperviscosity syndrome)**, con un punteggio molto alto (0,9976), ma **senza alcuno studio clinico e senza pubblicazioni** a sostegno di questa direzione.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Sindrome da iperviscosità policlonale (polyclonal hyperviscosity syndrome) |
| Punteggio di predizione TxGNN | 0,9976 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 12 su 14) |
| Numero di autorizzazioni | 14 (valide: 12) |
| Decisione raccomandata | Hold |

## Perché questa predizione potrebbe (o non potrebbe) essere ragionevole?

Secondo la sezione «Mechanism of Action» delle informazioni di prescrizione approvate dalla FDA statunitense (Prescribing Information) per Cefuroxime (traduzione non ufficiale): «Cefuroxima è un agente battericida che agisce inibendo la sintesi della parete cellulare batterica. Cefuroxima è attiva in presenza di alcune beta-lattamasi, sia penicillinasi sia cefalosporinasi, di batteri Gram-negativi e Gram-positivi.» Testo originale in inglese: "Cefuroxime is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Cefuroxime has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: cefuroxime sodium prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a145288-733a-4966-b7ae-dc96eb103d8c), versione del 2025-03-27; consultato il 2026-11-19). In base alle conoscenze generali, si tratta di una cefalosporina di seconda generazione con attività antibatterica, basata sull'inibizione della sintesi della parete cellulare.

La sindrome da iperviscosità policlonale è invece un disturbo reologico legato a un eccesso di proteine/immunoglobuline nel sangue. Non si individua un collegamento meccanicistico plausibile tra un antibatterico e una condizione di questo tipo. Il punteggio elevato deriva da un'associazione calcolata dal modello e non è supportato da evidenze cliniche o bibliografiche. Per questo motivo la predizione va considerata, allo stato attuale, solo un'ipotesi computazionale.

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati.

## Evidenze dalla letteratura

Al momento non è disponibile letteratura correlata.

## Informazioni sul mercato italiano

Nei dati compilati per questo report risultano 14 autorizzazioni a medicinali monocomponente a base di cefuroxima. Per questi prodotti il testo dell'indicazione approvata non è riportato nei dati locali.

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 037732308 | CEFUROXIMA 6 cpr rivestite 500 mg (Sandoz) | Compresse rivestite | Non registrata |
| 026915025 | ZINNAT 12 cpr rivestite 250 mg (Sandoz) | Compresse rivestite | Non registrata |
| 027002029 | ORAXIM 12 cpr rivestite 250 mg (Malesci) | Compresse rivestite | Non registrata |
| 026915037 | ZINNAT 6 cpr rivestite 500 mg (Sandoz) | Compresse rivestite | Non registrata |
| 023576022 | CUROXIM 1 flacone IM 500 mg + 1 fiala solvente 2 ml (Sandoz) | Flacone + solvente per uso intramuscolare | Non registrata |

## Considerazioni sulla sicurezza

Per la sicurezza si rimanda al foglio illustrativo: nei dati compilati non sono disponibili avvertenze o controindicazioni tratte dal testo autorizzato.

**Interazioni farmacologiche** (livello moderato, 100 interazioni complessive; principali segnalate):
- Antiacidi e farmaci che riducono l'acidità gastrica: famotidina, ranitidina, cimetidina, nizatidina, omeprazolo, esomeprazolo, lansoprazolo, dexlansoprazolo, pantoprazolo, rabeprazolo, idrossido di alluminio, carbonato di calcio, composti del magnesio, magaldrato
- Aminoglicosidi: kanamicina, neomicina
- Balsalazide

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La predizione principale non ha studi clinici né pubblicazioni a supporto, né un razionale meccanicistico plausibile; il livello di evidenza è L5, basato solo sul modello.

**Per procedere sarebbe necessario:**
- Dati sul meccanismo d'azione e un razionale biologico credibile per l'iperviscosità policlonale
- Studi preclinici o clinici che esaminino direttamente questa patologia
- Avvertenze e controindicazioni dal foglio illustrativo AIFA
- Verifica dello stato attuale delle autorizzazioni e della disponibilità dei prodotti in Italia

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina. La frase secondo cui non erano disponibili dati sul meccanismo d'azione è stata sostituita da un estratto delle informazioni di prescrizione ufficiali citate (con traduzione non ufficiale); le predizioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase «dati sul meccanismo d'azione non disponibili» sostituita da un estratto del foglietto statunitense | Frase sull'assenza di dati sul meccanismo d'azione sostituita da un estratto con fonte | [DailyMed: cefuroxime sodium prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a145288-733a-4966-b7ae-dc96eb103d8c) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

