# LLM-gestützte Programmgenerierung zur Lösung von ARC-AGI

Das vorliegende Repository enthält alle Pipelines, deren generierte Programme und andere Dateien, welche im Rahmen der Bachelorarbeit "LLM-gestützte Programmgenerierung zur Lösung von ARC-AGI" erstellt wurden.

## Überblick der Dokumente:

### Datensätze, Ordner und andere Dateien:
- ARC_Data: Öffentlicher Trainings- und Evaluationsdatensatz des ursprünglichen ARC-AGI-Datensatzes.
- ARC2_Data: Öffentlicher Trainings- und Evaluationsdatensatz des ARC-AGI-2-Datensatzes.
- Candidate_programs_*: Ordner, in welchem die gespeicherten Kandidatenprogramme der jeweiligen Pipeline hinterlegt sind, jeweils benannt nach der jeweiligen Pipeline.
- ConceptARC_Data: Teilmenge des ConceptARC-Datensatzes mit der ersten Aufgabe jeder Konzeptgruppe.
- corpus: Vollständiger ConceptARC-Datensatz.
- Evaluation_set: 100 zufällig gewählte Aufgaben des öffentlichen Evaluationsdatensatzes von ARC-AGI-1.
- Evaluation_set_ARC2: 100 zufällig gewählte Aufgaben des öffentlichen Evaluationsdatensatzes von ARC-AGI-2.
- submission_*: Submission-Datei mit den Vorhersagen der jeweiligen Pipelines, jeweils nach der dazugehörigen Pipeline benannt.
- classified_concepts.json: JSON-Datei zur Hinterlegung der Klassifizierung der Aufgaben nach den ConceptARC-Konzepten.

### Pipelines:

- Pipeline_basic_prompt_4.ipynb: Vergleichspipeline zur Erstellung von bis zu vier Kandidatenprogrammen je Aufgabe.
- Pipeline_basic_prompt_6.ipynb: Vergleichspipeline zur Erstellung von bis zu sechs Kandidatenprogrammen je Aufgabe.
- Pipeline_revision-loop.ipynb: Revisionsschleifen-Pipeline (RS-Pipeline) für Bearbeitung des ARC-AGI-1-Datensatzes unter Verwendung des o4-mini-Modells.
- Pipeline_revision-loop_4o.ipynb: RS-Pipeline für die Bearbeitung des ARC-AGI-1-Datensatzes unter Verwendung des GPT-4o-Modells.
- Pipeline_revision-loop_ARC2.ipynb: RS-Pipeline für die Bearbeitung des ARC-AGI-2-Datensatzes unter Verwendung des o4-mini-Modells.
- Pipeline_w_tailored_prompts_full.ipynb: Vollständige Pipeline zur Erstellung massgeschneiderter Abfragen (MA-Pipeline) zur Bearbeitung des ARC-AGI-1-Datensatzes unter Verwendung des o4-mini-Modells.
- Pipeline_w_tailored_prompts_encodings.ipynb: MA-Pipeline ohne Klassifizierungsschritt zur Bearbeitung des ARC-AGI-1-Datensatzes unter Verwendung des o4-mini-Modells.
- Pipeline_w_tailored_prompts_base.ipynb: MA-Pipeline ohne alternative Kodierung und Klassifizierungsschritt zur Bearbeitung des ARC-AGI-1-Datensatzes unter Verwendung des o4-mini-Modells.

### Weitere Notebooks:
- createEvalSet.py: Notebook zur Erstellung eines Ordners mit 100 zufällig gewählten Aufgaben eines spezifizierten Datensatzes.
- Accuracy.ipynb: Notebook zur Anzeige der erzielten Genauigkeiten. Hierbei kann sowohl der verwendete Datensatz (Evaluation_set oder Evaluation_set_ARC2) als auch die Submission-Datei der Pipeline angegeben werden, um die Genauigkeiten und Konzeptgenauigkeiten zu betrachten.
- classification_accuracy.ipynb: Notebook zur Klassifizierung der ConceptARC-Aufgaben und Ermittlung der Klassifizierungsgenauigkeit.

## Ausführung der Pipelines:

Um eine gewählte Pipeline auszuführen, muss ein API-Key im folgenden Format in einer Datei "key.env" abgelegt werden:

OPENAI_API_KEY=...

Soll eine Pipeline ausgeführt werden, kann das ganze Jupyter-Notebook ausgeführt werden, wodurch die Programmerstellung gestartet wird. Hierbei sollten entweder der Speicherort der zu generierenden Programme sowie die zu erzeugende Submission-Datei gewechselt werden oder die bestehenden gelöscht werden. Ansonsten werden die Kandidatenprogramme zusätzlich zu den bereits bestehenden generiert, was zu Fehlern bei manchen Pipelines führen kann.

Die erreichten Genauigkeiten eines Durchlaufs können durch Angabe des Namens der Submission-Datei und des bearbeiteten Datensatzes (Evaluation_set oder Evaluation_set_ARC2) in Accuracy.ipynb eingesehen werden.