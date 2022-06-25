# Development notes

Geneea REST API je popsáno zde: https://api.geneea.com/#!/geneea-api-v3/.
https://bitbucket.org/geneea/sdk/src/master

Návrh doménového modelu vychází z terminologického slovníku níže.

## Terminologický slovník

- Analysis:

- Text = original + analyzed content (this should be persisted in DB)

- Document: Dokument obsahující obsah (text), který chceme analyzova, může být v různých formátech (plain, HTML, Word, PDF).

- Language: Rozpoznaný jazyk dokumentu.

- Sentiment

- Entity:

  - type:
    - Person # basic
    - Organization
    - Location
    - Product
    - Event
    - General
    - URL # internet
    - Email
    - HashTag
    - Mention
    - Date # date and time
      - Time
      - Duration
    - Set
    - Number # numbers
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

Mám text např.

Populární známka se prodávala na jediném místě v centru Kyjeva, kde na ni každý den čekaly stovky lidí. Mezitím se arch šesti známek prodává na inzertních serverech za více než 10 tisíc korun.

Dokument je reprezentován svým obsahem (textem).

- Text má určitou délky (včetně bílých znaků).
- Může obsahovat gramatické chyby (můžeme zkusit korekci).
- Text

- Text se dá rozědlit na odstavce (paragrap).
- Odstavce se dále dělí na věty (sentence).
- Věty se dělí na tokeny (tokens) [slova | interpunkce] .

V rámci věty má token pozici reprezentovanu indexy začátku a konce.
V rámci odstavce má věta pozici reprezentovanu indexy začátku a konce.
V rámci celého textu má odstavec pozici reprezentovanu indexy začátku a konce.

Obsah dokumentu můžeme analyzovat a získat:

- sentiment: udává zabarvení (pozitivní, negativní, neutrální)
- kolekci entit (entit jso různého typu např. číslo, lokace atd.)
- kolekci relací (vztahů) mezi tokeny

Document:

Představ si že pošleš stejný text analyzovat na různé slyžby... dostaneš
jiné analyy pro stejný obsah. Jak implementuješ **eq**? Zřejme tohle může nastat.

Co když analyzujeme rozhovor... mluví dva respondenti... má smysl
analyzovat jejich promluvy zvlaste např jeden má jiný sentiment než druhý.
vzhledem k tématu rozhovoru.
