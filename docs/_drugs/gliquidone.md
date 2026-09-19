---
layout: default
title: Gliquidone
parent: Solo previsione del modello (L5)
nav_order: 119
evidence_level: L5
indication_count: 2
---

# Gliquidone
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **2** 
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

# Gliquidone: Dal Diabete Mellito di Tipo 2 alla Sindrome Focale della Rigidità degli Arti

## Riassunto in una frase

Gliquidone è un agente antidiabetico sulfonilurea di seconda generazione che stimola la secrezione di insulina bloccando i canali del potassio sensibili all'ATP (K-ATP) nelle cellule β pancreatiche ed è stato a lungo utilizzato nella gestione del diabete mellito di tipo 2.
Il modello TxGNN prevede che possa essere efficace per la **Sindrome Focale della Rigidità degli Arti** (e la strettamente correlata **Sindrome Classica della Rigidità della Persona**), entrambe con un punteggio di previsione di **99.00%**; tuttavia, attualmente non esistono **studi clinici** e **nessuna letteratura pubblicata** che supportino questa direzione — questa previsione si basa solo su inferenza del modello.

---

## Panoramica rapida

| Elemento | Contenuto |
|----------|-----------|
| Indicazione originale | Diabete mellito di tipo 2 (classe sulfonilurea) |
| Nuova indicazione prevista | Sindrome focale della rigidità degli arti |
| Punteggio di previsione TxGNN | 99.00% |
| Livello di evidenza | L5 |
| Stato di commercializzazione in Italia | ✗ Non commercializzato |
| Numero di autorizzazioni | 0 |
| Decisione consigliata | Rinviare |

---

## Perché questa previsione è ragionevole?

I dati dettagliati del meccanismo d'azione non sono attualmente disponibili nel Pacchetto di evidenze. In base alla farmacologia stabilita, gliquidone appartiene alla classe delle sulfoniluree e esercita il suo effetto antidiabetico legandosi al dominio recettore della sulfonilurea 1 (SUR1) dei canali del potassio sensibili all'ATP (K-ATP) sulle cellule β pancreatiche. Questo legame chiude il canale, innesca la depolarizzazione della membrana e stimola il rilascio di insulina. La sua efficacia nel ridurre la glicemia nel diabete mellito di tipo 2 è ben consolidata in decenni di uso clinico.

Il ponte proposto verso la sindrome focale della rigidità degli arti (FSLS) — una variante focale dello spettro della sindrome della rigidità della persona (SPS) — è costruito su un antigene molecolare condiviso: l'acido glutammico decarbossilasi 65 (GAD65). GAD65 è espresso sia nelle cellule β pancreatiche (dove è co-localizzato con il bersaglio SUR1 di gliquidone) che negli interneuroni inibitori GABAergici del midollo spinale e del tronco cerebrale, che sono i siti primari dell'attacco autoimmune nei disturbi dello spettro SPS. Il grafo della conoscenza di TxGNN sembra aver inferito questa connessione attraverso la catena di nodi GAD65 → SUR1 → canale K-ATP — essenzialmente trattando l'antigene autoimmune condiviso come un ponte di evidenza tra la farmacologia del diabete e la malattia neuroimmunologica.

Tuttavia, l'ipotesi meccanicistica affronta un ostacolo farmacologico critico. Gliquidone è altamente legato alle proteine e dimostra una scarsa penetrazione della barriera emato-encefalica (BEE), risultando in un'esposizione al farmaco nel sistema nervoso centrale (CNS) trascurabile sotto il dosaggio orale standard. Il suo meccanismo periferico che colpisce i canali K-ATP pancreatici non si traduce direttamente in modulazione GABAergica centrale, e attualmente nessuna evidenza sperimentale convalida l'ipotesi del percorso centrale. La previsione è intellettualmente interessante ma meccanicisticamente speculativa in questa fase.

---

## Evidenza da studi clinici

Attualmente non sono registrati studi clinici correlati.

---

## Evidenza dalla letteratura

Attualmente non è disponibile letteratura correlata.

---

## Informazioni sul mercato italiano

Gliquidone non è attualmente **commercializzato in Italia**. Non sono state identificate autorizzazioni AIFA e nessuna licenza di prodotto è registrata.

---

## Considerazioni sulla sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni sulla sicurezza.

---

## Conclusioni e passaggi successivi

**Decisione: Rinviare**

**Razionale:**
Questa previsione si basa interamente sull'inferenza del grafo della conoscenza di TxGNN (Livello di evidenza L5), con zero studi clinici o pubblicazioni sottoposte a revisione paritaria di supporto. Mentre l'ipotesi dell'antigene autoimmune GAD65 fornisce un ponte teorico tra il bersaglio farmacologico di gliquidone e il meccanismo della malattia SPS, la scarsa penetrazione del sistema nervoso centrale del farmaco rappresenta una barriera farmacocinetica fondamentale che dovrebbe essere risolta prima che qualsiasi lavoro traslazionale potesse procedere.

**Per procedere, è necessario quanto segue:**

- **Dati di farmacocinetica del CNS**: Confermare o quantificare la penetrazione della BEE di gliquidone e l'esposizione nel liquido cerebrospinale; valutare se una strategia di formulazione (ad es., somministrazione mirata al CNS) potrebbe raggiungere concentrazioni terapeutiche nei circuiti GABAergici
- **Convalida preclinica**: Condurre studi meccanicistici in modelli animali di SPS positivi agli anticorpi GAD65 per testare se la modulazione dei canali K-ATP influenza il tono inibitorio GABAergico nel midollo spinale
- **Documentazione del MOA**: Completare la query dell'API DrugBank (bonifica DG002) per ottenere l'annotazione meccanicistica completa, inclusi gli effetti fuori bersaglio noti
- **Profilo di sicurezza completo**: Recuperare il foglio illustrativo AIFA/italiano (bonifica DG001) per completare la valutazione di controindicazioni, avvertenze e interazioni farmacologiche prima che qualsiasi ipotesi clinica possa essere valutata
- **Controllo di fattibilità epidemiologica**: FSLS e SPS classica sono entrambe malattie ultra-rare; confermare se la dimensione della popolazione di pazienti supporterebbe anche uno studio proof-of-concept promosso da ricercatori indipendenti

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

