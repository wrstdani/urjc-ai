vector = [1, 2, 3]

function m = maximo(x)
  m = max(x);
end

function ind = indice(x)
  for i = x
    if i == max(x)
      ind = i
    endif
  endfor
end

maximo(vector)
indice(vector)
