# Vorlesung 3 (04.12.)

## Markdown
- Umwandlung von Code zu Text (wie hier)  
- Ähnlich wie LaTeX (glaube ich)  
- Kann auch in eine PDF konvertiert werden (dafür benutzt es glaube ich LaTeX)
  
[Synthax Guide](https://www.markdownguide.org/basic-syntax/)


## Git
- Tool zur Versionskontrolle  
- Speicherung verschiedener Versionen von Dateien  
=> ermöglicht das Zugreifen auf eine alte Version, die z.B. fehlerfrei funktioniert hat.  
- sinnvolle "Commit-Message" um zu verstehen, was sich in der Version geändert hat

### Branches
- Abzweigung von einer Version des Projekts
- Separate Arbeit an z.B. einem Programm  
=> kein Einfluss auf den "master-branch"
- nach z.B. Fertigstellung wieder "merch" mit dem master-branch  
=> Zusammenführen des Projekts


## Github
- Online-Tool zum Speichern und Teilen eines Projektes
- Cloud-Speicher
- Ermöglicht Zugriff von mehreren Computern (z.B Uni und Zuhause)
- Funktioniert zusammen mit Git  
  => aktuelle Versionen können auf Github "gepushed" werden

### Issues
- Quasi eine To-Do-Liste
- können einem Projekt zugeordnet werden (falls man an mehreren Projekten arbeitet)
- können über Keyword in der Commit-Message geschlossen werden
  - Close
  - Closes
  - Closed
  - Fix
  - Fixes
  - Fixed
  - Resolve
  - Resolves
  - Resolved

### Pages
Erstellt automatisch eine Website aus den Markdown files (Umwandlung in HTML)
- Settings --> Pages  
- Deploy from Branch (meistens master)  


### Releases
Ermöglicht anderen Leuten auf die releaste Version zuzugreifen
- So können Projekte/Daten über Github referenziert werden
- DOI für die Releases über Website [Zenodo](https://www.zenodo.org)

