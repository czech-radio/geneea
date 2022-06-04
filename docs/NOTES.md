# Development notes

Geneea REST API je popsáno zde: https://api.geneea.com/#!/geneea-api-v3/.

Návrh doménového modelu vychází z terminologického slovníku níže.

## Terminologický slovník

- Analysis:

- Text = original + analyzed content (this should be persisted in DB)

- Document: Dokument obsahující obsah (text), který chceme analyzova, může být v různých formátech (plain, HTML, Word, PDF).

- Language: Rozpoznaný jazyk dokumentu.

- Sentiment

- Entity:
  - type:
    - Person       # basic
    - Organization
    - Location
    - Product
    - Event
    - General
    - URL          # internet
    - Email
    - HashTag
    - Mention
    - Date         # date and time
      - Time
      - Duration
    - Set
    - Number      # numbers
      - Ordinal
      - Money
      - Percent

- Relation: Vztah mezi nějakými objekty/subjekty (entitami).

- Mention: Zmínka o nějaké objektu/subjektu (entitě).

- Token: Nejměnší jednotka na kterou text dělíme, v případě věty (sentence) jse o slovo.

- Paragraph:

- Sentence:

---
- We assume tahat all input texts are UTF-8 encoded.
- Text corrections, could contain various newline character types, no diacritics etc.
---

- [ ] Serialize/Deserialize JSON results into domain model.
