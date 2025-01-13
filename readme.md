# SMVIT - Lendify

**Lendify** je moderná aplikácia, ktorá spája ľudí, ktorí chcú prenajať svoje veci, s tými, ktorí ich 
potrebujú na krátky čas. Primárne sa zameriava na techniku, ako sú vŕtačky, píly, rebríky, stavebné a záhradné 
náradie, ale jej využitie je omnoho širšie. Či už ste domáci majster, ktorý potrebuje špecifický nástroj, alebo vlastníte 
vybavenie, ktoré nepoužívate často, Lendify ponúka jednoduchý a výhodný spôsob, ako ho zdieľať.

Aplikácia funguje na princípe vzájomného prenájmu – každý užívateľ môže svoje predmety ponúknuť na požičiavanie
, pričom si s nájomcom dohodne cenu a podmienky. Vďaka prehľadnému prostrediu a integrovanému hodnotiacemu systému 
aplikácia zabezpečuje dôveryhodné a bezpečné transakcie. 

Lendify podporuje filozofiu zdieľanej ekonomiky, ktorá prispieva k udržateľnosti a efektívnemu 
využívaniu zdrojov. Užívatelia nemusia investovať do nákupu drahého vybavenia, ktoré potrebujú len príležitostne, 
a majitelia zasa môžu získať pasívny príjem z predmetov, ktoré by inak len ležali nevyužité. 

Je to ideálne riešenie pre tých, ktorí si cenia flexibilitu, chcú ušetriť alebo prispieť k zníženiu zbytočného konzumu.
Lendify spája komunitu ľudí s podobnými záujmami a vytvára priestor pre jednoduché zdieľanie zdrojov.

### Komunikačné a prezentačné kanály
- Youtube kanál: [Skibidi IT RIZZ](https://www.youtube.com/@SKIBIDI_IT_RIZZLERS)
- Patreon: [Lendify](https://www.patreon.com/c/ShoppingRevolution)
- Linked In Skibidy IT RIZZ: [Lendify](https://www.linkedin.com/company/skibidi-it-rizz/)
- Linked In Matej: [Matej Pakán](https://www.linkedin.com/in/matejpakan/)
- Linked In Adam: [Adam Jankanič](https://www.linkedin.com/in/adam-jankani%C4%8D-46aa61238/)
- Linked In Ivan: [Ivan Gajdoš](https://www.linkedin.com/in/ivan-gajdos-175902267/)

### Spoločná práca
Počas semestra sme si viedli vlastný GitHub repozitár: https://github.com/Matt1s/SMVIT
Na v tomto repozitári sme si viedli zmeny na vlastných vetvách.

![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/3c6d2d06c0fc167930a65bab140f3b9463bbc45a/repos/github.png)

Na porovnávanie branchí sme použili LemonTree.

![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/3c6d2d06c0fc167930a65bab140f3b9463bbc45a/repos/lemontree.png)

Následne sme si forkli repozitár, a presunuli dáta na Bitbucket, kde sme dotvorili túto dokumentáciu.

## Minimum Viable Product

### Funkcie aplikácie Lendify
Aplikácia Lendify ponúka širokú škálu funkcií, ktoré zjednodušujú prenajímanie a správu produktov medzi používateľmi. Od intuitívneho pridávania produktov, prepracovaných filtrov a recenzií až integrovaný čet. Všetky funkcie sú navrhnuté s dôrazom na užívateľskú jednoduchosť a efektívnosť. Cieľom aplikácie je vytvoriť bezpečné a transparentné prostredie pre vzájomné zdieľanie zdrojov.
### Prihlásenie a registrácia
Používatelia sa môžu prihlásiť alebo zaregistrovať, pričom proces zahŕňa overenie dokladu totožnosti. Účty umožňujú editáciu údajov (meno, fotografia) a zobrazenie štatistík, ako je dĺžka registrácie a počet úspešných objednávok.


### Zalistovanie produktu
Je možné pridávať produkty s nasledovnými detailmi:
- Názov, popis a fotografie/videá
- Kategórie a podkategórie (napr. Náradie → Vŕtačka → Príklepové vŕtačky)
- Cena za časovú jednotku a výška zábezpeky
- Miesta a časy vyzdvihnutia a vrátenia

![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/14bdf4f8332732ae116e180f7b59cc890f1766bd/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/2_add_new_product.png)

Používatelia môžu pri pridávaní produktov využiť možnosť nahrávať kvalitné fotografie a videá, ktoré lepšie predstavia ponúkaný produkt. Taktiež môžu detailne špecifikovať kategórie a podkategórie, čo zjednodušuje vyhľadávanie zo strany zákazníkov. Pri každom produkte je možné uviesť viacero miest vyzdvihnutia, čo pridáva flexibilitu pre predávajúcich aj kupujúcich.

### Objednávka produktu
Objednávkový proces umožňuje jednoduché a intuitívne zadávanie presných časov vyzdvihnutia a vrátenia produktu. Používateľ má možnosť sledovať stav objednávky v reálnom čase a notifikácie ho upozornia na všetky dôležité zmeny. Po dokončení objednávky môže hodnotiť predávajúceho aj samotný produkt, čím prispieva k transparentnosti platformy.

![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/7d98e99d3d3f3809494fd76f966c14547e94ab86/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/4_single_item.png)
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/7d98e99d3d3f3809494fd76f966c14547e94ab86/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/5_checkout.png)

### Filter a vyhľadávanie
Je umožnené filtrovať produkty podľa:
- Vzdialenosti (vrátane mapy)
- Ceny
- Kategórie, podkategórie
- Recenzií produktu a používateľa
- Dostupnosti (v %)

![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/accdbbda8f292bf61bc4c7ee061c27b6e7892d0d/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/3_catalog.png)
Pokročilé filtre umožňujú presné hľadanie produktov podľa individuálnych potrieb. Napríklad pomocou mapy si môžu používatelia vyhľadať produkty v blízkosti a porovnať ceny rôznych predávajúcich. Systém zobrazuje aj hodnotenie produktov a predávajúcich, čo zjednodušuje rozhodovanie pri výbere.

### Čet a notifikácie
Integrovaný čet poskytuje rýchlu komunikáciu medzi predávajúcim a kupujúcim, čím urýchľuje riešenie nejasností alebo dohody o detailoch objednávky. Notifikácie informujú používateľov o príchode nových správ, zmenách v objednávkach či dôležitých aktualizáciách v aplikácii.


### Hodnotenie 
Systém hodnotení pomáha budovať dôveru medzi používateľmi. Okrem hodnotenia produktov môžu používatelia zanechať spätnú väzbu aj na správanie predávajúcich a kupujúcich. Všetky recenzie sú verejné a zobrazujú priemerné hodnotenie pre jednoduché porovnávanie. Týmto spôsobom sa vytvára komunita zodpovedných používateľov, ktorí si navzájom dôverujú.
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/accdbbda8f292bf61bc4c7ee061c27b6e7892d0d/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/8_personal_user_page.png)

#### Celý zoznam features:

Pre našu aplikáciu sme identifikovali nasledovné funkčné a nefunkčné požiadavky.
##### Zoznam požiadaviek pre MVP Lendify (funkcie)
- Vedenie účtu
  - prihlásenie / registrácia
  - overenie používateľa na základe dokladu
  - výber prevodom na účet
  - editácia účtu (minimálne meno + fotka)
      - zobrazovať dĺžku registrácie a úspešných objednávok
- Zalistovanie produktu
  - Názov
  - Popis
  - Fotografie, video
  - Kategorizácia (Náradie → Vŕtačka → Príklepové vŕtačky)
  - Cena za jednotku času
      - Zábezpeka
  - Miesta vyzdvihnutia
  - Možný čas vyzdvihnutia (dostupnosť)
  - Možný čas na vrátenie
  - Výpočet provízie
- Objednávka produktu
  - Čas vyzdvihnutia
  - Čas vrátenia
- Recenzie
  - Na konkrétny produkt konkrétneho používateľa
  - Priemer recenzií konkrétneho produktu všetkých používateľov
  - Recenzia predávajúceho
  - Recenzia kupujúceho
  - Schopnosť spraviť recenziu po objednávke
- Filter
  - Vzdialenosť (+ mapa)
  - Cena
    - za deň + prepočet na presný čas
  - Kategórie
    - podkategórie
  - Na základe recenzií produktu
  - Na záklde recenzií používateľa
  - Dostupnosť (v %)
- Zoradzovanie
- Manažment objednávok
  - Dashboard príjmov a skladu
  - Zoznam nových objednávok
  - Zoznam prebiehajúcich
  - Možnosť expirácie objednávky, ak predávajuci nezareaguje
  - Čet + notifikácia
- Support
  - Ticket systém
  - Vytvorenie ticketu
  - Čet s operátorom
##### Zoznam požiadaviek pre MVP Lendify (nefunkčné)
- Bezpečnosť peňazí
- Vedenie účtov
- Prevody peňazí
- Vedenie zábezpek
- Obchodné podmienky

### Výber technológií

Pri vývoji aplikácie Lendify je dôležité zvoliť vhodné technológie, ktoré zabezpečia plynulú funkčnosť, škálovateľnosť a bezpečnosť celého systému. Na základe požiadaviek a analýzy odporúčame nasledujúce technologické riešenia:

#### Frontend
Pre vývoj používateľského rozhrania je ideálnou voľbou **React** v kombinácii s **TypeScriptom**. Táto kombinácia umožňuje vytvárať modulárne a flexibilné komponenty, pričom TypeScript zabezpečuje vyššiu stabilitu kódu vďaka statickému typovaniu. Alternatívne je možné použiť **Next.js** na zlepšenie SEO a rýchlejšie načítanie stránok pomocou server-side rendering (SSR).

#### Backend
Na strane servera je vhodné použiť:
- **Node.js** s frameworkom **Express** – rýchly a škálovateľný nástroj pre REST API.
- Alternatívne **Django** (Python), ak by boli potrebné robustné nástroje na správu dát a užívateľov.

Tieto technológie poskytujú flexibilitu pri práci s dátami, vývoj modulov pre správu objednávok, notifikácií a bezpečnostných prvkov.

#### Databáza
Pre ukladanie štruktúrovaných údajov je najlepšou voľbou **PostgreSQL**, ktorý ponúka vysoký výkon a podporu komplexných dotazov. Na ukladanie neštruktúrovaných dát, ako sú obrázky a videá, môžeme použiť **Firebase** alebo **Cloud Storage**.

#### Platobné systémy
Integrácia platobných brán je nevyhnutná pre bezpečné spracovanie transakcií:
- **Stripe** – jednoduchá implementácia, široká podpora API a vysoká bezpečnosť.
- **PayPal API** – osvedčené riešenie na globálne platby.

#### Mapy a geolokácia
Na implementáciu filtrov podľa vzdialenosti a vyhľadávania na je najlepšou možnosťou **Google Maps API**, ktoré poskytuje robustné a presné geolokačné služby.

#### Zabezpečenie
Bezpečnosť je kľúčovým prvkom aplikácie:
- **OAuth 2.0** na autentifikáciu používateľov.
- Šifrovanie hesiel a citlivých údajov pomocou **bcrypt**.
- Zabezpečenie platieb a účtov pomocou TLS/SSL certifikátov.

#### Škálovanie a nasadenie
Pre zaistenie škálovateľnosti a dostupnosti aplikácie:
- Použitie **Docker** a **Kubernetes** na kontajnerizáciu a orchestru nasadení.


#### Mobilné aplikácie
Ak bude aplikácia rozšírená o natívne mobilné aplikácie môžeme použiť:
- **Swift** pre iOS a **Kotlin** pre Android, ak je prioritou výkonnosť.
- **React Native** na rýchlejší vývoj multiplatformových aplikácií.

Tieto technológie spoločne tvoria komplexnú infraštruktúru, ktorá zabezpečuje spoľahlivé a efektívne fungovanie aplikácie Lendify, pričom spĺňa všetky požiadavky na funkčnosť a bezpečnosť.

### Modely
Tieto diagramy lepšie predstavujú systém Lendify, zobrazený z rôznych uhlov pohľadu - technického, aplikačného, procesného, motivačného, organizačného a produktového.

##### Organization Viewpoint:
Predstavuje organizačnú štruktúru spoločnosti od vedenia (majitelia, investori, C-level) cez stredný manažment až po výkonných pracovníkov (programátori, návrhári, dizajnéri).
![Organization Viewpoint Diagram!](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/c644a032ff23172bed4f07b7054a536e6e327783/model/images/Organization%20Viewpoint.png "Organization Viewpoint Diagram")

##### Motivation Viewpoint:
Ukazuje motivačné faktory pre dve hlavné skupiny - vlastníkov a záujemcov. Pre vlastníkov je kľúčové zníženie času na získanie záujemcu, pre záujemcov flexibilita a úspora nákladov.
![Motivation Viewpoint Diagram!](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/c644a032ff23172bed4f07b7054a536e6e327783/model/images/Motivation%20Viewpoint.png "Motivation Viewpoint Diagram")

##### Product Viewpoint:
Zobrazuje proces zápožičky produktu v systéme od jeho zalistovania cez vytvorenie požiadavky na výpožičku až po platbu a uzatvorenie zmluvy. Zachytáva interakciu medzi zákazníkom, aplikáciou a podpornými službami.
![Product Viewpoint Diagram!](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/c644a032ff23172bed4f07b7054a536e6e327783/model/images/Product%20Viewpoint.png "Product Viewpoint Diagram")

##### Business Process Cooperation Viewpoint:
Zachytáva proces zalistovania produktu od vyplnenia povinných údajov až po overenie obsahu. Proces zahŕňa interakciu medzi používateľom, systémom, AI a redaktorom.
![Business Process Cooperation Viewpoint Diagram!](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/c644a032ff23172bed4f07b7054a536e6e327783/model/images/Business%20Process%20Cooperation%20Viewpoint.png "Business Process Cooperation Viewpoint Diagram")

##### Application Usage Viewpoint:
Opisuje proces požičiavania predmetu v troch hlavných krokoch - pridanie predmetu, požičanie a vzájomné hodnotenie. Všetky tieto služby sú prepojené s mobilnou/webovou aplikáciou.
![Application Usage Viewpoint!](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/c644a032ff23172bed4f07b7054a536e6e327783/model/images/Application%20Usage%20Viewpoint.png "Application Usage Viewpoint")

##### Technology Viewpoint:
Zobrazuje technickú architektúru systému postavenú na Kubernetes clusteri s MongoDB a PostgreSQL databázami. Systém je zabezpečený firewallom a obsahuje záložné riešenie pre dáta. Podporuje rôzne operačné systémy na strane klienta.
![Technology Viewpoint Diagram!](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/c644a032ff23172bed4f07b7054a536e6e327783/model/images/Technology%20Viewpoint.png "Technology Viewpoint Diagram")


### Low Fidelity

Nižšie zobrazujeme nákresy na papier, ako by mohla aplikácia vyzerať. Keďže sme to kreslili na papier, ušetrili sme mnoho času a mohli sme brainstormovať.

#### Domovská stránka
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/14bdf4f8332732ae116e180f7b59cc890f1766bd/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/1_homepage.png)

#### Pridanie nového produktu
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/14bdf4f8332732ae116e180f7b59cc890f1766bd/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/2_add_new_product.png)

#### Katalóg produktov 
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/14bdf4f8332732ae116e180f7b59cc890f1766bd/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/3_catalog.png)

#### Stránka produktu
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/14bdf4f8332732ae116e180f7b59cc890f1766bd/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/4_single_item.png)

#### Platba krok č.1
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/14bdf4f8332732ae116e180f7b59cc890f1766bd/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/5_checkout.png)

#### Platba krok č.2
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/14bdf4f8332732ae116e180f7b59cc890f1766bd/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/6_payment_details.png)

#### Platba krok č.3
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/14bdf4f8332732ae116e180f7b59cc890f1766bd/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/7_summary.png)

#### Stránka používateľa
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/14bdf4f8332732ae116e180f7b59cc890f1766bd/n%C3%A1%C4%8Drty/Fin%C3%A1lne%20n%C3%A1%C4%8Drty/desktop/8_personal_user_page.png)

### Klikateľný prototyp

Po iteráciach nad low-fidelity prototypom, sme vytvorili finálny, [klikateľný prototyp](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/src/_2024_PRJ_01-ST10-ST18-ST34-Lendify/klikate%C4%BEn%C3%BD%20prototyp/Lendify-Prototype.mp4).

##### Prihlásenie
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/ccda4363efeab853e69ba8b4294b9fda269a4895/klikate%C4%BEn%C3%BD%20prototyp/images/login.png)

##### Domovská stránka
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/ccda4363efeab853e69ba8b4294b9fda269a4895/klikate%C4%BEn%C3%BD%20prototyp/images/homepage.png)

##### Katalóg produktov
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/ccda4363efeab853e69ba8b4294b9fda269a4895/klikate%C4%BEn%C3%BD%20prototyp/images/Catalog.png)

##### Stránka produktu
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/ccda4363efeab853e69ba8b4294b9fda269a4895/klikate%C4%BEn%C3%BD%20prototyp/images/SingleItem.png)

##### Pridanie nového produktu
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/ccda4363efeab853e69ba8b4294b9fda269a4895/klikate%C4%BEn%C3%BD%20prototyp/images/addNewProduct.png)

##### Detail pôžičky
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/ccda4363efeab853e69ba8b4294b9fda269a4895/klikate%C4%BEn%C3%BD%20prototyp/images/borrowDetails.png)

##### Platba krok č.1
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/ccda4363efeab853e69ba8b4294b9fda269a4895/klikate%C4%BEn%C3%BD%20prototyp/images/checkout.png)

##### Platba krok č.2
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/ccda4363efeab853e69ba8b4294b9fda269a4895/klikate%C4%BEn%C3%BD%20prototyp/images/checkout2.png)

##### Platba krok č.3
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/ccda4363efeab853e69ba8b4294b9fda269a4895/klikate%C4%BEn%C3%BD%20prototyp/images/checkout3.png)

##### Košík
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/ccda4363efeab853e69ba8b4294b9fda269a4895/klikate%C4%BEn%C3%BD%20prototyp/images/Cart.png)


### 3D Printing

- 3D Printer Creality
- PLA Material
- Material Temperature 200°
- Bed Temperature 60°
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/accdbbda8f292bf61bc4c7ee061c27b6e7892d0d/3D%20print/images/3.png)

#### 3D Modeling with Blender
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/accdbbda8f292bf61bc4c7ee061c27b6e7892d0d/3D%20print/images/1.png)

#### CURA – program for 3D printer
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/accdbbda8f292bf61bc4c7ee061c27b6e7892d0d/3D%20print/images/2.png)

### Finálny produkt
![](https://bitbucket.org/st10-st18-st34-lendify/repo_sthdf_2024-2025/raw/accdbbda8f292bf61bc4c7ee061c27b6e7892d0d/3D%20print/images/4.png)

