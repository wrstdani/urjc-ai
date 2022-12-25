a=input('Primer número: ');
b=input('Segundo número: ');

function r = mcd(primer_num,segundo_num)
  while primer_num != 0 and segundo_num != 0
    if primer_num == segundo_num
      r = primer_num;
    endif


  endwhile
  if primer_num == 0
    r = segundo_num
  endif

  elseif segundo_num == 0
    r = primer_num
end


mcd(a,b)
gcd(a,b)
