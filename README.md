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

![Zobrazenie Usecase diagramu pre KubeGlimpse](assets/usecase.png)

### **1. Porozumenie štruktúre Kubernetesu**
Pre správu veľkých Kubernetes klastrov je kľúčové mať jasný prehľad o tom, ako jednotlivé komponenty (nody, pody, služby) spolu interagujú. KubeGlimpse poskytuje interaktívnu 3D vizualizáciu, ktorá umožňuje správcovi lepšie pochopiť vzťahy medzi komponentmi a rýchlo identifikovať neefektívne usporiadanie alebo nezrovnalosti v štruktúre klastra.

### **2. Analýza závislostí medzi podmi a službami**
KubeGlimpse umožňuje používateľom vizuálne skúmať, ako sú pody prepojené so službami a inými komponentmi v rámci klastra. Táto vizualizácia umožňuje rýchlo pochopiť zložité závislosti medzi aplikáciami a infraštruktúrou, čo je mimoriadne užitočné pri diagnostikovaní problémov alebo pri plánovaní zmien.

### **3. Vytváranie vizualizácií pre tímové stretnutia**
KubeGlimpse môže slúžiť ako nástroj na prezentovanie štruktúry klastra počas tímových stretnutí. Vizualizácie môžu pomôcť rôznym členom tímu, vrátane tých, ktorí nemajú technické zázemie, ľahšie pochopiť fungovanie Kubernetes a ako jednotlivé komponenty spolu interagujú, čím uľahčujú komunikáciu medzi rôznymi oddeleniami.

### **4. Porovnanie štruktúry v čase**
Pri aktualizáciách alebo zmenách v konfigurácii Kubernetes klastrov je často náročné pochopiť, ako sa štruktúra klastra zmenila. KubeGlimpse môže vytvárať vizualizácie, ktoré umožňujú porovnávať stav klastra pred a po zmene, čo pomáha pri overovaní správnosti nasadenia zmien a pri znižovaní rizika chýb.

### **5. Lepšia orientácia pre nových členov tímu**
Pre nových členov tímu, ktorí ešte nemajú skúsenosti so správou Kubernetes klastrov, môže byť pochopenie infraštruktúry náročné. KubeGlimpse poskytuje vizuálny nástroj, ktorý uľahčuje orientáciu v štruktúre klastra a pomáha im rýchlejšie sa zorientovať a pochopiť fungovanie jednotlivých komponentov a ich vzťahov.

## **4. Biznis pohľad KubeGlimpse**

**KubeGlimpse** ponúka jedinečný spôsob vizualizácie Kubernetes klastrov, čo prináša jasné výhody nielen pre technických odborníkov, ale aj pre manažérske a biznisové tímy. KubeGlimpse umožňuje prístup k vizualizáciám, ktorá sú ľahko pochopiteľná a umožňuje efektivnejšie pochopenie infraštruktúry, čo v dôsledku zlepšuje komunikáciu naprieč rôznymi tímami.

### **Použitie KubeGlimpse v praxi:**

1. **Podpora rozhodovania v IT oddeleniach**
   Pre manažérov a vedúcich IT oddelení je kľúčové mať prehľad o infraštruktúre, na ktorej závisí prevádzka aplikácií a služieb. KubeGlimpse poskytuje jednoduchý a prehľadný pohľad na celý Kubernetes klaster, čím umožňuje rýchlo zhodnotiť stav infraštruktúry a efektívnosť jej využívania. Vizualizácia môže slúžiť ako podklad pre rozhodovanie o škálovaní, nasadzovaní nových služieb alebo optimalizácii infraštruktúry.

2. **Zlepšenie medziodborovej komunikácie**
   Pre tímy mimo IT oddelení, ako sú produktoví manažéri, marketingové tímy či projektoví vedúci, môže byť zložité pochopiť technické detaily aplikácie. KubeGlimpse umožňuje ne-technickým tímom rýchlo pochopiť štruktúru systému, čo podporuje lepšiu koordináciu medzi technickými a obchodnými jednotkami v organizácii.

3. **Nasadzovanie v DevOps a SRE prostredí**
   DevOps tímy a SRE (Site Reliability Engineering) zvyčajne spravujú rozsiahle klastre, kde je neustála potreba vizuálne sledovať vzťahy medzi komponentmi a ich stav. KubeGlimpse môže byť kľúčovým nástrojom pri analýze výkonnosti, sledovaní preťaženia nodov alebo pri vizualizácii zmien v infraštruktúre počas nasadzovania nových verzií aplikácií.

4. **Podpora pri plánovaní a škálovaní infraštruktúry**
   Organizácie, ktoré neustále rastú a škálujú svoje Kubernetes klastre, môžu využívať KubeGlimpse na vizualizáciu budúcich zmien v infraštruktúre. Používanie vizualizácie pri plánovaní rozšírení pomáha pri optimalizácii zdrojov a zabraňuje vzniku preťažených alebo neefektívne využívaných nodov.

## **Trhové príležitosti a finančný potenciál**

Podľa najnovších analýz bol trh s Kubernetes v roku 2019 ocenený na **1,46 miliardy USD**, pričom sa očakáva, že do roku 2031 dosiahne hodnotu **9,69 miliardy USD** s ročným rastom (CAGR) **23,4 %** v období rokov 2024 – 2031. Kubernetes je najrýchlejšie rastúcim projektom v histórii open-source softvéru po Linuxe, a jeho adopcia sa stáva štandardom pre správu kontajnerizovaných aplikácií.

### **Firmy investujú do Kubernetes technológií kvôli:**

<ul>
  <li><b>Automatizácii:</b> Kubernetes umožňuje automatickú správu a škálovanie prostredí.</li>
  <li><b>Efektivite:</b> Znižovanie prevádzkových nákladov a optimalizácia využívania zdrojov.</li>
  <li><b>Multicloud a hybridné možnosti:</b> Kubernetes umožňuje nasadenie v multicloudových a hybridných prostrediach, čo firmám poskytuje väčšiu flexibilitu.</li>
  <li><b>Zlepšenej produktivite vývojárov:</b> Vďaka jednoduchšiemu nasadzovaniu aplikácií a lepšej správe infraštruktúry.</li>
</ul>

Rast Kubernetes trhu je poháňaný jeho širokým využitím v IT a telekomunikáciách, zdravotníctve, financiách a ďalších odvetviach. Najväčší trhový podiel má momentálne **Severná Amerika**, ale najrýchlejšie rastúcim regiónom je **Ázia-Pacifik**, kde je vysoký dopyt po modernizácii IT infraštruktúr.

![Zobrazenie trhu cloudoveho marketu](assets/app-cont-market-trends.png)

### **Rast Kubernetes trhu podľa regiónov (v miliardách USD)**

| **Rok** | **Severná Amerika** | **Ázia-Pacifik** | **Európa** | **Latinská Amerika** | **Blízky východ a Afrika** |
|---------|---------------------|------------------|------------|---------------------|---------------------------|
| 2023    | 0.54                | 0.49             | 0.44       | 0.40                | 0.35                      |
| 2024    | 0.66                | 0.60             | 0.55       | 0.49                | 0.44                      |
| 2025    | 0.80                | 0.74             | 0.68       | 0.62                | 0.55                      |
| 2026    | 0.97                | 0.91             | 0.84       | 0.77                | 0.70                      |
| 2027    | 1.19                | 1.11             | 1.03       | 0.95                | 0.87                      |
| 2028    | 1.45                | 1.36             | 1.27       | 1.18                | 1.09                      |
| 2029    | 1.78                | 1.67             | 1.57       | 1.47                | 1.36                      |
| 2030    | 2.18                | 2.06             | 1.94       | 1.82                | 1.70                      |


![Zobrazenie ocakavanie rastu trhu cloudoveho marketu](assets/app-cont-market.png)

**KubeGlimpse** má potenciál stať sa zaujímavým pre tento trh tým, že rieši existujúci problém s vizualizáciou zložitých infraštruktúr. Vizualizačné nástroje pre Kubernetes klastre sú nevyhnutné pre udržanie vysokej úrovne výkonu a spoľahlivosti systémov, čo zvyšuje dopyt po takýchto riešeniach. **KubeGlimpse** je schopný uspokojiť potreby malých startupov, ako aj veľkých korporácií spravujúcich tisíce nodov a podov.


## **5. Návrh dizajnu**

nothing to see here yet

## **6. Technologická vrstva**

V tejto sekcii sa pozrieme na technológie, ktoré boli použité pri vývoji KubeGlimpse, a rozdelíme ich na dve časti: **teoretickú** a **praktickú**. Najskôr si vysvetlíme jednotlivé komponenty, z ktorých sa projekt skladá, a prečo sme sa rozhodli použiť práve tieto technológie. V praktickej časti následne uvedieme konkrétne príklady toho, ako boli tieto technológie implementované v našom kóde, aby bolo jasné, ako celý systém funguje.

### **6.1 Teoretický pohľad na použité technológie**

**Frontend: Three.js**

Three.js je JavaScriptová knižnica na tvorbu 3D grafiky v prehliadači, ktorá používa WebGL. Poskytuje robustný súbor nástrojov na vytváranie interaktívnych 3D modelov a animácií, ktoré môžu byť vykresľované priamo v prehliadači bez potreby ďalších pluginov.

**Načo sa používa:**

<ul> 
<li><b>3D modelovanie:</b> Three.js umožňuje vytváranie komplexných 3D scén, modelov a objektov.</li>
<li><b>Interaktívnosť:</b> Knižnica podporuje interakciu používateľov s modelmi (napr. zoom, otáčanie, klikanie na objekty).</li>
<li><b>Rendering a fyzika:</b> Poskytuje pokročilé renderovacie techniky a podporu pre fyzikálne simulácie, ako napríklad svetlo, tieňovanie a textúrovanie objektov.</li></ul>

**Príklad základnej scény s 3D objektami:**


[Video ako táto základna scéna vyzerá](https://youtu.be/8r4LcAXUNDY)


**Backend: Python a Kubernetes API**

Backend KubeGlimpse je naprogramovaný v jazyku Python a používa Kubernetes API na získavanie aktuálnych informácií o klastroch. Python je obľúbený hlavne kvôli svojej jednoduchosti a bohatému ekosystému knižníc, ktoré uľahčujú prácu s API a databázami.

<ul> 
<li><b>Získavanie dát:</b> Pythonové skripty komunikujú s Kubernetes API a zhromažďujú informácie o nodoch, podoch, službách a iných objektoch v klastri.</li>
<li><b>Spracovanie dát:</b> Dáta sa spracovávajú a transformujú do podoby, ktorá sa dá následne uložiť do databázy Neo4j a vizualizovať na frontende.</li> 
<li><b>Automatizácia:</b> Python je tiež využívaný na automatické úlohy, ako je pravidelná aktualizácia dát alebo zisťovanie stavu klastra.</li> </ul>

**Databáza: Neo4j**

Neo4j je grafová databáza, ktorá umožňuje efektívne spravovať dáta a vzťahy medzi nimi v rámci Kubernetes klastrov. Je ideálna pre modelovanie zložitých štruktúr, ako sú klastre, pretože umožňuje efektívne dotazovanie a vizualizáciu vzťahov.

<ul>
<li><b>Ukladanie vzťahov:</b> Neo4j ukladá nody, pody a služby ako uzly, a vzťahy medzi nimi ako hrany, čím umožňuje modelovať zložité prepojenia v Kubernetes.</li> 
<li><b>Rýchle dotazovanie:</b> Databáza umožňuje efektívne vyhľadávať a získavať informácie o vzťahoch medzi rôznymi komponentmi klastra.</li> </ul>


### **6.2 Prakticky pohľad na použité technológie**

Ako som už spomenul niekoľkokrát , backend je naprogramovaný v Pythone a má tri hlavné funkcie:

**1. Získať dáta z Kubernetes API** (objekty ako pody, služby, deploymenty, atď).  
**2. Pretransformovať tieto dáta na uzly a vzťahy** (edges) vhodné pre grafovú databázu Neo4j.\
**3. Uložiť dáta do Neo4j**, čím sa vytvorí grafová reprezentácia Kubernetes klastra.\

#### Zber dát z Kubernetes API

Používa sa knižnica `kubernetes`, ktorá poskytuje jednoduchý prístup k rôznym API Kubernetes. Cieľom tejto časti je načítať všetky objekty z klastra, ktoré sú dôležité pre vizualizáciu (napr. nody, pody, služby).

```
# Kubernetes objects
pods = v1.list_pod_for_all_namespaces(watch=False).items
services = v1.list_service_for_all_namespaces(watch=False).items
deployments = apps_v1.list_deployment_for_all_namespaces(watch=False).items
replica_sets = apps_v1.list_replica_set_for_all_namespaces(watch=False).items
nodes = v1.list_node(watch=False).items
```

**Ako to funguje:** Volania ako `v1.list_pod_for_all_namespaces()` využívajú Kubernetes API na získanie informácií o všetkých objektoch daného typu v rámci všetkých namespace. Týmto získame zoznam objektov, pričom každý obsahuje metadáta (meno, namespace) a špecifikácie (napr. na akom node pod beží).

#### Ukladanie uzlov do Neo4j

Každý objekt Kubernetes (napr. pod, node, služba) je reprezentovaný ako uzol (node) v Neo4j. Na uloženie sa používa dotaz Cypher s príkazom `MERGE`.

```
for pod in pods:
    pod_id = f"Pod_{pod.metadata.namespace}_{pod.metadata.name}"
    query = """
    MERGE (p:Pod {id: $id, name: $name, namespace: $namespace})
    """
    parameters = {"id": pod_id, "name": pod.metadata.name, "namespace": pod.metadata.namespace}
    session.write_transaction(create_graph, query, parameters)
```

**Ako to funguje:** Uloží každý pod (identifikovaný kombináciou namespace a mena) ako uzol s atribútmi `id`, `name`, a `namespace`. Tento princíp sa opakuje aj pre ostatné komponenty Kubernetesu, kvôli jednoduchosti som uviedol len takýto príklad pre pody. 

#### Vytváranie vzťahov medzi uzlami

Okrem uzlov je dôležité modelovať aj vzťahy medzi nimi. Modelujeme vzťahy ako napríklad, ktorý node hosťuje ktorý pod, ktorá služba komunikuje s ktorým podom, ktorý deployment vlastní ktorý replicaSet. 

```
for pod in pods:
    pod_id = f"Pod_{pod.metadata.namespace}_{pod.metadata.name}"
    if pod.spec.node_name:
        node_id = f"Node_{pod.spec.node_name}"
        query = """
        MATCH (n:Node {id: $node_id})
        MATCH (p:Pod {id: $pod_id})
        MERGE (n)-[:HOSTS]->(p)
        """
        parameters = {"node_id": node_id, "pod_id": pod_id}
        session.write_transaction(create_graph, query, parameters)
```

Táto konkrétna časť kódu predstavuje vytvorenie vzťahu medzi nodom a podom.\
**Ako to funguje:** Najskôr nájde uzly reprezentujúce node (`Node`) a pod (`Pod`) podľa ich ID. Následne medzi nimi vytvorí vzťah HOSTS (node hostuje pod). Logika za tým je vytvoriť infraštruktúru vo forme grafovej reprezentácie, kde vzťahy reprezentujú skutočné interakcie v Kubernetes klastri.











