
%% ================== Cargamos el paquete de datos ===================

%
fprintf('Visualiando los datos ejemplos para PCA.\n\n');

%  El siguiente comando carga el conjunto de datos. Deberias tener una
%  variable X en tu entorno al ejecutar el comando.
load ('ex7data1.mat');
%  Visualizamos el conjunto de datos
plot(X(:, 1), X(:, 2), 'bo');
axis([0.5 6.5 2 8]); axis square;

fprintf('Programa pausado. Presiona intro para continuar.\n');
pause;


%% =============== Componentes principales ===============
%  Debes completar el codigo del fichero pca.m
%
fprintf('\nRunning Usamos componentes principales en nuestro ejemplo.\n\n');

%  Antes de aplicar componentes principales normalizamos nuestro conjunto de datos.
[X_norm, mu, sigma] = featureNormalize(X);

%  Aplicamos componentes principales
[U, S] = pca(X_norm);


%  Dibujamos los autovectores centrados en la media de los datos. Las lineas muestran
%  las direcciones de maxima variacion en el conjunto de datos.
hold on;
drawLine(mu, mu + 1.5 * S(1,1) * U(:,1)', '-k', 'LineWidth', 2);
drawLine(mu, mu + 1.5 * S(2,2) * U(:,2)', '-k', 'LineWidth', 2);
hold off;


fprintf('Mayor autovalor: \n');
fprintf(' U(:,1) = %f %f \n', U(1,1), U(2,1));
fprintf('\n(deberia aparecer -0.707107 -0.707107)\n');

fprintf('Programa pausado. Presiona intro para continuar.\n');
pause;


%% =================== Reduccion de la dimension ===================
%
%  Debes completar el codigo del fichero projectData.m
%
fprintf('\nReduccion de la dimension del conjunto de datos.\n\n');

%  Dibujamos el conjunto de datos normalizados (devueltos por pca)
plot(X_norm(:, 1), X_norm(:, 2), 'bo');
axis([-4 3 -4 3]); axis square

%  Proyectamos los datos sobre dimension K = 1
K = 1;
Z = projectData(X_norm, U, K);
fprintf('Proyeccion del primer ejemplo: %f\n', Z(1));
fprintf('\n(este valor deberia ser cercano a 1.481274)\n\n');



X_rec  = recoverData(Z, U, K);
fprintf('Aproximacion del primer ejemplo: %f %f\n', X_rec(1, 1), X_rec(1, 2));
fprintf('\n(Este valor deberia ser aproximadamente  -1.047419 -1.047419)\n\n');
%  Visualizamos las proyecciones de los datos (rojo) y
%  los datos originales normalizados (azul) en una misma grafica
hold on;
plot(X_rec(:, 1), X_rec(:, 2), 'ro');
for i = 1:size(X_norm, 1)
    drawLine(X_norm(i,:), X_rec(i,:), '--k', 'LineWidth', 1);
end
hold off

