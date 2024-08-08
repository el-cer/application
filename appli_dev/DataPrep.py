from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def split_data(data, target):
    X = data.drop(columns=target)
    y = data[target]
    X, y = encoding(X, y)
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)
    return X_train, X_test, y_train, y_test


def encoding(X, y):
    for i in X.columns:
        if X[i].dtypes=='object':
            X[i] = LabelEncoder().fit_transform(X[i])
    if y.dtype=='object':
        LabelEncoder().fit_transform(y)
    return X, y