---
layout: default
title: Teriparatide
parent: Solo previsione del modello (L5)
nav_order: 430
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "TERIPARATIDE"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
description: "Teriparatide: nuova indicazione prevista, Ulcera duodenale (duodenal ulcer (disease)) (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Teriparatide
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

## Teriparatide: Ulcera duodenale (duodenal ulcer (disease))
{: .text-alpha }

## Sintesi in una frase

Teriparatide è un analogo del paratormone (frammento PTH 1-34) usato per trattare l'osteoporosi, in particolare quella postmenopausale, nei pazienti ad alto rischio di frattura.
Il modello TxGNN lo indica come possibile candidato per l'**ulcera duodenale** con un punteggio molto alto, ma **senza alcuno studio clinico né pubblicazione** a supporto.
Si tratta quindi di una previsione puramente computazionale, priva di un razionale biologico evidente.

---

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Ulcera duodenale (duodenal ulcer (disease)) |
| Punteggio di previsione TxGNN | 0.9986 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: 10 su 10) |
| Numero di autorizzazioni | 10 (valide: 10) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è ragionevole?

Teriparatide è un analogo del paratormone umano (PTH 1-34). Agisce come agonista del recettore PTH1 (PTH1R) e, secondo i dati di farmacologia compilati, interagisce anche con il recettore PTH2. Con somministrazione intermittente esercita un'azione anabolica sull'osso, aumentando la formazione ossea e la densità minerale ossea. Una descrizione dettagliata e formale del meccanismo d'azione non è disponibile nei dati compilati per questo report.

Il legame con l'ulcera duodenale non è plausibile. L'osteoporosi è una malattia del rimodellamento osseo, mentre l'ulcera duodenale è un danno della mucosa gastrointestinale, e non emerge alcun collegamento tra la segnalazione di PTH1R e la fisiopatologia dell'ulcera. L'analisi condotta sui dati disponibili conclude che non c'è un razionale meccanicistico evidente.

L'elevato punteggio TxGNN (posizione 1153 nella classifica globale) deriva dal modello TxGNN (deep learning) e può riflettere somiglianze apprese dal modello tra malattie correlate, non un'evidenza biologica o clinica. Va considerato solo un segnale di partenza, da verificare.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati.

---

## Evidenze dalla letteratura

Al momento non risulta letteratura correlata.

---

## Informazioni sul mercato italiano

Si riportano le prime 5.

| Numero di autorizzazione | Nome del prodotto | Titolare |
|---------|------|------|
| 050007018 | SONDELBAY penna 2,4 ml SC 20 mcg/80 mcl | Accord Healthcare SLU |
| 045257033 | TERROSA cartuccia + penna 2,4 ml 20 mcg/80 mcl | Gedeon Richter Plc |
| 045257045 | TERROSA penna preriempita SC 2,4 ml 20 mcg/80 mcl | Gedeon Richter Plc |
| 045256031 | MOVYMIA cartuccia SC 2,4 ml 20 mcg/80 mcl + penna | Stada Arzneimittel AG |
| 035926017 | FORSTEO penna SC 2,4 ml 20 mcg/80 mcl | Eli Lilly Nederland BV |

---

## Considerazioni sulla sicurezza

Il testo delle controindicazioni e delle avvertenze del foglio illustrativo AIFA non è disponibile nei dati compilati; per questi aspetti si rimanda al foglio illustrativo.

- **Controindicazioni derivate dal grafo di conoscenza** (non provengono dal testo del foglio illustrativo): ipotensione, ipercalcemia, nefrocalcinosi, disturbi del metabolismo del fosforo, osteosarcoma osseo, malattia di Paget ossea, malattia di Paget giovanile, osteomalacia, rachitismo, urolitiasi, osteodistrofia renale, osteite fibrosa e iperparatiroidismo.
- **Interazioni farmacologiche** (8 segnalazioni totali, di cui 6 con farmaci):
  - Moderate: calcitriolo (topico), calcipotriolo (topico), digossina, digitossina.
  - Minori: idroclorotiazide, furosemide.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
Per l'ulcera duodenale esistono solo una previsione del modello e nessuno studio clinico o pubblicazione. In più non si individua alcun razionale meccanicistico.

<!-- review:begin it-lic-20261106-teriparatide-1 -->

> **Correzione di verifica (2026-11-06)**: Testo originale: «In più non si individua alcun razionale meccanicistico, e il prodotto non ha autorizzazioni valide in Italia.» Rimosso: il numero o lo stato delle autorizzazioni indicato non corrispondeva ai dati delle autorizzazioni (AIFA, elenco delle confezioni autorizzate, al 2026-11-06). Nei dati (AIFA, elenco delle confezioni autorizzate) risultano 10 autorizzazioni per questo farmaco, di cui 10 valide; i numeri aggiornati sono nella panoramica rapida e nelle informazioni sul mercato. Fonte: [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv).

<!-- review:end it-lic-20261106-teriparatide-1 -->

**Per procedere sarebbe necessario:**
- Acquisire e analizzare il foglio illustrativo AIFA per avvertenze e controindicazioni, una lacuna che oggi impedisce la valutazione di sicurezza.
- Completare i dati sul meccanismo d'azione.
- Individuare un razionale biologico credibile ed evidenze precliniche prima di qualsiasi sperimentazione.

**Nota sulle altre previsioni:** tra le altre indicazioni previste, l'osteoporosi in amenorrea ipotalamica funzionale (L4) ha un legame indiretto, limitato alla complicanza ossea.

<!-- review:begin log -->

## Registro delle verifiche

Di seguito il registro delle verifiche di questa pagina: affermazioni controllate sui dati ufficiali delle autorizzazioni (AIFA, elenco delle confezioni autorizzate). Le correzioni riguardano solo dati di base; le previsioni del modello, i livelli di evidenza e le conclusioni non sono stati riscritti.

| Data di verifica | Voce | Intervento | Fonte |
|------|------|------|------|
| 2026-11-06 | Rimosso: «e il prodotto non ha autorizzazioni valide in Italia» | Corretto | [AIFA – Elenco confezioni (open data)](https://drive.aifa.gov.it/farmaci/confezioni.csv) |

<!-- review:end log -->

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

