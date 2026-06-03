import numpy as np
# 1.Definir conjunto de ejemplos X y Etiquetas y

X = np.array([
[0, 0],
[0, 1],
[1, 0],
[1, 1]])
y = np.array([0,0,0,1])

#2. Se definen las epocas y la tasa de aprendizaje
epochs = 100
lr = 0.1

#3. Se agrega el cesgo

Xb = np.hstack([X, np.ones((X.shape[0], 1))])


#4. Se inicializan los pesos

np.random.seed(42)
w = np.random.uniform(-0.5, 0.5, size=(Xb.shape[1],))

#5. Se define la función de activación escalón

'''def step(z): # FUNCION ESCALERA
    return 1 if z >= 0 else 0'''
'''def signo(z):
    return 1 if z>-1 else -1'''
'''def sigmoide(z):
    return 1/(1+np.exp(-z))'''
def lineal(z):
    return (z)
#6. Se entrena el perceptrón

for epoch in range(epochs):                                                                     # Para cada época se itera sobre cada ejemplo
    errors = 0                                                                                  # Se inicializa el contador de errores
    for xi, yi in zip(Xb, y):                                                                   # Para cada ejemplo i = 1, 2, 3, 4 se obtiene el vector de características
        z = np.dot(xi, w)  
        yout = lineal(z)
        y_pred_clase = 1 if yout >= 0.5 else 0
        delta = yi - y_pred_clase

        if delta != 0:
            w += lr * delta * xi
            errors += 1
                                # Calcular potencial de activación Z = w1*x1 + w2*x2 + b
        '''yout = lineal(z)                                           # Calcular salida del perceptrón yout = f(z)
        delta = yi - yout                                                                       # Calcular error delta = yi - yout
        if delta != 0:                                                                          # Si el error es diferente de cero, se actualizan los pesos
            w += lr * delta * xi                                                                    # Se actualizan los pesos w = w + lr * delta * xi
            errors += 1'''
    if errors == 0:                                                                             # Se incrementa el contador de errores
        print(f"convergencia alcanzada en la epoca: {epoch+1} con pesos: {w}")
        break  
    print(f"Epoch {epoch+1}/{epochs}, Errores: {errors}")
 # 7. prediccion dado un nuevo x E {0,1}d: formar Xb = [x;1], calcular step((w,xb)) y mostrar resultado
'''def predict(x):
    xb = np.append(x, 1) # Agregar el sesgo al vector de características
    z= np.dot(xb, w)        # Calcular el potencial de activación
    return signo(z)          # Devolver la predicción usando la función de activacion

# 8. Imprimir predicciones para cada combinación de entrada
for x in X:
    print(f"Entrada: {x}, Predicción: {predict(x)}")'''
#Se definen funciones de evaluación para medir el desempeño del modelo
def mse(y_true, y_pred):
    return float(np.mean((y_true - y_pred) ** 2))
# El coeficiente de determinación R² se calcula como 1 menos la proporción de la suma de los residuos al total de la suma de los cuadrados, proporcionando una medida de qué tan bien el modelo explica la variabilidad de los datos.
def r2_score(y_true, y_pred):
    ss_res = float(np.sum((y_true - y_pred) ** 2))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    if ss_tot == 0:
        return 1.0 if ss_res == 0 else 0.0
    return 1.0 - (ss_res / ss_tot)
# Se utiliza la función de evaluación para medir el desempeño del modelo en el conjunto de entrenamiento
y_pred = np.array([lineal(np.dot(xi, w)) for xi in Xb])
print(f"MSE: {mse(y, y_pred)}, R²: {r2_score(y, y_pred)}")
