---
layout: default
title: Perindopril
parent: Solo previsione del modello (L5)
nav_order: 163
evidence_level: L5
indication_count: 5
---

# Perindopril
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

# Perindopril: Dall'Ipertensione all'Ipertensione Renovascolare Maligna

## Riepilogo in una frase

Perindopril è un inibitore dell'ACE (Enzima Convertitore dell'Angiotensina) consolidato, ampiamente utilizzato per il trattamento dell'ipertensione e dell'insufficienza cardiaca cronica. Il modello TxGNN prevede che possa essere efficace per l'**Ipertensione Renovascolare Maligna**, una grave emergenza ipertensiva guidata dal RAAS. Attualmente, **0 studi clinici** e **0 pubblicazioni direttamente pertinenti** supportano questa specifica direzione di riprogrammazione, collocando le prove a un livello basato esclusivamente sulla predizione del modello.

---

## Panoramica rapida

| Voce | Contenuto |
|------|-----------|
| Indicazione originale | Ipertensione, insufficienza cardiaca cronica (classe inibitore dell'ACE) |
| Indicazione nuova prevista | Ipertensione Renovascolare Maligna |
| Punteggio di previsione TxGNN | 99.77% |
| Livello di evidenza | L5 |
| Stato di commercializzazione in Italia | Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Attesa |

---

## Perché questa previsione è ragionevole?

Perindopril appartiene alla classe degli inibitori dell'ACE, che esercita il suo effetto primario bloccando la conversione dell'Angiotensina I in Angiotensina II all'interno del Sistema Renina-Angiotensina-Aldosterone (RAAS). Il risultato è una ridotta vasocostrizione, una minore secrezione di aldosterone e una diminuzione della pressione arteriosa. I dati dettagliati del MOA da DrugBank non sono stati recuperati in questa esecuzione della pipeline, ma il meccanismo a livello di classe è ben consolidato nella farmacologia clinica.

L'ipertensione renovascolare maligna è un'emergenza ipertensiva più comunemente causata da stenosi dell'arteria renale, che innesca un'attivazione incontrollata del RAAS — i livelli circolanti di Angiotensina II aumentano drammaticamente, determinando l'estremo aumento della pressione arteriosa che caratterizza la condizione. Poiché gli inibitori dell'ACE agiscono direttamente a monte di questa cascata bloccando la produzione di Ang II, la previsione ad alto punteggio del modello TxGNN è coerente dal punto di vista meccanicistico: colpire il fattore principale della vasocostrizione patologica è un approccio terapeutico logico.

Tuttavia, un paradosso clinico ben documentato complica significativamente questa previsione. Nei pazienti con stenosi dell'arteria renale bilaterale — o stenosi di un rene funzionalmente solitario — gli inibitori dell'ACE possono precipitare insufficienza renale acuta. Ciò accade perché, quando la pressione di perfusione renale è già criticamente ridotta dalla stenosi, la filtrazione glomerulare è mantenuta solo dalla costrizione mediata dall'Angiotensina II dell'arteriola efferente. Rimuovere quella costrizione con un inibitore dell'ACE collassa il gradiente di filtrazione. Questo è un problema di sicurezza inerente al meccanismo a livello di classe direttamente rilevante all'indicazione prevista, e deve essere affrontato prima di qualsiasi progressione ulteriore.

---

## Evidenza degli studi clinici

Attualmente nessuno studio clinico correlato registrato per perindopril nell'ipertensione renovascolare maligna.

---

## Evidenza dalla letteratura

Attualmente nessuna letteratura correlata disponibile che valuti direttamente il perindopril nell'ipertensione renovascolare maligna.

---

## Considerazioni di sicurezza

Si prega di consultare il foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusioni e prossimi passi

**Decisione: Attesa**

**Razionale:**
La previsione si basa interamente sul modello TxGNN (L5), senza prove cliniche di supporto o pubblicazioni direttamente pertinenti per questa indicazione; inoltre, il contesto della malattia prevista — ipertensione renovascolare associata a stenosi dell'arteria renale — rappresenta un'impostazione ad alto rischio ben nota per la classe degli inibitori dell'ACE, dove l'uso può paradossalmente precipitare insufficienza renale acuta, rendendo la progressione clinica ingiustificabile senza dati di sicurezza aggiuntivi.

**Per procedere, è necessario quanto segue:**

- **Conferma del MOA**: Recuperare il record completo di DrugBank per perindopril per documentare formalmente i dettagli del percorso RAAS e le controindicazioni note a livello di classe
- **Risoluzione del divario dei dati di sicurezza**: Ottenere e analizzare il foglio illustrativo AIFA (DG001 — attualmente a livello Blocking) per confermare il linguaggio relativo alle controindicazioni riguardante la stenosi dell'arteria renale
- **Ricerca bibliografica mirata**: Condurre una revisione sistematica specificamente sull'uso degli inibitori dell'ACE nell'ipertensione renovascolare (inclusi case series e studi di coorte osservazionali) per stabilire se qualche sottopopolazione — ad esempio, stenosi unilaterale con un rene contralaterale normale — possa beneficiare in modo sicuro
- **Quadro di stratificazione dei pazienti**: Definire i criteri di idoneità per identificare i casi in cui il rischio di deterioramento della funzione renale è gestibile (ad esempio, imaging funzionale per escludere stenosi bilaterale prima di qualsiasi studio)
- **Studi preclinici di supporto**: Se viene identificato un sottogruppo di pazienti potenzialmente idoneo, uno studio pilota prospettico di sicurezza con monitoraggio intensivo della funzione renale (creatinina sierica, eGFR, potassio) dovrebbe essere progettato prima di qualsiasi considerazione di Fase 2

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

