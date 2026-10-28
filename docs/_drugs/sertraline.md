---
layout: default
title: Sertraline
parent: Solo previsione del modello (L5)
nav_order: 402
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "Sertraline"
predicted_indications: ["schizoid personality disorder", "paranoid personality disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "benign paroxysmal torticollis of infancy", "agoraphobia", "dependent personality disorder", "narcissistic personality disorder"]
description: "Sertraline: nuova indicazione prevista, Schizoid personality disorder (livello di evidenza L5). Indicazione originale: Non riportata nei dati locali"
---

# Sertraline
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

## Sertraline: Schizoid personality disorder
{: .text-alpha }

## Riepilogo in una frase

La sertralina è un inibitore selettivo della ricaptazione della serotonina (SSRI), originariamente usato per disturbi d'ansia, disturbo ossessivo-compulsivo, disturbo da stress post-traumatico e fobia sociale.
Il modello TxGNN prevede un possibile effetto sul **disturbo schizoide di personalità**, ma i dati compilati per questo report non includono **nessuno studio clinico** e solo **1 pubblicazione**, non pertinente a questa condizione: la previsione resta puramente computazionale.

---

## Quadro di sintesi

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non riportata nei dati locali |
| Nuova indicazione prevista | Schizoid personality disorder |
| Punteggio di predizione TxGNN | 0.9993 |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | In commercio (autorizzazioni valide: almeno 20) |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

---

## Perché questa previsione è ragionevole?

Al momento non sono disponibili dati dettagliati sul meccanismo d'azione. In base alle informazioni note, la sertralina è un SSRI che agisce sul trasportatore della serotonina (SERT, gene SLC6A4), e la sua efficacia nei disturbi d'ansia e fobici è consolidata.

Il legame con il disturbo schizoide di personalità non è però supportato dai dati. L'unica pubblicazione associata (PMID 19794312) riguarda il disturbo da alimentazione incontrollata (binge-eating), non il disturbo schizoide. Il punteggio TxGNN elevato riflette probabilmente la vicinanza nella rete di conoscenza ad altre condizioni psichiatriche trattate con farmaci serotoninergici, più che una reale plausibilità clinica.

Nota: nello stesso gruppo di previsioni con punteggio identico compaiono anche i disturbi paranoide, schizotipico e istrionico di personalità. Tra le altre previsioni, l'**agorafobia** ha l'evidenza più solida (livello L2, numerosi studi sulla sertralina nel disturbo di panico con o senza agorafobia, tra cui trial in doppio cieco e network meta-analisi). Si tratta però in gran parte di un'estensione di indicazioni ansiose già esistenti, e sarebbe il candidato più sensato per un approfondimento.

---

## Evidenze da studi clinici

Al momento non risultano studi clinici registrati correlati a questa indicazione.

---

## Evidenze dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [19794312](https://pubmed.ncbi.nlm.nih.gov/19794312/) | 2009 | Altro (studio di trattamento multimodale) | International Clinical Psychopharmacology | Studio su 30 pazienti con binge-eating disorder, assegnati a dieta, terapia cognitivo-comportamentale e sertralina in tre gruppi per 6 mesi. Non riguarda il disturbo schizoide di personalità. |

---

## Informazioni sul mercato italiano

Il testo delle indicazioni approvate e la forma farmaceutica non sono disponibili nei dati compilati. Di seguito le principali (prime 5):

| Numero di autorizzazione | Nome prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 036803017 | Sertralina 30 cpr rivestite 50 mg (EG SpA) | Compresse rivestite | Non disponibile |
| 042398040 | Sertralina 30 cpr rivestite 100 mg (Tecnimede) | Compresse rivestite | Non disponibile |
| 027754086 | Tatig 30 cpr rivestite div 50 mg (Viatris Pharma) | Compresse rivestite | Non disponibile |
| 036764049 | Sertralina 30 cpr rivestite 100 mg (DOC Generici) | Compresse rivestite | Non disponibile |
| 027753096 | Zoloft soluzione orale 60 ml 20 mg/ml (Viatris Pharma) | Soluzione orale | Non disponibile |

---

## Considerazioni di sicurezza

- **Condizioni associate a controindicazione (dal grafo di conoscenza, non dal foglio illustrativo)**: epilessia, disturbo bipolare, disturbo affettivo maggiore, malattie epatiche, malattie della colecisti, disturbi della coagulazione, sindrome neurolettica maligna, sindrome da inappropriata secrezione di ADH, sindrome nefrogenica da inappropriata antidiuresi, sindrome serotoninergica.
- **Interazioni**: la ricerca ha restituito solo l'interazione farmacologica con il bersaglio SERT (trasportatore della serotonina), che corrisponde al meccanismo d'azione e non a un'interazione con un altro farmaco. Non sono emerse interazioni clinicamente rilevanti con altri medicinali.

Per le avvertenze e le controindicazioni ufficiali, consultare il foglio illustrativo.

---

## Conclusioni e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione per il disturbo schizoide di personalità si basa solo sul punteggio del modello, senza studi clinici né letteratura pertinente (livello L5). Inoltre, tutte le autorizzazioni italiane sono cancellate, e i dati di sicurezza ufficiali risultano mancanti.

**Per procedere, è necessario:**
- Reperire e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni), attualmente un ostacolo bloccante per lo screening di sicurezza
- Ottenere i dati sul meccanismo d'azione da DrugBank
- Verificare lo stato regolatorio attuale della sertralina in Italia, dato che tutte le autorizzazioni elencate sono cancellate
- Cercare studi clinici o letteratura specifici sulla sertralina nel disturbo schizoide di personalità
- Valutare in alternativa di dare priorità all'agorafobia (L2), che dispone di evidenze molto più ampie
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

