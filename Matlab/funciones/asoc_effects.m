function [givepars,giveparsnegative] = asoc_effects( adj_rho,effects,flavors )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
[ef,sa] =  find(adj_rho>0);
givepars = {};
disp('Positive')
for fila = 1:length(ef)
givepars{fila} = [effects(ef(fila)),flavors(sa(fila))] ;
disp(givepars{fila})
end

[ef,sa] =  find(adj_rho<0);

giveparsnegative = {};
disp('Negative')
for fila = 1:length(ef)
giveparsnegative{fila} = [effects(ef(fila)),flavors(sa(fila))] ;
disp(giveparsnegative{fila})
end

end

