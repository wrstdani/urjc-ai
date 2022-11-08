function X_rec = recoverData(Z, U, K)
%RECOVERDATA recupera una aproximacion de los datos originales usando los datos pryectados

%   X_rec = RECOVERDATA(Z, U, K) recupera una aproximacion de los datos orginales que
%  han sido reducidos a K dimension devuelve dicha aproximacion en la variable X_rec.
%

% Necesitas que el programa devuelva las siguiente variable de manera correcta.
X_rec = zeros(size(Z, 1), size(U, 1));

% ====================== Escribe tu codigo aqui ======================
% Instructions: calcula la aproximacion de los datos proyectando hacia atras
%               en el espacio original usando los K primeros autovectores de U
%
%               Para el i-esimo ejemplo Z(i,:), la (aproximacion) de los datos
%               recuperados para la dimension j viene dado como sigue:
%                    v = Z(i, :)';
%                    recovered_j = v' * U(j, 1:K)';
%
%               Notese que U(j, 1:K) es un vector columna.
%


% =============================================================

end
