function Z = projectData(X, U, K)
%PROJECTDATA Calcula los datos representados al proyectar solamente
%sobre las primeros k autovectores.

%   Z = projectData(X, U, K) calcula la proyeccion de los datos que
%    previamente han sido normalizados en el espacio de dimensión reducida
%    formado por las k primeras columnas de U. Devuelve los datos proyectados
%    en la matriz Z
%

% Debes hacer que el programa devuelva la siguiente variable de manera correcta.
Z = zeros(size(X, 1), K);

% ====================== ESCRIBE TU CODIGO AQUI ======================
% Instructions: Calcula la proyeccion de los datos usando solamente los
%               primeros k autovectores de U (k primeras columnas).
%               Consejo: para el i-esima observacion X(i,:) tenemos que
%               la proyeccion sobre el k-esimo autovector es dado como sigue:
%                    x = X(i, :)';
%                    projection_k = x' * U(:, k);
%



% =============================================================

end
