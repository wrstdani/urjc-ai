function [U, S] = pca(X)
%PCA Aplica el metodo de las componentes principales para el conjunto de datos X
%   [U, S, X] = pca(X) el método calcula los autovectores de la matriz de covarianzas de X.
%   Devuelve los autovectores calculados en una matriz U y los autovalores en una matriz diagonal S.

% Calculamos la dimension de la matriz X, siendo m las filas y n las columnas
[m, n] = size(X);

% Estas son las matrices que debes obtener
U = zeros(n);
S = zeros(n);

% ====================== Escribe tu codigo aqui ======================
% Instrucciones: Primero tienes que calcular la matriz de covarianzas de X. A continuacion,
%               usa la funcion "svd" para obtener los autovectores y los autovalores
%               de la matriz de covarianzas.
%
% Consejos: Recuerda que si nuestros datos han sido tratados previamente restando la media
% la matriz de covarianzas viene dada simplemente por 1/n (X^t X). Por tanto, utiliza primero
% la funcion featureNormalize al conjunto de datos X para poder aplicar la formula previa.



% =========================================================================

end
