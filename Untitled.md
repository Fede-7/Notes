```mermaid
@startuml
left to right direction
skinparam packageStyle rectangle
skinparam shadowing false

actor "Amministratore" as Admin
actor "Supereroe" as Hero

rectangle "Sistema Informativo Hero Association" {
  ' Casi d'uso Amministratore
  usecase "Registra nuovo eroe" as UC1
  usecase "Assegna nuova missione" as UC2
  usecase "Aggiorna stato missione" as UC3
  usecase "Aggiorna ranking" as UC4
  usecase "Valuta richiesta di abbandono" as UC5
  usecase "Accetta richiesta" as UC5a
  usecase "Rifiuta richiesta" as UC5b

  ' Casi d'uso Supereroe
  usecase "Consulta profilo" as UC6
  usecase "Visualizza missioni assegnate" as UC7
  usecase "Visualizza ranking" as UC8
  usecase "Invia richiesta di abbandono" as UC9
}

' Associazioni primarie
Admin -- UC1
Admin -- UC2
Admin -- UC3
Admin -- UC5

UC6 -- Hero
UC9 -- Hero

' Relazioni <<include>>
UC3 ..> UC4 : <<include>>
UC6 ..> UC7 : <<include>>
UC6 ..> UC8 : <<include>>

' Generalizzazioni
UC5a --|> UC5
UC5b --|> UC5
@enduml
```
