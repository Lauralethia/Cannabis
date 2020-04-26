function [ N_Ci_mean,Q_mean ] = opt_LSA_louvain( M ,iterac,gamma)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here iterac = 10

Ci_num = NaN(1,iterac);
Q = NaN(1,iterac);
for i = 1:iterac
    [Ci, Q(1,i)]=modularity_louvain_und(M,gamma);
    Ci_num(1,i) = max(Ci);
end

N_Ci_mean = mean(Ci_num);
Q_mean= mean(Q);
end



