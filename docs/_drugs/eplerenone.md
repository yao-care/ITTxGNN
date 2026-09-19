---
layout: default
title: Eplerenone
parent: Solo previsione del modello (L5)
nav_order: 94
evidence_level: L5
indication_count: 5
---

# Eplerenone
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

# Eplerenone: Dall'ipertensione / insufficienza cardiaca post-infarto miocardico all'ipertensione polmonare con meccanismo multifatteriale poco chiaro

## Sintesi in una frase

Eplerenone è un antagonista selettivo del recettore dei mineralcorticoidi (sMRA), farmacologicamente consolidato per l'ipertensione e l'insufficienza cardiaca post-infarto miocardico, anche se i dati dell'indicazione originaria non sono disponibili nel registro normativo italiano.
Il modello TxGNN prevede che potrebbe essere efficace per l'**ipertensione polmonare con meccanismo multifatteriale poco chiaro**, con un punteggio di previsione del **99.50%**.
Attualmente, non vi sono **studi clinici** e **nessuna pubblicazione direttamente rilevante** a supporto di questa nuova indicazione, collocando questa previsione al livello di evidenza **L5**.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originaria | Non disponibile nei dati normativi italiani (usi farmacologici consolidati: ipertensione, insufficienza cardiaca post-infarto miocardico) |
| Nuova indicazione prevista | Ipertensione polmonare con meccanismo multifatteriale poco chiaro |
| Punteggio di previsione TxGNN | 99.50% |
| Livello di evidenza | L5 |
| Stato del mercato italiano | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Sospendere |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati sul meccanismo d'azione non sono disponibili nel database normativo. Sulla base della farmacologia consolidata, l'eplerenone è un antagonista selettivo del recettore dei mineralcorticoidi (MR) — blocca competitivamente l'aldosterone presso l'MR, riducendo così la ritenzione di sodio, abbassando la pressione arteriosa sistemica e attenuando la fibrosi tessutale e l'infiammazione vascolare mediate dall'aldosterone. La sua efficacia nell'ipertensione e nella disfunzione ventricolare sinistra post-infarto è stata convalidata in studi di riferimento (ad es. EPHESUS, EMPHASIS-HF per la classe degli MRA).

La base biologica che collega l'eplerenone all'ipertensione polmonare è radicata nel sistema renina-angiotensina-aldosterone (SRAA). L'iperattivazione del SRAA è riconosciuta come fattore che contribuisce alla fisiopatologia dell'ipertensione arteriosa polmonare (IAP): l'aldosterone promuove la proliferazione delle cellule della muscolatura liscia arteriosa polmonare, la deposizione della matrice extracellulare e la vasocostrizione. I dati dei modelli animali relativi all'antagonismo dell'MR nell'ipertensione polmonare hanno generato segnali iniziali positivi. Il blocco dell'effettore MR terminale potrebbe teoricamente interrompere il ciclo di rimodellamento vascolare polmonare mediato dall'aldosterone.

Tuttavia, la classificazione del "meccanismo multifatteriale poco chiaro" riflette un sottogruppo IP altamente eterogeneo — eziologie sovrapposte multiple con diversi gradi di coinvolgimento del SRAA. Il grado in cui l'aldosterone è il fattore dominante in uno qualsiasi dei pazienti all'interno di questa categoria è sconosciuto. Sebbene esista una plausibilità meccanicistica, attualmente non vi è alcuno studio clinico e nessuna letteratura direttamente rilevante per validare questa ipotesi negli esseri umani. La previsione dovrebbe quindi essere trattata come un segnale di ricerca piuttosto che come un promettente farmaco terapeutico.

---

## Evidenza degli studi clinici

Attualmente non sono registrati studi clinici correlati.

---

## Evidenza dalla letteratura

Attualmente non è disponibile alcuna letteratura direttamente collegata all'eplerenone e all'ipertensione polmonare con meccanismo multifatteriale poco chiaro.

> **Nota:** La ricerca delle evidenze ha recuperato 20 pubblicazioni per l'indicazione correlata "ipertensione polmonare dovuta a malattia polmonare e/o ipossia" (classificazione 2), ma tutti gli articoli recuperati affrontano la biologia generale dell'ipossia (segnalazione di HIF-1α, ipossia neurologica, ipossia oncologica) e non contengono dati sull'eplerenone o sull'antagonismo dell'MR nell'ipertensione polmonare. Non sono presentati come evidenza di supporto.

---

## Informazioni sul mercato italiano

Eplerenone attualmente non detiene **nessuna autorizzazione all'immissione in commercio** in Italia e non è disponibile sul mercato italiano. Nessun dato di licenza del prodotto è registrato.

---

## Considerazioni sulla sicurezza

Si rimanda al foglio illustrativo per le informazioni sulla sicurezza.

> **Nota:** I dati sugli avvertimenti chiave, le controindicazioni e le interazioni farmacologiche non erano disponibili nel pacchetto di evidenze corrente. Il recupero del foglio illustrativo da fonti normative ufficiali è un prerequisito prima che qualsiasi valutazione clinica proceda.

---

## Conclusione e prossimi passaggi

**Decisione: Sospendere**

**Razionale:**
Questa previsione poggia interamente sull'output del modello TxGNN (livello di evidenza L5), senza alcun supporto di studi clinici e nessuna letteratura direttamente rilevante. L'ipotesi meccanicistica (rimodellamento vascolare polmonare mediato dall'aldosterone bloccato dall'eplerenone) è biologicamente coerente ma completamente non validata negli esseri umani. La natura eterogenea e poco definita del sottotipo IP "multifatteriale poco chiaro" riduce ulteriormente la probabilità che un singolo agente diretto al SRAA sarebbe ampiamente efficace.

**Per procedere, è necessario quanto segue:**

- **Prerequisiti di sicurezza:** Recuperare e analizzare il foglio illustrativo completo da fonti normative (TFDA/EMA/AIFA) per ottenere controindicazioni, avvertimenti chiave e interazioni farmacologiche — attualmente un divario di dati bloccante
- **Conferma del MOA:** Interrogare l'API DrugBank per documentare formalmente il meccanismo d'azione per l'analisi del collegamento meccanicistico
- **Ricerca di evidenza sugli effetti di classe:** Condurre una revisione sistematica della letteratura per la classe più ampia degli MRA (spironolattone, finerenone) nell'ipertensione polmonare, per valutare se esiste un segnale di classe prima di impegnarsi specificamente nell'eplerenone
- **Raffinamento del sottotipo IP:** Stratificare i pazienti con IP "multifatteriale" in base ai biomarcatori del SRAA (aldosterone plasmatico, attività della renina) per identificare una sottopopolazione più propensa a rispondere
- **Dati preclinici:** Identificare eventuali studi su animali o in vitro dell'eplerenone o dell'antagonismo selettivo dell'MR in modelli di ipertensione polmonare
- **Validazione da esperti:** Convocare specialisti di ipertensione polmonare e farmacologi clinici per valutare la fattibilità di uno studio pilota condotto da ricercatori indipendenti prima di impegnarsi nello sviluppo formale

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

