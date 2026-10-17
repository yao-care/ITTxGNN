---
layout: default
title: Ciclesonide
parent: Solo previsione del modello (L5)
nav_order: 106
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Ciclesonide: nuova indicazione prevista, Eczema atopico (livello di evidenza L5). Indicazione originale: Asma, asma intrinseco, asma allergico, rinite allergica…"
monitor_inn: "CICLESONIDE"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis"]
---

# Ciclesonide
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

# Ciclesonide: Dall'asma alla dermatite atopica (eczema atopico)

## Sintesi in una frase

Il ciclesonide è un corticosteroide inalatorio utilizzato per il trattamento dell'asma e della rinite allergica.
Il modello TxGNN prevede che possa essere efficace per l'**eczema atopico**, con un punteggio molto alto (99,96%).
Tuttavia, per questa indicazione **non risulta alcuno studio clinico né alcuna pubblicazione** a supporto: la previsione è basata esclusivamente sul modello computazionale.

## Quadro generale

| Voce | Contenuto |
|------|------|
| Indicazione originale | Asma, asma intrinseco, asma allergico, rinite allergica, rinite vasomotoria (dal grafo di conoscenza; il testo autorizzativo AIFA non è disponibile) |
| Nuova indicazione prevista | Eczema atopico |
| Punteggio di previsione TxGNN | 99,96% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 2 (entrambe cancellate) |
| Decisione raccomandata | Hold |

## Perché questa previsione è plausibile?

Il ciclesonide è un profarmaco corticosteroide inalatorio, attivato dalle esterasi nel metabolita attivo des-ciclesonide. I dati sul meccanismo d'azione originale non sono disponibili nei dati compilati per questo rapporto; la descrizione si basa quindi sulla conoscenza generale della classe.

I corticosteroidi, topici o sistemici, sono una terapia standard per l'eczema atopico perché sopprimono l'infiammazione cutanea. L'asma e la dermatite atopica condividono inoltre una componente infiammatoria atopica/allergica, il che fornisce una logica meccanicistica per la previsione.

Va però osservato che altri corticosteroidi topici dispongono già di solide evidenze in questa malattia, e il valore aggiunto del ciclesonide non è chiaro. Anche la compatibilità della via di somministrazione (formulazione inalatoria vs. cutanea) non è stata valutata.

Altre previsioni del modello, in ordine di punteggio: sensibilizzazione al 2-idrossietil metacrilato (99,76%), dermatite atopica (99,73%, sostanzialmente la stessa malattia dell'eczema atopico), bronchite (99,70%), dermatite da contatto (99,25%) e "tratti correlati all'asma, suscettibilità" (99,13%, probabile riformulazione dell'indicazione già esistente e non una vera nuova indicazione).

## Evidenza dagli studi clinici

Attualmente non risultano studi clinici registrati correlati.

## Evidenza dalla letteratura

Per l'indicazione principale (eczema atopico) non è disponibile alcuna letteratura. Per le previsioni secondarie è stato reperito solo materiale indiretto:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Revisione | Basic & Clinical Pharmacology & Toxicology | Linee guida finlandesi su diagnosi e farmacoterapia della BPCO stabile; evidenza indiretta (bronchite), senza dati specifici sul ciclesonide |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Caso clinico | Contact Dermatitis | Dermatite allergica sistemica da budesonide inalatorio con reattività crociata ai patch test con ciclesonide; è un segnale di sicurezza, non un beneficio terapeutico (dermatite da contatto) |

## Informazioni sul mercato italiano

| Numero di autorizzazione | Nome del prodotto | Forma farmaceutica | Indicazione approvata |
|---------|------|------|-----------|
| 038873055 | ALVESCO soluz. inal. 60 erog. 160 mcg (stato: cancellata) | Non indicata | Non disponibile |
| 038873030 | ALVESCO soluz. inal. 60 erog. 80 mcg (stato: cancellata) | Non indicata | Non disponibile |

## Considerazioni sulla sicurezza

- **Controindicazioni (dal grafo di conoscenza, non dal foglio illustrativo)**: cheratite da herpes simplex, insufficienza corticosurrenalica, malattia di Addison, osteoporosi (anche postmenopausale), infezioni fungine, dermatofitosi, ipertensione oculare, glaucoma, infezioni parassitarie.
- **Interazioni farmacologiche**: sono state identificate 63 interazioni. Tra quelle riportate:
  - **Maggiore**: cladribina.
  - **Moderate**: claritromicina, miconazolo, cobicistat, fostamatinib, abametapir (topico), fosamprenavir, atazanavir, amprenavir, ceritinib, boceprevir, conivaptan, insulina umana inalatoria ad azione rapida.
  - **Minori**: formoterolo, salbutamolo, arformoterolo.
  - Livello non definito: omeprazolo, lansoprazolo, prednisolone, famotidina.
- **Segnale di allergia di classe**: un caso clinico documenta reattività crociata tra budesonide e ciclesonide nei patch test, il che suggerisce cautela in pazienti con allergia ai corticosteroidi.

Per avvertenze e controindicazioni ufficiali si rimanda al foglio illustrativo, attualmente non disponibile nei dati compilati.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
La previsione ha un punteggio molto alto, ma non è supportata da alcuno studio clinico o pubblicazione specifica (livello L5). Inoltre le autorizzazioni italiane sono tutte cancellate, mancano i dati di sicurezza ufficiali e la compatibilità della via di somministrazione non è stata valutata.

**Per procedere sono necessari:**
- Foglio illustrativo AIFA con avvertenze e controindicazioni (lacuna bloccante per lo screening di sicurezza)
- Dati dettagliati sul meccanismo d'azione (ad esempio da DrugBank)
- Valutazione della compatibilità tra la formulazione/via di somministrazione disponibile e quella necessaria per l'uso cutaneo
- Ricerca di studi preclinici o clinici di ciclesonide nella dermatite atopica e confronto con i corticosteroidi topici già consolidati
- Chiarimento dello stato regolatorio attuale (autorizzazioni cancellate) e della disponibilità del prodotto
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

