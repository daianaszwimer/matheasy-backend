from src.modelTrainer import model, clean_text


def predict(statement):
    cleaned_statement = clean_text(statement)
    # print(model.predict([cleaned_statement])[0])
    return model.predict([cleaned_statement])[0]
