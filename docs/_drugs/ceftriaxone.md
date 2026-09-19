---
layout: default
title: Ceftriaxone
parent: Prove elevate (L1-L2)
nav_order: 49
evidence_level: L2
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

Livello di evidenza: **L2** | Indicazioni previste: **7** 
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

# Ceftriaxone: dalle Infezioni Batteriche Gravi alla Otite Media Infettiva

## Sintesi in una frase

La ceftriaxone è un antibiotico cefalosporina di terza generazione con utilizzo globale ben consolidato per infezioni batteriche gravi, inclusa meningite, sepsi e polmonite. Il modello TxGNN predice che potrebbe essere efficace per l'**Otite Media Infettiva**, con **3 studi clinici** e **19 pubblicazioni** attualmente a sostegno di questa direzione.

---

## Panoramica rapida

| Elemento | Contenuto |
|------|---------|
| Indicazione originale | Infezioni batteriche gravi (cefalosporina di terza generazione) |
| Indicazione nuova predetta | Otite Media Infettiva |
| Punteggio di previsione TxGNN | 99.26% |
| Livello di evidenza | L2 |
| Stato del mercato in Italia | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Procedere con cautele |

---

## Perché questa previsione è ragionevole?

Attualmente, dati dettagliati sul meccanismo d'azione non sono disponibili in questo set di dati. Sulla base delle informazioni farmacologiche note, la ceftriaxone è una cefalosporina di terza generazione che inibisce la sintesi della parete cellulare batterica legandosi alle proteine leganti la penicillina (PBP) — in particolare PBP2b e PBP2x — interrompendo il cross-linking del peptidoglicano e causando lisi cellulare battericida. Questo meccanismo conferisce un'attività ad ampio spettro contro patogeni sia Gram-positivi che Gram-negativi.

I tre organismi primari responsabili dell'otite media acuta (OMA) — *Streptococcus pneumoniae*, *Haemophilus influenzae* e *Moraxella catarrhalis* — sono tutti altamente sensibili alla ceftriaxone. Due RCT (PMID 8989332, 11099083) hanno dimostrato la sua efficacia nella OMA resistente al trattamento, in particolare quando gli antibiotici orali di prima linea hanno fallito. La sua lunga emivita di eliminazione (~8 ore) supporta schemi a singola dose o a breve corso intramuscolari (IM 50 mg/kg/die), che è particolarmente pratico nei contesti pediatrici dove l'aderenza orale è scarsa o è necessaria una risposta clinica rapida.

La connessione meccanicistica è diretta: la ceftriaxone bersaglia i patogeni causali dell'otite media infettiva attraverso lo stesso meccanismo antibatterico che sottende il suo utilizzo più ampio nelle malattie infettive. I dati farmacocinetici mostrano un'adeguata penetrazione del farmaco nel liquido dell'orecchio medio, fornendo un'ulteriore plausibilità biologica per la previsione TxGNN.

---

## Evidenza da studi clinici

| Numero dello studio | Fase | Stato | Arruolamento | Risultati principali |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Fase 2 | Terminato | 520 | Studio randomizzato in doppio cieco controllato con placebo confrontando il trattamento antibiotico di 5 giorni vs. 10 giorni per OMA in bambini di età 6–23 mesi — più direttamente rilevante per la durata della terapia antibiotica nell'OMA; terminato anticipatamente (motivo non riportato) |
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | NA | Completato | 250 | Inserimento di tubi di timpanostomia vs. gestione non chirurgica per OMA ricorrente — RCT chirurgico fornendo quadro comparativo e dati sul carico di OMA nel corso di 2 anni |
| [NCT01272999](https://clinicaltrials.gov/study/NCT01272999) | N/A | Completato | 391 | Studio osservazionale post-commercializzazione dell'impatto di Prevnar 13 sull'incidenza di OMA nei bambini — conferma la rilevanza del patogeno pneumococcico nel contesto della malattia OMA |

---

## Evidenza dalla letteratura

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|------|------|---------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | *Pediatrics* | Studio randomizzato prospettico in cieco singolo: singola dose di ceftriaxone IM vs. TMP-SMZ orale per 10 giorni per OMA — la ceftriaxone ha raggiunto un'efficacia clinica comparabile |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | RCT | *Pediatric Infectious Disease Journal* | Ceftriaxone IM da 1 giorno vs. 3 giorni per OMA non responsiva nei bambini — lo schema di 3 giorni ha dimostrato risultati batteriologici e clinici superiori |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Linea guida clinica | *JAMA Network Open* | Prescrizione di antibiotici pediatrici ottimale in ambulatorio — il 50% delle prescrizioni statunitensi è stata ritenuta non necessaria; la ceftriaxone è stata approvata come scelta di salvataggio appropriata per OMA |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Linea guida clinica | *Clinical Pediatrics* | Raccomandazioni di consenso per la gestione della OMA — la ceftriaxone è posizionata come agente di seconda linea quando l'amoxicillina orale ha fallito; fornisce criteri per le decisioni di prescrizione |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Coorte retrospettiva | *Int J Pediatric Otorhinolaryngology* | Utilizzo di ceftriaxone IM per OMA in una grande popolazione di cure primarie accademiche negli Stati Uniti — caratterizza i fattori di utilizzo nel mondo reale incluso l'aumento dell'uso IM per otite-congiuntivite |
| [12237596](https://pubmed.ncbi.nlm.nih.gov/12237596/) | 2002 | Coorte prospettica | *Pediatric Infectious Disease Journal* | Dinamica della colonizzazione nasofaringea di *S. pneumoniae* dopo ceftriaxone IM da 3 giorni vs. 1 giorno per OMA non responsiva — lo schema di 3 giorni sopprime meglio la colonizzazione di ceppi resistenti |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Revisione | *Otology & Neurotology* | Prevenzione e trattamento della OMA e meningite nei bambini con impianti cocleari — la ceftriaxone è stata identificata come agente IV/IM preferito per OMA pneumococcica invasiva |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Prospettico | *Pediatric Infectious Disease Journal* | Efficacia batteriologica di ceftriaxone IM da 3 giorni nella OMA non responsiva — ha stabilito i tassi di eradicazione dei patogeni contro *S. pneumoniae* resistente ai farmaci |
| [30279114](https://pubmed.ncbi.nlm.nih.gov/30279114/) | 2019 | Studio di sorveglianza | *Journal of Infection and Chemotherapy* | Suscettibilità antimicrobica dei patogeni OMA in Giappone (2014–2017) — dati di tendenza della resistenza che informano quali casi giustificano l'escalation della ceftriaxone |
| [20660544](https://pubmed.ncbi.nlm.nih.gov/20660544/) | 2010 | Revisione | *Pediatrics* | Bambini con impianto cocleare: prevenzione e linee guida per il trattamento della OMA e meningite — rafforza la ceftriaxone come agente di prima scelta per OMA complicata o invasiva |

---

## Informazioni sul mercato italiano

Nel database normativo italiano (AIFA) non sono state identificate autorizzazioni di commercializzazione per la ceftriaxone.

> **Nota:** La ceftriaxone è ampiamente disponibile a livello internazionale sotto nomi commerciali come Rocephin ed è inclusa nell'Elenco modello OMS dei farmaci essenziali. L'assenza di registrazioni in questo set di dati è probabilmente una lacuna nei dati piuttosto che un'effettiva indisponibilità in Italia.

---

## Considerazioni sulla sicurezza

Consultare il foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusione e prossimi passi

**Decisione: Procedere con cautele**

**Razionale:**
Due RCT indipendenti e multiple linee guida cliniche hanno stabilito la ceftriaxone intramuscolare come agente di seconda linea efficace per l'otite media acuta resistente al trattamento, con una base meccanicistica chiara e diretta che bersaglia i patogeni causali primari.

**Per procedere, è necessario quanto segue:**
- Verificare lo stato normativo italiano (AIFA) — l'assenza di registrazioni probabilmente riflette una lacuna nei dati data la disponibilità globale della ceftriaxone
- Recuperare e rivedere le avvertenze complete del foglio illustrativo e le controindicazioni (segnalate come lacuna nei dati in questo set di dati)
- Sviluppare un protocollo di dosaggio pediatrico con attenzione alla sicurezza neonatale dato l'elevato legame proteico della ceftriaxone (95–98%), che potrebbe spostare la bilirubina nei neonati
- Condurre una valutazione della stewardship antimicrobica — la ceftriaxone è un antibiotico del gruppo OMS Access; l'espansione nell'OMA dovrebbe essere limitata ai casi di fallimento del trattamento per limitare la pressione della resistenza
- Identificare o commissionare un RCT comparativo vs. amoxicillina ad alte dosi nella popolazione pediatrica europea per stabilire l'efficacia regionale e il posizionamento nel formulario

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

