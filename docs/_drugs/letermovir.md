---
layout: default
title: Letermovir
parent: Solo previsione del modello (L5)
nav_order: 261
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Letermovir: nuova indicazione prevista, Candidosi vulvovaginale (livello di evidenza L5). Indicazione originale: Infezione da citomegalovirus"
monitor_inn: "LETERMOVIR"
predicted_indications: ["vulvovaginal candidiasis"]
---

# Letermovir
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

## Letermovir: Da infezione da citomegalovirus a candidosi vulvovaginale
{: .text-alpha }

## Riepilogo in una frase

Letermovir è un antivirale originariamente utilizzato per l'infezione da citomegalovirus (CMV). Il modello TxGNN prevede una possibile efficacia nella **candidosi vulvovaginale**, ma al momento non risultano **studi clinici** né **pubblicazioni** a supporto: la previsione si basa esclusivamente sul modello computazionale.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Infezione da citomegalovirus |
| Nuova indicazione prevista | Candidosi vulvovaginale |
| Punteggio di previsione TxGNN | 0,9988 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 2 su 2) |
| Numero di autorizzazioni | 2 (valide: 2) |
| Decisione raccomandata | Hold |

## Perché questa previsione è ragionevole?

Allo stato attuale i dati dettagliati sul meccanismo d'azione non sono disponibili nei dati compilati per questo report. Letermovir è noto come inibitore del complesso terminasi del DNA del CMV (pUL56/pUL51/pUL89), un bersaglio specifico dei herpesvirus.

**Non è stato identificato un collegamento meccanicistico credibile** con la candidosi vulvovaginale. Candida è un fungo e per questo bersaglio virale non è noto alcun omologo. Non sono disponibili dati di attività antifungina in vitro né osservazioni cliniche che supportino la previsione.

Il punteggio molto elevato (0,9988) proviene dal modello TxGNN (deep learning) e può riflettere similarità apprese dal modello tra malattie correlate, non evidenza biologica; va quindi interpretato con cautela.

## Evidenze da studi clinici

Attualmente non risultano studi clinici correlati registrati.

## Evidenze dalla letteratura

Attualmente non risulta alcuna letteratura correlata disponibile.

<!-- review:begin it-lic-20261106-letermovir-1 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «Entrambe le autorizzazioni (titolare: Merck Sharp & Dohme BV) risultano cancellate; non vi sono autorizzazioni attualmente valide.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). Nei dati (AIFA, elenco delle confezioni autorizzate) risultano 2 autorizzazioni per questo farmaco, di cui 2 valide; i numeri aggiornati sono nella panoramica rapida e nelle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-letermovir-1 -->

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 045890023 | PREVYMIS 28x1 cpr rivestite 480 mg | Compresse rivestite | Non disponibile |
| 045890011 | PREVYMIS 28x1 cpr rivestite 240 mg | Compresse rivestite | Non disponibile |

## Considerazioni sulla sicurezza

I dati su avvertenze e controindicazioni non sono disponibili; si rimanda al foglio illustrativo per le informazioni complete.

**Interazioni farmacologiche**: dalla ricerca sono emerse 100 interazioni; le principali tra quelle elencate:

- **Gravi (Major)**: eliglustat, naloxegol, cisapride
- **Moderate**: idrocortisone, desametasone, betametasone, triamcinolone, budesonide (anche nasale), pioglitazone, aprepitant, omeprazolo, lansoprazolo, claritromicina, saxagliptin, glimepiride, clorpropamide, acetoexamide, naldemedina, nitisinone

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione si fonda solo sul modello (livello L5), senza studi clinici, letteratura o razionale meccanicistico credibile. Letermovir agisce su un bersaglio virale privo di omologhi noti nei funghi.

<!-- review:begin it-lic-20261106-letermovir-2 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «Letermovir agisce su un bersaglio virale privo di omologhi noti nei funghi, e in Italia le autorizzazioni sono attualmente cancellate.» Rimosso: l'affermazione che le autorizzazioni fossero revocate, annullate o non valide non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). Nei dati (AIFA, elenco delle confezioni autorizzate) risultano 2 autorizzazioni per questo farmaco, di cui 2 valide; i numeri aggiornati sono nella panoramica rapida e nelle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-letermovir-2 -->

**Per procedere sono necessari:**
- Dati sul meccanismo d'azione (MOA) da DrugBank
- Dati di attività antifungina in vitro contro *Candida* spp.
- Avvertenze e controindicazioni dal foglio illustrativo AIFA
- Verifica della compatibilità delle vie di somministrazione (per una candidosi vulvovaginale sarebbe rilevante una via locale)
- Chiarimento dello stato regolatorio in Italia

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-06 | Rimosso: «Entrambe le autorizzazioni (titolare: Merck Sharp & Dohme BV) risultano cancellate; non vi sono autorizzazioni attualmente valide» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |
| 2026-11-06 | Rimosso: «e in Italia le autorizzazioni sono attualmente cancellate» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

