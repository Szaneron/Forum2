## Forum internetowe

By powrócić do momentu w którym projekt znajduje się w wersji podatnej na ataki xss należy:

1. Zakomnetować podany fragment kodu w pliku views.py:

   Forum_Internetowe\app\views.py
![image](https://user-images.githubusercontent.com/58951668/155487856-440b504d-9576-4cd9-a6c0-edffe3cc0a64.png)

2. Zamienić url edycji projektu w pliku urls.py:(z lini 18 na zakomentowaną linię 19)

   Forum_Internetowe\app\urls.py
![image](https://user-images.githubusercontent.com/58951668/155488535-c33012d6-b0ed-4bd2-b281-a88ae44c2a22.png)

