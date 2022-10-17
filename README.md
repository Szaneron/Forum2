## Temat projektu: Forum internetowe 

## Cel projektu:
Celem projektu jest zaprojektowanie forum internetowego. Strona ma być tworzona przez społeczność, a nie tylko przez jednego autora – właściciela forum. 
W projekcie mają znaleźć się funkcjonalności pozwalające na integrację zrzeszonej społeczności w formie tworzenia rozbudowanych wątków, krótkich pytań, oraz komentarzy.

### Cele szczegółowe:
* Edycja profilu użytkownika.
* Formularz dodawania nowego projektu.
* Edycja oraz usuwanie dodanych projektów przez samego autora, badź administratora.
* Licznik polubień danego wątku.
* Sekcja komentarzy.
* Możliwość dodawania któtkich pytań.

### Funkcjonalności:
* Dodawanie projektów
* Edycja projektów
* Dodawanie komentarzy do projektów
* Dodawanie pytań
* Edycja pytań
* Dodawanie odpowiedzi do pytań
* System polubień projektów
* Wyszukiwanie projektów
* Prezentowanie 4 najnowszych projektów na stronie głównej
* Prezentowanie 3 najnowszych pytań na stronie głównej
* Paginacja stron

## Interfejs serwisu
<details> <summary>Ekran główny </summary>
  
Górną część strony zajmuje menu, które pozwala na przechodzenie pomiędzy podstronami. W obrębie przestrzeni banner’a znajduje się przycisk pozwalający na przejście do okna logowania lub rejestracji użytkownika. Menu jest w pełni responsywne.
  
  ![c3](https://user-images.githubusercontent.com/58951668/121755323-2e83ad80-cb17-11eb-9bef-4354767e0ac9.PNG)
  
Na stronie głównej prezentowany jest kolaż składający się z 4 najnowszych postów. Wyświetlana jest ich miniatura, tytuł ( jeśli się mieści to max 2 linie), oraz ilość polubień przez użytkowników.  
  ![c1](https://user-images.githubusercontent.com/58951668/121754718-9802bc80-cb15-11eb-8a85-b5e684c152a9.PNG)
  
Poniżej kolażu wyświetlane są 3 najnowsze pytania użytkowników.
  ![c2](https://user-images.githubusercontent.com/58951668/121754764-b799e500-cb15-11eb-8d2a-1e1045883653.PNG)

Na wszystkich podstronach aplikacji widnieje przycisk dodawania nowego projektu lub pytania. Po najechaniu na znany z wielu aplikacji przycisk  sprzęgany z tworzeniem nowej wiadomości wyświetlają się dwa kolejne, których ikony są skojarzone z ich funkcjonalnościami.
  ![c4](https://user-images.githubusercontent.com/58951668/121755204-e1074080-cb16-11eb-8fe6-746c31a846ad.png)
  
Stronę zamyka stopka w niespotykanym stylu. Ukośne kreski które w niej zastosowałem nadają dynamiki całości oraz przykuwają uwagę użytkownika. W stopce zostały zawarte najważniejsze informacje tj.: adres strony, dane kontaktowe oraz odnośniki do poszczególnych mediów społecznościowych.
  ![c5](https://user-images.githubusercontent.com/58951668/121755470-8c17fa00-cb17-11eb-99a6-108bdb690c26.PNG)


</details>
<details> <summary>Logowanie/Rejestracja</summary>
  
Formularz logowania jest prosty i przyjazny dla użytkownika.
  ![c6](https://user-images.githubusercontent.com/58951668/121755633-f6309f00-cb17-11eb-943f-75cda62e6680.PNG)

Rejestracja jest równie prosta. Wymaga uzupełnienia wszystkich pól wraz ze spełnieniem odpowiednich standardów.
  ![c7](https://user-images.githubusercontent.com/58951668/121755711-2ed07880-cb18-11eb-838f-8733cb068b9b.PNG)

</details>
<details> <summary>Tworzenie projektu</summary>
  
Podczas tworzenia projektu mamy dwa obowiązkowe do wypełnienia pola: tytuł oraz minuatura. Mamy tutaj dostęp to ckeditora który oferuje funkcje dostępne w tradycyjnych edytorach tekstu, takie jak formatowanie (pogrubienie, kursywa, podkreślenie, listy numerowane i punktowane), tabele, cytowanie blokowe, linkowanie do zasobów sieciowych, wstawianie grafik, wklejanie zawartości z Microsoft Word, cofanie i przywracanie operacji oraz inne narzędzia do formatowania HTML. Ma także wbudowane narzędzie do sprawdzania pisowni w locie.
  
  ![c8](https://user-images.githubusercontent.com/58951668/121755955-d483e780-cb18-11eb-9b31-ab0944dd4d3b.PNG)

</details>
<details> <summary>Tworzenie pytania</summary>
Użytkownicy mogą również oprócz projektów dodawać krótkie pytania. Posiadają one identyczne funkcjonalności jak projekty z tą różnicą, że mogą one zawierać jedynie pytania tekstowe.
  
  ![c9](https://user-images.githubusercontent.com/58951668/121756210-a18e2380-cb19-11eb-8d56-40e77473c301.PNG)

</details>
<details> <summary>Paginacja</summary>
  Dla widoku wszystkich projektów oraz pytań został zastosowany mechanizm paginacji stron. Ma on za zadanie zwiększyć szybkość ładowania strony. W rezultacie użytkownik traci mniej czasu na ładowanie treści, których nie potrzebuje w danym momencie. Dla pytań paginacja odbywa się gdy ich liczba przekroczy 10 natomiast w przypadku projektów limit na stronę wynosi 6.
  
  ![c10](https://user-images.githubusercontent.com/58951668/121756396-38f37680-cb1a-11eb-9533-2293e1404f5d.PNG)

</details>
<details> <summary>Widok projektu</summary>
Po wybraniu projektu ze strony głównej, lub widoku projektów użytkownik zostanie przeniesiony do szczegółów projektu. W widoku prezentowana jest cała treść zamieszczonego projektu. W górnej części znajduje się tytuł projektu, niżej dane osoby, która jest autorem projektu. Ponad to wyświetlana jest również liczba polubień oraz zdjęcie profilowe użytkownika. Następnie zostaje pokazane zdjęcie miniaturki projektu, po czym pojawia się właściwa treść postu. Projekt umożliwia edycję oraz jego usunięcie poprzez autora, oraz usunięcie przez administratora.
  
  ![c11](https://user-images.githubusercontent.com/58951668/121756521-aef7dd80-cb1a-11eb-921b-614016122751.PNG)
</details>
<details> <summary>Komentarze</summary>
Widok projektu posiada również sekcję komentarzy. Jest ona wyposażona w funkcję ich usuwania przez autora komentarza, oraz administratora. W komentarzu prezentowany jest pseudonim użytkownika, jego zdjęcie profilowe, oraz treść odpowiedzi.
  
  ![c12](https://user-images.githubusercontent.com/58951668/121756641-1f9efa00-cb1b-11eb-8e29-8d483dae40a7.PNG)

Sekcja komentarzy istnieje również dla pytań i jest tak samo wyposażona jak skecja komentarzy dla projektów.
  ![c13](https://user-images.githubusercontent.com/58951668/121756785-9936e800-cb1b-11eb-9bb4-8bf99568f896.PNG)

</details>
<details> <summary>Wyszukiwanie projektów</summary>
Na wszystkich podstronach aplikacji widnieje pole wyszukiwania projektu. Po wpisaniu całego bądź fragmentu tytułu i zatwierdzeniu ackji klawiszem enter zostanie wyświetlony poszukiwany przez nas projekt.
  
  ![c15](https://user-images.githubusercontent.com/58951668/121769741-9f51b680-cb65-11eb-8d39-7d897c8f54f7.PNG)

</details>

## Baza danych
Konfiguracja bazy danych odbywa się przez normalny moduł Pythona ze zmiennymi poziomu modułu reprezentującymi ustawienia Django. Domyślnie konfiguracja używa SQLite’a. SQLite jest zawarty w Pythonie, więc nie trzeba nic instalować, aby mieć bazę danych.

### Model bazy danych
Model jest pojedynczym, pełnym źródłem informacji o twoich danych. Zawiera zasadnicze pola i zachowania danych, które przechowujesz.

Każdy model jest reprezentowany przez klasę, która dziedziczy po **django.db.models.Model**. Każdy model ma kilka zmiennych klasowych, z których każda reprezentuje pole bazy    danych w modelu.

Każde pole jest reprezentowane przez instancję klasy Field – na przykład CharField dla pól znakowych i DateTimeField dla dat i czasu. Mówi to Django, jakie dane przechowuje każde pole.

Nazwa każdej instancji Field (np. title lub author) jest nazwą pola, w formacie przyjaznym maszynom.
Model bazy danych w kodzie wygląda tak:
  
  ![c16](https://user-images.githubusercontent.com/58951668/121770139-d6c16280-cb67-11eb-9504-94e486a9e1eb.PNG)


### Diagram ERD
![app](https://user-images.githubusercontent.com/58951668/114049692-f4362f80-988b-11eb-87ea-1e0195b8b860.png)
![image](https://user-images.githubusercontent.com/58951668/114904786-80aa9a00-9e18-11eb-8976-5cfb72d6db07.png)

### Skrypt do utworzenia struktury bazy danych
CREATE TABLE "app_thread" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NULL, "date_posted" datetime NOT NULL, "miniature" varchar(100) NOT NULL, "content" text NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "app_thread_likes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "thread_id" integer NOT NULL REFERENCES "app_thread" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "app_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "url" varchar(40) NOT NULL UNIQUE, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "app_commentthread" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "ddate_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" integer NOT NULL REFERENCES "app_thread" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "app_commentpost" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "ddate_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "post_id" integer NOT NULL REFERENCES "app_post" ("id") DEFERRABLE INITIALLY DEFERRED);

## Wykorzystane technologie
Aplikacja „JDIY.com” została napisana w języku pyton przy wykorzystaniu Framework’a Django. Interfejs graficzny został zaprojektowany przy pomocy składni HTML oraz CSS. W projekcie wykorzystywana jest również biblioteka BootStrap, przy jej pomocy obsługiwana jest większość elementów warstwy prezentacji. Do połączenia BootStrap’a z formularzami Django użyta została biblioteka CrispyForm, dzięki temu domyślne formularze generowane przez Django uzyskują wygląd spójny z resztą aplikacji. Do prawidłowego działania aplikacji moga być wyamgane dodatkowe biblioteki, jeśli nie będą one zawarte w IDE w którym projekt jest uruchamiany. Do głównych bibliotek które należy doinstalować jest:
- Pillow 8.2.0
aby zainstalować należy wpisać w terminalu swojego IDE nastepującą komende: pip install Pillow
- django-ckeditor-5 0.0.14
aby zainstalować należy wpisać w terminalu swojego IDE nastepującą komende: pip install django-ckeditor-5

Wszelkie nieuwzględnione biblioteki, których aplikacja będzie wymagała do poprwanego uruchomienia można znaleźć na stronie https://pypi.org/

## Proces uruchomienia aplikacji (krok po kroku)
Projekt został utworzony przy pomocy środowiska PyCharm. W celu uruchomienia wystarczy go zaimportować oraz ustawić konfigurację uruchomieniową jako aplikacja „Django Server”.

Aplikacje uruchamiamy poleceniem **python manage.py runserver** wpisywaną w terminalu naszego IDE.
![c14](https://user-images.githubusercontent.com/58951668/121757671-97225880-cb1e-11eb-8cf3-69e1b3958ba6.PNG)


W razie problemów z zarządzaniem aplikacją możemy utowrzyć nowe konto administartora. Aby utworzyć konto administratora należy użyć poniższej komendy w terminalu:
**python manage.py createsuperuser**

Aplikajca startuje na domyślnym porcie 8000

## Django administration
Jedną z najpotężniejszych części Django jest automatyczny interfejs administratora. Odczytuje metadane z modeli, aby zapewnić szybki, skoncentrowany na modelach interfejs, w którym zaufani użytkownicy mogą zarządzać treścią w witrynie. Zalecane użycie przez administratora ogranicza się do wewnętrznego narzędzia zarządzania organizacji. Nie jest przeznaczony do budowania całego frontendu. Aby przenieść się do interfejsu administartora nalezy dopisać \admin w adresie strony.

![c18](https://user-images.githubusercontent.com/58951668/121770437-95ca4d80-cb69-11eb-9845-50bd016fcedc.PNG)
 Po zatwierdzeniu klawiszem enter zostaniemy przeniesieni do centrum administracyjnego.
 
![c17](https://user-images.githubusercontent.com/58951668/121770475-c01c0b00-cb69-11eb-8c5f-2057160247db.PNG)

Administratora tworzymy używając komendy w terminalu PyCharm-a: **python manage.py createsuperuser**

## Wnioski końcowe
Stworzenie portalu społecznościowego od podstaw wymaga dobrego rozeznania na temat aktualnych trendów, oraz funkcjonalności oferowanych przez inne tego typu rozwiązania. Ponad to należy wykazać się inwencją twórczą, stosować dobrze funkcjonujące rozwiązania w nowej, lepszej odsłonie. Można również wprowadzać własne funkcjonalności, jednak należy mieć na uwadze, że muszą być one w formie jak najbardziej przystępnej dla użytkownika. Główną zaletą stworzonego przeze mnie serwisu społecznościowego jest prostota jego obsługi. Użytkownik nie jest przytłaczany nadmiarem funkcji, informacji, oraz masą powiadomień. Stworzenie tego projektu zdecydowanie poszerzyło moją wiedzę na temat projektowania portali społecznościowych, a także ich implementacji.
