---
layout: default
title: Isotretinoin
parent: Solo previsione del modello (L5)
nav_order: 246
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Isotretinoin"
predicted_indications: ["malignant hypertensive renal disease"]
description: "Isotretinoin: nuova indicazione prevista, Malattia renale ipertensiva maligna (malignant hypertensive renal disease) (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Isotretinoin
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **1** 
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

## Isotretinoin: Malattia renale ipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Riepilogo in una frase

Il modello TxGNN prevede un possibile effetto sulla **malattia renale ipertensiva maligna** (punteggio 0,9901), ma a oggi sono disponibili **0 studi clinici** e **0 pubblicazioni** a supporto: si tratta di una predizione puramente computazionale.

---

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Malattia renale ipertensiva maligna (malignant hypertensive renal disease) |
| Punteggio di predizione TxGNN | 0.9901 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 15 su 15) |
| Numero di autorizzazioni | 15 (valide: 15) |
| Decisione raccomandata | Hold |

---

## Perché questa predizione potrebbe essere ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. L'isotretinoina è un retinoide utilizzato principalmente nell'acne grave, e le indicazioni ipertensive registrate nel grafo di conoscenza non rappresentano usi clinici stabiliti.

Il segnalamento dei retinoidi è stato studiato in ambito renale e vascolare (ad esempio effetti sui podociti, sull'espressione della renina e sul rimodellamento vascolare), ma si tratta di ipotesi speculative non supportate dai dati compilati per questo report.

Va inoltre osservato che anche la seconda indicazione prevista (ipertensione renovascolare maligna) ha lo stesso identico punteggio (0,9901). Nessun legame meccanicistico può quindi essere verificato.

---

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

---

## Evidenze dalla letteratura

Attualmente non risulta disponibile letteratura correlata.

---

## Informazioni sul mercato italiano

Si elencano le prime 5:

<!-- review:begin it-lic-20261106-isotretinoin-1 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «Tutte le 15 autorizzazioni risultano cancellate; il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati. Si elencano le prime 5:» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). Nei dati (AIFA, elenco delle confezioni autorizzate) risultano 15 autorizzazioni per questo farmaco, di cui 15 valide; i numeri aggiornati sono nella panoramica rapida e nelle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-isotretinoin-1 -->

| Numero di autorizzazione | Nome del prodotto | Titolare | Stato |
|---------|------|------|-----------|
| 051504013 | Isotretinoina 30 cps molli 10 mg | DOC Generici Srl | Valida |
| 035258021 | Aisoskin 30 cps molli 20 mg | Fidia Farmaceutici SpA | Valida |
| 041853072 | Isdiben 30 cps molli 20 mg | ISDIN Srl | Valida |
| 041853045 | Isdiben 30 cps molli 10 mg | ISDIN Srl | Valida |
| 037551076 | Isoriac 30 cps molli 20 mg | Pierre Fabre Italia SpA | Valida |

---

## Considerazioni sulla sicurezza

- **Controindicazioni derivate dal grafo di conoscenza** (non provenienti dal foglio illustrativo): tra le condizioni associate figurano malattia renale, malattia epatica, pancreatite, malattie della colecisti, angioedema (incluse le forme ereditarie e acquisite), malattia infiammatoria intestinale, osteoporosi, lupus eritematoso sistemico, disturbi psicotici e mentali (inclusi ansia e disturbi distimici), diabete mellito e chetoacidosi diabetica, neutropenia e agranulocitosi, carenza di potassio, ipotensione. Molte di queste condizioni sono rilevanti in pazienti con malattia renale e cardiovascolare.
- **Interazioni farmacologiche**: sono registrate 98 interazioni. Tra quelle di livello **maggiore** figurano tetracicline (doxiciclina, minociclina, tetraciclina) e vitamina A. Tra quelle di livello **moderato** si segnalano corticosteroidi (betametasone, budesonide, desametasone, idrocortisone, prednisolone, prednisone, triamcinolone), warfarin e dicumarolo, etanolo, naltrexone, nitisinone, fostamatinib, ivacaftor, lumacaftor e abametapir.
- **Profilo generale noto**: teratogenicità, effetti epatici e sui lipidi, insieme all'elevato numero di interazioni, rappresentano ulteriori preoccupazioni in una popolazione con patologie renali e cardiovascolari.

Per avvertenze e controindicazioni ufficiali fare riferimento al foglio illustrativo, che non è stato ottenuto per questo report.

---

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Il profilo di sicurezza (teratogenicità, effetti epatici e lipidici, molte interazioni) sconsiglia di procedere senza dati a supporto.

**Per procedere sarebbe necessario:**
- Scaricare e analizzare il foglio illustrativo AIFA per avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Ottenere i dati sul meccanismo d'azione (ad esempio da DrugBank) per valutare un legame meccanicistico
- Verificare e correggere le indicazioni originali registrate nel grafo di conoscenza
- Condurre una revisione sistematica della letteratura preclinica sul segnalamento dei retinoidi nel rene e nel sistema renina-angiotensina

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-06 | Rimosso: «Tutte le 15 autorizzazioni risultano cancellate; il testo delle indicazioni approvate e la forma farmaceutica non sono riportati nei dati» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

