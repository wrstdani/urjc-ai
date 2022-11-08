function [X_norm, mu, sigma] = featureNormalize(X)
%FEATURENORMALIZE Normaliza el conjunto de datos X
%   FEATURENORMALIZE(X) devuelve el conjunto de datos X normalizado.
%   la media de cada variable es cero y la desviación típica 1.


mu = mean(X);
X_norm = bsxfun(@minus, X, mu);

sigma = std(X_norm);
X_norm = bsxfun(@rdivide, X_norm, sigma);


% ============================================================

end
