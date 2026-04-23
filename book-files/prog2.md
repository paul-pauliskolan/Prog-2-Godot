Jag vill att kursen baseras på The science of learning se bland annat de två PDF filerna i mappen book-files

Anvä'nd https://docs.godotengine.org/en/stable/tutorials/2d/ och https://docs.godotengine.org/en/stable/index.html som primära källor för tekniska genomgångar, kodexempel och övningar. Anpassa innehållet så att det passar kursens progression och nivåer, och integrera det centrala innehållet och betygskriterierna från Skolverket på ett tydligt sätt i varje del av kursen.

SoL (Science of Learning) ska styra hur materialet byggs upp för att optimera elevernas inlärning, men det ska inte nämnas eller förklaras i kursmaterialet.

Du ska skapa en komplett kurs i Programmering nivå 2 med fokus på spelutveckling i Godot och programmering i GDScript. Kursen ska utgå från Skolverkets centrala innehåll och betygskriterier för Programmering 2, och dessa ska genomsyra hela upplägget, både i innehåll, uppgifter och progression.

Strukturen ska bygga vidare på upplägget från Programmering nivå 1 så att det finns en tydlig röd tråd mellan kurserna. Tanken är att eleverna stegvis utvecklar sina kunskaper och i slutet av kursen ska kunna skapa ett eget spel i Godot som kan användas som grund för deras gymnasiearbete.

Kursen ska vara uppdelad i tydliga delar med lektioner, genomgångar, kodexempel och praktiska övningar som successivt ökar i svårighetsgrad. Den ska inspireras av kursen Create with Code i Unity och C#, men allt innehåll ska anpassas till Godot och GDScript. Där det är möjligt ska kursen vidareutvecklas och förbättras, men det är viktigt att det centrala innehållet och betygskriterierna fortfarande är tydligt integrerade.

Både 2D- och 3D-spelutveckling ska ingå i kursen, med konkreta exempel som visar hur elever kan arbeta i båda dimensionerna. Kursen ska också ge eleverna möjlighet att utveckla förståelse för strukturering av kod, objektorienterad programmering, problemlösning och hur olika delar samverkar i ett spelprojekt.

Det visuella temat för kursmaterialet ska vara genomtänkt och konsekvent. Blått och grönt ska undvikas som primärfärger eftersom de redan används i andra sammanhang. Istället ska en primärfärg väljas som ger bra kontrast mot ett blått tema och samtidigt känns modern och passar spelutveckling. En violett eller lila färg är att föredra eftersom den både särskiljer sig visuellt och ger ett kreativt och tekniskt uttryck.

Målet är att kursen ska vara tydlig, användbar i undervisning och tillräckligt genomarbetad för att elever självständigt ska kunna planera och utveckla ett spelprojekt med kvalitet som räcker för gymnasiearbete.

## Utkast: Programmering nivå 2 (Godot + GDScript)

### Översikt
- Omfattning: ca 18-20 veckor.
- Röd tråd: från styrd implementation till självständig spelutveckling.
- Slutprodukt: ett elevutvecklat spelprojekt (2D eller 3D) med dokumentation, testning och förbättringsarbete.

### Kursmål i praktiken
- Eleverna analyserar problem, bryter ned dem och designar lösningar innan kodning.
- Eleverna bygger objektorienterade system i GDScript med klasser, objekt och arv.
- Eleverna använder filhantering, enkel datalagring och internetkommunikation i spel.
- Eleverna arbetar systematiskt med felsökning, testning, undantagshantering och kodkvalitet.
- Eleverna utvecklar användarvänliga gränssnitt och strukturerad kod som går att vidareutveckla.

### Vad eleverna redan kan från tidigare kurser
- Från Programmering nivå 1 kommer grunderna i variabler, villkor, loopar, listor, funktioner, felsökning, undantagshantering, struktur och läsbar kod, användargränssnitt, projektarbete och versionshantering.
- Från Teknik 2 kommer arbetssätt kring projekt, analys, modeller, dokumentation, kvalitet, kommunikation, presentation och värdering av lösningar ur ett större sammanhang.
- Den här kursen använder därför samma arbetslogik som eleverna redan känner igen: läs, förstå, testa, förbättra, dokumentera och visa resultat.
- Godot och GDScript introduceras som ett nytt sammanhang, men inte som ett helt nytt sätt att tänka. Eleverna ska känna igen arbetsgången och samtidigt utmanas med objektorientering, spelarkitektur och större system.

### Differentierade spår: E, C och A
- E-spår: lärarstyrda genomgångar, färdiga mallar, mindre deluppgifter och tydligt avgränsade spelmoment. Fokus ligger på att formulera och lösa enkla problem, förstå grunderna i Godot och skapa fungerande program med viss anpassning till syfte, användare och tillgänglighet.
- C-spår: mer självständiga lösningar, längre deluppgifter och krav på motiverade designval. Fokus ligger på relativt komplex problemlösning, tydligare OOP-struktur, bättre användaranpassning och systematisk testning.
- A-spår: öppna uppgifter med flera möjliga lösningar, högre krav på analys, generalisering och kvalitet. Fokus ligger på komplex problemlösning, välstrukturerad kod, god felhantering, tydlig dokumentation och mycket god anpassning till syfte, användare och tillgänglighet.
- Alla elever arbetar i samma kursram, men med olika nivå på stöd, självständighet och omfattning. Uppgifterna byggs så att samma grundmoment kan lösas på E-, C- eller A-nivå.

### Hur nivåerna skiljer sig i praktiken
- Kapitel 1-3: E-elever följer tydliga exempel och återger grundläggande samband; C-elever förklarar och anpassar lösningar; A-elever jämför alternativ och bygger vidare självständigt.
- Kapitel 4-6: E-elever löser avgränsade problem med stöd; C-elever gör egna val i analys, design och datalagring; A-elever motiverar och generaliserar lösningar.
- Kapitel 7-10: E-elever testar och rättar enklare fel med hjälp av mallar; C-elever arbetar mer systematiskt med testning och användaranpassning; A-elever dokumenterar, förbättrar och kvalitetssäkrar på hög nivå.
- Kapitel 11-12: E-elever visar att de kan tillämpa grunder i 3D och slutprojekt; C-elever genomför ett sammanhållet projekt med viss självständighet; A-elever planerar, genomför och förbättrar ett projekt med hög självständighet och god kvalitet.

### Kapitel 1: Från Programmering 1 till Godot-projekt
- Beskrivning: Repetition av kärnkunskaper och uppstart i Godots arbetssätt.
- Delar: kodstruktur, scener/noder, signaler, versionshantering, arbetsflöde.
- Koppling till tidigare kurser: variabler, villkor, loopar, funktioner, felsökning, projektarbete och Git från Prog 1 samt dokumentation och presentationsvana från TEK 2.
- Fokus: hur 2D fungerar i Godot.
- Praktiskt arbete: bygg ett litet 2D-spel med tydlig projektstruktur.

#### Kapitelmål
- Eleverna ska känna igen arbetsflödet från Programmering 1 och samtidigt förstå hur det översätts till Godot.
- Eleverna ska kunna förklara hur ett 2D-spel är uppbyggt av scener, noder, script och input.
- Eleverna ska kunna bygga ett enkelt spel med tydlig struktur och fungerande spelmekanik.

#### Centrala begrepp
- scen, nod, script, Node2D, Sprite2D, Animation, input, collision, signal, export, project tree.

#### Steg i kapitlet
- Steg 1: översikt över Godot och hur kursen hänger ihop med Prog 1.
- Steg 2: bygga en enkel 2D-scen och förstå hur noder hänger ihop.
- Steg 3: koppla input till rörelse och handlingar.
- Steg 4: lägga till kollisioner, mål och enkel spelregel.
- Steg 5: reflektera över struktur, läsbarhet och vad som kan förbättras.

#### Övningar i kapitlet
- Övning 1: skapa en spelare som kan röra sig åt fyra håll.
- Övning 2: lägg till ett objekt som spelaren kan samla.
- Övning 3: skapa ett enkelt mål eller en dörr som avslutar nivån.
- Övning 4: skriv om koden så att den blir tydligare och lättare att återanvända.

#### Stöd för olika nivåer
- E: följ en mall, bygg grundläggande rörelse och få spelet att fungera.
- C: anpassa rörelse, struktur och spelregler samt förklara dina designval.
- A: utveckla egen spelidé inom samma ram, förbättra struktur och motivera tekniska val självständigt.

#### Så fungerar 2D i Godot
- 2D i Godot bygger på scener och noder i ett träd där varje objekt har en tydlig roll.
- Den vanligaste basklassen är Node2D, som används för position, rotation och skala i ett platt spelrum.
- Spelobjekt visas ofta med Sprite2D eller AnimatedSprite2D, medan beteendet styrs av ett script.
- Input från tangentbord, mus eller handkontroll översätts till rörelse, hopp, attack eller andra handlingar.
- Kollisioner och fysik används för att avgöra när objekt träffar varandra eller samspelar i spelvärlden.
- UI hålls separat från spelvärlden så att menyer, poäng och liv blir tydliga för spelaren.
- Poängen i 2D är att eleverna lär sig scenstruktur, koordinater, rörelse och kollisioner innan de går vidare till mer komplexa miljöer.

### Kapitel 2: Objektorienterad programmering i GDScript
- Beskrivning: Introduktion till objektorienterat tänk i spelutveckling.
- Delar: klasser, objekt, ansvarsfördelning, inkapsling.
- Praktiskt arbete: skapa återanvändbara spelobjekt med gemensamt API.

### Kapitel 3: Arv, komposition och klasshierarkier
- Beskrivning: Utveckla större system med hållbar arkitektur.
- Delar: arv, överskuggning, komposition, refaktorering av klasshierarkier.
- Praktiskt arbete: fiendesystem med basklass och specialiserade varianter.

### Kapitel 4: Problemlösning, analys och design
- Beskrivning: Träna systematisk analys före implementation.
- Delar: use case, nedbrytning, flödesmodeller, enkel UML-lik design.
- Perspektiv: sociala aspekter, etiska val och hur program påverkar användare och samhälle.
- Praktiskt arbete: designa och implementera inventory-, dialog- eller uppdragssystem.

### Kapitel 5: Strukturering av spelkod och samverkande system
- Beskrivning: Bygg kod som är läsbar, testbar och lätt att vidareutveckla.
- Delar: kodstandard, modulär struktur, signalflöden, beroenden mellan system.
- Praktiskt arbete: dela upp ett spel i tydliga subsystem (input, gameplay, UI, data).

### Kapitel 6: Lagrad data i filer och enkel datalagring
- Beskrivning: Hantera speldata på ett robust sätt.
- Delar: JSON, serialisering, spara/ladda, datavalidering.
- Praktiskt arbete: spara spelarprogression, inställningar och statistik.

### Kapitel 7: Testning, felsökning och kvalitetssäkring
- Beskrivning: Metodiskt arbete med att förebygga och åtgärda fel.
- Delar: syntaxfel, logiska fel, exekveringsfel, teststrategier, debugverktyg.
- Praktiskt arbete: skapa testplan, genomföra testpass, dokumentera och åtgärda buggar.

### Kapitel 8: Undantagshantering och robusta lösningar
- Beskrivning: Gör program stabila även vid oväntade händelser.
- Delar: felhantering, säkra indataflöden, fallback-lösningar.
- Praktiskt arbete: bygg felresistent hantering för fil- och nätverksoperationer.

### Kapitel 9: Internetkommunikation i spel
- Beskrivning: Introduktion till externa datakällor och nätverkslogik.
- Delar: HTTPRequest, API-svar, asynkrona flöden, enkel säkerhetstänk.
- Praktiskt arbete: hämta och visa extern data i spelet.

### Kapitel 10: Användarvänliga gränssnitt
- Beskrivning: Utforma tydliga och tillgängliga gränssnitt för spel.
- Delar: menystruktur, feedback, läsbarhet, tillgänglighet.
- Praktiskt arbete: designa och implementera komplett UI-flöde för ett spel.

### Kapitel 11: 3D-spelutveckling och teknisk fördjupning
- Beskrivning: Överför tidigare kunskaper till 3D-miljö.
- Delar: 3D-scenstruktur, kamera, rörelse, kollisionshantering, optimering.
- Praktiskt arbete: utveckla en spelbar 3D-prototyp med tydliga systemgränser.

#### Så fungerar 3D i Godot
- 3D i Godot bygger också på scener och noder, men här arbetar man i ett tredimensionellt koordinatsystem med höjd, bredd och djup.
- Den vanligaste basklassen för 3D-objekt är Node3D, som styr position, rotation och skala i 3D-rummet.
- Spelobjekt i 3D består ofta av en MeshInstance3D för modellen, CollisionShape3D för kollisioner och ett script som styr beteendet.
- Kameran blir extra viktig i 3D eftersom den bestämmer vad spelaren ser och hur miljön uppfattas. Små förändringar i kameravinkel kan förändra spelets känsla mycket.
- Rörelse i 3D innebär att objekt kan förflytta sig i flera riktningar samtidigt, och därför behöver eleverna förstå både riktning, hastighet och kamerans relation till spelaren.
- Kollisionshantering i 3D fungerar på samma princip som i 2D, men objekten är uppbyggda av volymer och former i tre dimensioner i stället för plana ytor.
- Ljus och material påverkar också spelet i 3D, eftersom spelaren måste kunna orientera sig i miljön och förstå avstånd, riktning och fokus.
- UI ligger fortfarande separat från själva spelvärlden, men i 3D blir kontrasten mellan spelrum och gränssnitt ännu viktigare för tydlighet och spelbarhet.
- Målet är att eleverna ska förstå att 3D i grunden bygger på samma scenlogik som 2D, men med ett extra dimensionstänk som gör design, rörelse och kamera mer komplexa.

### Kapitel 12: Självständigt slutprojekt (grund för gymnasiearbete)
- Beskrivning: Planera, genomföra och förbättra ett eget spelprojekt.
- Delar: projektplan, milstolpar, iteration, testning, dokumentation, presentation.
- Leverabler: designunderlag, teknisk dokumentation, spelbar version, reflektionsrapport.
- Progression efter tidigare kurser: ska kännas som nästa naturliga steg efter Prog 1-projektet och TEK 2-arbetsformerna, men med större tekniskt djup och mer eget ansvar.

### Kontroll mot centralt innehåll
- Det objektorienterade programmeringsparadigmet: täcks i kapitel 2 och 3.
- Analys, nedbrytning och modellering med analysverktyg: täcks i kapitel 4.
- Programmering i objektorienterat programspråk: täcks i kapitel 2-5.
- Verktyg för programutveckling och modelleringsverktyg: täcks i kapitel 4 och 12.
- Klasser och objekt utifrån analys och design: täcks i kapitel 2-3 och 4.
- Arv och utökning av beteende: täcks i kapitel 3.
- Generiska klasser och metoder: behandlas genom återanvändbara, typade lösningar i kapitel 5-6 och i jämförelser av API-design.
- Filer och databaser: täcks i kapitel 6.
- Internetkommunikation: täcks i kapitel 9.
- Syntaxfel, logiska fel och exekveringsfel: täcks i kapitel 7-8.
- Testning och undantagshantering: täcks i kapitel 7-8.
- Läsbarhet, dokumentation, testbarhet och kodstandard: täcks i kapitel 5 och 12.
- Strukturering av programkod och klasshierarkier: täcks i kapitel 3 och 5.
- Användarvänliga gränssnitt: täcks i kapitel 10 och i slutprojektet.
- Programmerbara system, programspråk och programmeringsparadigm: genom hela kursen, särskilt kapitel 1-3 och 12.
- Syfte, användare, tillgänglighet och sociala/etiska perspektiv: täcks i kapitel 4, 10 och 12.

### Progression i E, C och A genom kapitlen
- Kapitel 1-3: E-eleven följer exempel och bygger enkla system; C-eleven motiverar val och anpassar lösningar; A-eleven jämför lösningar och förbättrar struktur självständigt.
- Kapitel 4-6: E-eleven löser avgränsade design- och datauppgifter; C-eleven kopplar analys till implementation; A-eleven bygger robusta lösningar och generaliserar.
- Kapitel 7-10: E-eleven genomför grundläggande testning och UI-arbete; C-eleven arbetar systematiskt med förbättringar; A-eleven gör avancerad felsökning, tydlig användaranpassning och väl motiverade avvägningar.
- Kapitel 11-12: E-eleven visar att 3D och slutprojekt fungerar med stöd; C-eleven genomför ett sammanhållet projekt med viss självständighet; A-eleven planerar, genomför och förbättrar ett projekt med hög självständighet och god kvalitet.

### Lektionsstruktur (återkommande varje vecka)
- Lektion A: genomgång + lärarledd kodning + kort tillämpning.
- Lektion B: labbpass med handledning och checkpoint.
- Lektion C: challenge, kodgranskning, testning och reflektion.

### Bedömning och progression (E-C-A)
- E: fungerar med stöd, enkel struktur, grundläggande analys och testning.
- C: fungerande och relativt välstrukturerade lösningar, motiverade val, tydlig förbättring.
- A: välstrukturerade och generaliserbara lösningar, avancerad felsökning/testning, god självständighet och välgrundade avvägningar.

### Kommentar om generiska klasser och metoder i denna kurs
- Där GDScript saknar direkt motsvarighet till klassisk generik tränas samma förmåga genom generella, återanvändbara lösningar med typade collections, parametrisering och tydliga API-kontrakt.

------  Detta är kraven från skolverket

Programmering
Programmering har stor betydelse för och påverkan på arbetslivet och samhället. Ämnet programmering behandlar hur mjukvaror skapas, anpassas och utvecklas samt programmeringens roll i informationstekniska sammanhang som datorsimulering och praktisk datoriserad problemlösning. Ämnet behandlar även hur programmerade system påverkar maskiner, utrustning och beslutsfattande.

Ämnets syfte
Undervisningen i ämnet programmering ska syfta till att eleverna utvecklar kunskaper om programmeringens grunder, färdigheter i att tillämpa relevanta metoder för programutveckling och förmåga att lösa programmeringstekniska problem. Undervisningen ska också leda till att eleverna utvecklar färdigheter i programvaruutveckling och förståelse av hur programvaror och programmerbara system påverkar sin omgivning.

Undervisningen ska bidra till att eleverna utvecklar förmåga att analysera, designa och vidareutveckla program. Undervisningen ska också bidra till att eleverna utvecklar kunskaper om några vanligt förekommande programspråk samt traditioner och nya trender i utvecklingen av programspråk. Eleverna ska även ges möjlighet att utveckla förståelse för hur programmering används utifrån olika sociala aspekter, som exempelvis genus, kultur och socioekonomisk bakgrund. Dessutom ska undervisningen leda till att eleverna utvecklar kunskaper om datorns användning i samhället och datorns möjligheter och begränsningar.

I undervisningen ska eleverna ges möjlighet att arbeta i projekt och att enskilt eller i grupp utföra programmeringsuppgifter av varierande komplexitet och inom olika tillämpningsområden. Undervisningen ska lämna utrymme för diskussion om och reflektion över etiska frågor och olika handlingsalternativ inom programmering.

Undervisningen i ämnet programmering ska ge eleverna förutsättningar att utveckla följande:
Kunskaper om programmerbara system, programspråk och programmeringsparadigm.
Förmåga att formulera och skapa lösningar för programmeringsproblem.
Förmåga att skapa program med anpassning till syfte, användare och tillgänglighet.


Nivåkod: PROG2000X
Centralt innehåll
Undervisningen i ämnet programmering på nivå 2 ska behandla följande centrala innehåll:

System

Det objektorienterade programmeringsparadigmet.
Problemlösning

Analys, nedbrytning och modellering av programmeringstekniska problem med lämpligt analysverktyg, till exempel användningsfall. Design av lämplig lösning utifrån gjord analys med lämpliga verktyg och metoder.
Programmering

Programmering i objektorienterat programspråk.
Användning av relevanta verktyg för programutveckling, till exempel modelleringsverktyg.
Skapande och användning av klasser och objekt utifrån gjord analys och design.
Hur arv används för att förändra eller utöka beteende hos klasser som ingår i egna och andras klasshierarkier och standardbibliotek.
Användning av generiska klasser och metoder.
Skrivning och läsning av lagrad data i filer och databaser.
Utveckling av program som nyttjar kommunikation över internet.
Metoder för att förebygga, finna, analysera, åtgärda och förhindra syntaxfel, programmeringslogiska fel och exekveringsfel.
Testning och undantagshantering.
Normer och värden inom programmering, till exempel läsbarhet, dokumentation, testbarhet och nyttan av kodstandard.
Strukturering av programkod och klasshierarkier.
Skapande av användarvänliga gränssnitt.