% script para evaluar orden del LSA
%% Path
addpath(genpath('...\Matlab\funciones'))
addpath(genpath('..\2014_04_05 BCT'))%https://sites.google.com/site/bctnet/
%%

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
hibridas = strcmp(strains,'Hybrid')*2;
indicas = strcmp(strains,'Indica')*3;

neworder = sativas+ hibridas+indicas;
 
files = dir('...\tf_idf_correlacion_nd*');

% promedios = zeros(3,length(files));
 N_Ci_mean = zeros(1,length(files));
 Q_mean = zeros(1,length(files));
 gamma = 1;
for k = 1:length(files)%[12,34,45,55,70]%
    M = csvread(strcat('...\matrices\',files(k).name));

%     promedios(:,k) = opt_LSA( M,neworder );
    [ N_Ci_mean(1,k),Q_mean(1,k) ]  = opt_LSA_louvain( M,100,gamma );
k
end

% plot(promedios','*')
close all
SMO = 3
figure;
plot(smooth(N_Ci_mean(1:70)',SMO))
title('N_Ci_mean')
figure;
plot(smooth(Q_mean(1:70)',SMO))
title('Q_mean')


%% PCA componentes
F = csvread(strcat('....\tf_idf_freq_low_rank_nd_50.csv'));

[COEFF, SCORE, LATENT, TSQUARED, EXPLAINED] = pca(F');

sum(EXPLAINED(1:5))
plot(EXPLAINED,'*')
CoefAbs = abs(COEFF);

