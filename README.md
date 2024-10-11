# Kubeglimpse

## Popis projektu

**KubeGlimpse** je 3D vizualizačná aplikácia navrhnutá na interaktívne prehliadanie a analýzu Kubernetes klastrov. Je postavená na technológiách **Python**, **Three.js** a **Neo4j**, a slúži na dynamickú a prehľadnú reprezentáciu zložitých Kubernetes infraštruktúr. Cieľom aplikácie je pomôcť používateľom efektívne spravovať, diagnostikovať a analyzovať klastre prostredníctvom vizuálne prívetivého rozhrania.


### **Ako KubeGlimpse funguje?**

1. **Získavanie dát z Kubernetes API**  
   Aplikácia napísaná v **Pythone** pravidelne pristupuje k **Kubernetes API** a získava všetky potrebné informácie o klastroch. Tieto dáta obsahujú:


   <ul>
  <li><b>Nody:</b> Fyzické alebo virtuálne servery, ktoré hostia **pody**. Nody sú základnými stavebnými jednotkami Kubernetes klastrov a poskytujú výpočtový výkon, na ktorom aplikácie bežia.</li>
  <li>Najmenšie a najzákladnejšie vykonávateľné jednotky v Kubernetes. Pody predstavujú zoskupenie jedného alebo viacerých kontajnerov, ktoré bežia spolu a zdieľajú rovnaké zdroje (napr. sieť a úložisko).</li>
  <li>**Služby (Services)**: Abstrakcia, ktorá definuje, ako aplikácie (pody) komunikujú s inými aplikáciami alebo klientmi. Služby umožňujú trvalý prístup k podom, aj keď sa ich IP adresy dynamicky menia.</li>
  <li>**Namespaces**: Logické oddelenia v Kubernetes, ktoré umožňujú rozdelenie klastrov na izolované časti. Používajú sa na organizovanie a správu rôznych projektov, tímov alebo prostredí v rámci toho istého klastra.</li>
</ul>e

1. **Ukladanie dát do Neo4j**  
   Po zozbieraní sa dáta ukladajú do **Neo4j**, grafovej databázy optimalizovanej na modelovanie a spracovanie vzťahov medzi jednotlivými objektmi v Kubernetes klastroch. Neo4j databáza umožňuje efektívne dotazovanie a manipuláciu s dátami, ktoré reprezentujú vzťahy medzi podmi, nodmi, službami a ďalšími komponentmi klastra.

2. **Transformácia dát do JSON**  
   Zozbierané dáta sú transformované do **JSON formátu**, ktorý slúži ako podklad pre vizualizáciu. Tento formát je ideálny pre rýchle načítanie a manipuláciu v 3D grafickom prostredí.

3. **3D Vizualizácia pomocou Three.js (Forced Graph)**  
   Vizualizácia v **Three.js** využíva 3D **forced graph** na zobrazenie vzťahov medzi komponentmi. Tento typ grafu simuluje fyzikálne interakcie medzi objektmi, čím sa dynamicky zobrazuje štruktúra klastra. Uzly reprezentujú jednotlivé komponenty (nody, pody, služby), zatiaľ čo hrany zobrazujú vzťahy medzi nimi (napr. ktorý pod beží na ktorom node).

4. **Interaktívne funkcie vizualizácie**  
   Používatelia môžu s 3D modelom klastra interagovať, približovať ho, otáčať a klikať na jednotlivé uzly, aby zobrazili podrobnosti o danom komponente (napr. stav podu, alokované zdroje, metadáta). Táto funkcia umožňuje detailnú analýzu klastrov a rýchlu identifikáciu problémov alebo nezrovnalostí.

5. **Škáľovateľnosť a výkonnosť**  
   KubeGlimpse je optimalizovaný tak, aby zvládal vizualizáciu malých aj veľkých klastrov. Vďaka efektívnej práci s dátami v Neo4j a používaniu Three.js pre vykresľovanie 3D grafov môže aplikácia plynule fungovať aj pri komplexných infraštruktúrach.



* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact