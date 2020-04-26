% asoc_fla_ev = Effects_filtrados_norm*Flavor_filtrados_norm';
%% Path
addpath(genpath('~Data\funciones'))
%%
load('~Data\data3.mat')
[numeros, texto, todo] = xlsread('~Data\datos_porrito.xlsx');
flavors = texto(1,60:107);
effects = texto(1,1:19);
texto_m = texto(2:end,:);

filter = numeros(:,111);
N = length(find(filter));

texto_f = texto_m(find(filter) ,:);

strains = texto_f(:,109);
strain_names = texto_f(:,108);

sativas = strcmp(strains,'Sativa');
hibridas = strcmp(strains,'Hybrid');
indicas = strcmp(strains,'Indica');

%% Without dismish 0-0 lines
% asoc_fla_ev

[rho, pval] = corr(Effects_filtrados_norm',Flavor_filtrados_norm','type','Spearman');
[h, crit_p, adj_p] = fdr_bh (pval,0.05,'dep');
mask = adj_p<0.05;
adj_rho = rho.*mask;

elsupertitulo = 'Con los 0s';
[ con0positivos,con0negativos ] = Figurita( rho,adj_rho,effects,flavors ,elsupertitulo);

%% Taking into acount rows while them has some non empty value
[rho_f,pval_f,adj_p] = correlacioname_filtrado_esto( Effects_filtrados_norm,Flavor_filtrados_norm);
mask = adj_p<0.05;
adj_rho = rho_f.*mask;

elsupertitulo = 'Sin los 0s';
[ sin0positivos,sin0negativos ] = Figurita( rho_f,adj_rho,effects,flavors ,elsupertitulo);
