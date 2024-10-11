# Kubeglimpse

## 1. Popis projektu

**KubeGlimpse** je 3D vizualizačná aplikácia navrhnutá na interaktívne prehliadanie a analýzu Kubernetes klastrov. Je postavená na technológiách **Python**, **Three.js** a **Neo4j**, a slúži na dynamickú a prehľadnú reprezentáciu zložitých Kubernetes infraštruktúr. Cieľom aplikácie je pomôcť používateľom efektívne spravovať, diagnostikovať a analyzovať klastre prostredníctvom vizuálne prívetivého rozhrania.


### **Ako KubeGlimpse funguje?**

1. **Získavanie dát z Kubernetes API**  
   Základ aplikácie je naprogramovaný v **Pythone**, ktorý pravidelne pristupuje k **Kubernetes API** a získava všetky potrebné informácie o Kubernetese. Tieto informácie o obsahujú:


   <ul>
  <li><b>Nody (Nodes):</b> Fyzické alebo virtuálne servery, ktoré hostia <b>pody</b>. Nody sú základnými stavebnými jednotkami Kubernetes klastrov a poskytujú výpočtový výkon, na ktorom aplikácie bežia.</li>
  <li><b>Pody (Pods):</b> Najmenšie a najzákladnejšie vykonávateľné jednotky v Kubernetes. Pody predstavujú zoskupenie jedného alebo viacerých kontajnerov, ktoré bežia spolu a zdieľajú rovnaké zdroje (napr. sieť a úložisko).</li>
  <li><b>Služby (Services):</b> Abstrakcia, ktorá definuje, ako aplikácie (pody) komunikujú s inými aplikáciami alebo klientmi. Služby umožňujú trvalý prístup k podom, aj keď sa ich IP adresy dynamicky menia.</li>
  <li><b>Namespaces:</b> Logické oddelenia v Kubernetes, ktoré umožňujú rozdelenie klastrov na izolované časti. Používajú sa na organizovanie a správu rôznych projektov, tímov alebo prostredí v rámci toho istého klastra.</li>
  <li><b>ConfigMap a Secret:</b> Konfiguračné objekty používané na správu nastavení aplikácií. <b>ConfigMap</b> slúži na ukladanie nekritických dát ako sú konfiguračné súbory, zatiaľ čo <b>Secret</b> je používaný na ukladanie citlivých informácií (napr. heslá alebo API kľúče).
</ul>

2. **Ukladanie dát do Neo4j**  
   Po zozbieraní sa dáta ukladajú do **Neo4j**, grafovej databázy optimalizovanej na modelovanie a spracovanie vzťahov medzi jednotlivými objektmi v Kubernetese. Neo4j databáza umožňuje robiť efektívne databázove dotazy a manipuláciu s dátami, ktoré reprezentujú vzťahy medzi podmi, nodmi, službami a ďalšími komponentmi klastra.

3. **Transformácia dát do JSON**  
   Zozbierané dáta sú transformované do **JSON formátu**, ktorý slúži ako podklad pre vizualizáciu. Tento formát je ideálny pre rýchle načítanie a manipuláciu v 3D grafickom prostredí.

4. **3D Vizualizácia pomocou Three.js (Forced Graph)**  
   Vizualizácia v **Three.js** využíva 3D **forced-graph** na zobrazenie vzťahov medzi komponentmi. Tento typ grafu simuluje fyzikálne interakcie medzi objektmi, čím sa dynamicky zobrazuje štruktúra klastra. Uzly reprezentujú jednotlivé komponenty (nody, pody, služby), zatiaľ čo hrany zobrazujú vzťahy medzi nimi (napr. ktorý pod beží na ktorom node).

5. **Interaktívne funkcie vizualizácie**  
   Používatelia môžu s 3D modelom klastra interagovať, približovať ho, otáčať a klikať na jednotlivé uzly, aby zobrazili podrobnosti o danom komponente (napr. stav podu, alokované zdroje, metadáta). Táto funkcia umožňuje detailnú analýzu klastrov a rýchlu identifikáciu problémov alebo nezrovnalostí.

6. **Škáľovateľnosť a výkonnosť**  
   KubeGlimpse je optimalizovaný tak, aby zvládal vizualizáciu malých aj veľkých klastrov. Vďaka efektívnej práci s dátami v Neo4j a používaniu Three.js pre vykresľovanie 3D grafov môže aplikácia plynule fungovať aj pri komplexných infraštruktúrach.


## **2. Motivácia**

Kubernetes sa stal jednou z najpopulárnejších platforiem na správu kontajnerizovaných aplikácií v moderných IT infraštruktúrach, najmä pre veľké a dynamické prostredia. Jeho schopnosť automatizovať nasadzovanie a škálovanie aplikácií je zásadná, avšak čím je klaster väčší a zložitejší, tým je pre správcov náročnejšie získať prehľad o tom, ako jednotlivé komponenty, ako sú nody, pody a služby, medzi sebou interagujú. Textové alebo tabuľkové výstupy z bežných nástrojov často neposkytujú dostatočne intuitívny pohľad na celý systém, čo môže skomplikovať riešenie problémov a optimalizáciu klastrov.

Existujúce vizualizačné nástroje pre Kubernetes klastre sú často nepresné, ťažko ovládateľné alebo ponúkajú len základné informácie. **KubeGlimpse** rieši túto medzeru tým, že poskytuje interaktívnu 3D vizualizáciu, ktorá zobrazuje presné vzťahy medzi jednotlivými komponentmi klastrov. Tento nástroj umožňuje používateľom efektívne prehliadať klastre, rýchlo identifikovať problémy a lepšie porozumieť dynamike a štruktúre infraštruktúry, čím zjednodušuje správu aj veľmi komplexných systémov.

## **3. Prípady použitia**

### **1. Porozumenie štruktúre Kubernetes klastrov**
Pre správu veľkých Kubernetes klastrov je kľúčové mať jasný prehľad o tom, ako jednotlivé komponenty (nody, pody, služby) spolu interagujú. KubeGlimpse poskytuje interaktívnu 3D vizualizáciu, ktorá umožňuje správcovi lepšie pochopiť vzťahy medzi komponentmi a rýchlo identifikovať neefektívne usporiadanie alebo nezrovnalosti v štruktúre klastra.

### **2. Analýza závislostí medzi podmi a službami**
KubeGlimpse umožňuje používateľom vizuálne skúmať, ako sú pody prepojené so službami a inými komponentmi v rámci klastra. Táto vizualizácia umožňuje rýchlo pochopiť zložité závislosti medzi aplikáciami a infraštruktúrou, čo je mimoriadne užitočné pri diagnostikovaní problémov alebo pri plánovaní zmien.

### **3. Vytváranie vizualizácií pre tímové stretnutia a dokumentáciu**
KubeGlimpse môže slúžiť ako nástroj na prezentovanie štruktúry klastra počas tímových stretnutí. Vizualizácie môžu pomôcť technickým aj netechnickým členom tímu lepšie pochopiť, ako Kubernetes klaster funguje, a môžu byť využité pri vytváraní dokumentácie, aby zložité koncepty boli prístupnejšie.

### **4. Porovnanie štruktúry pred a po zmene konfigurácie**
Pri aktualizáciách alebo zmenách v konfigurácii Kubernetes klastrov je často náročné pochopiť, ako sa štruktúra klastra zmenila. KubeGlimpse môže vytvárať vizualizácie, ktoré umožňujú porovnávať stav klastra pred a po zmene, čo pomáha pri overovaní správnosti nasadenia zmien a pri znižovaní rizika chýb.

### **5. Lepšia orientácia pre nových členov tímu**
Pre nových členov tímu, ktorí ešte nemajú skúsenosti so správou Kubernetes klastrov, môže byť pochopenie infraštruktúry náročné. KubeGlimpse poskytuje vizuálny nástroj, ktorý uľahčuje orientáciu v štruktúre klastra a pomáha im rýchlejšie sa zorientovať a pochopiť fungovanie jednotlivých komponentov a ich vzťahov.




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