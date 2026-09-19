---
layout: default
title: Pioglitazone
parent: Solo previsione del modello (L5)
nav_order: 165
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **9** 
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

# Pioglitazone: Dal Diabete Mellito di Tipo 2 all'Opsismodisplasia

## Riassunto in una frase

La pioglitazone è un agonista PPARγ della classe delle tiazolidinedioni (TZD), ampiamente utilizzato nel trattamento del diabete mellito di tipo 2 mediante il miglioramento della sensibilità insulinica periferica.
La predizione di più alto rango del modello TxGNN lo posiziona come candidato potenziale per l'**opsismodisplasia**, una displasia scheletrica rara e grave causata da mutazioni del gene *INPPL1* (SHIP2).
Questa predizione è attualmente supportata da **0 studi clinici** e **0 pubblicazioni**, e la logica meccanicistica solleva preoccupazioni significative riguardo la plausibilità biologica.

---

## Panoramica rapida

| Elemento | Contenuto |
|---|---|
| Indicazione Originaria | Diabete Mellito di Tipo 2 |
| Nuova Indicazione Predetta | Opsismodisplasia |
| Punteggio di Predizione TxGNN | 99.59% |
| Livello di Evidenza | L5 |
| Stato del Mercato Italiano | ✗ Non commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In sospeso |

---

## Perché questa predizione è ragionevole?

I dati formali del meccanismo d'azione non sono stati recuperati dal foglio illustrativo normativo per questo rapporto. Sulla base della farmacologia consolidata, la pioglitazone è un **agonista PPARγ (Recettore gamma attivato da proliferatori di perossisomi) selettivo** della classe delle tiazolidinedioni. L'attivazione di PPARγ rimodella i programmi di trascrizione genica nel tessuto adiposo, nel muscolo scheletrico e nel fegato, riducendo infine la resistenza all'insulina. Questa è anche la base di tutti i nove record bibliografici identificati per la pioglitazone nel sistema — tutti affrontano il diabete mellito di tipo 2 e le condizioni metaboliche correlate, senza alcun collegamento diretto con le malattie scheletriche.

L'opsismodisplasia è causata da mutazioni con perdita di funzione in *INPPL1*, che codifica per la fosfatasi SHIP2. SHIP2 modula l'asse di segnalazione PI3K/Akt, essenziale per la normale differenziazione dei condrociti e l'ossificazione endocondrale. Sebbene la pioglitazone interagisca indirettamente con i bersagli a valle di PI3K/Akt attraverso PPARγ, il collegamento è meccanicamente problematico piuttosto che supportivo: l'attivazione di PPARγ è ben documentata nel **sopprimere** la differenziazione degli osteoblasti antagonizzando i percorsi RUNX2 e Wnt/β-catenina — i programmi di trascrizione stessi richiesti per la corretta formazione ossea.

In una condizione già caratterizzata da mineralizzazione scheletrica gravemente compromessa, l'agonismo PPARγ potrebbe plausibilmente peggiorare piuttosto che migliorare la fisiopatologia. Il punteggio di alta confidenza del modello TxGNN (99.59%) molto probabilmente riflette la topologia di rete condivisa con vicini metabolici o di segnalazione nel grafo conoscitivo, piuttosto che una rilevanza meccanicistica convalidata per questa indicazione scheletrica rara. La plausibilità biologica complessiva è valutata come **bassa a negativa**.

---

## Evidenza da studi clinici

Attualmente non ci sono studi clinici correlati registrati.

---

## Evidenza bibliografica

Attualmente nessuna letteratura correlata disponibile.

---

## Informazioni sul mercato italiano

La pioglitazone non detiene alcuna autorizzazione alla commercializzazione in Italia. Nessun prodotto approvato o record di indicazione è disponibile dal database normativo.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusione e prossimi passi

**Decisione: In sospeso**

**Logica:** Questo candidato si basa interamente su una predizione del modello (Livello di Evidenza L5) senza alcuno studio clinico di supporto o letteratura pubblicata. Più criticamente, l'analisi meccanicistica attuale suggerisce che l'agonismo PPARγ potrebbe essere controproducente nell'opsismodisplasia — un disturbo scheletrico dove la funzione degli osteoblasti e dei condrociti è già compromessa — rendendo questa un'ipotesi di riutilizzo a bassa plausibilità indipendentemente dal punteggio TxGNN elevato.

**Per procedere, è necessario quanto segue:**
- Studi preclinici (in vitro/in vivo) che esaminano l'effetto della modulazione di PPARγ in modelli di condrociti o tessuti scheletrici carenti di *INPPL1*/*SHIP2*
- Chiarimento meccanicistico di se qualsiasi azione indipendente da PPARγ della pioglitazone (ad es., effetti anti-infiammatori, mitocondriali) potrebbe offrire qualche beneficio parziale in questo contesto di malattia
- Recupero formale dei dati MOA e di sicurezza: query API DrugBank per la farmacologia completa, e revisione AIFA/foglio illustrativo per avvertenze, controindicazioni e interazioni farmacologiche note
- Rivalutazione delle predizioni TxGNN di rango inferiore (ad es., Ranghi 5–8: sottotipi di lipodistrofia) che portano una logica meccanicistica più forte attraverso il ruolo di PPARγ come regolatore principale dell'adipogenesi, e potrebbero rappresentare candidati di riutilizzo più praticabili per il follow-up prioritario

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

