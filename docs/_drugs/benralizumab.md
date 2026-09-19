---
layout: default
title: Benralizumab
parent: Solo previsione del modello (L5)
nav_order: 35
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **5** 
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

# Benralizumab: da asma eosinofila grave a trombocitopenia da distruzione immune

## Riassunto in una frase

Benralizumab è un anticorpo monoclonale umanizzato anti-IL-5Rα approvato a livello mondiale (nome commerciale: Fasenra) per il trattamento di mantenimento aggiuntivo dell'asma eosinofila grave, anche se non è attualmente registrato a Taiwan.
Il modello TxGNN prevede che potrebbe essere efficace per la **Trombocitopenia da distruzione immune (ITP)**, classificandola come la candidata principale con un punteggio del 99.34%.
Tuttavia, **nessuna sperimentazione clinica** e **nessuna letteratura pubblicata** attualmente supportano questa direzione — si tratta di una previsione solo del modello senza confermazione empirica.

---

## Panoramica rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione originale | Asma eosinofila grave (approvazione mondiale; non registrato a Taiwan) |
| Nuova indicazione prevista | Trombocitopenia da distruzione immune |
| Punteggio di previsione TxGNN | 99.34% |
| Livello di evidenza | L5 |
| Stato del mercato Taiwan | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Mantenere |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili in questo Evidence Pack (query API DrugBank in sospeso). Basandosi su informazioni farmacologiche note, benralizumab è un anticorpo monoclonale umanizzato anti-IL-5Rα che colpisce direttamente la subunità alfa del recettore IL-5 su eosinofili e basofili. Attraverso la citotossicità cellulare dipendente da anticorpi potenziata (ADCC), raggiunge un'eliminazione quasi completa e rapida degli eosinofili circolanti. La sua efficacia clinica per l'asma eosinofila grave è stata stabilita in numerosi studi di fase 3 globali.

Il nesso meccanicistico tra l'asse IL-5Rα/eosinofilo e la trombocitopenia immunomediata (ITP), tuttavia, è estremamente debole. L'ITP è principalmente guidata da autoanticorpi IgG anti-piastrine che colpiscono le glicoproteine GPIIb/IIIa e GPIb/IX sulla superficie piastrinica, portando all'eliminazione accelerata delle piastrine da parte dei macrofagi splenici. Gli eosinofili non svolgono un ruolo stabilito in questo processo; la malattia è fondamentalmente mediata da anticorpi e cellule T, non guidata dagli eosinofili.

L'elevato punteggio TxGNN molto probabilmente riflette un **effetto bystander computazionale** nel grafo della conoscenza: gli eosinofili partecipano a reti infiammatorie sistemiche più ampie che condividono nodi con citopenie autoimmuni, portando il modello ad assegnare punteggi di somiglianza elevati. Si tratta di un'inferenza statistica, non di un'ipotesi guidata dal meccanismo. Senza alcuna evidenza preclinica o clinica corroborante, questa previsione dovrebbe essere trattata solo come un segnale esplorativo — non è un candidato di riposizionamento clinicamente praticabile in questa fase.

---

## Evidenza da studi clinici

Attualmente nessuna sperimentazione clinica correlata registrata per la trombocitopenia da distruzione immune.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile per la trombocitopenia da distruzione immune.

---

## Informazioni sul mercato di Taiwan

Benralizumab non ha prodotti autorizzati registrati a Taiwan (0 licenze in archivio presso TFDA). Il farmaco è commercializzato globalmente come **Fasenra** (AstraZeneca) per l'asma eosinofila grave ma non ha ottenuto l'approvazione normativa di Taiwan.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

> **Nota:** I dati del foglio illustrativo TFDA sono stati interrogati ma il contenuto completo della sicurezza (avvertenze, controindicazioni) non ha potuto essere analizzato in questa versione di Evidence Pack. La query API DrugBank è anche in sospeso. Questi sono contrassegnati come lacune di dati ad alta priorità che richiedono remediation prima che qualsiasi valutazione clinica possa procedere.

---

## Conclusione e prossimi passi

**Decisione: Mantenere**

**Giustificazione:**
Il modello TxGNN produce un punteggio di elevata confidenza (99.34%), ma questo manca completamente di supporto da studi clinici o letteratura pubblicata, e la giustificazione meccanicistica che collega il blocco IL-5Rα alla distruzione immunitaria delle piastrine non è biologicamente stabilita. Procedere senza un fondamento empirico comporterebbe un rischio scientifico inaccettabile.

**Per procedere, è necessario quanto segue:**
- **Dati preclinici**: Studi in modelli animali per investigare se l'eliminazione degli eosinofili influisce sul conteggio piastrinico o sui titoli di autoanticorpi anti-piastrine nei modelli ITP
- **Ricerca della letteratura**: Ricerca sistematica di eventuali casi segnalati di utilizzo di benralizumab in ITP, sindrome ipereosinofila con trombocitopenia, o citopenie autoimmuni correlate
- **Chiarimento del meccanismo d'azione**: Evidenza sottoposta a revisione paritaria che stabilisca un ruolo (se presente) di IL-5 o eosinofili nei percorsi di distruzione immunitaria delle piastrine
- **Documentazione MoA**: Query API DrugBank per completare il profilo del meccanismo d'azione (attualmente contrassegnato come gap di dati ad alta gravità DG002)
- **Profilazione della sicurezza**: Estrazione del testo completo del foglio illustrativo TFDA per abilitare lo screening di sicurezza S1 (contrassegnato come gap di dati bloccante DG001)
- **Valutazione del percorso normativo**: Poiché benralizumab non è registrato a Taiwan, una revisione di fattibilità normativa completa sarebbe necessaria prima di qualsiasi applicazione clinica

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

