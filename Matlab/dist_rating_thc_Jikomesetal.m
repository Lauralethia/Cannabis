condpath = '~Data';
[numeros, texto, todo] = xlsread([condpath ,'rating_thc_Jikomesetal.xlsx']);
data = numeros(:,:);
nombres = texto(1,:);
figure;
plot(data(:,3),(data(:,1)+eps),'*')

xlabel('THCmax_mean')
ylabel('CBDmax_mean')


chemo = data(:,3)./(data(:,1)+eps);
chemotipe = ones(size(chemo))*2;
chemotipe(chemo>5) =  1;
chemotipe(chemo<1/5) =  3;
%  chemotipe(chemo<median(chemo)) =  1;
hist(chemotipe,3);
