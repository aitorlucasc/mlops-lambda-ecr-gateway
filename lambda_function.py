import pickle


def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load('dv.bin')
model = load('model1.bin')


def predict(user):
    X = dv.transform([user])
    y_pred = model.predict_proba(X)[0, 1]
    get_credit = y_pred >= 0.5

    result = {
        'get_credit_probability': float(y_pred),
        'get_credit': bool(get_credit)
    }

    return result


def lambda_handler(event, context):
    result = predict(event)
    return result
