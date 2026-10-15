---
layout: default
title: Exemestane
parent: Solo previsione del modello (L5)
nav_order: 187
evidence_level: L5
indication_count: 7
---

# Exemestane
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **7** 
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

# Exemestane: dal carcinoma mammario all'amenorrea (predizione di bassa plausibilità)

## Riepilogo in una frase

Exemestane è un inibitore steroideo dell'aromatasi, usato nel trattamento del carcinoma mammario ormono-dipendente. Il modello TxGNN lo associa con punteggio elevato all'**amenorrea** (e a diverse condizioni trombofiliche ed emicraniche), ma la predizione di rango 1, il **deficit di antitrombina di tipo 2**, non ha **alcuno studio clinico né pubblicazione** a supporto. La predizione di rango 2, l'amenorrea, ha **0 studi clinici** e **5 pubblicazioni** indirette, che descrivono un effetto farmacologico atteso più che una indicazione terapeutica.

## Panoramica rapida

| Voce | Contenuto |
|------|------|
| Indicazione originale | Non disponibile nei dati compilati (i testi delle indicazioni delle autorizzazioni AIFA sono vuoti) |
| Nuova indicazione predetta | Deficit di antitrombina di tipo 2 (rango 1) |
| Punteggio di predizione TxGNN | 99,83% |
| Livello di evidenza | L5 |
| Stato di mercato in Italia | Solo autorizzazioni revocate/cancellate |
| Numero di autorizzazioni | 20 (tutte cancellate) |
| Decisione raccomandata | Hold |

## Perché questa predizione è ragionevole?

I dati sul meccanismo d'azione non sono al momento disponibili nei dati compilati. In base alle conoscenze generali, exemestane è un inibitore steroideo dell'aromatasi che riduce la sintesi di estrogeni; la sua efficacia nel carcinoma mammario ormono-positivo in postmenopausa è nota.

Per il deficit di antitrombina di tipo 2 **non emerge alcun razionale meccanicistico**: si tratta di un difetto ereditario del gene SERPINC1, e la soppressione estrogenica non corregge la funzione dell'antitrombina. Lo stesso vale per il fattore V in eccesso con trombosi spontanea e per il deficit del cofattore II dell'eparina: la predizione è solo un output del modello, senza supporto clinico o bibliografico.

Per l'**amenorrea**, exemestane sopprime gli estrogeni, quindi l'amenorrea è più correttamente un effetto farmacologico atteso o un esito legato al trattamento che un bersaglio terapeutico. La letteratura riguarda il recupero della funzione ovarica dopo chemioterapia e la soppressione ovarica nelle pazienti premenopausali con carcinoma mammario, non il trattamento dell'amenorrea con exemestane.

Per la trombofilia esiste solo un razionale debole e speculativo (meno estrogeni, minor ipercoagulabilità indotta da estrogeni), mentre per l'emicrania (comune e con aura del tronco encefalico) l'ipotesi estrogenica è teorica e gli inibitori dell'aromatasi possono causare cefalea.

## Evidenza da studi clinici

Al momento non risultano studi clinici correlati registrati per la predizione di rango 1 (deficit di antitrombina di tipo 2).

## Evidenza dalla letteratura

Per la predizione di rango 1 non è disponibile letteratura correlata. Di seguito la letteratura per il rango 2 (amenorrea), che resta indiretta:

| PMID | Anno | Tipo | Rivista | Risultati principali |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Coorte | Annals of Oncology | Incidenza e fattori predittivi del recupero della funzione ovarica in pazienti con carcinoma mammario e amenorrea indotta da chemioterapia passate da tamoxifene a exemestane |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Revisione | Oncology (Williston Park) | Ruolo della soppressione ovarica nelle donne premenopausali con carcinoma mammario HR-positivo in fase precoce |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Revisione | J Clin Oncol | Necessità del monitoraggio dell'estradiolo nelle donne in soppressione ovarica per carcinoma mammario |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Revisione | Recenti Progressi in Medicina | Ruolo attuale degli analoghi LHRH nel carcinoma mammario precoce e avanzato in premenopausa |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Revisione | Klinicka Onkologie | Trattamento con inibitori dell'aromatasi in postmenopausa e possibilità di gestirne gli effetti collaterali |

## Informazioni sul mercato italiano

Tutte le 20 autorizzazioni risultano cancellate; nessuna è attualmente valida. Il testo dell'indicazione approvata e la forma farmaceutica non sono riportati nei dati. Principali autorizzazioni:

| N. autorizzazione | Nome prodotto | Forma farmaceutica | Titolare | Stato |
|---------|------|------|------|-----------|
| 034678033 | Aromasin 30 cpr rivestite 25 mg | Compresse rivestite | Pfizer Italia Srl | Cancellata |
| 045700010 | Aromasin 30 cpr rivestite 25 mg | Compresse rivestite | Medifarm Srl | Cancellata |
| 040320018 | Exemestane 30 cpr rivestite 25 mg | Compresse rivestite | EG SpA | Cancellata |
| 040535041 | Exemestane 30 cpr rivestite 25 mg | Compresse rivestite | Sandoz SpA | Cancellata |
| 040012015 | Axelta 30 cpr rivestite 25 mg | Compresse rivestite | Ist. Gentili Srl | Cancellata |

## Citotossicità

Exemestane è un farmaco antineoplastico (inibitore dell'aromatasi, terapia ormonale), non un citotossico convenzionale.

| Voce | Contenuto |
|------|------|
| Classificazione | Terapia ormonale/mirata (inibitore steroideo dell'aromatasi) |
| Rischio di mielosoppressione | Si rimanda alle avvertenze e precauzioni del foglio illustrativo |
| Classificazione emetogena | Si rimanda alle avvertenze e precauzioni del foglio illustrativo |
| Parametri da monitorare | Si rimanda al foglio illustrativo (tipicamente emocromo, funzionalità epatica e renale) |
| Protezione nella manipolazione | Si rimanda al foglio illustrativo |

## Considerazioni sulla sicurezza

Le informazioni su avvertenze e controindicazioni dal foglio illustrativo AIFA non sono disponibili nei dati compilati; si rimanda al foglio illustrativo.

**Interazioni farmacologiche:** la ricerca ha individuato 100 interazioni (20 mostrate nei dati). Quelle di livello **moderato** sono con **desametasone** e **troglitazone**. Le altre, tra cui pantoprazolo, morfina, metformina, omeprazolo, simvastatina, acido acetilsalicilico e rosuvastatina, hanno livello di gravità non classificato.

Nota di contesto: le condizioni trombofiliche predette sono rilevanti poiché gli inibitori dell'aromatasi hanno proprie avvertenze tromboemboliche, seppur inferiori a quelle del tamoxifene.

## Conclusione e prossimi passi

**Decisione: Hold**

**Motivazione:**
Le predizioni si basano solo sul punteggio del modello (livello L5 per il rango 1; L4 per l'amenorrea, che è un effetto farmacologico atteso e non un obiettivo di riposizionamento). Mancano studi clinici, razionale meccanicistico e dati di sicurezza dal foglio illustrativo. Inoltre, tutte le autorizzazioni italiane sono cancellate.

**Per procedere sono necessari:**
- Scaricare e analizzare il foglio illustrativo AIFA (avvertenze e controindicazioni), lacuna bloccante per la valutazione di sicurezza
- Dati sul meccanismo d'azione da DrugBank
- Chiarimento delle indicazioni originali approvate e della forma farmaceutica
- Verifica del motivo della cancellazione delle autorizzazioni e dell'eventuale disponibilità attuale del prodotto
- Per qualsiasi indicazione candidata, razionale biologico credibile e dati preclinici o clinici prima di riconsiderare la decisione
## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

