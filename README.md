# oop-prosjekt-oppgave

ting som mangler:
- Klassediagram
- README(litt)

# CASINO

Et casino spill laget i python med fokus på OOP

## Instalere og kjøre

Programmet bruker [UV](https://docs.astral.sh/uv/) for å hånter biblioteker, for å installere bibliotekene kjør
```bash
uv sync
```
Og for å starte programmet kjør
```bash
uv run casino
```

## Hva programmet gjør 

Når programmet starter, leser den json filen `data/player.json` og basert på om den finnes, eller er tom, velger den om du kan bare lage ny bruker, eller om du kan også loade en eksisterende spiller

Etter det kjører den casino classen fra [app.py](/src/casino/app.py) og det er den klassen som hånterer hva som skjer i spillet.

## Kilder

Jeg har ikke tatt kode fra andre kilder, det nermeste jeg kommer er å bruke kilder for å prøve å gjøre roulette mer realistisk, og dokumentasjon for python og biblioteker (og [ai](#ai-bruk))

[Roulette kilde](https://www.wikihow.com/Play-Roulette)

## AI bruk

### Verktøy

Jeg har brukt ai som chatgpt og claude på nettet for å kunne lære meg og hjelpe meg med bibliotekene \
Når jeg ville gjøre gjøre større endringer og ideer som krevde hele kodebasen, brukte jeg opencode (mer spesifikt, GLM 5.3 - Flash Free)

### Hva brukt for

Jeg har brukt ai hovedsaklig for å komme med ideer og hjelpe meg med å jobbe med biblioteker som rich, en del av [ui.py](/src/casino/ui.py) er skrevet av ai. Jeg har også brukt ai til å lese gjennom koden, og finne feil som jeg selv fikset.

## Logg