x = 2
n = 5

function valor_salida = sumatorio(num, exp_denom)
  valor_salida = 0;
  for i = 1:exp_denom
    valor_salida  = valor_salida + ((num^exp_denom) / exp_denom);
  endfor
end

sumatorio(x, n)
