function [ promedios ] = opt_LSA( M,neworder )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
Msort = [M,neworder];
Msort2 = sortrows(Msort,length(Msort)) ;
Msort3 = Msort2(:,1:end-1)';
Msort3 = [Msort3,neworder];
Msort4 = sortrows(Msort3,length(Msort)) ;
figure;
imagesc(Msort4(:,1:end-1))
caxis([0,1])
colormap jet
shg
pause(1.5)
close
N1 = length(find(neworder ==1));
N2 = length(find(neworder ==2));
N3 = length(find(neworder ==3));

meme = 1;%mean(mean(Msort4));
promedios = [mean(mean(Msort4(1:N1,1:N1)))/meme;mean(mean(Msort4(1+N1:N1+N2,1+N1:N1+N2)))/meme;mean(mean(Msort4(1+N2+N1:N1+N2+N3,1+N2+N1:N1+N2+N3)))/meme];

end

