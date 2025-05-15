# Cloud computing

## Co to jest chmura obliczeniowa?

Chmura obliczeniowa (cloud computing) to dostarczanie usług IT (np. serwerów, baz danych, przechowywania, analizy, sztucznej inteligencji) przez Internet – na żądanie, elastycznie, bez inwestycji w fizyczną infrastrukturę.

Przykład: Zamiast kupować serwer do hostowania strony internetowej, w Azure uruchamiasz maszynę wirtualną w kilka minut i płacisz tylko za czas jej działania.

## Hierarchia zarządzania w Azure

1. Microsoft Entra ID Tenant (wcześniej Azure Active Directory Tenant)
    * To najwyższy poziom w strukturze – reprezentuje całą organizację.
    * Zawiera użytkowników, grupy, aplikacje, role i zasady tożsamości.
    * Każdy Tenant ma unikalny identyfikator (np. twojafirma.onmicrosoft.com).
    * W tenancie możesz mieć wiele subskrypcji.
    * Przykład: Firma "Contoso" ma jedną dzierżawę AAD, a w niej dział IT, HR, Finanse – każdy z dostępem tylko do swoich subskrypcji.

2. Management Group
    * Organizuje wiele subskrypcji w strukturę hierarchiczną.
    * Służy do wspólnego zarządzania politykami, kontrolą dostępu, itd.

3. Subscription (subskrypcja)
    * To poziom rozliczeń i kontroli dostępu do zasobów.
    * Każda subskrypcja ma unikalny ID i limit zasobów.
    * Można mieć wiele subskrypcji w jednej dzierżawie – np. osobna dla dev, osobna dla produkcji.

4. Resource Group
    * Logiczna "paczka" zasobów – trzymasz tam powiązane elementy aplikacji.
    * Można stosować do organizacji, zarządzania uprawnieniami, tagowania itd.

5. Resource (zasób)
    * Pojedynczy element w chmurze: VM, baza danych, App Service, Storage Account, itd.
    * Zawsze należy do jednej resource group i jednej subskrypcji.

```
Azure Active Directory Tenant
│
├── Management Groups (opcjonalne)
│   ├── Subscription A
│   │   ├── Resource Group A
│   │   │   ├── Resource 1 (VM)
│   │   │   └── Resource 2 (Storage)
│   │   ├── Resource Group B
│   │   │   └── Resource 3 (Azure Function)
│   └── Subscription B
│       └── Resource Group C
│           └── Resource 4 (SQL Database)
```

## Regiony i dostępność

### Region (np. Poland Central, Sweden Central, North Europe, East US)

To fizyczne lokalizacje centrów danych Azure, rozproszone globalnie. Wybór regionu wpływa na:

* Szybkość działania aplikacji (im bliżej użytkownika, tym lepiej),
* Spełnienie przepisów prawnych (np. przetwarzanie danych tylko w UE),
* Koszty (niektóre regiony są tańsze).
* Dostępność usług (niektóre usługi, w szczególności nowe albo specjalistyczne, jak Azure OpenAI, są dostępne tylko w wybranych regionach).

### Availability Zones (AZ)

To fizycznie niezależne strefy w jednym regionie – każda ma własne zasilanie, chłodzenie, sieć. Dzięki temu można osiągnąć:

* Wysoką dostępność (High Availability),
* Odporność na awarie jednej strefy (failover),
* Automatyczne przełączanie ruchu (load balancing).

Przykład: Twoja aplikacja działa w 3 strefach w regionie West Europe. Jeśli jedna strefa przestanie działać, ruch automatycznie przekieruje się do pozostałych.

Uwaga! Nie każdy region Azure ma AZ!

## Modele usług w Azure

1. IaaS – Infrastructure as a Service

    Wynajmujesz "gołą" infrastrukturę: maszyny wirtualne (Azure Virtual Machines), sieci, storage.

2. PaaS – Platform as a Service

    Dostajesz gotowe środowisko do uruchamiania aplikacji (np. Azure App Service). Nie interesuje cię np. system operacyjny i wersja np. Ubuntu.

3. SaaS – Software as a Service

    Gotowe aplikacje w chmurze (np. Microsoft 365, Azure DevOps).

4. FaaS – Function as a Service

    Kod działa tylko, gdy trzeba (np. Azure Functions). Jedyne, co trzeba zrobić, to przygotować kod w wybranym języku. Idealne do event-driven logiki np. reagowanie na przesłanie pliku.

## Skalowalność, redundancja, balansowanie ruchu

1. Skalowalność

    Azure umożliwia automatyczne skalowanie (np. App Service Plan, VM Scale Sets) – czyli uruchamia więcej instancji, gdy rośnie ruch.

2. Redundancja i Load Balancing

    * Load Balancer (Azure Load Balancer / Application Gateway) – rozdziela ruch między serwery.
    * Geo-replikacja – dane/aplikacje są dostępne z wielu regionów (np. Azure Traffic Manager, Azure Front Door), co:
        * Skraca czas ładowania globalnie (np. użytkownik z Japonii trafia do najbliższego serwera),
        * Zwiększa dostępność (jeśli region A padnie, przełącza się na B).

## Modele chmury obliczeniowej

### Public Cloud (Chmura publiczna)

To najczęstszy model – usługi i infrastruktura są własnością Microsoftu i dostępne przez internet dla wielu klientów.

Zalety:

* Brak kosztów infrastruktury – wszystko zapewnia Azure (np. serwery, sieć, chłodzenie).
* Skalowalność – zasoby można elastycznie zwiększać i zmniejszać.
* Płacisz tylko za to, co używasz – model "pay-as-you-go".
* Szybkie wdrożenie – masz dostęp do gotowych usług (np. Azure App Services, Azure VMs).

Wady:

* Mniejsza kontrola nad infrastrukturą – wszystko zarządzane przez dostawcę.
* Zależność od połączenia internetowego.
* Potencjalne ryzyko związane z przechowywaniem danych poza organizacją (choć Azure ma wysokie standardy bezpieczeństwa).

### Private Cloud (Chmura prywatna)

Wszystkie zasoby działają na infrastrukturze firmy, ale z wykorzystaniem technologii chmurowej.

Zalety:

* Pełna kontrola nad danymi i infrastrukturą – istotne np. przy danych medycznych, finansowych.
* Większe bezpieczeństwo i zgodność z regulacjami (np. RODO).
* Możliwość dostosowania pod konkretne potrzeby organizacji.

Wady:

* Wysokie koszty początkowe – trzeba kupić i utrzymać własny sprzęt.
* Konieczność posiadania własnego zespołu IT do zarządzania infrastrukturą.
* Mniejsza elastyczność skalowania niż w public cloud.

### Hybrid Cloud (Chmura hybrydowa)

Łączy chmurę publiczną (np. Azure) i prywatną (np. Azure Stack lub lokalne serwery). Można np. przechowywać dane w chmurze prywatnej, a aplikacje uruchamiać w publicznej. Mogą być połączone poprzez VPN lub ExpressRoute (dedykowane, prywatne łącze do Azure, nie przez Internet)

Zalety:

* Elastyczność – możesz korzystać z chmury publicznej, ale wrażliwe dane trzymasz lokalnie.
* Optymalizacja kosztów – mniej krytyczne operacje możesz przenieść do tańszej chmury publicznej.
* Zgodność z przepisami – np. przetwarzanie danych w kraju.

Wady:

* Złożoność konfiguracji i zarządzania – wymaga dobrego planowania.
* Większe wymagania dla zespołu IT – muszą ogarniać oba światy (lokalne + cloud).
* Potencjalne problemy z integracją danych i aplikacji między środowiskami.

## Ciekawostki

1. Microsoft Azure dąży by do 2025 r. wszystkie centra danych były zasilane energią odnawialną i inwestują na rzecz innowacji energetycznych. [link](https://azure.microsoft.com/pl-pl/explore/global-infrastructure/sustainability#tabx077fd50b9cc143d5a072535575115edc)

2. Azure, AWS, GCP to chmury komercyjne. Możliwe jest zbudowanie chmury prywatnej, na własnych zasobach, np. używając:
    * Azure Stack – lokalna wersja Azure działająca we własnym data center.
    * Open source'owe rozwiązania jak OpenStack, VMware vSphere.

## Dlaczego firmy przechodzą do chmury?

* Mniejsze koszty (brak fizycznych serwerowni)
* Łatwe skalowanie zasobów
* Dostępność z każdego miejsca
* Automatyczne aktualizacje
* Wysoka niezawodność i odporność na awarie

## Linki i wskazówki przydatne przy pracy z projektem

Linki:

* [Materiały treningowe Microsoft Azure](https://learn.microsoft.com/en-us/)
* [Tutorial Azure Container App](https://medium.com/@radha.sable25/how-to-use-azure-container-app-service-for-efficient-app-deployment-a-devops-guide-2633a83af6e4)
* [Python i Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=connection-string%2Croles-azure-portal%2Csign-in-azure-cli&pivots=blob-storage-quickstart-scratch)

Wskazówki:

* Tutorial z linku pokazuje jak wdrożyć na chmurę aplikację ze zbudowanego już wcześniej kontenera znajdującego się w rejestrze. W projekcie, natomiast, wdrażanie nowych wersji ma następować z użyciem pipeline'u CI/CD.
* W celu zapisywania danych w Azure Blob Storage, można skorzystać z łatwiejszej metody autoryzacji, czyli tzw. `Connection String`. W środowiskach produkcyjncyh rekomendowanym podejściem jest to oparte na Azure RBAC (Azure Role-Based Access Control), natomiast wymaga ono dodatkowej konfiguracji (użycie tego podejscia w projekcie będzie na plus).
* Klucze i sekrety niezbędne do działania aplikacji można ustawić manualnie w Azure Portal jako zmienne środowiskowe aplikacji. W środowiskach produkcyjncyh rekomendowanym podejściem jest korzystanie z Azure Key Vault, natomiast wymaga to dodatkowej konfiguracji (użycie tego podejscia w projekcie będzie na plus).
