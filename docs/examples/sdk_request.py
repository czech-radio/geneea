# Copyright 2019 Geneea Analytics s.r.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Analyzes several texts and extracts the entities, tags and relations contained in them.
"""

import datetime
import sys, os

from geneeanlpclient import g3


USER_KEY = os.environ.get("GENEEA_API_KEY")

TEXTS = [
    "I was in Paris last week. The Eiffel tower is great.",
]


def main():
    print("USER_KEY", USER_KEY, file=sys.stderr)

    requestBuilder = g3.Request.Builder(
        analyses=[g3.AnalysisType.ALL],
        referenceDate=datetime.datetime.now(),
        returnMentions=True,
        returnItemSentiment=True,
    )

    # req = requestBuilder.build(id=0, text=TEXTS[0])

    # print(req)

    # sys.exit()

    with g3.Client.create(userKey=USER_KEY) as analyzer:
        for idx, text in enumerate(TEXTS):
            analysis = analyzer.analyze(requestBuilder.build(id=str(idx), text=text))

            print(text)
            print("--- Entities ---")
            for e in analysis.entities:
                print(f"\t{e.type}: {e.stdForm}")

                for m in e.mentions:
                    prevToken = m.tokens.first.previous()
                    nextToken = m.tokens.last.next()
                    snippet: str = f'{prevToken.text if prevToken else ""} [{m.text}] {nextToken.text if nextToken else ""}'
                    print(f"\t\t{m.mwl}: {snippet}")

            print("--- Tags ---")
            for t in analysis.tags:
                print(f"\t{t.type}: {t.stdForm}")

                for m in t.mentions:
                    prevToken = m.tokens.first.previous()
                    nextToken = m.tokens.last.next()
                    snippet: str = f'{prevToken.text if prevToken else ""} [{m.tokens.text}] {nextToken.text if nextToken else ""}'
                    print(f"\t\t{snippet}")

            print("--- Relations ---")
            for r in analysis.relations:
                argsStr = ", ".join(f"{a.type}: {a.name}" for a in r.args)
                modalityStr = r.modality or ""
                negatedStr = "-not" if r.isNegated else ""

                print(f"\t{r.type}: {modalityStr}{r.name}{negatedStr}({argsStr})")

            print("--- Document Sentiment ---")
            print(f"\t{analysis.docSentiment}")

            # ############################################################### #

            print("--- Document Paragraphs ---")
            for m in analysis.paragraphs:
                print(m)

            # ############################################################### #


if __name__ == "__main__":
    main()
