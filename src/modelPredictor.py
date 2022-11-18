from src.modelTrainer import model, clean_text
import re


def predict(statement):
    statement_with_no_spaces = statement.replace(" ", "")
    if bool(re.match(r'\d', statement)) or statement.startswith("x"):
        return "ecuacion-explicita"
    else:
        cleaned_statement = clean_text(statement)
        return model.predict([cleaned_statement])[0]
