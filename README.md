# LLM-gestützte Programmgenerierung zur Lösung von ARC-AGI

Dieses Repository enthält sämtliche Pipelines, deren generierte Programme und weitere Dateien, die im Rahmen der Bachelorarbeit "LLM-gestützte Programmgenerierung zur Lösung von ARC-AGI" erstellt wurden.

## Überblick der Dokumente:

### Datensätze, Ordner und andere Dateien:
- ARC_Data: Öffentlicher Trainings- und Evaluationsdatensatz des ursprünglichen ARC-AGI-Datensatzes.
- ARC2_Data: Öffentlicher Trainings- und Evaluationsdatensatz des ARC-AGI-2-Datensatzes.
- Candidate_programs_*: Ordner mit den gespeicherten Kandidatenprogrammen der jeweiligen Pipeline (benannt nach der jeweiligen Pipeline).
- ConceptARC_Data: Teilmenge des ConceptARC-Datensatzes (jeweils die erste Aufgabe jeder Konzeptgruppe).
- corpus: Vollständiger ConceptARC-Datensatz.
- Evaluation_set: 100 zufällig gewählte Aufgaben des öffentlichen Evaluationsdatensatzes von ARC-AGI-1.
- Evaluation_set_ARC2: 100 zufällig gewählte Aufgaben des öffentlichen Evaluationsdatensatzes von ARC-AGI-2.
- submission_*: JSON-Dateien mit den Vorhersagen der jeweiligen Pipelines (benannt nach der jeweiligen Pipeline).
- classified_concepts.json: Enthält die Klassifizierung der bearbeiteten Aufgaben nach den ConceptARC-Konzepten.

### Pipelines:

- Pipeline_basic_prompt_4.ipynb: Vergleichspipeline zur Erstellung von bis zu vier Kandidatenprogrammen pro Aufgabe für ARC-AGI-1 mit dem o4-mini-Modell.
- Pipeline_basic_prompt_6.ipynb: Vergleichspipeline zur Erstellung von bis zu sechs Kandidatenprogrammen pro Aufgabe für ARC-AGI-1 mit dem o4-mini-Modell.
- Pipeline_revision-loop.ipynb: Revisionsschleifen-Pipeline (RS) für ARC-AGI-1 mit dem o4-mini-Modell.
- Pipeline_revision-loop_4o.ipynb: RS-Pipeline für ARC-AGI-1 mit dem GPT-4o-Modell.
- Pipeline_revision-loop_ARC2.ipynb: RS-Pipeline für ARC-AGI-2 mit dem o4-mini-Modell.
- Pipeline_w_tailored_prompts_full.ipynb: Vollständige Pipeline zur Erstellung massgeschneideter Abfragen (MA-Pipeline) für ARC-AGI-1 mit dem o4-mini-Modell.
- Pipeline_w_tailored_prompts_encodings.ipynb: MA-Pipeline ohne Klassifizierungsschritt für ARC-AGI-1 mit dem o4-mini-Modell.
- Pipeline_w_tailored_prompts_base.ipynb: MA-Pipeline ohne alternative Kodierung und ohne Klassifizierung für ARC-AGI-1 mit dem o4-mini-Modell.

### Weitere Notebooks:
- createEvalSet.py: Skript zur Erstellung eines Evaluationsordners mit 100 zufälligen Aufgaben.
- Accuracy.ipynb: Anzeige der Genauigkeiten für eine gewählte Submission-Datei und Datensatz.
- classification_accuracy.ipynb: Klassifizierung der ConceptARC-Aufgaben und Berechnung der Klassifizierungsgenauigkeit.

## Ausführung der Pipelines:

Für die Ausführung ist ein OpenAI-API-Key erforderlich, der in einer Datei key.env im folgenden Format hinterlegt wird:

OPENAI_API_KEY=...

Zur Ausführung einer Pipeline das entsprechende Jupyter-Notebook starten und vollständig ausführen. Vorher sollte entweder:

- der Speicherort für Programme und Submission-Dateien angepasst werden.

- bestehende Dateien (Ablageordner der Kandidatenprogramme und Submission-Datei) gelöscht werden.

da sonst zusätzliche Programme zu bestehenden hinzukommen und dadurch Fehler auftreten können.

--- 
Beispiel: Ausführung "Pipeline_revision-loop.ipynb":

1. Speicherort für Programme oder Submission-Dateien anpassen oder "Candidate_programs_revision-loop" und "submission_revision-loop.json" löschen.
2. Alle Zellen des Jupyter-Notebooks ausführen.
---

Die erzielten Genauigkeiten können in Accuracy.ipynb durch Angabe des Namens der Submission-Datei und des Datensatzes (Evaluation_set oder Evaluation_set_ARC2) ausgewertet werden.
