---
layout: default
title: Captopril
parent: Prove moderate (L3-L4)
nav_order: 45
evidence_level: L4
indication_count: 4
---

# Captopril
{: .fs-9 }

Livello di evidenza: **L4** | Indicazioni previste: **4** 
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

# Captopril: Dall'ipertensione alla malattia renale ipertensiva maligna

## Sommario in una frase

Captopril è un inibitore dell'ACE di prima generazione con un ruolo consolidato nel trattamento dell'ipertensione, dell'insufficienza cardiaca e della nefropatia diabetica; tuttavia, il dataset attuale non contiene registrazioni formali di indicazioni approvate per l'Italia.
Il modello TxGNN prevede che potrebbe essere efficace per la **malattia renale ipertensiva maligna**, con **nessuna sperimentazione clinica registrata** e solo **1 segnalazione di caso pubblicata** che supporta attualmente questa direzione specifica.
Un'indicazione strettamente correlata — **ipertensione renovascolare maligna** (TxGNN rank #2, punteggio identico) — ha una base meccanicistica più forte ed è sostenuta da 20 pubblicazioni (Evidence Level L3), meritando attenzione insieme alla previsione principale.

---

## Panoramica rapida

| Elemento | Contenuto |
|------|---------|
| Indicazione originale | Non disponibile dal dataset normativo italiano (nessuna licenza approvata in cartella) |
| Indicazione prevista | Malattia renale ipertensiva maligna |
| Punteggio previsione TxGNN | 99.28% |
| Livello di evidenza | L4 |
| Stato del mercato italiano | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Hold |

---

## Perché questa previsione è ragionevole?

Attualmente, i dati dettagliati del meccanismo di azione non sono disponibili dalla fonte dati. Sulla base della farmacologia clinica consolidata, Captopril è un inibitore dell'enzima convertitore dell'angiotensina (ACE) che blocca la conversione dell'Angiotensina I in Angiotensina II (Ang II). Riducendo i livelli di Ang II, riduce la resistenza vascolare sistemica, diminuisce l'ipertensione capillare glomerulare e attenua la proteinuria — un profilo meccanicisticamente rilevante per il danno renale causato da ipertensione grave.

Nella malattia renale ipertensiva maligna, il RAAS è spesso patologicamente iperattivato, innescando un ciclo vizioso di elevati livelli di Ang II, ischemia renale progressiva e ulteriore secrezione di renina. Captopril interrompe direttamente questo asse, rendendo la previsione del TxGNN coerente dal punto di vista logico. Tuttavia, esiste un'importante avvertenza clinica: nei pazienti con stenosi bilaterale dell'arteria renale (BRAS) o stenosi in un rene funzionante solitario, l'inibizione dell'ACE può compromettere acutamente e gravemente la filtrazione glomerulare rimuovendo il tono dell'arteriola efferente dipendente da Ang II che sta mantenendo la perfusione residua — una controindicazione ben nota che deve essere sottoposta a screening prima di qualsiasi applicazione terapeutica.

La previsione strettamente correlata al rank #2 — **ipertensione renovascolare maligna** — segue la stessa logica meccanicistica e ha una letteratura di supporto sostanzialmente più ampia. Nell'ipertensione renovascolare causata da stenosi dell'arteria renale, la fisiologia ad alta renina/alto Ang II è la lesione definente, e Captopril è sia l'antidoto meccanicistico che una sonda diagnostica utilizzata da tempo (scintigrafia renale con captopril). Questa convergenza di utilità diagnostica e terapeutica nello spettro dell'ipertensione guidata dal RAAS rafforza la plausibilità biologica di entrambe le previsioni.

---

## Evidenza da studi clinici

Attualmente nessuna sperimentazione clinica registrata per Captopril nella malattia renale ipertensiva maligna o nell'ipertensione renovascolare maligna.

---

## Evidenza dalla letteratura

### Indicazione primaria: Malattia renale ipertensiva maligna (Rank #1)

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|------|------|---------|-------------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Segnalazione di caso | Clinical Nuclear Medicine | Scintigrafia renale con captopril positiva in un paziente con ipertensione dipendente dalla renina causata da carcinoma renale cromofobico (non stenosi dell'arteria renale); l'ipertensione è risolta dopo nefrectomia — illustra i meccanismi dipendenti dalla renina che mimano la malattia renale renovascolare |

### Evidenza supplementare: Ipertensione renovascolare maligna (Rank #2)

| PMID | Anno | Tipo | Rivista | Risultati chiave |
|------|------|------|---------|-------------|
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Studio clinico | Clinical Science | Captopril e saralasin hanno indotto elevazione marcata dell'attività plasmatica della renina (>14 ng/h/mL) in 43/44 pazienti con ipertensione renovascolare non trattata; riduzione della pressione diastolica ≥9% — stabilisce captopril come sonda diagnostica e meccanicistica |
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Studio clinico (Non-RCT) | Biull Vsesoiuznogo Kardiologicheskogo Nauchnogo Tsentra | Valutazione clinica diretta di captopril in ipertensione arteriosa sia stabile che in fase maligna |
| [3894732](https://pubmed.ncbi.nlm.nih.gov/3894732/) | 1985 | Coorte / Revisione | Japanese Journal of Medicine | Significato del test con captopril nella diagnosi dell'ipertensione renovascolare; importanza dell'equilibrio del sodio nella valutazione del RAAS |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Studio sperimentale / clinico | Japanese Heart Journal | Misurazioni neurormali seriali (attività plasmatica della renina, Ang I, Ang II, catecolamine, vasopressina) durante le fasi benigne e maligne dell'ipertensione Goldblatt 2K2C nei cani; definisce il contributo del RAAS alla transizione maligna |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Revisione | Journal of Pediatrics | Fisiopatologia e gestione dell'ipertensione maligna comprendenti i meccanismi del RAAS |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Segnalazione di caso | Clinical Nuclear Medicine | Scintigrafia renale con captopril falso-positiva nell'ipertensione maligna senza stenosi anatomica dell'arteria renale; evidenzia l'iperattivazione del RAAS come fattore causale autonomo |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Revisione / Serie di casi | Endocrinology & Metabolism Clinics of North America | Tumori iuxtaglomerulari secretori di renina; la pressione arteriosa cala costantemente con il trattamento con inibitori dell'ACE; il test con captopril mostra autonomia variabile della renina plasmatica |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Serie di casi | Pediatric Nephrology | Ipertensione renovascolare associata a NF1 in 27 pazienti pediatrici valutati con test con captopril e ultrasonografia Doppler |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Segnalazione di caso + Revisione | Clinical Nephrology | Due casi di ipertensione renovascolare in neurofibromatosi; la stimolazione con captopril ha aumentato l'attività plasmatica della renina da 2.8 a 12.6 ng/mL/h, confermando il meccanismo dipendente dalla renina |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Revisione | Minerva Medica | Concetti clinici nell'ipertensione renovascolare: fisiopatologia del RAAS, iter diagnostico e strategie di trattamento; viene discusso il ruolo dell'inibitore dell'ACE |

---

## Informazioni sul mercato italiano

Captopril è attualmente **non commercializzato in Italia**. Nessuna autorizzazione normativa è stata trovata nel dataset. Questo è rilevante considerando che captopril è un inibitore dell'ACE generico fuori brevetto a livello mondiale; l'assenza dal registro del mercato italiano potrebbe riflettere la completezza dei dati piuttosto che un'effettiva assenza dal mercato, e richiede verifica rispetto al database ufficiale dell'AIFA.

---

## Considerazioni di sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni di sicurezza.

> **Nota clinica a livello di classe:** Come inibitore dell'ACE, Captopril presenta considerazioni di sicurezza ben consolidate che sono particolarmente rilevanti per le indicazioni renali previste. La stenosi bilaterale dell'arteria renale o la stenosi unilaterale in un rene funzionante solitario è una **controindicazione nota** — l'inibizione dell'ACE in queste condizioni può precipitare insufficienza renale acuta. Gli effetti di classe aggiuntivi includono iperkaliemia (rischio amplificato in CKD), tosse secca indotta da inibitore dell'ACE e angioedema (raro ma potenzialmente grave). La documentazione di sicurezza formale dal foglio illustrativo o dall'etichetta della TFDA dovrebbe essere ottenuta prima di procedere.

---

## Conclusione e fasi successive

**Decisione: Hold**

**Razionale:**
Per l'indicazione primaria prevista (malattia renale ipertensiva maligna, rank #1), è disponibile solo una singola segnalazione di caso e nessuna sperimentazione clinica è stata registrata, posizionando l'evidenza squarely al livello L4. La base meccanicistica è coerente ma insufficiente di per sé per supportare una decisione di repurposing. L'indicazione strettamente correlata del rank #2 (ipertensione renovascolare maligna) presenta un profilo più actionable (evidenza L3, 20 pubblicazioni, raccomandazione: Proceed with Guardrails) e dovrebbe essere elevata come candidato primario per il follow-up.

**Per procedere, è necessario quanto segue:**

- **Revisione sistematica della letteratura per il rank #2**: L'ipertensione renovascolare maligna ha evidenza L3 e un caso meccanicistico più forte — considerare l'avanzamento di questa indicazione a valutazione formale
- **Verifica database AIFA**: Confermare lo stato del mercato italiano tramite interrogazione diretta dell'AIFA; il dataset attuale mostra zero licenze che potrebbe riflettere un gap nei dati
- **Recupero del foglio illustrativo**: Ottenere controindicazioni e avvertenze formali (etichetta TFDA/EMA) per completare lo screening di sicurezza S1 — attualmente bloccante
- **Recupero dati MOA**: Interrogare l'API di DrugBank per il profilo completo del meccanismo di azione di Captopril per rafforzare l'analisi del collegamento meccanicistico
- **Definizione del requisito di imaging renale**: Per qualsiasi percorso clinico che coinvolga inibitori dell'ACE nell'ipertensione maligna, lo screening della stenosi bilaterale dell'arteria renale (ultrasonografia Doppler o angiografia RM) deve essere definito come criterio di sicurezza prerequisito
- **Indicazioni rank #3 e #4 (ipertensione polmonare)**: Entrambe sono valutate L5 con raccomandazione Hold e mancano di supporto meccanicistico per Captopril — nessuna azione ulteriore consigliata in questa fase

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

