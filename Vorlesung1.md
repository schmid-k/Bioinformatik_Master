# Vorlesung 1 (20.11.)


## Python Grundlagen
ChatGPT ist grundsätzlich eine gute Hilfe beim Programmieren


### Variablen
- Speicherung von Werten zur späteren Verwendung
- Inhalt kann alles Mögliche sein: Zahlen, Text, Wahr-Falsch etc.
```python
variable1 = 1
variable2 = "Text"
```


#### Zahlen
- Integer  
=> ganze Zahlen
```python
variable1 = 1
variable2 = variable1 + 2
```

- Floats  
=> Gleitkomma-Zahlen
```python
variable1 = 1.00
variable2 = variable1 + 3.14
```

- Können konvertiert werden:
```python
floatVariable = 3.1415
intVariable = int(floatVariable)
intVariable = 3
floatVariable = float(intVariable)
```

- Außerdem sind alle üblichen arithmetischen Operationen möglich
  - Addition (+)
  - Subtraktion (-)
  - Multiplikatíon (*)
  - Division (/) --> Ergebnis ist float
  - Power (**)
  - Modulo (%) --> Ergebnis ist Rest aus Division
  - Floor Division (//) --> Ergebnis ist integer
  

- Assignments  
=> Vereinfachen einfache Operationen  
folgendes beschreibt dasselbe:
```python
x = x + 1
x += 1
```


#### Boolean
- Kann wahr (True) oder falsch (False) als Werte annehmen
- Dafür Vergleichsoperatoren
  - < kleiner als
  - \> größer als
  - == ist gleich
  - \>= größer gleich
  - <= kleiner gleich
  - != nicht gleich
```python
zahl1 = 1
zahl2 = 2
falseStatement = zahl1 == zahl2
trueStatement = zahl1 <= zahl2

falseStatement = False
trueStatement = True
```


#### Strings
```python
variable1 = "Text"
variable2 = variable1 + "input"
```

