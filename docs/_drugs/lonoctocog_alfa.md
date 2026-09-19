---
layout: default
title: Lonoctocog Alfa
parent: Solo previsione del modello (L5)
nav_order: 140
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
{: .fs-9 }

Livello di evidenza: **L5** | Indicazioni previste: **4** 
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

# Lonoctocog Alfa: dall'Emofilia A alla Pseudo-malattia di von Willebrand

## Sintesi in una Frase

Lonoctocog alfa è un concentrato puro di Fattore VIII (FVIII) ricombinante utilizzato per il trattamento e la profilassi delle emorragie nell'Emofilia A.
Il modello TxGNN predice che potrebbe avere una potenziale rilevanza clinica per la **Pseudo-malattia di von Willebrand**,
tuttavia il collegamento meccanicistico è indiretto e la base di evidenze è limitata interamente alla previsione del modello — **nessuno studio clinico o pubblicazione di supporto** è stato identificato.

---

## Panoramica Rapida

| Voce | Contenuto |
|------|---------|
| Indicazione Originale | Emofilia A (deficit congenito di Fattore VIII) |
| Indicazione Nuova Predetta | Pseudo-malattia di von Willebrand |
| Punteggio di Previsione TxGNN | 99.85% |
| Livello di Evidenza | L5 |
| Stato del Mercato in Italia | Non Commercializzato |
| Numero di Autorizzazioni | 0 |
| Decisione Consigliata | In Sospeso |

---

## Perché Questa Previsione è Ragionevole?

Lonoctocog alfa è un FVIII ricombinante con dominio B troncato progettato per sostituire il cofattore della coagulazione mancante nell'Emofilia A. Il suo meccanismo d'azione si basa sulla ricostituzione del complesso tenasi intrinseco (FVIIIa–FIXa) sulla superficie carica positivamente per fosfatidilserina (PS) delle piastrine attivate, generando così una quantità sufficiente di trombina per formare un coagulo di fibrina stabile. Una caratteristica distintiva di questo prodotto è che non contiene **alcun Fattore di von Willebrand (vWF)** — a differenza di molti concentrati di FVIII derivati dal plasma — il che è rilevante per l'indicazione predetta.

La pseudo-malattia di von Willebrand (vWD di tipo piastrinico) è causata da mutazioni gain-of-function nel gene **GP1BA**, che codifica per il recettore di superficie piastrinico GPIbα. Queste mutazioni causano alle piastrine di legarsi spontaneamente al vWF, consumando multimeri di vWF ad alto peso molecolare e talvolta innescando lieve trombocitopenia. La malattia clinicamente assomiglia al vWD di tipo 2B ma è meccanicisticamente un disturbo piastrinico piuttosto che una carenza di proteina plasmatica.

Il collegamento tra lonoctocog alfa e pseudo-vWD è indiretto e meccanicisticamente debole. Esiste un argomento teorico di sicurezza: poiché lonoctocog alfa è privo di vWF, evita il rischio che i prodotti contenenti vWF potrebbero stimolare ulteriormente le piastrine iper-reattive in questi pazienti. Tuttavia, i pazienti con pseudo-vWD non hanno deficit di FVIII, quindi non esiste nessun difetto della coagulazione che lonoctocog alfa possa correggere. L'alto punteggio di previsione TxGNN molto probabilmente riflette la **vicinanza di rete** tra FVIII e vWF nel grafo della conoscenza biologica piuttosto che una vera e propria motivazione terapeutica diretta. In alcuni scenari clinici, aumentare le concentrazioni di FVIII senza affrontare l'iperattivazione sottostante di GPIbα potrebbe teoricamente esacerbare la formazione di trombi locali senza migliorare i risultati emorragici.

---

## Evidenze da Sperimentazioni Cliniche

Attualmente nessuna sperimentazione clinica correlata registrata per Lonoctocog Alfa nella Pseudo-malattia di von Willebrand.

---

## Evidenze da Letteratura

Attualmente nessuna letteratura correlata disponibile per Lonoctocog Alfa nella Pseudo-malattia di von Willebrand.

---

## Ulteriori Previsioni TxGNN

Oltre all'indicazione di primo livello, TxGNN ha identificato tre altri candidati di disturbi piastrinici. Tutti rimangono al livello di evidenza L5 con una raccomandazione In Sospeso o Domanda di Ricerca, ma le motivazioni meccanicistiche differiscono significativamente nella loro plausibilità scientifica:

| Rango | Indicazione Predetta | Punteggio TxGNN | Raccomandazione | Plausibilità Meccanicistica |
|------|---------------------|-------------|----------------|--------------------------|
| 2 | Disordine Primario di Rilascio delle Piastrine | 99.84% | In Sospeso | Molto debole — i difetti di rilascio dei granuli α/δ non coinvolgono la via del FVIII |
| 3 | Trombastenia di Glanzmann | 99.76% | Domanda di Ricerca | Indiretto — il precedente con rFVIIa suggerisce che la generazione di trombina sulla superficie piastrinica può parzialmente compensare; FVIII potrebbe condividere una logica simile ma manca qualsiasi dato clinico |
| 4 | Sindrome di Scott | 99.44% | Domanda di Ricerca | Più meccanicisticamente coerente — la sindrome di Scott compromette direttamente l'esternalizzazione di PS (proprio la superficie su cui si assembla il complesso tenasi); aumentare la concentrazione di FVIII potrebbe teoricamente migliorare l'efficienza di utilizzo della superficie PS, sebbene la disponibilità di PS rimanga il fattore limitante |

**La Sindrome di Scott è il candidato più interessante dal punto di vista scientifico** nonostante la sua rarità estrema (meno di 10 casi segnalati a livello globale), poiché la motivazione è radicata direttamente nella biochimica del complesso tenasi piuttosto che nella sola vicinanza di rete.

---

## Considerazioni di Sicurezza

Si prega di fare riferimento al foglio illustrativo per le informazioni di sicurezza.

> Nessun avvertimento, controindicazione o dato di interazione farmacologica era disponibile nel pacchetto di evidenze attuali. Una caratterizzazione completa della sicurezza è necessaria prima di qualsiasi considerazione clinica.

---

## Conclusione e Prossimi Passi

**Decisione: In Sospeso**

**Razionale:**
Il punteggio TxGNN per pseudo-vWD è guidato dalla vicinanza di rete biologica tra FVIII e vWF piuttosto che da un collegamento meccanicistico clinicamente utilizzabile. Non ci sono studi clinici, pubblicazioni o precedenti normativi di supporto per questo uso, e lonoctocog alfa non affronta il meccanismo patologico primario — l'iperattivazione del GPIbα piastrinico. Procedere senza una base scientifica più forte introdurrebbe un'incertezza clinica e di sicurezza inaccettabile.

**Per procedere, è necessario quanto segue:**

- **Risoluzione del divario nei dati di sicurezza**: Ottenere il foglio illustrativo completo (avvertimenti, controindicazioni, precauzioni) per lonoctocog alfa prima che qualsiasi screening di indicazione possa procedere oltre lo Stage S0
- **Chiarimento del meccanismo d'azione**: Confermare il profilo farmacologico preciso di lonoctocog alfa (caratteristiche della truncazione del dominio B, emivita, profilo di immunogenicità) per valutare se differisce significativamente da altri prodotti FVIII in un contesto adiacente a vWD
- **Prioritizzazione della Sindrome di Scott**: Se si perseguono una qualsiasi di queste quattro previsioni, la sindrome di Scott offre la motivazione più scientificamente fondata e dovrebbe essere elevata per considerazione della ricerca di base prima delle altre tre
- **Revisione ematologica da parte di esperti**: Uno specialista in disturbi emorragici rari dovrebbe valutare se FVIII privo di vWF ha un ruolo di sicurezza nichè negli episodi emorragici di pseudo-vWD (ad esempio, in contesti perioperatori), indipendente dall'ipotesi di riutilizzo
- **Percorso di registrazione in Italia**: Poiché lonoctocog alfa non è attualmente commercializzato in Italia, qualsiasi sviluppo futuro richiederebbe una strategia normativa completa; confermarne lo stato di approvazione EMA attuale e le condizioni di rimborso come prerequisito

## Avvertenza

Questo contenuto è solo a scopo di ricerca e non costituisce un parere medico.
È necessaria una validazione clinica prima di qualsiasi applicazione clinica.

---

