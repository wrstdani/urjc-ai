n = 5;

function val_salida = fact(x)
  if x == 0
    val_salida = 1
  endif
  val_salida = 1;
  while x > 1
    val_salida = val_salida * x;
    x = x - 1;
  endwhile
end

fact(n)
